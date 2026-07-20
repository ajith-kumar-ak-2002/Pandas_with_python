## Python with pandas

imported pandas 
  * Pandas Series          ---- one Dimenision
  * DataFrame on Pandas        --- Two Diminisions

## Exproing Data Frame Properities in pandas
  * shape, size, index, columns
  * dtype, ndim, values, axes
  * Data Inspection using info() , describe()
  * How to access rows , columns and cells using direct access .iloc and .loc
  * memory Usage

## Importing & Exploring Datasets in Pandas
  * read_csv() and read_excel()
  * head(), tail(), sample() for preview
  * Real-world dataset walkthrough

## Filtering Data in Pandas     (Contain with "Student Mental Health Data Set")
  * Filter with Logical Conditions: >, <, ==, !=
  * Combine Conditions with & and |
  * Filter Text Columns using .str.contains() and .str.startswith()
  * Reset index after filtering
  * Filter Boolean columns (True / False)

## Handling Missing Data in Pandas    (Contain with "titanic_dataset")
  * Detecting missing values   
  * Dropping missing rows/columns
  * Filling missing data using mean, median, mode, or custom values

## Data Cleaning & Type Conversion in Pandas  (Contain with "Store Dataset")
  * Replacing missing or incorrect values
  * Renaming confusing column names
  * Converting column data types (e.g., strings to numbers)
  * Removing duplicate rows
  * Trimming whitespace and fixing inconsistent text

## Applying Functions to Data                 (Contain With " StudentDataset.csv ")
 ### Why is this important? Functions help us transform raw data into meaningful insights - like converting grades to letter grades, categorizing sales performance, or calculating custom metrics!
  * apply() for column/row-wise operations
      * What is apply()? It applies a function to each element in a column or row.
        ## Basic Syntax:
          * df['column'].apply(function) - applies to each element in a column
          * df.apply(function, axis=1) - applies to each row
          * df.apply(function, axis=0) - applies to each column
  * map() and lambda functions.
    # What is lambda? A lambda function is a small, one-line function that doesn't need a name.
       * Syntax: lambda x: expression
     # What is map()? Similar to apply() but works great with dictionaries for value mapping.
  * Creating new columns from logic
  * Use cases: grading, categorization

## Sorting Data in Pandas
   * sort_values()       We use sort_values() to sort data by a specific column. ( df.sort_values(by='column_name', ascending=True or False) )
   * Sorting by Index    Use sort_index() when you want to sort by row numbers or labels.
        ----- Real-Life Use Case – Ranking Students      --- calculate each student’s total score and then sort them to rank.
