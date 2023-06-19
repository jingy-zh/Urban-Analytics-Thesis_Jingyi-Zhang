import pandas as pd

# Read the data from the CSV file into a pandas DataFrame
df = pd.read_csv('Civic Plaza or Square_new_photos.csv')

# Check initial number of rows
print(f"Initial number of rows: {len(df)}")

# Remove duplicates
df = df.drop_duplicates()

# Check number of rows after removing duplicates
print(f"Number of rows after removing duplicates: {len(df)}")

# Save the cleaned DataFrame back to the CSV file
df.to_csv('Zoological Garden_new_photos.csv', index=False)


# replace file name

# 'Mini Park_new_photo.csv',
# 'Neighborhood Park or Playground_new_photo.csv',
# 'Regional Park_new_photo.csv',
