import pandas as pd
# this file count the posts of each *_flickr_posts file,
# and generate a new file whtich named *_post_count
# Read the data from the CSV file into a pandas DataFrame

# replace file name for each category of parks

# 'Civic Plaza or Square_flickr_posts.csv',
# 'Mini Park_flickr_posts.csv',
# 'Neighborhood Park or Playground_flickr_posts.csv',
# 'Regional Park_flickr_posts.csv']

df = pd.read_csv('Mini Park_new_photos.csv')

# Group by 'park_name' and count the number of posts in each park
park_post_count = df.groupby('location_name').size().reset_index(name='post_count')

# Calculate the total number of posts
total_posts = park_post_count['post_count'].sum()

# Append total count to the DataFrame
total_row = pd.DataFrame([['Total', total_posts]], columns=['park_name', 'post_count'])
park_post_count = pd.concat([park_post_count, total_row])

# Save the result to a new CSV file
# replace file name for each category
park_post_count.to_csv('Mini Park_post_count', index=False)

