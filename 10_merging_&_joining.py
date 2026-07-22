import pandas as pd

#Students info
df_students = pd.DataFrame({
    'Student_ID': [101, 102, 103, 104],
    'Name': ['Aarav', 'Bhavya', 'Charan', 'Deepika'],
    'Grade': ['A', 'B', 'A', 'B']
})

# Test scores
df_scores = pd.DataFrame({
    'Student_ID': [101, 102, 104, 105],
    'Math_Score': [90, 85, 88, 95],
    'Science_Score': [92, 89, 84, 90]
})

print(df_students)
print(df_scores)


##Merging DataFrame using merge()
    #Default is INNER JOIN on common column (Student_ID)

    # Inner join (only matching rows)
inner_join = pd.merge(df_students, df_scores, on='Student_ID', how='inner')
print(inner_join)

    # Left join (keep all students, add matching scores)
left_join = pd.merge(df_students, df_scores, on='Student_ID', how='left')
print(left_join)

    # Right join (keep all scores, add matching student info)
right_join = pd.merge(df_students, df_scores, on='Student_ID', how='right')
print(right_join)

    # Outer Join (keep all rows from both)
outer_join = pd.merge(df_students, df_scores, on='Student_ID', how='outer')
print(outer_join)



##Concatenating DataFrames using concat()
    # Vertical stacking (add more student rows)
df_more_students = pd.DataFrame({
    'Student_ID': [106, 107],
    'Name': ['Esha', 'Farhan'],
    'Grade': ['A', 'B']
})

more_student = pd.concat([df_students, df_more_students])
print(more_student)

    # Horizontal stacking (add more columns side-by-side)
df1 = pd.DataFrame({ 'A' : [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({ 'C': [5, 6], 'D': [7, 8]})
print(pd.concat([df1, df2], axis=1))