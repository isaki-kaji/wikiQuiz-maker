from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
def set_firestore(json_name):
    cred = credentials.Certificate(json_name)
    firebase_admin.initialize_app(cred)
    db = firestore.client()