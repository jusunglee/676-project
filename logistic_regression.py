from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
import numpy as np
from bag_of_words import get_bag_of_words, get_filtered_words
import pandas as pd
import collections


class MBTILogisticRegressionWithBagOfWords:
    def __init__(self):
        '''
        mbti_type_series = df['type']
        '''
        words, bag_of_words = get_bag_of_words()
        df = pd.read_csv('mbti_1.csv')
        mbti_type_series = df['type']
        self.words = words
        self.i_classifier = None
        self.n_classifier = None
        self.t_classifier = None
        self.j_classifier = None
        self.__train__(mbti_type_series, bag_of_words, words)


    def __train__(self, mbti_type_series, bag_of_words, words):
        y = mbti_type_series
        X = pd.DataFrame(bag_of_words.todense(), columns=words)

        self.i_classifier = LogisticRegression(random_state=0, solver='liblinear')
        self.i_classifier.fit(X, y.apply(lambda x: x[0] == 'I'))

        self.n_classifier = LogisticRegression(random_state=0, solver='liblinear')
        self.n_classifier.fit(X, y.apply(lambda x: x[1] == 'N'))

        self.t_classifier = LogisticRegression(random_state=0, solver='liblinear')
        self.t_classifier.fit(X, y.apply(lambda x: x[2] =='T'))

        self.j_classifier = LogisticRegression(random_state=0, solver='liblinear')
        self.j_classifier.fit(X, y.apply(lambda x: x[3] == 'J'))

                
                
    def classify(self, corpus):
        corpus = get_filtered_words(corpus)
        counter = collections.Counter(corpus)
        bow_row = [[counter.get(word, 0) for word in self.words]]

        answer = [None, None, None, None]
        probabilities = [None, None, None, None]

        i_prob = self.i_classifier.predict_proba(bow_row)[0][0]
        if i_prob > 0.5: 
            answer[0] = 'I'
            probabilities[0] = i_prob
        else:
            answer[0] = 'E'
            probabilities[0] = 1 - i_prob

        n_prob = self.n_classifier.predict_proba(bow_row)[0][0]
        if n_prob > 0.5: 
            answer[1] = 'N'
            probabilities[1] = n_prob
        else:
            answer[1] = 'S'
            probabilities[1] = 1 - n_prob

        t_prob = self.t_classifier.predict_proba(bow_row)[0][0]
        if t_prob > 0.5: 
            answer[2] = 'T'
            probabilities[2] = t_prob
        else:
            answer[2] = 'F'
            probabilities[2] = 1 - t_prob

        j_prob = self.j_classifier.predict_proba(bow_row)[0][0]
        if j_prob > 0.5: 
            answer[3] = 'J'
            probabilities[3] = j_prob
        else:
            answer[3] = 'P'
            probabilities[3] = 1 - j_prob

        return ''.join(answer), probabilities[0] * probabilities[1] * probabilities[2] * probabilities[3]
            


# model = MBTILogisticRegressionWithBagOfWords()
# print(model.classify('  its not the end of the world please relax theres still music and art'))
