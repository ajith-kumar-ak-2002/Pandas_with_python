import pandas as pd

df = pd.read_csv('student_mental_health.csv')
print(df.head())

print(df[df['age'] > 20])


print(df[(df['age'] > 20) & (df['gender'] == 'Male') & (df['year_of_study'] == 3)])


print(df[df['gender'].str.startswith('M')])



f = df[df['physical_activity_days_per_week'] < 3]
f.reset_index(inplace=True)
print(f)