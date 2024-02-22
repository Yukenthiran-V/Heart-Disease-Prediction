from tkinter import *
import os

import csv
import sample_data
from tkinter import *
import tkinter.ttk as ttk
import csv
########################################################### function
def next_page():
    irrelevant_values_data_main.destroy()
    import attribut_extraction
def read_data_set():
    TableMargin = Frame(irrelevant_values_data_main, width=500)
    TableMargin.place(x=50, y=110, width=655, height=255)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Patient ID","age", "sex", "cp", "trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Patient ID', text="Patient ID", anchor=W)
    tree.heading('age', text="age", anchor=W)
    tree.heading('sex', text="sex", anchor=W)
    tree.heading('cp', text="cp", anchor=W)
    tree.heading('trestbps', text="trestbps", anchor=W)
    tree.heading('chol', text="chol", anchor=W)
    tree.heading('fbs', text="fbs", anchor=W)

    tree.heading('restecg', text="restecg", anchor=W)
    tree.heading('thalach', text="thalach", anchor=W)

    tree.heading('exang', text="exang", anchor=W)
    tree.heading('oldpeak', text="oldpeak", anchor=W)

    tree.heading('slope', text="slope", anchor=W)
    tree.heading('ca', text="ca", anchor=W)

    tree.heading('thal', text="thal", anchor=W)
    tree.heading('target', text="target", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.column('#6', stretch=NO, minwidth=0, width=200)
    tree.column('#7', stretch=NO, minwidth=0, width=200)
    tree.column('#8', stretch=NO, minwidth=0, width=200)
    tree.column('#9', stretch=NO, minwidth=0, width=0)
    tree.column('#10', stretch=NO, minwidth=0, width=200)
    tree.column('#11', stretch=NO, minwidth=0, width=200)
    tree.column('#12', stretch=NO, minwidth=0, width=200)
    tree.column('#13', stretch=NO, minwidth=0, width=200)
    tree.column('#14', stretch=NO, minwidth=0, width=200)


    tree.pack()
    ob=sample_data
    file="data_set/missing.csv"
    with open(file) as f, open('data_set/irrelevant.csv', 'w',newline='') as csvfile:

        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["Patient ID","age", "sex", "cp", "trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"])
        for row in reader:
            #print row
             t0 = row['Patient ID']
             t1 = row['age']
             t2 = row['sex']
             t3 = row['cp']
             t4 = row['trestbps']
             t5 = row['chol']
             t6 = row['fbs']
             t7 = row['restecg']
             t8 = row['thalach']

             t9 = row['exang']
             t10 = row['oldpeak']
             t11 = row['slope']
             t12 = row['ca']
             t13 = row['thal']
             t14 = row['target']
             #print t1
             if ((t1.replace('.', '', 1).isdigit()==False)or(t2.replace('.', '', 1).isdigit()==False)
                 or(t3.replace('.', '', 1).isdigit()==False)or(t4.replace('.', '', 1).isdigit()==False)
                 or(t5.replace('.', '', 1).isdigit()==False)or(t6.replace('.', '', 1).isdigit()==False)
                 or(t7.replace('.', '', 1).isdigit()==False)or(t8.replace('.', '', 1).isdigit()==False)
                 or(t9.replace('.', '', 1).isdigit()==False)or(t10.replace('.', '', 1).isdigit()==False)
                 or(t11.replace('.', '', 1).isdigit()==False)or(t12.replace('.', '', 1).isdigit()==False)
                 or(t13.replace('.', '', 1).isdigit()==False)or(t14.replace('.', '', 1).isdigit()==False)
):
                l=0#print "yes"
             else:
                 tree.insert("", 0, values=(t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14))
                 filewriter.writerow([t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14])

############################################################
irrelevant_values_data_main = Tk()
w=750
h=550
ws = irrelevant_values_data_main.winfo_screenwidth()
hs = irrelevant_values_data_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
irrelevant_values_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))
irrelevant_values_data_main.title("Heart Disease Prediction")

########################################################### Element design


message = Label(irrelevant_values_data_main, text="Heart Disease Prediction",fg="#003366", width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)

compare_dataset = Button(irrelevant_values_data_main, text="Irrelevant values",width=15,command=read_data_set  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=150, y=400)
resust_dataset = Button(irrelevant_values_data_main,command=next_page , text="Next",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)

irrelevant_values_data_main.mainloop()
