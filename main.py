import mysql.connector as ms

c = ms.connect(host="localhost", user='root', password='harsh1234', database='LMS')
cur = c.cursor()

def main():
    print("\n--------WELCOME TO LIBRARY MANAGEMENT SYSTEM---------\n")
    print("""WHAT WOULD YOU LIKE TO DO:
    1.BOOK MANAGEMENT
    2.EMPLOYEE MANAGEMENT
    3.CUSTOMER MANAGEMENT
    4.EXIT""")
    ch = int(input("ENTER YOUR CHOICE:"))

    if ch == 1:
        def add_books():
            bcode = int(input("ENTER THE BOOK CODE:"))
            bname = input("ENTER THE BOOK NAME:")
            author = input("ENTER THE AUTHORS NAME:")
            status = input("ENTER THE BOOK STATUS:")
            pub = input("ENTER THE DATE WHEN IT WAS PUBLISHED:")
            genre = input("ENTER THE BOOK GENRE:")
            lan = input("ENTER THE LANGUAGE IN WHICH THE BOOK IS WRITTEN:")
            cost = float(input("ENTER THE BOOKS COST:"))
            stock = int(input("ENTER THE STOCK:"))
            q = "insert into book values(%s,'%s','%s','%s','%s','%s','%s',%s,%s)" % (
            bcode, bname, author, status, pub, genre, lan, cost, stock)
            cur.execute(q)
            c.commit()

        def edit_books():
            bcode = int(input("ENTER THE BOOK CODE OF THE BOOK TO BE UPDATED:"))
            print("""WHAT WOULD YOU LIKE TO UPDATE
            1.BOOK NAME
            2.AUTHOR NAME
            3.STATUS
            4.PUBLISHED YEAR
            5.GENRE
            6.LANGUAGE
            7.COST
            8.STOCK""")
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
                pub = input("ENTER THE CORRECT YEAR WHEN THE BOOK WAS PUBLISHED:")
                q = "update book set PUB_YEAR='%s' where bcode=%s" % (pub, bcode)
                cur.execute(q)
                c.commit()
            elif ch == 5:
                genre = input("ENTER THE BOOK GENRE:")
                q = "update book set genre='%s' where bcode=%s" % (genre, bcode)
                cur.execute(q)
                c.commit()
            elif ch == 6:
                lan = input("ENTER THE CORRECT LANGUAGE:")
                q = "update book set language='%s' where bcode=%s" % (lan, bcode)
            elif ch == 7:
                cost = float(input("ENTER THE BOOKS COST:"))
                q = "update book set cost=%s where bcode=%s" % (cost, bcode)
                cur.execute(q)
                c.commit()
            elif ch == 8:
                stock = int(input("ENTER THE STOCK:"))
                q = "update book set stock=%s where bcode=%s" % (stock, bcode)
                cur.execute(q)
                c.commit()
            else:
                print("INVALID INPUT:")

        def remove_books():
            bcode = int(input("ENTER THE BOOK CODE OF THE BOOK TO BE REMOVED:"))
            q = "delete from book where bcode=%s" % (bcode,)
            cur.execute(q)
            c.commit()

        while True:
            print("\n-------------BOOK MANAGEMENT-----------------\n")
            print("""\n1.ADD BOOKS
            2.EDIT BOOKS
            3.REMOVE BOOKS\n""")
            ch = int(input("ENTER YOUR CHOICE:"))
            if ch == 1:
                add_books()
            elif ch == 2:
                edit_books()
            elif ch == 3:
                remove_books()
            else:
                print("INVALID INPUT:")
            ch1 = input("WOULD YOU LIKE TO CONTINUE: (y/n)")
            if ch1 == 'y':
                ch2 = int(input("""WHAT WOULD YOU LIKE TO DO:
                1.RETURN TO MAIN MENU
                2.CONTINUE ON THIS MENU"""))
                if ch2 == 1:
                    main()
                elif ch2 == 2:
                    continue
            elif ch1 == 'n':
                break
            elif ch == 2:
                pass

    def main1():
        print("\n--------WELCOME TO THE ONLINE LIBRARY---------\n")
        print("""WHAT WOULD YOU LIKE TO DO:
        1.BROWSE BOOK
        2.ISSUE A BOOK
        3.RETURN A BOOK
        4.EXIT""")
        ch = int(input("ENTER YOUR CHOICE:"))

        if ch == 1:
            while True:
                q = "select * from book"
                cur.execute(q)
                for x in cur:
                    print(x)
                ch1 = input("WOULD YOU LIKE TO FILTER THE DATA (Y/N):")
                if ch1 == 'y':
                    print("""\nHOW WOULD YOU LIKE TO FILTER THE DATA:
                    1.BOOK
                    2.AUTHOR
                    3.GENRE
                    4.COST\n""")
                    ch2 = int(input("ENTER YOUR CHOICE"))
                    if ch2 == 1:
                        bname = input("WHICH BOOK ARE YOU LOOKING FOR:")
                        q = "select * from book where bname='%s'" % (bname,)
                        cur.execute(q)
                        for x in cur:
                            print(x)
                    elif ch2 == 2:
                        author = input("WHICH AUTHOR ARE YOU LOOKING FOR:")
                        q = "select * from book where author='%s'" % (author,)
                        cur.execute(q)
                        for x in cur:
                            print(x)
                    elif ch2 == 3:
                        genre = input("WHAT GENRE ARE YOU LOOKING FOR:")
                        q = "select * from book where genre='%s'" % (genre,)
                        cur.execute(q)
                        for x in cur:
                            print(x)
                    elif ch2 == 4:
                        lo = int(input("ENTER THE LOWER LIMIT:"))
                        up = int(input("ENTER THE UPPER LIMIT:"))
                        q = "select * from book where cost between %s and %s" % (lo, up)
                        cur.execute(q)
                        for x in cur:
                            print(x)
                elif ch1 == 'n':
                    pass
                ch2 = input("WOULD YOU LIKE TO CONTINUE: (y/n)")
                if ch2 == 'y':
                    main1()
                elif ch1 == 'n':
                    break
                elif ch == 2:
                    pass

        def issue():
            orderid = int(input("ENTER THE ORDER ID:"))
            regid = int(input("ENTER THE REGISTRATION ID:"))
            custname = input("ENTER THE CUSTOMERS NAME:")
            bname = input("ENTER THE BOOKS NAME:")
            issue_date = input("ENTER THE ISSUE DATE:")
            time = input("ENTER THE ISSUE TIME:")
            cost = float(input("ENTER THE BOOKS COST:"))
            payment = input("ENTER THE STATUS OF THE ORDER:")
            lib = input("ENTER THE LIBRARIAN IN CHARGE:")
            from datetime import datetime
            from datetime import timedelta
            given_date = str(issue_date)
            date_format = '%Y/%m/%d'
            dtObj = datetime.strptime(given_date, date_format)
            n = 14
            return_date = dtObj + timedelta(days=n)
            print("THE DEADLINE TO RETURN THIS BOOK IS", return_date)
            q = "insert into issue values(%s,%s,'%s','%s','%s','%s',%s,'%s','%s','%s')" % (
            orderid, regid, custname, bname, issue_date, time, cost, payment, return_date, lib)
            cur.execute(q)
            c.commit()
            q1 = "update book set stock=stock-1 where bname='%s'" % (bname,)
            cur.execute(q1)
            c.commit()

        def update_issue():
            orderid = int(input("ENTER THE ORDER ID:"))
            print("""WHAT WOULD YOU LIKE TO UPDATE
            1.CUSTOMERS REGISTRATION ID
            2.CUSTNAME
            3.BNAME
            4.PAYMENT DETAILS""")
            ch = int(input("ENTER YOUR CHOICE:"))
            if ch == 1:
                regid = int(input("ENTER THE CUSTOMERS REGISTRATION ID:"))
                q = "update returnbook set regid=%s where orderid=%s" % (regid, orderid)
                cur.execute(q)
                c.commit()
            elif ch == 2:
                custname = input("ENTER THE NEW CUSTOMER NAME:")
                q = "update issue set custname='%s' where orderid=%s" % (custname, orderid)
                cur.execute(q)
                c.commit()
            elif ch == 3:
                bname = input("ENTER THE BOOKS NAME:")
                q = "update issue set bname='%s' where orderid=%s" % (bname, orderid)
                cur.execute(q)
                c.commit()
            elif ch == 4:
                payment = input("ENTER THE STATUS OF THE PAYMENT:")
                q = "update issue set issue_date='%s' where orderid=%s" % (payment, orderid)
                cur.execute(q)
                c.commit()
            else:
                print("INVALID INPUT:")

        def display_issue():
            print("""WHAT WOULD YOU LIKE TO DO:
            1.DISPLAY ALL DATA
            2.SEARCH A SPECIFIC ORDER
            """)
            ch = int(input("ENTER YOUR CHOICE:"))
            if ch == 1:
                q = "select * from issue"
                cur.execute(q)
                for x in cur:
                    print(x)
            elif ch == 2:
                orderid = int(input("ENTER THE REGISTRATION ID NO OF THE CUSTOMER:"))
                q = "select * from issue where orderid=%s" % (orderid,)
                cur.execute(q)
                for x in cur:
                    print(x)
            else:
                print("INVALID INPUT!")

        def delete_issue():
            orderid = int(input("ENTER THE REGISTRATION ID OF THE CUSTOMER WHOESE ORDER TO BE REMOVED:"))
            q = "delete from issue where orderid=%s" % (orderid,)
            cur.execute(q)
            c.commit()

        while True:
            print("\n-------------ISSUE A BOOK-----------------\n")
            print("""\n1.PLACE AN ORDER
            2.UPDATE AN ORDER
            3.DISPLAY ORDERS
            4.DELETE AN ORDER\n""")
            ch = int(input("ENTER YOUR CHOICE:"))
            if ch == 1:
                issue()
            elif ch == 2:
                update_issue()
            elif ch == 3:
                display_issue()
            elif ch == 4:
                delete_issue()
            else:
                print("INVALID OUTPUT:")
            ch1 = input("WOULD YOU LIKE TO CONTINUE: (y/n)")
            if ch1 == 'y':
                ch2 = int(input("""WHAT WOULD YOU LIKE TO DO:
                1.RETURN TO MAIN MENU
                2.CONTINUE ON THIS MENU
                """))
                if ch2 == 1:
                    main1()
                elif ch2 == 2:
                    continue
            elif ch1 == 'n':
                break
            elif ch == 3:
                pass

    def return_book():
        orderid = int(input("ENTER THE ORDER ID:"))
        regid = int(input("ENTER THE CUSTOMERS REGISTRATION ID:"))
        custname = input("ENTER THE CUSTOMERS NAME:")
        bname = input("ENTER THE BOOKS NAME:")
        return_date = input("ENTER THE RETURN DATE:")
        payment = input("ENTER THE STATUS OF THE ORDER:")
        review = input("ENTER THE CUSTOMERS REVIEW ON THE BOOK:")
        q = "insert into returnbook values(%s,%s,'%s','%s','%s','%s','%s')" % (
        orderid, regid, custname, bname, return_date, payment, review)
        cur.execute(q)
        c.commit()
        q1 = "update book set stock=stock+1 where bname='%s'" % (bname,)
        cur.execute(q1)
        c.commit()
        q1 = "select deadline from issue where orderid=%s" % (orderid,)
        cur.execute(q1)
        x = cur.fetchall()
        q2 = "select return_date from returnbook where orderid=%s" % (orderid,)
        cur.execute(q2)
        y = cur.fetchall()
        if x<y:
            print("PLS PAY THE PENANLTY FEES!!")
        elif x>y:
            pass
            
    def update_return():
        orderid = int(input("ENTER THE REGISTRATION ID OF THE CUSTOMER WHOSE ORDER HAS TO BE UPDATED:"))
        print("""WHAT WOULD YOU LIKE TO UPDATE
        1.CUSTOMER'S REGISTRATION ID
        2.CUSTOMER NAME
        3.BOOK NAME
        4.RETURN DATE
        5.PAYMENT DETAILS
        6.REVIEW""")
        ch = int(input("ENTER YOUR CHOICE:"))
        if ch == 1:
            regid = int(input("ENTER THE CUSTOMER'S REGISTRATION ID:"))
            q = "update returnbook set regid=%s where orderid=%s" % (regid, orderid)
            cur.execute(q)
            c.commit()
        elif ch == 2:
            custname = input("ENTER THE NEW CUSTOMER NAME:")
            q = "update returnbook set custname='%s' where orderid=%s" % (custname, orderid)
            cur.execute(q)
            c.commit()
        elif ch == 3:
            bname = input("ENTER THE BOOK'S NAME:")
            q = "update returnbook set bname='%s' where orderid=%s" % (bname, orderid)
            cur.execute(q)
            c.commit()
        elif ch == 4:
            return_date = input("ENTER THE DATE WHEN THE BOOK WAS RETURNED:")
            q = "update returnbook set return_date='%s' where orderid=%s" % (return_date, orderid)
            cur.execute(q)
            c.commit()
        elif ch == 5:
            payment = input("ENTER THE STATUS OF THE PAYMENT:")
            q = "update returnbook set payment='%s' where orderid=%s" % (payment, orderid)
            cur.execute(q)
            c.commit()
        elif ch == 6:
            review = input("ENTER THE NEW REVIEW:")
            q = "update returnbook set review='%s' where orderid=%s" % (review, orderid)
            cur.execute(q)
            c.commit()
        else:
            print("INVALID INPUT:")
    
    def display_returns():
        print("""WHAT WOULD YOU LIKE TO DO:
        1.DISPLAY ALL DATA
        2.SEARCH A SPECIFIC ORDER
        """)
        ch = int(input("ENTER YOUR CHOICE:"))
        if ch == 1:
            q = "select * from returnbook"
            cur.execute(q)
            for x in cur:
                print(x)
        elif ch == 2:
            orderid = int(input("ENTER THE ORDER ID NO OF THE CUSTOMER:"))
            q = "select * from returnbook where orderid=%s" % (orderid,)
            cur.execute(q)
            for x in cur:
                print(x)
    
    def remove_return():
        orderid = int(input("ENTER THE ORDER ID OF THE CUSTOMER TO BE REMOVED:"))
        q = "delete from returnbook where orderid=%s" % (orderid,)
        cur.execute(q)
        c.commit()
    
    while True:
        print("\n-------------RETURN A BOOK-----------------\n")
        print("""\n1.RETURN BOOK
        2.UPDATE A RETURN
        3.DISPLAY RETURNS
        4.REMOVE RETURN\n""")
        ch = int(input("ENTER YOUR CHOICE:"))
        if ch == 1:
            return_book()
        elif ch == 2:
            update_return()
        elif ch == 3:
            display_returns()
        elif ch == 4:
            remove_return()
        else:
            print("INVALID OUTPUT:")
        
        ch1 = input("WOULD YOU LIKE TO CONTINUE: (y/n)")
        if ch1 == 'y':
            ch2 = int(input("""WHAT WOULD YOU LIKE TO DO:
            1.RETURN TO MAIN MENU
            2.CONTINUE ON THIS MENU
            """))
            if ch2 == 1:
                main()
            elif ch2 == 2:
                continue
        elif ch1 == 'n':
            break
    
    du = {"1": "ram123", "2": "raj123", "3": "rahul123"}
    de = {"harsh": "1234", "saneen": "password", "sanchit": "050234"}
    ut = int(input("""ENTER THE USER TYPE
    1.ADMIN
    2.CUSTOMER\n"""))
    if ut == 1:
        u = input("ENTER YOUR USERNAME:")
        p = input("ENTER YOUR PASSWORD:")
        if u in de.keys():
            if de[u] == p:
                print("ACCESS GRANTED")
                main()
            else:
                print("INVALID USERNAME / PASSWORD")
    elif ut == 2:
        r = input("ENTER YOUR REGISTRATION ID:")
        p = input("ENTER YOUR PASSWORD:")
        if r in du.keys():
            if du[r] == p:
                print("ACCESS GRANTED")
                main1()
            else:
                print("INVALID USERNAME / PASSWORD")
