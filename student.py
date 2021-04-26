import sys
import mysql.connector
class lib_student:
    def __init__(self,cur):
        self.cur=cur
    def student(self):
        print("====Student Menu====\n"
              "What would you like to do?\n"
              "1. Display the list of books available.\n"
              "2. Lend a book.\n"
              "3. Return a book.\n"
              "4. Exit. ")
        choice1=int(input("Enter your query number?\n"))
        if choice1==1:
            self.display1()
        elif choice1==2:
            self.lend()
        elif choice1==3:
            self.returnbook()
        elif choice1==4:
            print("This project is created by SHIVAM ARORA.\nThank you for using.")
            sys.exit()
    def display1(self):
        print("====Books available in this library.\n")
        s="SELECT * from book"
        self.cur.execute(s)
        result=self.cur.fetchall()
        for rec in result:
            print(rec)
        self.more1()
    def more1(self):
        k=input("\nDo you want to do anything else?(y/n)")
        if k=='y':
            self.student()
        else:
            print("This project is created by SHIVAM ARORA.\nThank you for using.")
            sys.exit()
    def lend(self):
        name=input("Enter your name")
        roll=int(input("Enter your university roll number"))
        n=int(input("How many books do u want?"))
        books=[]
        for i in range(n):
            bookname=input("Enter the name of the book")
            number=int(input("Enter the bookid"))
            s="SELECT * from book"
            self.cur.execute(s)
            res=self.cur.fetchall()

            for book_title,bookid in res:
                if bookid==number:
                    b1=(bookname,number,name,roll)
                    books.append(b1)
                    s="DELETE FROM book WHERE book_id= %s"
                    self.cur.execute(s, (number,))
                    mydb.commit()
                    print("Book has been issued.")
                    break
            else:
                print("Book not available")

        s="INSERT INTO issuedbooks (book_name,book_id,student_name,student_rollnumber) VALUES(%s, %s, %s, %s)"
        self.cur.executemany(s, books)
        mydb.commit()
        self.more1()
    def returnbook(self):
        name = input("Enter your name")
        roll = int(input("Enter your university roll number"))
        n = int(input("How many books do u want to return?"))
        books = []
        for i in range(n):
            bookname=input("Enter the name of the book")
            number=int(input("Enter the bookid"))
            b1=(bookname, number)
            books.append(b1)
        s="INSERT INTO book(book_name, book_id) VALUES(%s, %s)"
        self.cur.executemany(s, books)
        mydb.commit()

        s="DELETE FROM issuedbooks WHERE book_id= %s"
        self.cur.execute(s, (number, ))
        mydb.commit()
        print("Book has been returned.")
        self.more1()

mydb=mysql.connector.connect(host='localhost',user='root',password='rootpasswordgiven',database='db1')
cur=mydb.cursor()

obj2=lib_student(cur)