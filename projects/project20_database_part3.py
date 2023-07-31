# creating and deleting record from database

from tkinter import *
import sqlite3

def createDatabase():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE records(
                name text,
                age integer,
                email text)"""
                )

    conn.commit()
    conn.close()

# createDatabase()

root = Tk()
root.title("Info")
root.geometry("505x500")

frame1 = LabelFrame(root, text="info.db", padx=10, pady=10)
frame1.grid(columnspan=2, padx=10, pady=10)

# creating label and entry boxes
name_label = Label(frame1, text="Name")
age_label = Label(frame1, text="Age")
email_label = Label(frame1, text="Email")

name = Entry(frame1, width=70)
name.insert(0, "Full Name")
age = Entry(frame1, width=70)
email = Entry(frame1, width=70)


# showing them in the screen with grid
name_label.grid(row=0, column=0)
age_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)

name.grid(row=0, column=1)
age.grid(row=1, column=1)
email.grid(row=2, column=1)

def submit():
    global message_label
    message_label.destroy()
    if name.get() == "" or age.get() == "" or email.get() == "":
        message_label = Label(frame1, text="Fill up the form correctly", fg="red")
        message_label.grid(row=3, column=1, sticky=W)
        return
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("""INSERT INTO records VALUES(
                :name,
                :age,
                :email)""",
                {
                    "name": name.get(),
                    "age": age.get(),
                    "email": email.get()
                }
                )
    message_label = Label(frame1, text="Submitted successfully!", fg="green")
    message_label.grid(row=3, column=1, sticky=W)

    conn.commit()
    conn.close()

    name.delete(0, END)
    age.delete(0, END)
    email.delete(0, END)

    show()

def show():
    global record_label
    record_label.destroy()
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    cur.execute("""SELECT *, oid FROM records""")
    records = cur.fetchall()
    string_record = ""
    record_list = ""
    for record in records:
        for data in record:
            string_record += f"{data} - "
        record_list += string_record[-4:-3] + ". " + string_record[:-7] + "\n"
        string_record = ""
    record_label = Label(root, text=record_list)
    record_label.grid(row=3, column=1, padx=10, pady=10, sticky=E)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    try:
        cur.execute("""DELETE FROM records WHERE oid = """ + oid.get())
        conn.commit()
        conn.close()
        show()
    except sqlite3.OperationalError:
        conn.commit()
        conn.close()


global editor, name_editor, age_editor, email_editor

def update():
    global editor
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * FROM records WHERE oid = """ + oid.get())
        records = cur.fetchall()
        index_error_catcher = records[0][0]

        editor = Tk()
        editor.title("Update a record")
        editor.geometry("505x150")

        frame1_editor = LabelFrame(editor, text="id = " + oid.get(), padx=10, pady=10)
        frame1_editor.grid(columnspan=2, padx=10, pady=10)

        global name_label, age_label, email_label, name_editor, age_editor, email_editor

        # creating label and entry boxes
        name_label = Label(frame1_editor, text="Name")
        age_label = Label(frame1_editor, text="Age")
        email_label = Label(frame1_editor, text="Email")


        name_editor = Entry(frame1_editor, width=70)
        age_editor = Entry(frame1_editor, width=70)
        email_editor = Entry(frame1_editor, width=70)

        name_editor.insert(0, records[0][0])
        age_editor.insert(0, records[0][1])
        email_editor.insert(0, records[0][2])

        # showing them in the screen with grid
        name_label.grid(row=0, column=0)
        age_label.grid(row=1, column=0)
        email_label.grid(row=2, column=0)

        name_editor.grid(row=0, column=1)
        age_editor.grid(row=1, column=1)
        email_editor.grid(row=2, column=1)

        submit_button_editor = Button(frame1_editor, text="Update", command=save)
        submit_button_editor.grid(row=3, column=1, sticky=E)

        conn.commit()
        conn.close()
    except IndexError:
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        conn.commit()
        conn.close()

def save():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    cur.execute("""UPDATE records SET
                name = :name_editor,                
                age = :age_editor,                
                email = :email_editor
                WHERE oid = :oid""",
                {
                    "name_editor": name_editor.get(),
                    "age_editor": age_editor.get(),
                    "email_editor": email_editor.get(),
                    "oid": oid.get()
                }
                )
    conn.commit()
    conn.close()
    editor.destroy()
    show()


message_label = Label(root)

submit_button = Button(frame1, text="Submit", command=submit)
submit_button.grid(row=3, column=1, sticky=E)


oid = Entry(root, width=5)
oid.insert(0, "id")
oid.grid(row=1, column=0, padx=10, sticky=W)
Button(root, text="Delete record", command=delete, bg="red", fg="white").grid(row=2, column=0, padx=10, ipadx=2, sticky=NW)
Button(root, text="Update record", command=update, bg="blue", fg="white").grid(row=3, column=0, padx=10, sticky=NW)
Button(root, text="Show records", command=show).grid(row=1, column=1, padx=10, sticky=E)

record_label = Label(root)

root.mainloop()
