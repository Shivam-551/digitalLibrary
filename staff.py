import sys
import mysql.connector
class lib_staff:
    def __init__(self,cur):
        self.cur=cur
    def staff(self):
        print("====Library Staff Menu====\n"
              "What would you like to do?\n"
              "1. Add new books\n"
              "2. Display all available books\n"
              "3. Record of books issued\n"
              "4. Exit")
        choice1 =int(input("Enter your query number(1,2,3 or 4)?\n"))
        if choice1==1:
            self.add_books()
        elif choice1==2:
            self.display()
        elif choice1==3:
            self.issued()
        elif choice1==4:
            print("This project is created by SHIVAM ARORA.\nThank you for using.")
            sys.exit()
    def add_books(self):
        print("How many books do you want to add?")
        n=int(input())
        books=[]
        for i in range(n):
            name=input("Enter the name of the book")
            bookid=int(input("Enter the book Id"))
            b1=(name,bookid)
            books.append(b1)
        s="INSERT INTO book (book_name,book_id) VALUES(%s,%s)"
        self.cur.executemany(s,books)
        mydb.commit()
        print("New book added to Library")

        self.more()
    def display(self):
        print("====Books available in this Library====\n")
        s="SELECT * from book"
        self.cur.execute(s)
        result=self.cur.fetchall()
        for rec in result:
            print(rec)
        self.more()
    def issued(self):
        print("====Books issued from this Library====\n")
        s="SELECT * from issuedbooks"
        self.cur.execute(s)
        result=self.cur.fetchall()
        for rec in result:
            print(rec)
        self.more()
    def more(self):
        k=input("\nDo you want to do anything else?(y/n)")
        if k=='y':
            self.staff()
        else:
            print("This project is created by SHIVAM ARORA.\nThank you for using.")
            sys.exit()
mydb=mysql.connector.connect(host='localhost',user='root',password='rootpasswordgiven',database='db1')
cur=mydb.cursor()
obj1=lib_staff(cur)

