# %%
import pandas as pd
import numpy as np
import datetime

# %% Load Data
path = 'KPMG_VI_New_raw_data_update_final.xlsx'
df_transc = pd.read_excel(path, sheet_name=1, header=1)
print(df_transc.tail())

df_new_custs = pd.read_excel(path, sheet_name=2, header=1)
print(df_new_custs[:10])
df_new_custs.drop(['Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20'], axis=1, inplace=True)
print(df_new_custs.head())

df_cust_demg = pd.read_excel(path, sheet_name=3, header=1)
print(df_cust_demg.head())

df_cust_addr = pd.read_excel(path, sheet_name=4, header=1)
print(df_cust_addr.head())

# %% Data Exploration
df_rel_transc = df_transc.drop(['transaction_date', 'online_order', 'order_status', 'brand', 'product_line',
                                'product_class', 'product_size', 'product_first_sold_date'], axis=1)
print(df_rel_transc.head())

# group by customer_id
gp_transc = df_rel_transc.groupby('customer_id')
# display first element in each
print(f"First Elements in each group: \n{gp_transc.first()}")
# print group with customer id 1
print(f"Customer ID 1 group: \n{gp_transc.get_group(1)}")

# create new dataframe to store sum of products, total list_price, total standard_cost
df_final_transc = pd.DataFrame(columns=['customer_id', 'total_number_of_products', 'total_list_price',
                                        'total_standard_cost'])

for name, group in gp_transc:
    num = len(gp_transc.get_group(name).index)
    price = gp_transc.get_group(name).list_price.sum()
    cost = gp_transc.get_group(name).standard_cost.sum()
    df_final_transc = df_final_transc.append(
        {'customer_id': name, 'total_number_of_products': num, 'total_list_price': price,
         'total_standard_cost': cost}, ignore_index=True)

# format data types of columns
df_final_transc.customer_id = df_final_transc.customer_id.astype('int')
df_final_transc.total_number_of_products = df_final_transc.total_number_of_products.astype('int')
print(f"\n {df_final_transc.head()}")
star = '*'
print('\n')
print(85 * star)
# add average list_price and average standard_cost
df_final_transc['av_list_price'] = round(df_final_transc.total_list_price / df_final_transc.total_number_of_products, 2)
df_final_transc['av_standard_cost'] = round(
    df_final_transc.total_standard_cost / df_final_transc.total_number_of_products, 2)
print(f"\n {df_final_transc[:10]}")

# %%
df_final_cust_demg = df_cust_demg.drop(['first_name', 'last_name', 'default'], axis=1)
print(df_final_cust_demg.head())
print(df_final_cust_demg.columns)

df_final_cust_addr = df_cust_addr.drop(['address', 'country'], axis=1)
print(df_final_cust_addr.head())
print(df_final_cust_addr.columns)

# %% Merge Dataframes
frames = [df_final_cust_addr.set_index('customer_id'), df_final_cust_demg.set_index('customer_id'),
          df_final_transc.set_index('customer_id')]

df_fin = pd.concat(frames, axis=1).reset_index()

print(df_fin.head())
print(df_fin.columns)
print(len(df_fin.index))



