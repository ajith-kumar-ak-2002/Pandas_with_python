import pandas as pd

df = pd.read_csv("titanic_dataset.csv")
print(df.head())

## Checking Missing Values
print(df.isnull())                            #Returns Total Null Values in the formate of TRUE or FALSE

print(df.isnull().sum())                      #Returns Null Values only columns wise

print(df.isnull().sum().sum())                #Returns How Many null Values in the Entire Dataset

print(df.isnull().sum() / len(df) * 100)      #Returns Null Percentage 


# Dropping Mising Values
print(df.dropna())                            #Drop All Null values

print(df.dropna(axis=1))                      #Drop Null Columns

print(df.dropna(subset=['Cabin']))            #Drop Null Values in a Particular Column 


#Filling Missing Data With (Mean , Mode, Median)

fill_with_mean = df['Age'].fillna(df['Age'].mean)
print(fill_with_mean)                          #in the age column null values fill with mean values

fill_with_medien = df['Age'].fillna(df['Age'].median)
print(fill_with_medien)                        #in the age column null values fill with medien values

fill_with_mode = df['Embarked'].fillna(df['Embarked'].mode()[0])
print(fill_with_mode)                           #in the Embarked Column null Values fill with mode Values

fill_with_custom = df['Cabin'].fillna("Info Null")
print(fill_with_custom)                        #in the Cabin Column null values fill with Custom information

forward_fill = df['Age'].fillna(0)
print(forward_fill)                            #in the age column null values fill with 0 values                      