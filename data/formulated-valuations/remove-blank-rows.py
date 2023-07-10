import pandas as pd

df = pd.read_csv("C:/Users/Toby Chiu/Desktop/Coding/Personal Projects/Personal/wins-above-rep-soccer/data/formulated-valuations/keepers_final.csv")

df.dropna(subset=['MP_Playing'], inplace=True)

print(df.shape)

df.to_csv("C:/Users/Toby Chiu/Desktop/Coding/Personal Projects/Personal/wins-above-rep-soccer/data/keepers_final_vF.csv")
