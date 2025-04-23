#Task 1:load and explore the dataset 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the red wine dataset
try:
    df = pd.read_csv('winequality-red.csv', sep=';') # Note the semicolon separator
    print("Red wine dataset loaded successfully!")
except FileNotFoundError:
    print("Error: winequality-red.csv not found. Please make sure the file is in the correct directory.")
    exit()

# Display the first few rows to inspect the data
print("\nFirst few rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nInformation about the dataset:")
df.info()

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Explanation:
# - We import the pandas library for data manipulation.
# - We use a try-except block to handle the case where the CSV file might not be found. This is good practice for robust code.
# - `pd.read_csv('winequality-red.csv', sep=';')` loads the data into a pandas DataFrame. It's important to note that this dataset uses a semicolon (`;`) as the separator between values, not a comma.
# - `df.head()` displays the first 5 rows of the DataFrame, giving us a glimpse of the data and the column names.
# - `df.info()` provides a summary of the DataFrame, including the data types of each column and the number of non-null values. This helps us understand the data we're working with.
# - `df.isnull().sum()` calculates the number of missing values in each column. In this dataset, you'll likely find no missing values, but it's always a good step to check.

# Clean the dataset (if needed)
# In this case, the Wine Quality dataset is usually clean and doesn't contain missing values.
# If there were missing values, you might use techniques like:
# df.fillna(value) to fill missing values with a specific value (e.g., mean, median, or a constant).
# df.dropna() to remove rows containing missing values.

#Task 2:basic data analysis
# Compute basic statistics for numerical columns
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Explanation:
# - `df.describe()` calculates and displays descriptive statistics for all the numerical columns in the DataFrame. This includes count, mean, standard deviation, minimum, maximum, and the 25th, 50th (median), and 75th percentiles. This gives us a good overview of the distribution and central tendency of each feature.

# Perform groupings on a categorical column (quality) and compute the mean of a numerical column for each group
print("\nMean of features grouped by wine quality:")
print(df.groupby('quality').mean())

# Explanation:
# - `df.groupby('quality')` groups the DataFrame by the 'quality' column. Although 'quality' is an integer rating (3 to 8), we can treat it as a categorical variable for grouping purposes to see how other features vary with wine quality.
# - `.mean()` calculates the mean of each of the other numerical columns for each quality group. This can help us identify trends. For example, do wines with higher quality have higher alcohol content?

# Identify any patterns or interesting findings from your analysis.
print("\nInteresting findings:")
print("- Higher quality wines tend to have a higher alcohol content.")
print("- There might be subtle differences in other chemical properties across different quality ratings, which can be further explored with visualizations.")
# (Add more observations as you explore the output)


#Task 3:data visualization 
# 1. Bar chart: Average of a feature per quality rating (e.g., average alcohol content)
average_alcohol = df.groupby('quality')['alcohol'].mean()
plt.figure(figsize=(8, 6))
average_alcohol.plot(kind='bar', color='skyblue')
plt.title('Average Alcohol Content per Wine Quality')
plt.xlabel('Wine Quality')
plt.ylabel('Average Alcohol (%)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Explanation:
# - We group the data by 'quality' and calculate the mean of the 'alcohol' column for each quality level.
# - `plot(kind='bar')` creates a bar chart.
# - We set the title, labels for the axes, and rotate the x-axis labels for better readability.
# - `plt.grid(axis='y')` adds horizontal grid lines.

# 2. Histogram: Distribution of a numerical column (e.g., pH)
plt.figure(figsize=(8, 6))
plt.hist(df['pH'], bins=15, color='lightcoral', edgecolor='black')
plt.title('Distribution of pH in Red Wines')
plt.xlabel('pH')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Explanation:
# - `plt.hist()` creates a histogram of the 'pH' column.
# - `bins=15` specifies the number of bins (intervals) to divide the data into.
# - We set the title and axis labels for clarity.

# 3. Scatter plot: Relationship between two numerical columns (e.g., fixed acidity vs. pH)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='fixed acidity', y='pH', data=df, color='orange')
plt.title('Fixed Acidity vs. pH in Red Wines')
plt.xlabel('Fixed Acidity')
plt.ylabel('pH')
plt.grid(True)
plt.show()

# Explanation:
# - `sns.scatterplot()` from the seaborn library creates a scatter plot. Seaborn often provides more visually appealing default styles.
# - We specify the 'fixed acidity' for the x-axis and 'pH' for the y-axis.
# - The `data=df` argument tells seaborn which DataFrame to use.

# 4. Box plot: Comparing a numerical feature across different quality ratings (e.g., residual sugar vs. quality)
plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='residual sugar', data=df, palette='viridis')
plt.title('Residual Sugar Distribution per Wine Quality')
plt.xlabel('Wine Quality')
plt.ylabel('Residual Sugar')
plt.show()

# Explanation:
# - `sns.boxplot()` creates box plots, which are useful for visualizing the distribution of a numerical variable across different categories.
# - Here, we're comparing the distribution of 'residual sugar' for each wine 'quality' rating. The box shows the quartiles, the whiskers extend to show the range (with outliers potentially marked), and the line inside the box represents the median.
# - `palette='viridis'` uses a specific color palette for better visual distinction.

