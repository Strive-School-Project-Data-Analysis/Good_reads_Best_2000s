import pandas as pd
import numpy as np
import re
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.express as px
import requests
import geopy
import plotly.graph_objs as go
import plotly.offline as pyo
import matplotlib as plt

cf.go_offline()
threshhold = 4
def min_max(series):
    """ Returns the Min-Max normalised values for the average ratings value"""
    max = series.max()
    new_dseries = series.apply(lambda x: 1 + (((x-threshhold)/(max-threshhold)) * 9))
    return new_dseries


def norm_series(series):
    """ Returns the Normalised values for the Average rating values"""
    pd_series_mean = series.mean(skipna=True)
    max = series.max()
    # print(pd_series_mean)
    normed = series.apply(lambda x: 6 + ((x-pd_series_mean)/(max-threshhold)) * 9)
    return normed


df = pd.read_csv('big_books_clean.csv')
filter1 = df['Average_rating'] >= threshhold

min_max_norm = min_max(df['Average_rating'][filter1])
normalised = norm_series(df['Average_rating'][filter1])
print(normalised)

trace0 = go.Histogram(x=min_max_norm,
                      name='Average rating min max',
                      opacity=.5)
trace1 = go.Histogram(x=normalised,
                      name='Average rating normalised',
                      opacity=.5)

data = [trace0, trace1]
layout = go.Layout(title='Average rating Distribution')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)


