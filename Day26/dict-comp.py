import random
import pandas

#Create new dict from list
#new_dict = {new_key:new_value for item in list}

#Create new dict from other dict, IF conditional is tested
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

#Randomly geerate scores by looping through a list and create a dict frm the resulting k/v
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print (students_scores)

#Use generated dict, loop through, only add passing students to new dict - 26.3
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

#Create dict with word length count from string Dict Comp 1 - 26.4 Exercise
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split()
result = {word:len(word) for word in word_list}
print(result)

#Convert dict of celsius temps to F - Dict Comp 2 - 26.5 Exercise
#(temp_c * 9/5) + 32 = temp_f
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
def convert_f(temp_c):
  temp_f = (temp_c * 9/5) + 32
  return temp_f

weather_f = {day:(convert_f(temp_c)) for day, temp_c in weather_c.items()}
print(weather_f)

#Iterate over Pandas DataFrame - Functionally identical to looping through dict
student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}
student_df = pandas.DataFrame(student_dict)
print(student_df)

#standard loop method
#for (k, v) in student_df.items():
#    print(k, v)

#IterRows
for (index, row) in student_df.iterrows():
    print(row.student)
#Sample output:
# Angela
#James
#Lilly 

#Can use conditionals on Iterrows also
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)




