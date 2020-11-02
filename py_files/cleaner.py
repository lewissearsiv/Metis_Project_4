'''This is a simple and adjustable cleaning function for NLP which takes
a string and returns clean tokens for analysis. Used for sentiment analysis
of trumps tweets, but easy plug in play for other general projects.
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
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

def mr_clean_and_tokenize(text):
    '''In order: make text lowercase, tokenize with multiword phrases 
    if desired,remove numbers, remove all stop words as desired, and 
    remove all words with non-alphabetic symbols.'''
    
        #English stopwords
    stop_words = stopwords.words('english')
        #Add your stopwords in a list
    additional_stop_words = ['rt', 'https']
    stop_words.extend(additional_stop_words)
        #Add Multiword phrases. Add to multiwords so not deleted by .isalnum()
    mwe_tokenizer = MWETokenizer([('make','america','great','again'),('america','first')])
    multiwords = ['make_america_great_again', 'america_first']
    
    
        #Begin cleaning
    lower_text = text.lower()
    tokenize_text = mwe_tokenizer.tokenize(word_tokenize(lower_text))  
    #if no multiword tokens desired -------> tokenize_text = word_tokenize(lower_text)
    no_num = [re.sub('\w*\d\w*','',word) for word in tokenize_text]
    no_stop_text = [word for word in no_num if not word in stop_words]
    final_tokenized_text = [word for word in no_stop_text if word in multiwords or word.isalnum()]
    
    return final_tokenized_text