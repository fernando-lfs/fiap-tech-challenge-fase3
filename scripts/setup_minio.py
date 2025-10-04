import os
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

# --- Configurações do MinIO ---
MINIO_ENDPOINT = "127.0.0.1:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
BUCKET_NAME = "student-stress"

# --- Configurações do Dataset ---
LOCAL_DATA_PATH = os.path.join("data", "StressLevelDataset.csv")
MINIO_OBJECT_NAME = "StressLevelDataset.csv"


def setup_minio():
    """
    Script para inicializar o ambiente MinIO:
    1. Conecta-se ao servidor MinIO.
    2. Cria o bucket se ele não existir.
    3. Faz o upload do dataset para o bucket se ele não existir.
    """
    print("--- Iniciando a configuração do ambiente MinIO ---")

    # 1. Conectar ao cliente S3 (MinIO)
    try:
        s3_client = boto3.client(
            "s3",
            endpoint_url=f"http://{MINIO_ENDPOINT}",
            aws_access_key_id=MINIO_ACCESS_KEY,
            aws_secret_access_key=MINIO_SECRET_KEY,
        )
        print("✅ Conexão com o MinIO estabelecida com sucesso.")
    except EndpointConnectionError:
        print("❌ Erro: Não foi possível conectar ao servidor MinIO.")
        print(f"   Verifique se o MinIO está em execução no endereço: {MINIO_ENDPOINT}")
        return

    # 2. Verificar e criar o bucket
    try:
        s3_client.head_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket '{BUCKET_NAME}' já existe.")
    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print(f"Bucket '{BUCKET_NAME}' não encontrado. Criando...")
            s3_client.create_bucket(Bucket=BUCKET_NAME)
            print(f"✅ Bucket '{BUCKET_NAME}' criado com sucesso.")
        else:
            print(f"❌ Erro ao verificar o bucket: {e}")
            return

    # 3. Verificar e fazer upload do dataset
    # Primeiro, verificar se o arquivo local existe
    if not os.path.exists(LOCAL_DATA_PATH):
        print(
            f"❌ Erro: O arquivo do dataset não foi encontrado em '{LOCAL_DATA_PATH}'."
        )
        print(
            "   Por favor, garanta que o arquivo 'StressLevelDataset.csv' esteja na pasta 'data'."
        )
        return

    try:
        s3_client.head_object(Bucket=BUCKET_NAME, Key=MINIO_OBJECT_NAME)
        print(f"Dataset '{MINIO_OBJECT_NAME}' já existe no bucket.")
    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print(f"Dataset '{MINIO_OBJECT_NAME}' não encontrado. Fazendo upload...")
            s3_client.upload_file(LOCAL_DATA_PATH, BUCKET_NAME, MINIO_OBJECT_NAME)
            print(f"✅ Dataset '{MINIO_OBJECT_NAME}' enviado com sucesso.")
        else:
            print(f"❌ Erro ao verificar o objeto no bucket: {e}")
            return

    print("\n--- Configuração do ambiente MinIO concluída! ---")


if __name__ == "__main__":
    setup_minio()
