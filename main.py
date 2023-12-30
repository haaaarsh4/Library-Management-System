import mysql.connector as ms

c = ms.connect(host="localhost", user='root', password='harsh1234', database='LMS')
cur = c.cursor()


def main():
    print("\n--------WELCOME TO LIBRARY MANAGEMENT SYSTEM---------\n")
    print("""WHAT WOULD YOU LIKE TO DO:
    1.BOOK MANAGEMENT:
    2.EMPLOYEE MANAGEMENT:
    3.CUSTOMER MANAGEMENT
    4.ISSUE A BOOK:
    5.RETURN A BOOK
    6.EXIT""")
    ch = int(input("ENTER YOUR CHOICE:"))

    if ch == 1:
        book_management()
    elif ch == 2:
        employee_management()
    elif ch == 3:
        customer_management()
    elif ch == 4:
        issue_book()
    elif ch == 5:
        return_book()
    elif ch == 6:
        pass  # exit or return, depending on your use case
    else:
        print("INVALID INPUT:")


def book_management():
    while True:
        print("\n-------------BOOK MANAGEMENT-----------------\n")
        print("""\n1.ADD DATA
        2.UPDATE DATA
        3.DISPLAY DATA
        4.DELETE DATA
        5.SEARCH DATA\n""")
        ch = int(input("ENTER YOUR CHOICE:"))

        if ch == 1:
            add_data()
        elif ch == 2:
            update()
        elif ch == 3:
            display()
        elif ch == 4:
            remove()
        elif ch == 5:
            search()
        else:
            print("INVALID INPUT:")

        ch1 = input("WOULD YOU LIKE TO CONTINUE: (y/n)")

        if ch1 == 'n':
            break
        elif ch1 == 'y':
            ch2 = int(input("""WHAT WOULD YOU LIKE TO DO:
            1.RETURN TO MAIN MENU
            2.CONTINUE ON THIS MENU
            """))
            if ch2 == 1:
                main()
            elif ch2 == 2:
                continue


def add_data():
    bcode = int(input("ENTER THE BOOK CODE:"))
    bname = input("ENTER THE BOOK NAME:")
    author = input("ENTER THE AUTHORS NAME:")
    status = input("ENTER THE BOOK STATUS:")
    stock = int(input("ENTER THE STOCK:"))
    genre = input("ENTER THE BOOK GENRE:")
    cost = float(input("ENTER THE BOOKS COST:"))
    q = "insert into book values(%s,'%s','%s','%s',%s,'%s',%s)" % (bcode, bname, author, status, stock, genre, cost)
    cur.execute(q)
    c.commit()


def update():
    bcode = int(input("ENTER THE BOOK CODE OF THE BOOK TO BE UPDATED:"))
    print("""WHAT WOULD YOU LIKE TO UPDATE
    1.BOOK NAME
    2.AUTHOR
    3.STATUS
    4.STOCK
    5.GENRE
    6.COST""")
    ch = int(input("ENTER YOUR CHOICE:"))

    if ch == 1:
        bname = input("ENTER THE NEW BOOK NAME:")
        q = "update book set bname='%s' where bcode=%s" % (bname, bcode)
        cur.execute(q)
        c.commit()
    elif ch == 2:
        author = input("ENTER THE AUTHORS NAME:")
        q = "update book set author='%s' where bcode=%s" % (author, bcode)
        cur.execute(q)
        c.commit()
    elif ch == 3:
        status = input("ENTER THE BOOK STATUS:")
        q = "update book set status='%s' where bcode=%s" % (status, bcode)
        cur.execute(q)
        c.commit()
    elif ch == 4:
        stock = int(input("ENTER THE STOCK:"))
        q = "update book set stock=%s where bcode=%s" % (stock, bcode)
        cur.execute(q)
        c.commit()
    elif ch == 5:
        genre = input("ENTER THE BOOK GENRE:")
        q = "update book set genre='%s' where bcode=%s" % (genre, bcode)
        cur.execute(q)
        c.commit()
    elif ch == 6:
        cost = float(input("ENTER THE BOOKS COST:"))
        q = "update book set cost=%s where bcode=%s" % (cost, bcode)
        cur.execute(q)
        c.commit()
    else:
        print("INVALID INPUT:")


def display():
    q = "select * from book"
    cur.execute(q)
    for x in cur:
        print(x)


def remove():
    bcode = int(input("ENTER THE BOOK CODE OF THE BOOK TO BE REMOVED:"))
    q = "delete from book where bcode=%s" % (bcode,)
    cur.execute(q)
    c.commit()


def search():
    print("""\nHOW WOULD YOU LIKE TO SEARCH THE DATA:
    1.BOOK
    2.AUTHOR
    3.GENRE\n""")
    ch = int(input("ENTER YOUR CHOICE"))

    if ch == 1:
        bname = input("WHICH BOOK ARE YOU LOOKING FOR:")
        q = "select * from book where bname='%s'" % (bname,)
        cur.execute(q)
        for x in cur:
            print(x)
    elif ch == 2:
        author = input("WHICH AUTHOR ARE YOU LOOKING FOR:")
        q = "select * from book where author='%s'" % (author,)
        cur.execute(q)
        for x in cur:
            print(x)
    elif ch == 3:
        genre = input("WHAT GENRE ARE YOU LOOKING FOR:")
        q = "select * from book where genre='%s'" % (genre,)
        cur.execute(q)
        for x in cur:
            print(x)


if __name__ == "__main__":
    main()
