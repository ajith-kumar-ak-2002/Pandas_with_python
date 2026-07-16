import pandas as pd

##Import And Export Datasets
    #import Dataset
df = pd.read_csv("student_mental_health.csv")
print(df)

    #First 5 Rows
df.head()
print(df.head())

    #Last 5 Rows
df.tail()
print(df.tail())

    #Random for Sample
df.sample()
print(df.sample(5))

    #Data Structure and Summary
df.info()
print(df.info())

    #Describe --- Summary Statistics for Numeric Columns
df.describe()
print(df.describe())

    #Custoom index
df_indexed = df.set_index('student_id')
df_indexed
print(df_indexed)

    #Access a row using new index
print(df_indexed.loc['STU1003'])