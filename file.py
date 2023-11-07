print("Print the mean word")

my_list = [1, 2, 3, 4, 5]
other_list = [7, 8, 9]
my_list.remove(3)
my_list.append(5)
last_element = my_list.pop(1)
print(last_element)

#delete_at = __import__('file').delete_at

idx = 3
new_list = FileExistsError(my_list, idx)
print(new_list)
print(my_list)
my_list.extend(other_list)

print(my_list)

a = 89
b = 10
a, b = b, a
print("a={:d} _ b={:d}".format(a, b))

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del(my_list)[idx]
        return(my_list)