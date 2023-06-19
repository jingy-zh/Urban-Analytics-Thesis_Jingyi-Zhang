import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns
# correlation analysis
# Pearson Correlation Coefficient

# load data
df = pd.read_csv('Neighborhood Park or Playground_post_count.csv')  # replace files

# Calculate the Pearson correlation coefficient and the p-value
corr, p_value = pearsonr(df['posts_count'], df['facilities_count'])

# print the results
print('Pearson Correlation Coefficient: ', corr)

# scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='facilities_count', y='posts_count', data=df)

# regression line
sns.regplot(x='facilities_count', y='posts_count', data=df)

# title and labels
# replace titles
plt.title('Neighborhood Park or Playground')  # Correlation between Number of Facilities and Number of Posts
plt.xlabel('Number of Facilities')
plt.ylabel('Number of Posts')

# show the plot
plt.show()
