#import csv

#with open("weather_data.csv") as data:
#    raw_data_list = data.readlines()
#    data_list = []
#    for item in raw_data_list:
#        data = item.strip()
#        data_list.append(data)

#with open("weather_data.csv") as data:
#    data_list = csv.reader(data)
#    print(data_list)
#    temp_list = []
#    for row in data_list:
#        if row[1] != "temp":
#            temp_list.append(int(row[1]))
#print(temp_list)
#
import pandas

data = pandas.read_csv("weather_data.csv")

#Convert Pandas data to dict
#data_dict = data.to_dict()
#print(data_dict)

#Convert panads data to list
#temp_list = data["temp"].to_list()
#print(temp_list)

#Find average (long way)
#temp_list = data["temp"].to_list()
#total_sum = sum(temp_list)
#average_temp = total_sum / len(temp_list)
#print(round(average_temp))

#Easy way
#print(data["temp"].mean())
#print(data["temp"].max())

#data.temp is the same as data["temp"]. data.temp will pull the temp column only, data[data.temp == "24"] will pull ROW where this temp matches!
#print(data[data.temp == data.temp.max()]) # Prints entire row where the temp was max
#monday = data[data.day == "Monday"] # set variable based on match condition
#print(monday.condition) # Returns the weather conditions based on variable, as variable inherits object attribs (day, temp, condition)

#Convert Monday temp to Fahrenheit
# monday = data[data.day == "Monday"]
#monday_f = (monday.temp * (9/5)) + 32
#print(monday_f)

#Create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
student_data = pandas.DataFrame(data_dict)
print(student_data)
student_data.to_csv("student_data")