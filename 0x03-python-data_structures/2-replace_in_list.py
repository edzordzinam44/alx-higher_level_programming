#!/usr/bin/python3

def replace_in_listt(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element # Replace the element a he specified index
    return my_list