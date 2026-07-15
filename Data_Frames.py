import pandas as pd

#Exproing Data Frame Properities in pandas
## shape, size, index, columns
## dtype, ndim, values, axes
## Data Inspection using info() , describe()
## How to access rows , columns and cells using direct access .iloc and .loc
## memory Usage

#Create a simple DataFrame

data = {
    "Name": ["Ajith", "Raj", "Babu"],
    "Subjects": ["Maths", "Science", "Social"],
    "Marks": [56, 54, 47],
    "Passed": [True, True, False]
}
df = pd.DataFrame(data)
df                              #Proper Table format will written
print(df)                       #Unstructured Table formate will return


## Basic structure
    #Shape ---(rows , columns)
df.shape
print(df.shape)             #Both Will Work

    #Size ---Total No of Elements(rows * columns)
df.size
print(df.size)

    #ndim ---No of diminision 
df.ndim   
print(df.ndim)


## Labels and metadata
    #Index --- rows index
df.index
print(df.index)

    #columns --- Column Labels
df.columns
print(df.columns)

    # Axes ---Returs both rows and columns labels
df.axes
print(df.axes)


## Data Types and internal Values
    #dtypes --- Datatypes of each columns
df.dtypes
print(df.dtypes)

    # Values --- It will Return in arrays
df.values
print(df.values)


## Data Inspection Tools
    ##These are Used to Understand large Datasets Quickly
    #info() --- Structure, Non-Null Cound, Datatype
df.info()
print(df.info())

    #describe() ---Statistics summary (Numeric Only)
df.describe()
print(df.describe())

    #Memory_Usage()  ---Memory Used by Each Column
df.memory_usage()
print(df.memory_usage())


## Find Data Type Issues
    #Check for Object (String) columns 
df.select_dtypes(include= 'object')
print(df.select_dtypes(include='object'))

    #Check for Numeric columns
df.select_dtypes(include='number')
print(df.select_dtypes(include='number'))

    #Check for Bool columns
df.select_dtypes(include='bool')
print(df.select_dtypes(include='bool'))


## Accessing Data in a Data Frame
    #Access Single Column
df['Marks']
print(df["Marks"])

    #Access Multiple Columns 
df[["Name", "Marks"]]
print(df[["Name", "Marks"]])

    #Access row by Position using .iloc
df.iloc[0:2]
print(df.iloc[0:2])    #It will be not Include 2 row

    #Access row by label using .loc
df.loc[0:2]
print(df.loc[0:2])     #It Will Be include 2 row also 

    #Access Specific Cell
df.iloc[1,2]            #2nd row and 3rd Column
print(df.iloc[1,2])

    #Access Cell by Label
df.loc[2, 'Passed']
print(df.loc[2, "Passed"])

    #Access Multiple rows and columns
df.loc[0:2, ["Name", "Subjects"]]
print(df.loc[0:2, ['Name', 'Subjects']])