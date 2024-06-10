import os
from dotenv import load_dotenv
import pyrebase

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Verificar que las variables de entorno se han cargado correctamente
private_key = os.getenv("SERVICE_ACCOUNT_PRIVATE_KEY")
if not private_key:
    raise ValueError("SERVICE_ACCOUNT_PRIVATE_KEY no está definido en el archivo .env")

service_account = {
    "type": "service_account",
    "project_id": "marketplace-6efa7",
    "private_key_id": "afd6a756fc194b1e74f5153dfd3e280e44f71001",
    "private_key": private_key.replace("\\n", "\n"),
    "client_email": "firebase-adminsdk-p3onu@marketplace-6efa7.iam.gserviceaccount.com",
    "client_id": "101195155078292401693",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-p3onu%40marketplace-6efa7.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

firebaseConfig = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": "marketplace-6efa7.firebaseapp.com",
    "projectId": "marketplace-6efa7",
    "storageBucket": "marketplace-6efa7.appspot.com",
    "messagingSenderId": "52600668814",
    "appId": "1:52600668814:web:439086a7d8cb1170a1d0cf",
    "serviceAccount": service_account,
    "databaseURL": "gs://marketplace-6efa7.appspot.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)