import pandas as pd  # Import the pandas library for data manipulation

# Read the CSV file into a DataFrame
output = pd.read_csv('datas.csv')

# Initialize column and row boundaries
col_strat = 0
col_end = 5
row_start = 0
row_end = 10

# Loop through the DataFrame in chunks of 10 rows
for _ in range((len(output.axes[0]) + 1) // 10):
    # Loop through the DataFrame in chunks of 5 columns
    for _ in range((len(output.columns)) // 5):
        # Create a new DataFrame for the specified row and column slice
        df = pd.DataFrame(output.iloc[row_start:row_end, col_strat:col_end])
        # Print the DataFrame as a string
        print(df.to_string())

        # Update column boundaries for the next chunk
        col_strat += 5
        col_end += 5

    # Reset column boundaries for the next set of rows
    col_strat = 0
    col_end = 5

    # Update row boundaries for the next chunk of rows
    row_start += 10
    row_end += 10

    # Print a separator line for clarity
    print('<=============================================>\n<=============================================>')
