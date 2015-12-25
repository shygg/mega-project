#!/usr/bin/python

import tkinter


#command from the open button calls this fine func
def open_file():
    print(text_field.get())
    print("hello")
    f = open(text_field.get(), "r+")
    data = f.read()
    print(data)
    f.close()
    text_area.delete("1.0", tkinter.END)
    text_area.insert("1.0", data)


#command from the save button calls this fine func
def save_file():
    print(text_field.get())
    f = open(text_field.get(), "w")
    data = text_area.get("1.0", tkinter.END)
#it had to be done, else I would be getting a newline after each save
    f.write(data[0:-1])
    f.close()
    open_file()

window = tkinter.Tk()
# Code to add widgets will go here...
window.title("dengra's' text editor")
window.geometry("400x400")
window.wm_iconbitmap("favicon.ico")

###open, edit, and save button

#file name field
text_field = tkinter.Entry(window)

#file name label
file_name_field = tkinter.Label(window, text="filename")


#text-area
text_area = tkinter.Text(window, height="100", width="100")

#open button
open_button = tkinter.Button(window, text="Open...", command=open_file)
#save
save_button = tkinter.Button(window, text="Save...", command=save_file)

#adding it to my window var
file_name_field.pack()
text_field.pack()
open_button.pack()
save_button.pack()
text_area.pack()

#window loop
window.mainloop()
