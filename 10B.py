import pymysql
import tkinter


def get():
    db = pymysql.connect(user='root', password='',
                         host='localhost', db='syitbdemo')
    cur = db.cursor()
    str = "select * from demo where PERCENTAGE='"+IENTRY.get()+"'"
    cur.execute(str)
    for (fn, ln, age, sex, percentage) in cur:
        print("fn:{},ln:{},age:{},sex:{},percentage:{}".format(
            fn, ln, age, sex, percentage))
    db.commit()
    db.close()


root = tkinter.Tk()
root.title("search data")
tkinter.Label(root, text="percentage").grid(row=0, column=0)
IENTRY = tkinter.Entry(root, width=10)
IENTRY.grid(row=0, column=1)
tkinter.Button(root, text="search", command=get).grid(row=0, column=2)
root.mainloop()
