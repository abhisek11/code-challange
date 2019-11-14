'''
Write a simple program that reads a line from the keyboard and outputs the same line where
every word is reversed. A word is defined as a continuous sequence of alphanumeric characters
or hyphen (‘-’). For instance, if the input is
“We are at Ignite Solutions! Their email-id is careers@ignitesol.com”
the output should be
“eW era ta etingI snoituloS! riehT di-liame si sreerac@losetingi.moc”
 
HINT: ​ Read the problem and the example carefully before starting.
'''

def inner_reverse(value):
    string=''
    data=[]
    for i in value:
        if i.isalpha():
            string+=i
        elif i !='-':
            string=string[::-1]+i
            data.append(string)
            string=''
        else:
            string+='-'
    print("".join(map(str,data))+string[::-1])

inner_reverse('We are at Ignite Solutions! Their email-id is careers@ignitesol.com')
   



# def reverse(value):
#     array = list(map(str,value.split(' ','')))
#     for word in array:


#     final_op = [ for x in array]
#     print(final_op)
# # re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', a)
# reverse('We are at Ignite Solutions! Their email-id is careers@ignitesol.com')