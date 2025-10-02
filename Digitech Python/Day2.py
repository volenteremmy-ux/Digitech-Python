my_list =[1,10,2,3,4,4]
print(my_list)

my_list.append(5)
print(my_list)

my_list.extend([6,7,8])
print(my_list)

my_list.insert(2, 9)
print(my_list)

my_list.remove(9)
print(my_list)

popping = my_list.pop(7)
print(my_list, "removed element is : ", popping)

# my_list.index(7)
# print(my_list)

counting = my_list.count(4)
print(counting)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

length = len(my_list)
print(length)

maximum = max(my_list)
print(maximum)

minimum = min(my_list)
print(minimum)

checking = 3 not in my_list
print(checking)

phoenix = my_list.copy()
print(phoenix)

# my_list.clear()
# print(my_list)

# print(phoenix)

print(phoenix)

print(phoenix[6])

getting = phoenix[6]
print(getting)

checking = phoenix.index(3)
print(checking)