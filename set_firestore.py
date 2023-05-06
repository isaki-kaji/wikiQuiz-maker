from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("〇〇.json")
firebase_admin.initialize_app(cred)
db = firestore.client()