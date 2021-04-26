from staff import *
from student import *
def main():
    print("====Welcome to Online Library====\n"
          "Login access:\n"
          "1. Library staff\n"
          "2. Student")
    choice=int(input("(1/2)?"))
    if choice==1:
        obj1.staff()
    elif choice==2:
        obj2.student()
main()