#for i in range(0,99):
#    if i % 5 == 0 and i % 3 == 0
#        print("fizzbuzz")
#    if i % 3 == 0:
#        print("fizz")
#    elif i % 5 == 0:
#        print("Buzz")
    

# # age = string


# def isnan(input):
#     try:
#         input = int(input)
#         return True

#     except:
#         return False






 age = input("Gebe dein Alter ein: ")

 retard_grad = input("Geben sie den Grad ihrer Behinderung ein: ")

 verschwendete_zeit = input("Wie lange sind Sie schon im Unternehmen tätig?: ")


 if isnan(age) == False or isnan(retard_grad) == False or isnan(verschwendete_zeit) == False:
     print("Gebe Zahlen ein du Mongo")
 else: 
     age = int(age)

     retard_grad = int(retard_grad)

     verschwendete_zeit = int(verschwendete_zeit)


     urlaubstage = 26

     if age < 18:
         urlaubstage = 30

     if age > 55:
         urlaubstage = urlaubstage + 2

     if retard_grad > 50:
         urlaubstage = urlaubstage + 5

     if verschwendete_zeit > 10:
         urlaubstage = urlaubstage + 2

     print(urlaubstage)





# # age = integer
# age = int(age)

# if age >= 18:
#     print("you shall pass")
# else:
#     print("you shall not pass")