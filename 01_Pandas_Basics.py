import pandas as pd 

#Pandas Series          ---- one Dimenision
marks = pd.Series([85, 45, 76, 98])
print("Series in Pandas: \n", marks)


#DataFrame on Pandas        --- Two Diminisions
data = {
    'Name': ['AJith', 'Kumar', 'Sai', 'kiran'],
    'marks': [45, 65, 76,86]
}

name_marks = pd.DataFrame(data)
print("Data Frame in Pandas: \n", name_marks)