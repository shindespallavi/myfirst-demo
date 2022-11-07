# problem 1
#num = int(input("Enter the number"))
#for i in range(1,11):
    #print(str(num) + "x"+ str(i) +"=" + str(i*num))
 # print(f"{num}X{i}={num*i}")

#problem 2
#to greet the person whose name starts from s
#l1 = ["harry","sachin","sohan","rahul"]
#for name in l1:
   # if name.startswith("s"):
   #     print("hello " + name )
        

  #problem 4

num = int(input("Enter the number")) 
prime = True
for i in range(2,num):
    if(num%i == 0 ):
        prime = False
        break
    if prime:
        print("This number is prime")
    else:
            print("This number is not prime")
