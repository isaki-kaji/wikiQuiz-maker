def get_document(category,title):
    doc_ref = db.collection(category).document(title)
    doc_dict = doc_ref.get().to_dict()
    print(doc_dict["text"])