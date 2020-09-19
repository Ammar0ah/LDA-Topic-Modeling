import pandas as pd
data = pd.read_csv('Text/file1.txt',sep='.',header=None)
# data.columns = ['a'] * len(data.columns)
df = pd.DataFrame(data)
df = df.T
df.columns = ["content"]
df["content"][1]._combine_match_index(2)
print(df["content"])