import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd
import plotly.express as px
import matplotlib as mtp

df =pd.read_csv('data_set_plus.csv')
filter = df['Adaptations'] == 1
adap_df = df[filter]


group = df[['Title', 'Year']].sort_values('Year').groupby(df['Year'], sort=True)
group2 = df[['Author', 'Year']].sort_values('Year').groupby(df['Year'], sort=True)
group3 = adap_df[['Adaptations', 'Year']].dropna().sort_values('Year').groupby(df['Year'], sort=True)
group4 =df[['Awards_no', 'Year']].dropna().sort_values('Year').groupby(df['Year'], sort=True)

new_df = group.size().reset_index()
new_df2 = group2.size().reset_index()
new_df3 = group3.size().reset_index()
new_df4 = group4.size().reset_index()

filter2 = (df['Year'] == 2006) & (df['Average_rating'] > 4.2)

best = df[filter2].sort_values('Average_rating', ascending=False)

fig = px.scatter_3d(best, x='Pages', y=best['Rating']/1000, z='Average_rating', color='Series',hover_name='Title',title='The Best books of 2006')
pyo.plot(fig)


# print(best)
# best.to_csv('bestof2006.csv', index=False)










