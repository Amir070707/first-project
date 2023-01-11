str_x1 = 'spam'
list1 = []
list2 = list(str_x1)
list1.append(7)
list1.extend(list2)
print(list1* 5)
