import pandas as pd

# read in the spreadsheet as a pandas dataframe
df = pd.read_excel('path/to/spreadsheet.xlsx')

# define a function to split the first two words of a string into separate columns
def split_first_two_words(s):
    words = s.split(' ')
    return (words[0], ' '.join(words[1:]))

# apply the function to the 'Name' column and create new columns for the results
df[['Type', 'Name']] = df['Name'].apply(split_first_two_words).apply(pd.Series)

# save the cleaned-up spreadsheet as a new file
df.to_excel('./cleaned_up_spreadsheet.xlsx', index=False)