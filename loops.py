# we have two kind of loops in it and both are necessary to understand
# 1. while

# while True : 
   # print("hello")

    
# but the above syntax doesnt contains any end of the loop so it will go on till infinity.

# a = 1
# while a <= 9 :
#     print("hello")
#     a += 1

# password checker

password = ""
attempt = 0 
 
while password != "secret" and attempt < 3:
   password = input("Enter Password :")
   if password == "secret":
     print("Access Granted")
   else:
      print("Wrong Password")

if password != "secret" and attempt == 3:
   print("too many attempt, account lockeds")
