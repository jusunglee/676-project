from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stop_words =  set(stopwords.words('english'))
ps = PorterStemmer()
import pandas as pd

def __letters_only__(word):
    for x in word:
        if x not in set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            return False
    return True


def __not_stop_word__(word):
    return word not in stop_words


def __word_filter__(word):
    return __letters_only__(word) and __not_stop_word__(word)


def get_filtered_words(post):
    filtered_words = filter(lambda word: __word_filter__(word.lower()), post.split())
    stemmed_words = map(lambda word: ps.stem(word), filtered_words)
    return stemmed_words


def get_bag_of_words(word_column='posts',df=pd.read_csv('mbti_1.csv'), min_df=2):
    '''
    input:
        - df: pandas dataframe
        - word_column: string of column name that contains the corpus in the df
        - min_df: minimum number of occurences of words to include in bag of words. i.e. must appear x times.
    output:
        - list of words in the bag of words
        - the bag of words matrix for each row and word
    '''
    rows = [row[word_column].split('|||') for _, row in df.iterrows()]
    corpus = [' '.join([ps.stem(i) for i in row if __word_filter__(i)]) for row in rows]
    vectorizer = CountVectorizer(min_df=min_df)
    X = vectorizer.fit_transform(corpus)
    return vectorizer.get_feature_names(), X
