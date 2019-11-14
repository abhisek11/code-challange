'''
Write a program in Python,JavaScript or Ruby to populate and then sort a 
randomly distributed list of 1 million integers,each integer having a value
>= 1 and <= 100 without using any builtin/external library/function for sorting
Your program should carefully consider the input and come up with the most efficient
sorting solution you can think of. Provide the space and time complexity of your algorithm'''

#Answer

def sort(s, n):
    if n <= 1000000: 
        for i in range(1, n): 
            temp = s[i] 
            j = i - 1
            while j >= 0 and temp < s[j]: 
                s[j + 1] = s[j] 
                j -= 1
            s[j + 1] = temp 
        return s

array = [99,12,1,8,45,47]
op = sort(array,len(array))
print("Output of sorting :- ",op)
