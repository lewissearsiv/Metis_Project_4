#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:56:04 2020

@author: lewissears
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_rows', 500)
%config InlineBackend.figure_format = 'svg'
%matplotlib inline
sns.set()
from sklearn.decomposition import PCA
from nltk.cluster import KMeansClusterer
from py_files.vectorizer import Vectorizer_I_Hardly_Know_Her
from py_files.cleaner import mr_clean_and_tokenize

d2v_labels = pd.read_csv('d2v_labels.csv',index_col=0)
tokenized_tweets = df_trump['text'].apply(mr_clean_and_tokenize)
for tokens in tokenized_tweets:
    if 'amp' in tokens:
        tokens.remove('amp')
df_vectorized = Vectorizer_I_Hardly_Know_Her(tokenized_tweets)
pca_viz = PCA(n_components=2)
pca_viz.fit(df_vectorized)
pca_viz_df = pd.DataFrame(pca_viz.transform(df_vectorized))


d2v_labels.label.value_counts()


#graph
labels = d2v_labels.label
x = pca_viz_df[0]
y = pca_viz_df[1]
color = 'brgcmyk'
label_color = [color[l] for l in labels]
plt.scatter(x, y, c=label_color)
plt.title('Doc2Vec Clusters')


# plt.savefig('Doc2VecClusters.png');

