import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
df = pd.read_excel('C:\\Users\\pealik\\Documents\\kodu2\\Online Retail.xlsx')
print('--- df.head')
#print(df.head())
df.head()
df['Description'] = df['Description'].str.strip()
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)

df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]
#####df.to_csv('C:\\Users\\pealik\\Documents\\kodu2\\dataframe1.csv', index=False, header=True)
#print(df)

basket = (df[df['Country'] =="France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))
#print('--- basket')
#print(basket)
#basket
df=basket
df.to_csv('C:\\Users\\pealik\\Documents\\kodu2\\df2-basket.csv', index=False, header=True)


#print(basket)
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace=True, axis=1)

#print('--- basket_sets')
#print(basket_sets)
df=basket_sets
df.to_csv('C:\\Users\\pealik\\Documents\\kodu2\\df3-basket_sets.csv', index=False, header=True)
#print(df)
frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

#print('--- rules.head')
#print(rules.head())
rules[ (rules['lift'] >= 6) &
      (rules['confidence'] >= 0.8) ]

#print('--- rules')
#print(rules)
df=rules
df.to_csv('C:\\Users\\pealik\\Documents\\kodu2\\df4-rules.csv', index=False, header=True)
#print(df)
