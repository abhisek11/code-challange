'''
Question 5.
Consider the following pattern: 
A → D
a → d
M → P
m → p
X → A 
x → a 
Now, write a program to solve the following message using Python, JavaScript or Ruby.  
Vrphwklqj phdqlqjixo 
Hint: The answer is something meaningful. 
'''
def decript_message(value):
    result=''
    for x in value:
        if x.isupper():
            result += chr(((ord(x)+23-65)%26+65))
        elif x.islower():
            result += chr((ord(x)+23-97)%26+97)
        else:
            result += x

    return result

    # data ="".join(map(chr,[((ord(x)+3-65)%26+65) if x.isupper() else ((ord(x)+3-97)%26+97) for x in value ]))
    # print(data)

print(decript_message('vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu dojrulwkp'))

