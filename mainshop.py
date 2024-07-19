from shop1 import saveempdata
from shop2 import disprecords
from shop_Search import searchrecord
from shop_search1 import searchrecord1
while(True):
    print("*"*50)
    print("Employee Information System")
    print("*"*50)
    print("\t1.Add New Employee(s) Data")
    print("\t2.Display Employee Data")
    print("\t3.Search Single Employee Data with name")
    print("\t4.Search Single Employee Data with id")
    print("\t5.Exit")
    print("*"*50)
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                saveempdata()
            case 2:
                disprecords()
            case 3:
                searchrecord()
            case 4:
                searchrecord1()

            case 5:
                print("Thx for Using This Program")
                break
            case _:
                print("Ur Selection of Operation is wrong try again")
    except ValueError:
       print("Don't enter alnums,strs and symbols for choice-try again")
