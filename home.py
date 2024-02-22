
import os

import csv
from tkinter import *
from tkinter.filedialog import askopenfilename


import sample_data

##################################################################   read dataset
def read_first_data():
    a=0
    csv_file_path = askopenfilename()
    fpath= os.path.dirname(os.path.abspath(csv_file_path))
    fname=(os.path.basename(csv_file_path))
    fsize=os.path.getsize(csv_file_path)
    txt.delete(0,END)
    txt.insert(0,fpath)
    txt2.insert(0,fname)
    with open(csv_file_path, 'r') as csvFile:
        i=0
        reader = csv.reader(csvFile)
        for row in reader:
            i+=1
        s=sample_data
        s.total_record=i
        s.f_filepath=csv_file_path
        s.f_path=fpath
        print(csv_file_path)
        txt3.insert(0,i)
################################################################## Next page
def next_page():
    root.destroy()
    import read_data_set

##################################################################    main loop
root = Tk()
w=750
h=550
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Heart Disease Prediction")
################################################################## components design
message = Label(root, text="Heart Disease Prediction",fg="#003366", width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=20)
#######
lbl = Label(root,justify=CENTER, text="PATH", width=20, height=2, fg="black", font=('times', 15, ' bold '))
lbl.place(x=100, y=150)
lbl2 = Label(root,justify=RIGHT, text="DATA SET", width=20, fg="black",  height=2, font=('times', 15, ' bold '))
lbl2.place(x=100, y=225)
lbl3 = Label(root,justify=RIGHT, text="VALUES", width=20, fg="black",  height=2, font=('times', 15, ' bold '))
lbl3.place(x=100, y=300)
#######
txt = Entry(root, validate="key", width=20, font=('times', 25, ' bold '))
txt.place(x=300, y=150)

txt2 = Entry(root, width=20, font=('times', 25, ' bold '))
txt2.place(x=300, y=225)

txt3 = Entry(root, width=20, font=('times', 25, ' bold '))
txt3.place(x=300, y=300)
######## button with command function
compare_dataset = Button(root, text="Select Data",width=15,command=read_first_data  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=250, y=400)
resust_dataset = Button(root, text="Next",width=15  ,height=1,command=next_page,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)

root.mainloop()
