grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students =list(students) #Перевод множества в список
list_students.sort() #упорядочивание списка по алфавиту
index = 0 #индекс для списка среднего балла и для итогового словаря
GPA = list() # список для сохранения среднего балла каждого студента
rez = dict() # словарь для вывода результата
while index<len(grades):
    GPA.append(sum(grades[index])/len(grades[index])) #формирование списка среднего балла каждого студента
    rez.update ({list_students[index]:GPA[index]})
    index = index+1
print(rez)
