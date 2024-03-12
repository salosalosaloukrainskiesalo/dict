import pandas as pd

df_produkty = pd.read_csv('zadanie_1.csv', sep=';')
product_a_data = df_produkty[df_produkty['Product'] == 'Product_A']
sum = (product_a_data['Amount'] * product_a_data['Quantity']).sum()
n = product_a_data['Quantity'].sum()

print('Średnia dla A:', sum/n)

product_a_data = df_produkty[df_produkty['Product'] == 'Product_B']
sum2 = (product_a_data['Amount'] * product_a_data['Quantity']).sum()
n = product_a_data['Quantity'].sum()

print('Średnia dla B:', sum2/n)

product_a_data = df_produkty[df_produkty['Product'] == 'Product_C']
sum3 = (product_a_data['Amount'] * product_a_data['Quantity']).sum()
n = product_a_data['Quantity'].sum()

print('Średnia dla C:', sum3/n)