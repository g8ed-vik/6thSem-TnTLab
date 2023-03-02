#Write a program in Python to get the largest element of a list using recursion

def largest_element(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], largest_element(list[1:]))
    
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Largest element in", list, "is", largest_element(list))