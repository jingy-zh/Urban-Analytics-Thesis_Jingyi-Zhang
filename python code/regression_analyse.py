import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#regression analysis using OLS model

df = pd.read_csv('Regional Park_post_count.csv')  # replace csv file

# Define independent variable (x) and dependent variable (y)
x = df['facilities_count']
y = df['posts_count']


# Add a constant to the independent variable
x = sm.add_constant(x)

# Perform the regression
model = sm.OLS(y, x)
results = model.fit()

# Print out the statistics
print(results.summary())

# Create a scatter plot of the data
sns.scatterplot(x='facilities_count', y='posts_count', data=df)

# Generate and plot the regression line
x_pred = pd.DataFrame({'facilities_count': range(0, df['facilities_count'].max()+1)})
x_pred = sm.add_constant(x_pred)
y_pred = results.predict(x_pred)
plt.plot(x_pred['facilities_count'], y_pred, color='red')
plt.title('Neighborhood Park or Playground')  # replace title

# Show the plot
plt.show()




