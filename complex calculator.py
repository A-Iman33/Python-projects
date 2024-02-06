print ('this is my calculor')

x = input ('give an number: ')
operator = input ('would you like to +, -, *, /: ')
y = input ('give another number: ')
another_choise = input ('would you like to do another calculation? yes or no: ')
if 'yes':
        operator = input ('would you like to +, -, *, /: ')
else:
    print('invalid')
     
    

if type(x) == 'int' and type(y) == 'int' and operator == '+':
   answer = print (int(x) + int(y))
elif type(x) == 'int'  and type(y) == 'int' and operator == '-':
    answer = print (int(x) - int(y))
elif type(x) == 'int' and  type(y) == 'int' and operator == '*':
    answer = print (int(x) * int(y))
elif type(x) == 'int' and  type(y) == 'int' and operator == '/':
    answer = print (int(x) / int(y))
else:
     print('answer')
#else:
#      print ('calculation not valid')


#print (f"{x} {operator} {y} = {ans}")





# else:
#      print ('calculation not valid')

# choise = True
# while True:
#     input ('would you like to do another calculation? yes or no: ')
    
#     if 'yes':
#         operator = input ('would you like to +, -, *, /: ')

#     elif type(y) == 'int' and operator == '+':
#         z = input ('give a number: ')
#         print (f"{x} {operator} {y} {operator} {z} = {ans}")
#     elif 'no':
#         print(ans)
#     else:
#         print ('calculation not valid')

    # elif new_operator == "-":
    #     ans -= 1
    # elif new_operator == "*":
    #     ans *= 1
    # elif new_operator == "/":
    #     ans /= 1
    # else:
    #     print("Invalid operation!")
       



     


    





