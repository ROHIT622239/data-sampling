import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics as st
import csv
import pandas as pd 

df = pd.read_csv('newdata.csv')
data=df['average'].tolist()
def randomsetofmean (counter):
    dataset = []
    for i in range(0,counter):
        random_index =random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean=st.mean(dataset)
    return mean

def show_fig(meanlist):
    df=meanlist
    mean = st.mean(df)
    fig=ff.create_distplot([df],['average'],show_hist=False)
    fig.show()

def setup():
    meanlist=[]
    for i in range (0,1000):
        setofmeans = randomsetofmean(100)
        meanlist.append(setofmeans)

    show_fig(meanlist)


setup()