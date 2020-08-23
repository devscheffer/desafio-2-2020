class cls_Model_Document:
    def __init__(self):
        self.dict_doc = {}

    def doc_create(self):
        dict_doc = {
        'param': {
            'id' : []
            ,'model': []
            ,'accuracy': []
            ,'method': []
            ,'classifier': []
            ,'description': []
            }
        }
        self.dict_doc = dict_doc


    def doc_set_id(self,text):
        # self.dict_doc['param']['id'].append(text)
        self.dict_doc['param']['id'] = text


    def doc_add_method(self,text):
        self.dict_doc['param']['method'].append(text)

    def doc_add_model(self,text):
        self.dict_doc['param']['model'].append(text)

    def doc_add_classifier(self,text):
        self.dict_doc['param']['classifier'].append(text)

    def doc_add_description(self,text):
        self.dict_doc['param']['description'].append(text)

    def doc_add_accuracy(self,text):
        self.dict_doc['param']['accuracy'].append(text)

