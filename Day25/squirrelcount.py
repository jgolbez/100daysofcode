import pandas

squirrel_data = pandas.read_csv("squirrel_data.csv")

#Get unique entries for colors in column
#color_list = []
#for color in squirrel_data["Primary Fur Color"]:
#    if color not in color_list:
#        color_list.append(color)
#print(color_list)

#Standard way to derive color/count
##gray_color = 0
#black_color = 0
#cinn_color = 0
#for colors in squirrel_data["Primary Fur Color"]:
#    if colors == "Gray":
#        gray_color += 1
#    elif colors == "Black":
#        black_color += 1
#    elif colors == "Cinnamon":
#        cinn_color += 1



#Use Pandas value_counts method to return series value of color/count
fur_count = squirrel_data["Primary Fur Color"].value_counts()
#DEBUG: Print returned DF output
#print(fur_count)
'''
Sample output:
Gray        2473
Cinnamon     392
Black        103
Name: Primary Fur Color, dtype: int64
'''

#Convert output to a dict for manipulation (Is there another option?)
fur_dict = dict(fur_count)
#DEBUG: Print Dict
#print(fur_dict) # Sample Returned data: {'Gray': 2473, 'Cinnamon': 392, 'Black': 103}

#seperate returned dict into columns for creating data frame
color_list = []
color_count = []
for k, v in fur_dict.items():
    color_list.append(k)
    color_count.append(v)

#DEBUG: Print Lists
#print(color_list) # Sample Returned data: ['Gray', 'Cinnamon', 'Black']
#print(color_count) # Sample Returned data: [2473, 392, 103]

#Create Dict from Lists (There has to be a better way to use Pandas to return a DF than converting to dict/list/dict again)
squirrel_dict = {
    "Fur Color": color_list,
    "Count": color_count
}

#Create Pandas DF and save to csv
fur_df = pandas.DataFrame(squirrel_dict)
fur_df.to_csv("squirrel_fur_count.csv")
