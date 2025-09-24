import pandas as pd

df= pd.read_csv('metadata.csv', nrows=500)
df.to_csv("cord_sample.csv", index=False)