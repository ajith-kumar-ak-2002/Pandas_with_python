import pandas as pd

df = pd.read_csv("StoreData.csv")
print(df.head())


# Understand the Dataset
print(df.shape)
print(df.info())
print(df.sample(5))


#Clean Column Names
    #Remove Extra Spaces
df.columns = df.columns.str.strip().str.title().str.replace("_", " ")
print(df.columns)    

    #Trim Whitespaces from text
for col in df.select_dtypes(include=['object' , 'string']).columns:
    df[col] = df[col].str.strip()

    #Remove Duplicate Rows
print("Before: ", len(df))
df.drop_duplicates(inplace=True)
print("After: " , len(df))

#Convert Datatype   
    #Remove % and convert in float
df['Discount'] = df['Discount'].str.replace('%', '', regex=False)
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')
print(df['Discount'])

    #convert Date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
print(df['Order Date'])


    #Convert Numeric Columns
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
print(df['Quantity'])

df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
print(df['Sales'])

df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
print(df['Profit'])