import pandas as pd

data = {
    'Name': ['AJith', 'Ravi', 'Sagar', 'Pavan', 'Babu'],
    'Math_Score': [85, 92, 78, 90, 88],
    'Science_Score': [89, 95, 80, 85, 91],
    'English_Score': [86, 87, 83, 80, 89]
}

df = pd.DataFrame(data)
print(df)



#Sort by One Column
    #We use sort_values() to sort data by a specific column.

    #Sort by Math_Score in ascending order
print(df.sort_values(by='Math_Score', ascending=True))

    #Sort by Science_Score in Descending Order
print(df.sort_values(by='Science_Score', ascending=False))



#Sorting by Index
    #Use sort_index() when you want to sort by row numbers or labels.
print(df.sort_index())







### Real-Life Use Case – Ranking Students
    ## Add Total_Score column
df['Total_Score'] = df['Math_Score'] + df['Science_Score'] + df['English_Score']

    ## Sort by Total_Score (high to low)
df_sorted = df.sort_values(by='Total_Score', ascending=False)
print(df_sorted)