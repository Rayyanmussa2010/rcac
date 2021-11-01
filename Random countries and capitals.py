# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:49:52 2021

@author: DELL
"""

from tkinter import *
import random

root=Tk()
root.title("Picnic bag list")
root.geometry("600x600")
list1=[]

entry=Entry(root)
entry.place(relx=0.5, rely=0.1, anchor=CENTER)
label_list=Label(root)
label_list.place(relx=0.5, rely=0.2, anchor=CENTER)

entry2=Entry(root)
entry2.place(relx=0.5, rely=0.3, anchor=CENTER)
label2_list=Label(root)
label2_list.place(relx=0.5, rely=0.4, anchor=CENTER)

def add():
    list1.append(entry.get())
    label_list["text"]="The list of your items in the bag"+str(list1)
    
    list2.append(entry2.get())
    label2_list["text"]="The list of your items in the bag"+str(list2)

button2=Button(root, text="Add", command=add)
button2.place(relx=0.5, rely=0.5, anchor=CENTER)






label1=Label(root)
label2=Label(root)


def random_number():
    random_no=random.randint(0, 4)
    print(random_no)
    random_lucky_friend=list1[random_no]
    label1["text"]="The item which you should is: "+random_lucky_friend
    
button1=Button(root, text="Which item should I pick", command=random_number)
button1.place(relx=0.5, rely=0.6, anchor=CENTER)
label1.place(relx=0.5, rely=0.7, anchor=CENTER)
label2.place(relx=0.5, rely=0.8, anchor=CENTER)













root.mainloop()