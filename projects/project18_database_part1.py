# finally we will add database to out project

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

title = "Connecting Database"
root = Tk()
root.title(title)

# database

# creating a database or connect to a database
conn = sqlite3.connect("address_book.db")

# creating a cursor - which will do some changes in the database and come back with result
cur = conn.cursor()

# create database table
# sqlite has only five data types -> text, integer, real, null, blob
'''
cur.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )
            """)
'''
# # commented out once table created

# creating input box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

def submit():
    global conn, cur
    # creating a database or connect to a database
    conn = sqlite3.connect("address_book.db")
    # creating a cursor - which will do some changes in the database and come back with result
    cur = conn.cursor()

    # insert data into table
    cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                {
                    "f_name": f_name.get(),
                    "l_name": l_name.get(),
                    "address": address.get(),
                    "city": city.get(),
                    "state": state.get(),
                    "zipcode": zipcode.get()
                }
                )

    # commit the changes
    conn.commit()
    # close the database connection
    conn.close()

    # clear input boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def show():
    global conn, cur
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()

    cur.execute("SELECT *, oid FROM addresses")
    records = cur.fetchall() # we can also use -> fetchone(), fetchmany(number)
    print(records)

    conn.commit()
    conn.close()

# creating input boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# creating submit buttons
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=6, column=1, padx=20, pady=10, sticky=E)

# creating a query button
query_button = Button(root, text="Show Records", command=show, relief=SOLID)
query_button.grid(row=7, columnspan=2, ipadx=100)

# commit the changes
conn.commit()

# close the database connection
conn.close()

root.mainloop()
