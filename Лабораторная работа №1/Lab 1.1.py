my_list = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_1 = sum(my_list[:4])
sum_2 = sum(my_list[5:])
sum_12 = sum_1+sum_2
count = len(my_list)
average = sum_12 / count
my_list[4] = average
print("Измененный список:", my_list)
