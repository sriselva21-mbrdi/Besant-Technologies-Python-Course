#  --------------------------- Python List exercise problems with solutions  -----------------------------  #


#  1. Write a Python program to sum all the items in a list.

def sum_list(lst):
    total = sum(lst)  # sum is built-in method, sum is a function which adds the value
    return total


def lst_sum(lst):
    total = 0
    for i in lst:
        total += i  # using + (increment operator) to update the total value by adding the iterating value
    return total


#  2. Write a Python program to multiply with same numbers which present in a list.

def lst_mul(lst):
    mul_lst = [i * i for i in lst]
    return lst, mul_lst


#  3. Write a Python program to get the largest number from a list.

def lst_max(lst):
    return max(lst)  # max is pre-defined function, which finds the highest number from a sequence.


def max_lst(lst):
    highest = lst[0]
    for i in lst:
        if i > highest:
            highest = i
    return highest


#  4. Write a Python program to get the smallest number from a list.

def lst_min(lst):
    return min(lst)  # min is pre-defined function, which finds the lowest number from a sequence.


def min_lst(lst):
    lowest = lst[0]
    for i in lst:
        if i < lowest:
            lowest = i
    return lowest


#  5. Write a Python program to count the number of strings from a given list of strings and return only strings whose
#  length is 2 or more and the first and last characters are the same.
#  Sample List: ['mom', 'dad', 'son', 'daughter', 'malayalam']
#  Excepted Output: ['mom', 'dad', 'malayalam]

def string_count(lst):
    new_lst = []
    for i in lst:
        if len(i) > 1 and i[0] == i[-1]:
            new_lst.append(i)
    return new_lst


#  6. Write a Python program to remove duplicates from a list.
#  Sample List : [2, 55, 1, 22, 4, 4, 2, 3, 2, 1]
#  Expected Result : [1, 2, 3, 4, 22, 55]

def remove_duplicate(lst):
    return list(set(lst))


def duplicate_lst(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return sorted(new_lst)


#  7. Write a Python program to check if a list is empty or not.

def check_lst_empty(lst):
    if lst:
        return f'List is not empty {lst}'
    else:
        return f'List is empty {lst}'


def empty_lst_check(lst):
    if not lst:
        return f'List is empty {lst}'
    else:
        return f'List is not empty {lst}'


#  8. Write a Python program to clone or copy a list.

def clone_lst(lst):
    original = lst
    clone = original.copy()  # copy is a pre-defined list method, it copies the value of the list to new variable
    return original, clone


#  9. Write a Python program to find the list of words that are longer than n from a given list of words.

def words_lst(n, lst):
    new_lst = []
    for i in lst:
        if len(i) > n:
            new_lst.append(i)
    return new_lst


#  10. Write a Python function that takes two lists and returns True if they have at least one common member.

def common_lst(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return True


#  11. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#  Sample List : ['Red', 'Red', 'White', 'Black', 'Pink', 'Yellow']
#  Expected Output : ['Red', 'White', 'Black']

def rmv_lst_inx(lst):
    inx = (0, 4, 5)
    new_lst = []
    for lst_inx, i in enumerate(lst):  # enumerate returns the index and value of each element from sequences.
        if lst_inx not in inx:
            new_lst.append(i)
    return new_lst


#  12. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def rmv_even(lst):
    new_lst = [i for i in lst if i % 2 != 0]
    return new_lst


#  13. Write a Python program to generate and print a list of the first and last 2 elements where the values are
#  square numbers between 1 and 30 (both included).

def square():
    lst = [i*i for i in range(1,6)]
    return lst, lst[:2], lst[-2:]


#  14. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers
#  are prime otherwise False.
#  Sample Data:
#  ([0, 3, 4, 7, 9]) -> False
#  ([3, 5, 7, 13]) -> True
#  ([1, 5, 3]) -> False


#  15. Write a Python program to generate all permutations of a list in Python.

def lst_methods():
    lst = [10, 20, 30]
    new_lst = lst.copy()  # copies the lst values to new_lst
    lst.append([30])  # adds 30 to the existing lst list
    lst.count(30)  # finds number 30 how many times repeated
    lst.extend([20, 20, 40])  # adds the values existing lst list without [ ]
    lst.index(10)  # finds the value 10 index location, it will give least/first index value
    lst.insert(1, 1000)  # to insert value at specific index/position 1 - index, hello - value
    lst.pop()  # deletes last item default
    lst.pop(0)  # deletes the position value 0 - index value
    lst.remove(20)  # deletes the value 20, it will delete least/first index value
    lst.reverse()  # reverse the values inside the list
    lst.sort()  # arranges the value in ascending order, it will sort only when list have same data types (numbers/str)
    lst.sort(reverse=True)  # arranges the value in descending order, give False to get in ascending order
    lst.clear()  # deletes all values from the list and will return empty list
    return lst



if __name__ == "__main__":
    print(lst_methods())
