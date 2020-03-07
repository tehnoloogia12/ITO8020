### algne töökäik pärineb https://www.edureka.co/blog/apriori-algorithm/

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
df = pd.read_excel('C:\\Users\\pealik\\Documents\\kodu2\\Online Retail.xlsx')
print('--- df.head')
print(df.head())
df.head()
df['Description'] = df['Description'].str.strip()
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)

df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]

#algselt basket = (df[df['Country'] =="France"]
basket = (df[df['Country'] =="United Kingdom"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))
print('--- basket')
print(basket)

df=basket
# ekspordi kõik basketid
#df.to_csv('C:\\Users\\pealik\\Documents\\kodu2\\df2-basket.csv', index=False, header=True)

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace=True, axis=1)

df=basket_sets
# ekspordi csv-sse
#df.to_csv('C:\\Users\\pealik\\Documents\\kodu2\\df3-basket_sets.csv', index=False, header=True)

# originaalis min_support=0.07, vähendame selle 0.02 peale
frequent_itemsets = apriori(basket_sets, min_support=0.02, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

rules[ (rules['lift'] >= 6) &
      (rules['confidence'] >= 0.8) ]

df=rules
# ekspordi lõpptulem
df.to_csv('C:\\Users\\pealik\\Documents\\kodu2\\df4-rules-conf80-lift6.csv', index=False, header=True)
