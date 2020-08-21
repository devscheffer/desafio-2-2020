class cls_Model_Document:
    def __init__(self):
        self.dict_doc = {}

    def doc_create(self):
        dict_doc = {
        'model': []
        ,'accuracy': []
        ,'method': []
        ,'classifier': []
        ,'description': []
        }
        self.dict_doc = dict_doc

    def doc_add_method(self,text):
        self.dict_doc['method'].append(text)
    def doc_add_model(self,text):
        self.dict_doc['model'].append(text)
    def doc_add_classifier(self,text):
        self.dict_doc['classifier'].append(text)
    def doc_add_description(self,text):
        self.dict_doc['description'].append(text)
    def doc_add_accuracy(self,text):
        self.dict_doc['accuracy'].append(text)


