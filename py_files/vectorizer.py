'''This function takes a column from a dataframe that is cleaned and tokenized 
and puts it through NLTK CountVectorizer. After the df_vectorized dataframe is 
created, there is an option to delete words from consideration that are sparse.
'''
import pandas as pd
pd.set_option('display.max_rows', 500)
import numpy as np
import datetime
import re
import string
import nltk
import sklearn
from nltk.tokenize import MWETokenizer 
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

def Vectorizer_I_Hardly_Know_Her(cleaned_text):
    '''The input cleaned_text must be an array with each entry tokenized and 
    cleaned text. 
    The second part allows you to determine how many instances of a word
    justifies consideration.
    '''
    #Make a NLTK CountVectorizer DataFrame
    cv = CountVectorizer(analyzer=lambda x:x)
    vectorized_words = cv.fit_transform(cleaned_text).toarray()
    col_names = cv.get_feature_names()
    df_vectorized = pd.DataFrame(vectorized_words, columns = col_names)

    #Filtering out sparse words
    col_sums = df_vectorized.sum(axis = 0)
    important_words = [] 
    for i in range(len(col_sums)):
        #Give a threshhold minimum value
        if col_sums[i] > 15:
            important_words.append(col_sums.index[i])

    #final dataframe
    return df_vectorized[important_words]