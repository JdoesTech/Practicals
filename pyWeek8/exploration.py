import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import streamlit as st

# Load the dataset
df=pd.read_csv('cord_sample.csv')
print(df.info())
print(df.describe())
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())

# Cleaning Data
df["publish_time"]=pd.to_datetime(df['publish_time'], errors="coerce", format="mixed")
df.drop(columns=["who_covidence_id","arxiv_id", "s2_id"], inplace=True)
df.drop_duplicates(inplace=True)
df.dropna(subset=["sha","cord_uid", "publish_time"], inplace=True)
df.fillna("missing", inplace=True)
df=df.reset_index(drop=True)

# Distribution of a numerical column
plt.figure(figsize=(10, 6))


#count how many lines are in the file
    #first declare a new column for the counted lines
df["line_count"]=0
count=0

# iterate through each row, counting the lines in each file
for index, rows in df.iterrows():
	url = rows.get("url", None)
	if pd.notnull(url):
		try:
			response= requests.get(url)
			if response.status_code ==200:
				count = len(response.text.splitlines())
				df.at[index, "line_count"] =count
			else:
				df.at[index, "line_count"]=0
		except:
			df.at[index, "line_count"]= "Not accessible"

# top journals by line count
line_ranking=df.sort_values("line_count",ascending=False).head(10)
#visualizing
sns.barplot(x="cord_uid", y="line_count", data=line_ranking, color="yellow")
plt.xticks(rotation=80)
plt.xlabel("cord_uid")
plt.ylabel("line_count")
plt.title("Top 10 Journals by lines")
plt.show()

#Getting number of publications per year
yearly_pub_num= df.groupby(df["publish_time"].dt.year).size().reset_index()
yearly_pub_num.columns = ["Year", "Number"]
sns.lineplot(data=yearly_pub_num, y="Number", color="red")
plt.xticks(rotation=80)
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.title("Number of Publications per Year")	
plt.show()

#top journals churning research
top_journals=df["journal"].value_counts().reset_index()
top_journals.columns = ["journal", "number"]
# visualizing
sns.barplot(data=top_journals, x="journal", y="number", color="blue")
plt.xticks(rotation=80)
plt.xlabel("Journals")
plt.ylabel("Number of Publications")
plt.title("Top Journals Churning Research")		
plt.show()

#frequent words in titles
df["title"]=df["title"].astype(str)
df["title"]=df["title"].str.replace('[^a-zA-Z0-9\']','', regex=True)
df["title"]=df["title"].str.strip()
all_words=df["title"].str.split().explode()
frequ=all_words.value_counts()
frequ_plot=frequ.sort_values(ascending=False).head(10)
most_used_word=frequ.max() #most used word count
#visualizing
sns.barplot(data=frequ_plot, x=frequ_plot.index, y=frequ_plot.values, color="green")
plt.xticks(rotation=80)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Most Frequent Words in Titles")
plt.show()

#paper counts per source
source_counts=df["source_x"].value_counts().head(10)
source_df=source_counts.reset_index()
source_df.columns=["source", "count"]
#visualizing
sns.barplot(data=source_df, x="source", y="count", color="purple")
plt.xticks(rotation=80)
plt.xlabel("Source")
plt.ylabel("Number of Publications")
plt.title("Top 10 Sources by Number of Publications")	
plt.show()
    
