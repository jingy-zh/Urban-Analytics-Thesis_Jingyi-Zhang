import pandas as pd

# read "Recreation_and_Parks_Properties.csv"
# and split parks by park categories
# generate new files named *_parks.csv

# Load the CSV file
df = pd.read_csv("Recreation_and_Parks_Properties.csv")

# Get the unique categories in the "PropertyType" column
categories = df["PropertyType"].unique()

# Loop through each category and create a new CSV file with only rows from that category
for category in categories:
    # Create a new DataFrame with only rows from the current category
    category_name = df[df["PropertyType"] == category]

    # Save the new DataFrame to a CSV file with a name based on the category
    filename = f"{category}_parks.csv"
    category_name.to_csv(filename, index=False)
