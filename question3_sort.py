'''Question 3.  Python, Ruby or JavaScript    Most languages have a built in sort method that will sort an array of strings alphabetically.  Demonstrate how to sort an array of strings by the length of each string, shortest strings first.     Hint:​ clean, small code wins.  '''

def sort(s, n): 
    for i in range(1, n): 
        temp = s[i] 
        j = i - 1
        while j >= 0 and len(temp) < len(s[j]): 
            s[j + 1] = s[j] 
            j -= 1
        s[j + 1] = temp 
    return s

array = ['waste','time','dont','my']
op = sort(array,len(array))
print("Output of sorting :- ")
for words in op:
    print(words,end=" ")