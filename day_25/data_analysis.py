import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data.groupby(["Primary Fur Color"])["Primary Fur Color"].count()
fur_color.columns = ["Fur Color","Total"]
fur_color.to_csv("four_colors_rename.csv")