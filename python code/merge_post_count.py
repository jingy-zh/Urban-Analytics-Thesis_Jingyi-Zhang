import pandas as pd
import glob

# to merge the number of posts in all parks from all categories
# Write the merged dataframe to a new CSV file named 'merged_posts_count.csv'

# Get a list of all CSV files in current directory
csv_files = glob.glob('*_post_count.csv')

# Initialize an empty list to hold dataframes
dfs = []

# Loop through the list of CSV files
for filename in csv_files:
    # Read each file into a dataframe
    df = pd.read_csv(filename)

    # Extract category name from filename
    category_name = filename.split('_post_count.csv')[0]

    # Add a new column for category name
    df['category_name'] = category_name

    # Reorder the columns to make category_name the first column
    df = df[['category_name', 'park_name', 'posts_count', 'facilities_count']]

    # Append the dataframe to the list
    dfs.append(df)

# Concatenate all dataframes in the list
merged_df = pd.concat(dfs, ignore_index=True)

# Write the merged dataframe to a new CSV file
merged_df.to_csv('merged_posts_count.csv', index=False)
