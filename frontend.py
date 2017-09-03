"""
A program that stores this book information:
serverip,Author,Year,ISBN

User can:
view all records
search an entry
add entry
update entry
delete
close
"""

from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(serverip_text.get(),owner_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(serverip_text.get(),owner_text.get(),username_text.get(),password_text.get())
    list1.delete(0,END)
    list1.insert(END,(serverip_text.get(),owner_text.get()))
    view_command()

def get_selected_row(event):
    #listeden birine tikladiginda indexini bulur.
    global  selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)

    #fill in the boxes with selected row's data
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[4])


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

window = Tk()
window.wm_title("ServerList")

l1 = Label(window,text = "Server IP")
l1.grid(row=0,column=0)

l2 = Label(window,text = "Owner")
l2.grid(row=1,column=0)

l3 = Label(window,text = "Username")
l3.grid(row=0,column=2)

l4 = Label(window,text = "Password")
l4.grid(row=1,column=2)

serverip_text = StringVar()
e1 = Entry(window, textvariable = serverip_text)
e1.grid(row=0,column=1)

owner_text = StringVar()
e2 = Entry(window, textvariable = owner_text)
e2.grid(row=1,column=1)

username_text = StringVar()
e3 = Entry(window,textvariable = username_text)
e3.grid(row=0,column=3)

password_text = StringVar()
e4 = Entry(window,textvariable = password_text)
e4.grid(row=1,column=3)


list1 = Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",get_selected_row)

b1 = Button(window,text="View all", width=15, command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search Entry", width=15, command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add Server", width=15, command=add_command)
b3.grid(row=4,column=3)

b5 = Button(window,text="Delete Selected", width=15, command = delete_command)
b5.grid(row=5,column=3)

b6 = Button(window,text="Close", width=15, command=window.destroy)
b6.grid(row=6,column=3)


def key(event):
    if len(event.char) == 1:
        msg = event.keysym
        if(msg == 'Return'):
            add_command()

window.bind_all('<Key>', key)

window.mainloop()
