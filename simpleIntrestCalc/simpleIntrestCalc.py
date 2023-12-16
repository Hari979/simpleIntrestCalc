print("This is simple interest calulator...!\nCalculate your simple interest related queries\n")
print("==> Press 1 to find your simple interest\n")
print("==> Press 2 to find your principal amount\n")
print("==> Press 3 to find your rate of interest\n")
print("==> Press 4 to find your number of terms\n")
siq=int(input())
if siq==1:
    p=int(input("Enter your principal amount rs\n"))
    n=int(input("Enter number of years\n"))
    r=int(input("Enter rate of interest\n"))
    if p==0 or n==0 or r==0:
        print("Oops you enter a null value!!!!")
    else:
        si=float((p*n*r)/100)
        print(f"Simple Interest you need to pay rs {round(si,2)}")
elif siq==2:
    n=int(input("Enter number of years\n"))
    r=int(input("Enter rate of interest\n"))
    si=int(input("Enter your simple interest rs\n"))
    if n==0 or r==0 or si==0:
        print("Oops you enter a null value!!!!")
    else:
        p=float((100*si)/(r*n))
        print(f"Your Principal amount is rs {round(p,2)}")
elif siq==3:
    n=int(input("Enter number of years\n"))
    p=int(input("Enter your principal amount rs\n"))
    si=int(input("Enter your simple interest rs\n"))
    if n==0 or p==0 or si==0:
       print("Oops you enter a null value!!!!")
    else:
       r=int((100*si)/(p*n))
       print(f"Your Rate of Interest is {r}%")
elif siq==4:
    r=int(input("Enter rate of interest\n"))
    p=int(input("Enter your principal amount rs\n"))
    si=int(input("Enter your simple interest rs\n"))
    if r==0 or p==0 or si==0:
       print("Oops you enter a null value!!!!")
    else:
       n=int((100*si)/(p*r))
       print(f"Terms = {n} years")
else:
    print("Press the correct key")