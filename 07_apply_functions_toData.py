import pandas as pd

df = pd.read_csv("StudentDataset.csv")
print(df.head(10))


print(df.shape)
print(df.info())
print(df.describe())




#Understanding apply() Function
    #Basic Syntax:
        #df['column'].apply(function) - applies to each element in a column
        #df.apply(function, axis=1) - applies to each row
        #df.apply(function, axis=0) - applies to each column
def pass_fail(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"
    
    ##Apply this function to Math_Score column
df['Math_Result'] = df['Math_Score'].apply(pass_fail)
print(df[['Student_Name', 'Math_Score', 'Math_Result']].head(10))




#Using Lambda Function
    #What is Lambda Function? A Lambda Function is Small,one line function that doesn't need a name.

    #Instead of creating a Saperate function, we can use lambda 
df['Science_Result'] = df['Science_Score'].apply(lambda X: "Pass" if X >= 50 else "Fail")
print(df[['Student_Name', 'Science_Score', 'Science_Result']].head(10))




#Convert Scores to Letter Grades
    #Convert Score to letter grades using lambda 
df['Math_Result'] = df['Math_Score'].apply(
    lambda X: 'A' if X >= 90 else 'B' if X >= 80 else 'C' if X >= 70 else 'D' if X >= 60 else 'F'
)
df['Is_Adult'] = df['Age'].apply(lambda X: "Yes" if X >= 20 else "No")
print(df[['Student_Name', 'Math_Score', 'Math_Result', 'Age', 'Is_Adult']].head(10))




#Using map() Function
    #What is map()? Similer to apply() but works great with dictionaries for value mapping
    #Create a mapping dictionary
grade_mapping = {
    'A': 'Excellent',
    'B': 'Good',
    'c': 'Average',
    'D': 'Below Average',
    'F': 'Poor'
}
    #Use map() to convert grades to descriptions
df['Grade_Description'] = df['Math_Result'].map(grade_mapping)
print(df[['Student_Name', 'Math_Result', 'Grade_Description']].head(10))


    

##Apply Functions to Multiple Columns (Row-wise)
    #Sometimes we need to use multiple columns together to create new data.

    #Calculate average score for each student
def Avg_Score(row):
    return(row['Math_Score'] + row['Science_Score'] + row['English_Score']) / 3
df['Student_avg_Score'] = df.apply(Avg_Score, axis=1)

    ## Calculate total score using lambda
df['Total_Score'] = df.apply(lambda row: row['Math_Score'] + row['Science_Score'] + row['English_Score'], axis=1)
print(df[['Student_Name', 'Math_Score', 'Science_Score', 'English_Score', 'Student_avg_Score', 'Total_Score']])    