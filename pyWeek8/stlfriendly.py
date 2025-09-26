import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import streamlit as st

# Load the dataset
df = pd.read_csv('cord_sample.csv')
st.subheader("Dataset Overview")
st.dataframe(df.head())
st.write("Summary Statistics")
st.dataframe(df.describe())
st.write("Missing Values")
st.dataframe(df.isnull().sum())
st.write("Duplicate Rows:", df.duplicated().sum())

# Cleaning Data
df["publish_time"] = pd.to_datetime(df['publish_time'], errors="coerce", format="mixed")
df.drop(columns=["who_covidence_id", "arxiv_id", "s2_id"], inplace=True)
df.drop_duplicates(inplace=True)
df.dropna(subset=["sha", "cord_uid", "publish_time"], inplace=True)
df = df.reset_index(drop=True)

# count how many lines are in the file
df["line_count"] = 0
count = 0

# iterate through each row, counting the lines in each file
progress = st.progress(0)
for index, rows in df.iterrows():
    url = rows.get("url", None)
    if pd.notnull(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                count = len(response.text.splitlines())
                df.at[index, "line_count"] = count
            else:
                df.at[index, "line_count"] = 0
        except:
            df.at[index, "line_count"] = 0
    progress.progress((index + 1) / len(df))

# top journals by line count
line_ranking = df.sort_values("line_count", ascending=False).head(10)
fig1, ax1 = plt.subplots()
sns.barplot(x="cord_uid", y="line_count", data=line_ranking, color="yellow", ax=ax1)
plt.xticks(rotation=80)
plt.xlabel("cord_uid")
plt.ylabel("line_count")
plt.title("Top 10 Journals by lines")
st.pyplot(fig1)

# Getting number of publications per year
yearly_pub_num = df.groupby(df["publish_time"].dt.year).size().reset_index()
yearly_pub_num.columns = ["Year", "Number"]
fig2, ax2 = plt.subplots()
sns.lineplot(data=yearly_pub_num, x="Year", y="Number", color="red", ax=ax2)
plt.xticks(rotation=80)
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.title("Number of Publications per Year")	
st.pyplot(fig2)

# top journals churning research
top_journals = df["journal"].value_counts().reset_index()
top_journals.columns = ["journal", "number"]
fig3, ax3 = plt.subplots()
sns.barplot(data=top_journals.head(10), x="journal", y="number", color="blue", ax=ax3)
plt.xticks(rotation=80)
plt.xlabel("Journals")
plt.ylabel("Number of Publications")
plt.title("Top Journals Churning Research")		
st.pyplot(fig3)

# frequent words in titles
df["title"] = df["title"].astype(str)
df["title"] = df["title"].str.replace('[^a-zA-Z0-9\']', '', regex=True)
df["title"] = df["title"].str.strip()
all_words = df["title"].str.split().explode()
frequ = all_words.value_counts()
frequ_plot = frequ.sort_values(ascending=False).head(10)
most_used_word = frequ.max()
st.write("Most Used Word Count:", most_used_word)
frequ_plot_df = frequ_plot.reset_index()
frequ_plot_df.columns = ['word', 'Frequency']
fig4, ax4 = plt.subplots()
sns.barplot(data=frequ_plot_df, x="word", y="Frequency", color="green", ax=ax4)
plt.xticks(rotation=80)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Most Frequent Words in Titles")
st.pyplot(fig4)

# paper counts per source
source_counts = df["source_x"].value_counts().head(10)
source_df = source_counts.reset_index()
source_df.columns = ["source", "count"]
fig5, ax5 = plt.subplots()
sns.barplot(data=source_df, x="source", y="count", color="purple", ax=ax5)
plt.xticks(rotation=80)
plt.xlabel("Source")
plt.ylabel("Number of Publications")
plt.title("Top 10 Sources by Number of Publications")	
st.pyplot(fig5)
