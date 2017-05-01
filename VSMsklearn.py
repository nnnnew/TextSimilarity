from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dataloader import load_data
import numpy as np

class VectorSupportModel:

    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer()
        self.document = ();
        self.path_file = [];

    def similaity_score(self, text):
        score = cosine_similarity(text, self.tfidf_matrix)
        return score

    def tranfrom_vector(self):
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.document)

    def initailize_doc(self):
        doc_list = []
        for file in self.path_file:
            doc = load_data(file)
            doc_list.append(doc)
        self.document = tuple(doc_list)

    def initailize_path(self):
        path = '/Users/nnnnew/PycharmProjects/VectorSpaceModel/data/'
        for i in range(88):
            num_file = i + 1
            if(num_file < 10):
                file_name = '0' + str(num_file)
            else:
                file_name = str(num_file)
            path_file = path + file_name + '.txt'
            self.path_file.append(path_file)

    def searching(self):
        self.init_variable()
        while True:
            text = input('Searching word: ')
            t = self.tfidf_vectorizer.transform([text])
            score = self.similaity_score(t)[0]
            for i in range(5):
                max = np.argmax(score)
                score[max] = -1
                print(self.document[max])
                print('-------------------------------------------------------------------')

    def init_variable(self):
        self.initailize_path()
        self.initailize_doc()
        self.tranfrom_vector()

if __name__ == '__main__':
    v = VectorSupportModel()
    v.searching()