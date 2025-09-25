import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

df=pd.read_csv('cord_sample.csv')
df.info()
df.describe()
df.head()
df.isnull().sum()
df.duplicated().sum()

df["publish_time"]=pd.to_datetime(df['publish_time'])
df=df.drop(columns=["who_covidence_id","arxiv_id", "s2_id"])
df=df.drop_duplicates()
df=df.dropna(subset=["sha","cord_uid"], inplace=True)
df=df.fillna("missing")
df=df.reset_index(drop=True)

# Distribution of a numerical column
plt.figure(figsize=(10, 6))


#count how many lines are in the file
    #first declare a new column for the counted lines
df["line_count"]=None
count=0

for index, rows in df.iterrows():
	url = rows["url"]
	try:
		with open("url", 'r')  as f:
			lines=f.readlines()
		print(f"{len(lines)} lines from this journal. ")
		response= requests.get(url)
		if response.status_code ==200:
			count = len(response.text.splitlines())
			df.at[index, "line_count"] =count
		else:
			df.at[index, "line_count"]=0
	except:
		df.at[index, "line_count"]=0


line_ranking=df["line_count"].sort_values(ascending=False)
#visualize
sns.barplot(x="cord_uid", y="line_count", data=df, color="yellow")
plt.xticks(rotation=80)
plt.xlabel("cord_uid")
plt.ylabel("line_count")
plt.legend()
plt.show()

#Getting number of publications per year
yearly_pub_num= df.groupby(df["publish_time"].dt.year).size()
sns.lineplot(data=yearly_pub_num, y="line_count", color="red")
plt.xticks(rotation=80)
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.legend()
plt.show()

#top journals churning research
top_journals=df["journals"].value_counts()
sns.barplot(data=top_journals, x=top_journals.index, y=top_journals.values, color="blue")
plt.xticks(rotation=80)
plt.xlabel("Journals")
plt.ylabel("Number of Publications")
plt.legend()
plt.show()

#frequent words in titles
df["title"]=df["title"].astype(str)
df["title"]=df["title"].str.replace('[^a-zA-Z0-9\'\]','', regex=True)
df["title"]=df["title"].str.strip()
all_words=df["title"].str.split().explode()
frequ=all_words.value_counts()
#for index, row in df.iterrows():
    #frequ=df["title"].str.split().value_counts()
frequ_plot=frequ.sort_values(ascending=False).head(10)
most_used_word=frequ.max()
sns.barplot(data=frequ_plot, x=frequ_plot.index, y=frequ_plot.values, color="green")

#paper counts per source
source_counts=df["source_x"].value_counts()
source_df=source_counts.reset_index()
source_df.columns=["source", "index"]
sns.barplot(data=source_df, x="source", y="count", color="purple")
plt.xticks(rotation=80)
plt.xlabel("Source")
plt.ylabel("Number of Publications")
plt.legend()
plt.show()
    

