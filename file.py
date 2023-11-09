print("Print the mean word.\nI have hope.\n")
print("I'm now learning python")
my_list = [1, 2, 3, 4, 5]
other_list = [7, 8, 9]
result_list = [10, 11, 12, 13]
class_list = [20, 21, 21, 21, 22, 23, 24, 25]

my_list.remove(3)
append = my_list.append(5)
pop = my_list.pop(2)
count = class_list.count(21)
clear = result_list.clear()

#print(last_element)
print(pop)

#delete_at = __import__('file').delete_at

idx = 3
new_list = FileExistsError(my_list, idx)
print(new_list)
print(my_list)
extend = my_list.extend(other_list)

#print(my_list)
print(result_list)
print(count)
print(append)
print(pop)
print(clear)

a = 89
b = 10
a, b = b, a
print("a={:d} _ b={:d}".format(a, b))

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del(my_list)[idx]
        return("my_list" )

result = [99, 88, 77, 10]
result = (1 + 2) * 3
print(result)  # Output: 9

