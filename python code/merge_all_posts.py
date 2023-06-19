import pandas as pd
import glob
# merge all files names ending with *_new_photos
# to generate a new file named 'all_flickr_post.csv' containing all flickr posts

# Get a list of all the file names
file_names = glob.glob('*_new_photos.csv')

# Read the first file
merged_df = pd.read_csv(file_names[0])

# Loop over the rest of the files and append them to the merged_df
for file_name in file_names[1:]:
    df = pd.read_csv(file_name)
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# Save the merged data frame to a new CSV file
merged_df.to_csv('all_flickr_post.csv', index=False)

