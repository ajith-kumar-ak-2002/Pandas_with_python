import pandas as pd

data = {
    'Name': ['Ajith', 'Kumar', 'Sai', 'Krishna', 'Babu', 
             'Bunty', 'Yuvaraj', 'Nanda', 'Ram', 'Krishna'],
    'Grade': ['A', 'A', 'B', 'A', 'B',
              'B', 'A', 'B', 'B', 'A'],
    'Subject': ['Math', 'Math', 'Math', 'Math', 'Math',
                'Science', 'Science', 'Science', 'Science', 'Science'],
    'Marks': [87, 93, 76, 89, 91,
              85, 83, 78, 90, 86]
}

df = pd.DataFrame(data)
print(df)


# What is groupby()?
            #The groupby() function in pandas is used to split the data into groups, apply an Operation,
            # and then combain the result.
print(df.groupby('Grade').count())


    #Aggregation Function (Mean Marks by grade)
print(df.groupby('Grade')['Marks'].mean())

    #Total Marks by Subject
print(df.groupby('Subject')['Marks'].sum())

    #Count of Students in each Grade
print(df.groupby('Grade')['Name'].count())

    #Groupby Multiple Columns
print(df.groupby(['Grade', 'Subject'])['Marks'].mean())

    #Multiple Aggregation with agg()
print(df.groupby('Subject')['Marks'].agg(['mean', 'max', 'min', 'count']))

    #Rename Columns in aggregation
print(df.groupby('Subject')['Marks'].agg(
    average = 'mean',
    highest = 'max',
    lowest = 'min'
))

