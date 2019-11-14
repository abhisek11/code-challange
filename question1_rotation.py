'''
Question 1. 
Write a function that takes an array of integers and returns that array rotated by N positions  using Python or Ruby or JavaScript.    For example, if N=2, given the input array [1, 2, 3, 4, 5, 6]   the function should return [5, 6, 1, 2, 3, 4] 
'''
#answer 

def rotation(array,N):
    '''
    rotation() function take 2 parameters 
    1)a list input 
    2)integer number for roation
    '''
    output = array[len(array)-N:]+array[:len(array)-N]
    return output

print("The rotated array is :- ",rotation([1, 2, 3, 4, 5, 6],2))