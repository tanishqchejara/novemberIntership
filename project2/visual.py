import pandas as pd#importing panda lib
import matplotlib.pyplot as plt#importing matplot lib
import seaborn as sns#importing seaborn lib

# Load the dataset

df = pd.read_csv("dataset_netflix1.csv")

# Display the first few rows of the dataset
print(df.head())


# Countplot for 'type' column
plt.figure(figsize=(8, 6))
sns.countplot(x='type', data=df)
plt.title('Count of Movies and TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

#drawing a Bar plot for top 10 countries with most content
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_countries.plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries with Most Content')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

#creating a Histogram for release year
plt.figure(figsize=(10, 6))
sns.histplot(df['release_year'], bins=30, kde=True, color='orange')
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Frequency')
plt.show()
