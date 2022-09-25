# with open("weather.csv") as data:
#     datafile = data.readlines()
#     print(datafile)


# import csv
# with open("weather.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures =[]
#     for row in data:
#         if row[1] !="temp":
#             temperatures.append(int(row[1]))


import pandas

data = pandas.read_csv("weather.csv")

# print(data[data.day == "monday"])

data_dict ={
    "studens":['amy', 'james', 'hoang'],"scores":[76,78,100]
}

data_stu = pandas.DataFrame(data_dict)
print(data_stu)
data_stu.to_csv("data_stu.csv")