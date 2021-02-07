with open("file1.txt") as file1:
    file1_list = file1.readlines() 
    file1_numbers = [int(num) for num in file1_list]

with open("file2.txt") as file2:
    file2_list = file2.readlines()
    file2_numbers = [int(num) for num in file2_list]

result = [common_num for common_num in file1_numbers if common_num in file2_numbers]
print(result)
