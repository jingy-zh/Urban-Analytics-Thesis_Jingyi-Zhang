import pandas as pd

# Read the data from the CSV file into a pandas DataFrame
# replace file
df = pd.read_csv('Civic Plaza or Square_flickr_posts.csv')

# check initial number of rows
print(f"Initial number of rows: {len(df)}")

# remove duplicates
df = df.drop_duplicates()

# check number of rows after removing duplicates
print(f"Number of rows after removing duplicates: {len(df)}")

# save the cleaned DataFrame back to the CSV file
df.to_csv('Civic Plaza or Square_flickr_posts.csv', index=False)


# replace file name

# 'Mini Park_flickr_posts.csv',
# 'Neighborhood Park or Playground_flickr_posts.csv',
# 'Regional Park_flickr_posts.csv',
