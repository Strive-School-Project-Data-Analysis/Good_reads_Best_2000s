import pandas as pd
a = {'url':'https://www.dgdg.com','title':'The book thief', 'author':'Markus Zusak', 'no_reviews':53463,'no_ratings':46577647,'avg_rating':4.3,'no_pages':756,'year':2003,'series':0,'genres':['war','fiction'],'awards':['bestbook2004','award1'],'places':'Germany'}

b = {'url':'https://www.dgdgfdg.com','title':'The Hunger games', 'author':' Suzanne Collins', 'no_reviews':46547, 'no_ratings':46574658,'avg_rating':4.3,'no_pages':432,'year':2009,'series':1,'genres':['drama','fiction'],'awards':'1award','places':'panem'}

c = {'url':'https://www.dgdhgg.com','title':'How to kill a mockingbird', 'author':'Harper collins', 'no_reviews':45345,'no_ratings':234254,'avg_rating':4.6,'no_pages':543,'year':2001,'series':0,'genres':'fiction', 'awards':['2award','4award'],'places':'usa'}

list_dict = [a, b, c]

test_df = pd.DataFrame(list_dict)
test_df.to_csv('test_csv.csv')
print(test_df)