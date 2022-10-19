import tkinter
import tkinter.messagebox
import pymysql


def put(*args):
    db = pymysql.connect(user='root', password='',
                         host='localhost', db='syitbdemo')
    cursor = db.cursor()
    sqlquery1 = "INSERT INTO demo(FIRST_NAME,LAST_NAME, AGE, SEX, PERCENTAGE) VALUES ('"+fn.get(
    )+"','"+ln.get()+"','"+age.get()+"','"+sex.get()+"','"+percentage.get()+"')"
    try:
        # Execute the SQL command
        cursor.execute(sqlquery1)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    tkinter.messagebox.showinfo("info msg", "Record Inserted")
# db.commit()
    db.close()


def get():
    db = pymysql.connect(user='root', password='',
                         host='localhost', db='syitbdemo')
    cursor = db.cursor()
    cursor.execute("select * from demo ")
    results = cursor.fetchall()
    row = cursor.fetchone()
    tkinter.messagebox.showinfo("info msgs", results)
    db.close()


root = tkinter.Tk()
root.title("Insert Data")
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
tkinter.Button(root, text="Insert", command=put).grid()
tkinter.Button(root, text="Display", command=get).grid()
root.mainloop()
