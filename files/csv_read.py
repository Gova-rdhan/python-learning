# with open("./input/weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# import csv
#
# with open("./input/weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temp = []
#     for i in data:
#         if i[1] != "temp":
#             temp.append(int(i[1]))
# print(temp)
import pandas
from pandas import DataFrame
data = pandas.read_csv("./input/weather_data.csv")
# temp = data["temp"].mean()
# max_value = data["temp"].max()
# print(max_value)

monday = data[data.day == "Monday"]
temp = (monday.temp * 9/5) + 32
print(temp)