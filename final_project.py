a=[]  # credicted amount
d=[]  # Debicted amount
f=[]  # Credicted note 
h=[]  # Debicted note 
o=[]  # date
p=[]  # time 
v=[]# credicted 
w=[] #  debicted

# importing then library functions

from tabulate import tabulate
import datetime
now = datetime.datetime.now()

for i in range(0,100):
    print("If the amuont is credicted then select 1 ")
    print("If the amount is debicted then select 0 ")
    
    b=int(input())
    if b==1 :

            a.append(int(input("Enter the amount to be credicted ")))
            f.append(input("entre note : "))
            o.append(now.strftime("%d-%m-%Y  "))
            p.append(now.strftime ("%H:%M:%S"))
            print(a)
            print(f)
            print("\n")

            
            
            
        
    elif b==0 :
        
             d.append(int(input("Enter the amount to be debicted  ")))
             h.append(input("entre note : "))
             o.append(now.strftime("%d-%m-%Y  "))
             p.append(now.strftime ("%H:%M:%S"))
             print(d)
             print(h)
             print("\n")
             
             
             
    else :
        print("Select the valid option")
        print("\n")
    c=(input("If you want to see another history n 'y/n'"))
    if c=='y':
        continue
    elif c=='n':
        break


print("\n")

# printing the table 
for i in range(0,10):
        m = input("Select 'c' for credicted history \n Select'd' for debicted history  \n")
        if m == 'c':
                    print("You have done credicted transactions ",len(a))
                    r=int(input("Enter the valid transactions you want  : "))
                    for i in range(0,r) :
                          v.append([a[i],f[i],o[i],p[i]])
                    head=["CREDICTED   ","NOTE ","DATE " ,"TIME" ]
                    print(tabulate(v,headers=head,tablefmt="grid"))
                    print("\n")
                    

        elif m == 'd':
                    print("You have done credicted transactions ",len(d))

                    r=int(input("Enter the valid transactions you want  : "))
                    for i in range(0,r) :
                          w.append([d[i],h[i],o[i],p[i]])
                    head=["DEBICTED  ","NAME  ","DATE ","TIME" ]
                    print(tabulate(w,headers=head,tablefmt="grid"))
                    print("\n")


        else:
                    print("Select the valid option !") 

        c=(input("If you want to enter the another entry select 'y/n'"))
        if c=='y':
           continue
        elif c=='n':
           break


# total debicted and credicted amounrt 

print("\n")
print("------------------------------------------------***************************--------------------------------")
print("Total amount credicted =  ",sum(a))
print("Total amount debicted  =  ",sum(d))
print("\n")
print("Current balance =   ",sum(a)-sum(d))

print(" HAVE A GOOD DAY ! ")
