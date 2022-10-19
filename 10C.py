import tkinter
import pymysql
import tkinter.messagebox


def upd():
    db = pymysql.connect(user='root', password='',
                         host='localhost', db='syitbdemo')
    cur = db.cursor()
    str = "update demo set age=20 where PERCENTAGE='"+IENTRY.get()+"'"
    cur.execute(str)
    tkinter.messagebox.showinfo("info msg", "Record updated")
    db.commit()
    db.close()


def dele():
    db = pymysql.connect(user='root', password='',
                         host='localhost', db='syitbdemo')
    cur = db.cursor()
    str = "delete from demo where PERCENTAGE='"+IENTRY.get()+"'"
    cur.execute(str)
    tkinter.messagebox.showinfo("info msg", "Record deleted")
    db.commit()
    db.close()


def put(*args):
    db = pymysql.connect(user='root', password='',
                         host='localhost', db='syitbdemo')
    cursor = db.cursor()
    sqlquery1 = "INSERT INTO demo(FIRST_NAME,LAST_NAME, AGE, SEX, PERCENTAGE) VALUES ('"+fn.get(
    )+"','"+ln.get()+"','"+age.get()+"','"+sex.get()+"','"+percentage.get()+"')"
    cursor.execute(sqlquery1)
    db.commit()
    tkinter.messagebox.showinfo("info msg", "Record Inserted")
    db.commit()
    db.close()


def get():
    db = pymysql.connect(user='root', password='',
                         host='localhost', db='syitbdemo')
    cur = db.cursor()
    cur.execute("select * from demo")
    results = cur.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3], row[4])
    db.close()


root = tkinter.Tk()
root.title("INSERT DATA")
fn = tkinter.Entry(root, width=7)
ln = tkinter.Entry(root, width=7)
age = tkinter.Entry(root, width=7)
sex = tkinter.Entry(root, width=7)
percentage = tkinter.Entry(root, width=7)
fn.grid(row=0, column=1)
ln.grid(row=1, column=1)
age.grid(row=2, column=1)
sex.grid(row=3, column=1)
percentage.grid(row=4, column=1)
tkinter.Label(root, text='First_name').grid(row=0, column=0)
tkinter.Label(root, text='Last_name').grid(row=1, column=0)
tkinter.Label(root, text='age').grid(row=2, column=0)
tkinter.Label(root, text='sex').grid(row=3, column=0)
tkinter.Label(root, text='percentage').grid(row=4, column=0)
tkinter.Button(root, text="Insert", command=put).grid(row=5, column=1)
tkinter.Button(root, text="Display", command=get).grid(row=5, column=2)
tkinter.Label(root, text='percentage').grid(row=6, column=0)
IENTRY = tkinter.Entry(root, width=7)
IENTRY.grid(row=7, column=1)

tkinter.Button(root, text="Delete", command=dele).grid(row=8, column=0)
tkinter.Button(root, text="Update", command=upd).grid(row=8, column=1)

root.mainloop()
