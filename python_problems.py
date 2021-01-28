"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by 
lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list."""

def list_op_from_cli():
    N = int(input())
    list_tmp = []
    for _ in range(N):
        inputs = [str(elem) for elem in input().split()]
        command, values = inputs[0], inputs[1:]
        if command == 'print':
            print(list_tmp)
        elif values:
            eval(f"list_tmp.{command}(*values)")
        else:
            eval(f"list_tmp.{command}()")

"""
Task

You are given a 2-D array with dimensions X.
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format

The first line of input contains space separated values of  and .
The next  lines contains  space separated integers.

Output Format

Compute the sum along axis . Then, print the product of that sum."""

def numpy_prob():
    #Demonstration
    import numpy as np
    my_array = np.array([[1, 2], [3, 4], [5, 6]])
    print(np.sum(my_array, axis=0))
    print(np.sum(my_array, axis=1))
    print(np.sum(my_array, axis=None))
    print(np.sum(my_array))
    print(np.prod(my_array, axis=0))
    print(np.prod(my_array, axis=1))
    print(np.prod(my_array, axis=None))
    print(np.prod(my_array))
    in_array = get_list()
    new_np_array = np.array(in_array)
    print("Sum: ", np.sum(new_np_array, axis=0))
    print(np.prod(np.sum(new_np_array, axis=0), axis=0))
def get_list():
    n, m = [int(el) for el in input().split()]
    in_array = []
    for _ in range(n):
        in_array.append([int(el) for el in input().split()])
    return in_array

#numpy_prob()


"""
Task

You are given a 2-D array with dimensions X.
Your task is to perform the min function over axis  and then find the max of that.

Input Format

The first line of input contains the space separated values of  and .
The next  lines contains  space separated integers.

Output Format

Compute the min along axis 1 and then print the max of that result.
"""

def numpy_prob1():
    import numpy 
    # axis 0 it is x axis and 1 it is y axis
    my_array = numpy.array([[2, 5],
                            [3, 7],
                            [1, 3],
                            [4, 0]])
    print(numpy.min(my_array, axis=0))
    print(numpy.min(my_array, axis=1))
    print(numpy.min(my_array, axis=None))
    print(numpy.min(my_array))
    new_np_array = numpy.array(get_list())
    print(numpy.max(numpy.min(new_np_array, axis=1)))

numpy_prob1()
