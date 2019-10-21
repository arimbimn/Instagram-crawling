import csv
import pandas as pd

data = pd.read_csv('dataframe.csv')
#print(df)

print("Dataset yang dimiliki :")
likes = data['likes'].count()
likes = data['likes'].astype(int)
total_likes = data.loc[:,['account','likes']]
print(total_likes)
print("=======================================================")
print("Jumlah Likes Terbanyak dimiliki oleh:")
print(total_likes.max())


#private = data['private']
private = data.loc[:,['account', 'private']]
private = private.drop_duplicates()
print(private)

count = 0
for index, row in private.iterrows():
    if row['private'] == True:
        count = count + 1
print("=======================================================")
print("Jumlah Account Instagram yang di private: ")
print(count)
