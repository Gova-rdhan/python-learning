import pandas

data = pandas.read_csv("./input/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
result = data.groupby(["Primary Fur Color"])['Primary Fur Color'].count()
df = pandas.DataFrame(result)
df.to_csv("squirrel_count")