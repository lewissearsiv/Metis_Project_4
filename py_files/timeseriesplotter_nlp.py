import statistics
import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn as sns
#pd.set_option('display.max_rows', 500)
#%config InlineBackend.figure_format = 'svg'
#%matplotlib inline
sns.set()



def WordVec_to_TimeSeries_Plotter(df, word,freq,theta,frame,save):
    '''This function takes a dataframe that has counts aggregated by month for a certain word.
    To use this function, take a word vectorizer and do a groupby with by month summing all 
    words. Input dataframe must have the year-month as DateTime and then input the dataframe, 
    the desired word, and the ammount of vertical lines you desire. The vertical lines should 
    be chosen after looking at the output graph and can't exceed 6. The labels for the
    vertical lines are given by theta. The final two variables are subject to interpretation.
    Input 'default' for a fitted frame and if you don't want to save the image. Otherwise, 
    give a range for the y-values of the graph as a list for frame and putting in a name
    for save will save it under the given name.'''
    
    #The Setup 
    ts = df['{}'.format(word)]
    df_ts = pd.DataFrame({'Frequency': ts.values})
    df_ts.index = [str(date) for date in ts.index]
    df_ts['counter'] = [i for i in range(len(df_ts))]
    most_freq_months = list(df_ts['Frequency'].sort_values(ascending = False).index[:freq])
    x_vals = [df_ts.loc[month].counter for month in most_freq_months]
    max_count = df_ts.Frequency.max()
    
    
    #####Disregard this section if you do not have multiword tokens. Change as desired:#####
    mwt = ['make_america_great_again', 'america_first', 'fake_news']
    if word in mwt:
        word_replaced = word.replace('_', ' ')
        string_list = word_replaced.split()
        capital_list = [word.capitalize() for word in string_list]
        final_text = ''
        for cap_word in capital_list:
            final_text += cap_word+ ' '
        title_word = final_text
    if word not in mwt:
        title_word = word.capitalize()   
    #########################################################################################  
    
    
    #This is the plotting function
    fig = plt.figure(figsize=(11,6))
    colors = ['r','darkviolet','dodgerblue','darkgreen','goldenrod','slategray']
    ax = fig.add_subplot(1,1,1)
    ax.plot(df_ts['Frequency'])
    plt.xticks(fontsize=14, fontweight = 'bold')
    plt.yticks(fontsize=14)
    ax.set_title("Frequency by Month: \"{}\"".format(title_word),fontsize=20,fontweight = 'bold', y=1.03)
    #Vertical lines
    for i in range(len(most_freq_months)):
        ax.axvline(x=x_vals[i], ymin=-1, ymax=0.95, color = colors[i], 
                    ls = ':')
        plt.text(x_vals[i],df_ts.loc[most_freq_months[i]].Frequency * 1.05,'{}'.format(most_freq_months[i]),rotation=theta, fontweight = 'bold')
    
    if frame == 'default':
        ax.set_ylim([-2,max_count*1.12])
    else:
        ax.set_ylim(frame)
    ax.xaxis.set_major_locator(plt.MaxNLocator(9))
    if save == 'default':
        return plt.show()
    else:
        plt.savefig('{}.png'.format(save))
        return plt.show()

