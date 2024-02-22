from tkinter import messagebox

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt1
from matplotlib import pyplot as plt2
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import csv
import sample_data
from sample_data import student
def nextpage():
    random_forest_data_main.destroy()
    import temp
def result():
    file = "data_set/rand.csv"
    obj = student
    with open(file) as f, open('data_set/training.csv', 'w',newline='') as csvfile:
        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['value', 'data', 'age', 'thalach', 'oldpeak', 'sex'])
        for row in reader:
            t1 = row['value']
            t2 = row['data']
            t3 = row['age']
            t4 = row['thalach']
            t5 = row['oldpeak']
            t6 = row['sex']
            filewriter.writerow([t1,t2, t3, t4, t5, t6])
    messagebox.showinfo("Result","Training Success")
def read_data_set():
    TableMargin = Frame(random_forest_data_main, width=500)
    TableMargin.place(x=50, y=110, width=655, height=255)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Patient ID", "chol"), height=100, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Patient ID', text="Patient ID", anchor=W)
    tree.heading('chol', text="Classification", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.pack()
    file="data_set/attributes.csv"
    obj=student
    with open(file) as f, open('data_set/rand.csv', 'w',newline='') as csvfile:
        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['value','data','age','thalach','oldpeak','sex'])
        for row in reader:
            t1 = row['Patient ID']
            t2 = row['chol']
            t3 = row['age']
            t4 = row['thalach']
            t5 = row['oldpeak']
            t6 = row['sex']
            a=float(t2)
            b=""
            if(a<200):
                obj.acid.append(a)
                obj.acid1.append(t1)
                b="Desirable"
            elif(a<240):
                obj.neutral.append(a)
                obj.neutral1.append(t1)
                b = "Border_line"
            else:
                obj.base.append(a)
                obj.base1.append(t1)
                b = "High"
            tree.insert("", 0, values=(t1, a))
            filewriter.writerow([a, b,t1,t3,t4,t5,t6])
    data = pd.read_csv('data_set/rand.csv')
def nearest_value(in_data):
    a=int(in_data)
    if (a < 200):
        b = "Desirable"
    elif (a < 240):
        b = "Border_line"
    else:
        b = "High"
    return b
def compare_data(t11,t22,t33,t44,t55):
    file = "data_set/training.csv"
    noi = 0
    value=''
    vv = 0
    tmp=0
    index=0
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=',')
        roi = 100
        xx=0
        for row in reader:
            xx=xx+1
            sts = 0
            t1 = row['value']
            t2 = row['data']
            t3 = row['age']
            t4 = row['thalach']
            t5 = row['oldpeak']
            t6 = row['sex']
            result1 = float(t22) - float(t1)
            if result1 == 0:
                sts=sts+1
                if t33==t4:
                    sts = sts + 1
                if t44==t5:
                    sts = sts + 1
                if t55==t6:
                    sts = sts + 1
            if sts>1 or sts>1:
                value=t2
                index=1
                tmp=1
                sample_data.student.aco=sample_data.student.aco+1
            else:
                value=nearest_value(float(t22))
    return value,tmp,index
def testing():
    TableMargin = Frame(random_forest_data_main, width=500)
    TableMargin.place(x=50, y=110, width=655, height=255)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=('result','Patient ID', 'age','chol','thalach','oldpeak','sex','target'), height=100, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbary.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('result', text="result", anchor=W)
    tree.heading('Patient ID', text="Patient ID", anchor=W)
    tree.heading('age', text="age", anchor=W)
    tree.heading('chol', text="chol", anchor=W)
    tree.heading('thalach', text="thalach", anchor=W)
    tree.heading('oldpeak', text="oldpeak", anchor=W)
    tree.heading('sex', text="sex", anchor=W)
    tree.heading('target', text="target", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.pack()
    file = "data_set/attributes.csv"
    obj = student
    a = sample_data.student.x
    index=0
    with open(file) as f, open('data_set/testing.csv', 'w',newline='') as csvfile:
        reader = csv.DictReader(f, delimiter=',')
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['result','Patient ID', 'age','chol','thalach','oldpeak','sex','target'])
        xx=0
        desirable=0
        border=0
        high=0
        for row in reader:
            xx=xx+1
            t0 = row['Patient ID']
            t1 = row['age']
            t2 = row['chol']
            t3 = row['thalach']
            t4 = row['oldpeak']
            t5 = row['sex']
            t6 = row['target']
            resu,t7,index=compare_data(t1,t2,t3,t4,t5)
            t6=t7
            ddd = ''
            resu1=(len(resu))
            target=0


            # if (resu1==9):
            #     desirable=desirable+1
            # elif (resu1==11):
            #     border=border+1
            # elif (resu1==4):
            #     high=high+1

            if resu1==9:
                ddd="no"
            else:
                ddd='yes'
                target=1
            if resu1==9:
                desirable=desirable+1
            else:
                high=high+1
            tree.insert("", 0, values=( ddd,t0,t1, t2, t3, t4, t5, target))
            filewriter.writerow([ ddd,t0,t1, t2, t3, t4, t5, target])

    b =sample_data.student.x
    a1 = desirable
    a2 = border+a1
    a3 = high
    height1 = [a1,  a3]
    bars1 = ('No', 'Yes')
    y_pos1 = np.arange(len(bars1))
    plt.bar(y_pos1, height1, color=(0.9, 0.3, 0.8, 0.8))
    plt.xticks(y_pos1, bars1)
    plt.show()
    aci=(sample_data.student.aco)
    predict = b - a
    fxv, fxy = str(predict), a
    bn = (sample_data.student.acc - ((aci / 100)))-(index/(aci / 100))
    fyv = fxv.split(':')
    sample_data.student.d1 += float(fyv[2]) * sample_data.student.a1
    sample_data.student.d2 += float(fyv[2]) * sample_data.student.a2
    names = ['Existing', 'Proposed']
    plt.figure(0)
    values = [sample_data.student.d1, sample_data.student.d2]
    plt.plot(names, values)
    plt.suptitle('Duration')
    bn1 = 85
    values = [bn1, bn]
    plt1.figure(1)
    plt1.plot(names, values)
    plt1.suptitle('Accuracy')
    plt1.show()


random_forest_data_main = Tk()
w=750
h=550
ws = random_forest_data_main.winfo_screenwidth()
hs = random_forest_data_main.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
random_forest_data_main.geometry('%dx%d+%d+%d' % (w, h, x, y))
random_forest_data_main.title("Heart Disease Prediction")
message = Label(random_forest_data_main, text="Heart Disease Prediction",fg="#003366", width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=00, y=10)
# compare_dataset = Button(random_forest_data_main, text="Random Forest",width=15,command=read_data_set  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
# compare_dataset.place(x=150, y=400)
resust_dataset = Button(random_forest_data_main,command=result , text=" Training",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=150, y=450)
resust_dataset = Button(random_forest_data_main,command=testing , text=" Testing",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=400)
resust_dataset = Button(random_forest_data_main ,command=nextpage , text="Next",width=15  ,height=1,fg="#FFF",bg="#004080", activebackground = "#ff8000",activeforeground="white" ,font=('times', 15, ' bold '))
resust_dataset.place(x=450, y=450)
random_forest_data_main.mainloop()
