while(True) :
    try:
        a=float(input("enter a number : "))
        if(a>0):
            print("{}:  is positive number ".format(a))
        elif(a<0):
            print("{}:  is negative number ".format(a))
        else:
            print("{}:  number is zero".format(a))
    except ValueError:
        print("enter valid number ")