# %%
import pandas as pd

# %% Load Data
path = 'KPMG_VI_New_raw_data_update_final.xlsx'
df_transc = pd.read_excel(path, sheet_name=1, header=1)
print(df_transc.tail())
print(df_transc.describe())
print(df_transc.columns)

# %%
df_custs = pd.read_excel(path, sheet_name=2, header=1)
print(df_custs[:10])
df_custs.drop(['Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20'], axis=1, inplace=True)
print(df_custs.head())
print(df_custs.describe())
print(df_custs.columns)

# %%
df_cust_demg = pd.read_excel(path, sheet_name=3, header=1)
print(df_cust_demg.head())
print(df_cust_demg.describe())
print(df_cust_demg.columns)


# %%
df_cust_addr = pd.read_excel(path, sheet_name=4, header=1)
print(df_cust_addr.tail())
print(df_cust_addr.describe())
print(df_cust_addr.columns)


# %% Function to do analysis
def analyze(df):
    # get data types
    print(df.dtypes)
    # find unique values and check if nan in columns
    for col in df.columns:
        print(f"Column Name: {col}")
        print(f"Number of unique values: {df[col].nunique()}")
        print(f"None Values?: {df[col].isna().values.any()}")
        print(f"Number of None: {df[col].isna().sum()}")
        if df[col].dtypes == 'object':
            print(f"Unique values: {df[col].unique()}")
            print(f"Value Counts: \n{df[col].value_counts()}")
        elif df[col].dtypes == 'int' or 'float':
            print(f"{col} described: \n{df[col].describe()}")
        print("\n\n")


# %%
analyze(df_custs)
