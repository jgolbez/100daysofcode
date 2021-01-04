# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(student_heights)
listnum = 0
newheight = 0
for height in student_heights:
#DEBUG:  print(f" Before calc height is {height}")
  newheight += height
  listnum += 1
#DEBUG:  print(f" After calc, height is: {newheight}")
#DEBUG:  print(f" listnum is: {listnum}")
average = round(newheight / listnum)
print(f" The average is {average}")
