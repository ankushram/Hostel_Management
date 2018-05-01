from Tkinter import *
from tkFont import Font
import os
os.chdir('C:\Python27\Programs\Python')
root=Tk()

count=0

l1=Label(root,text='Hostel Management System',fg='black',font='Times',padx=10,pady=10,bg='green')
l2=Label(root,text='Hostel Details..',fg='Black')

l3=Label(root,text='Hostel Type',fg='black')
l4=Label(root,text='Hostel Address',fg='black')
l5=Label(root,text='Caretaker name',fg='black')
l6=Label(root,text='Caretaker Phone No.',fg='black')
l7=Label(root,text='Rent',fg='black')
l8=Label(root,text='Enter Phone No.',fg='black')
l9=Label(root,text='Dont Know',fg='black')

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()

e1=Entry(root,textvariable=s1)
e2=Entry(root,textvariable=s2)
e3=Entry(root,textvariable=s3)
e4=Entry(root,textvariable=s4)
e5=Entry(root,textvariable=s5)
e6=Entry(root,textvariable=s6)

l1.grid(row=0,columns=2)
l2.grid(row=1,column=0,sticky=W)

l3.grid(row=2,sticky=W)
l4.grid(row=3,sticky=W)
l5.grid(row=4,sticky=W)
l6.grid(row=5,sticky=W)
l7.grid(row=6,sticky=W)


e1.grid(row=2,column=1)
e2.grid(row=3,column=1)
e3.grid(row=4,column=1)
e4.grid(row=5,column=1)
e5.grid(row=6,column=1)

b3=Button(root,text='First Record',fg='white',bg='black',relief=SUNKEN)
b3.grid(row=7,column=0,sticky=NSEW)
b4=Button(root,text="Last Record",fg='white',bg='black',relief=SUNKEN)
b4.grid(row=7,column=2,sticky=NSEW)
b6=Button(root,text="Previous Record",fg='white',bg='black',relief=SUNKEN)
b6.grid(row=8,column=0,sticky=NSEW)
b1=Button(root,text="Next Record",fg='white',bg='black',relief=SUNKEN)
b1.grid(row=8,column=2,sticky=NSEW)
b2=Button(root,text="Add Record",fg='white',bg='black',relief=SUNKEN)
b2.grid(row=9,column=0,sticky=NSEW)
b8=Button(root,text="Update Record",fg='white',bg='black',relief=SUNKEN)
b8.grid(row=9,column=2,sticky=NSEW)
b5=Button(root,text="Search Record",fg='white',bg='black',relief=SUNKEN)
b5.grid(row=10,column=0,sticky=NSEW)
b7=Button(root,text="Delete Record",fg='white',bg='black',relief=SUNKEN)
b7.grid(row=10,column=2,sticky=NSEW)
b9=Button(root,text="Exit",fg='white',bg='black',relief=SUNKEN,padx=10)
b9.grid(row=0,column=3,columnspan=2,sticky=NSEW)

def display(event):
    data=open('sketch.txt','r')
    data_list=[]
    j=0
    s=data.readlines()
    for i in s:
        l=s[j].split("\t")
        j+=1
        data_list.append(l)
    global count
    if count<=len(data_list)-1:
        s1.set(data_list[count][0])
        s2.set(data_list[count][1])
        s3.set(data_list[count][2])
        s4.set(data_list[count][3])
        s5.set(data_list[count][4])
        count+=1
        data.close()
    else:
        count=0

def record_added():
    l8=Label(root,text='Record Added')
    l8.grid(row=20,columns=3)
    
def updated():
    l8=Label(root,text='Record Updated')
    l8.grid(row=20,columns=3)

def error():
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    l8=Label(root,text='**Error**ALL FIELDS ARE NECESSARY')
    l8.grid(row=20,columns=3)
def data_error():
    l8=Label(root,text='INCORRECT DATE')
    l8.grid(row=20,columns=3)
def add(event):
    data=open('sketch.txt','a')
    name=s1.get()
    rm_tp=s2.get()
    ck_in=s3.get()
    ck_out=s4.get()
    num=s5.get()
    if name=="" or rm_tp=="" or ck_in=="" or ck_out=="" or num=="":
        error()
    else:
        for i in range(len(name),14):
            name=name+""
        for i in range(len(rm_tp),50):
            rm_tp=rm_tp+""
        for i in range(len(ck_in),14):
            ck_in=ck_in+""
        for i in range(len(ck_out),14):
            ck_out=ck_out+""
        for i in range(len(num),14):
            num=num+""
        data.writelines(name+"\t"+rm_tp+"\t"+ck_in+"\t"+ck_out+"\t"+num+"\n")
        s1.set("")
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
        record_added()
    data.close()

def display_first(event):
    import re
    data=open('sketch.txt','r')
    s=data.readline()
    string=re.sub(' +',' ',s)
    l=string.split("\t")
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
    data.close()
    
def display_last(event):
    import re
    data=open('sketch.txt','r')
    for i in data:
        s=i
    string=re.sub(' +',' ',s)
    l=string.split("\t")
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
    data.close()

def ok(event):
    import re
    flag=1
    data=open('sketch.txt','r')
    phn_no=s6.get()
    for i in data:
        s=i
        string=re.sub(' +',' ',s)
        l=string.split("\t")
        print l
        if phn_no==l[-2]:
            s1.set(l[0])
            s2.set(l[1])
            s3.set(l[2])
            s4.set(l[3])
            s5.set(l[4])
            flag=1
            break
        else:
            flag=0
            pass
    if flag==0:
        s1.set('**No record Found**')
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
    data.close()

def delete(event):
    data=open('sketch.txt','r')
    phn_no=s6.get()
    data_list=[]
    j=0
    s=data.readlines()
    for i in s:
        l=s[j].split("\t")
        j+=1
        data_list.append(l)
    print(data_list)
    data.close()
    data=open('sketch.txt','w')
    for i in range(0,len(data_list)):
        if phn_no!=data_list[i][-2]:
            name=data_list[i][0]
            rm_tp=data_list[i][1]
            ck_in=data_list[i][2]
            ck_out=data_list[i][3]
            num=data_list[i][4]
            amt=data_list[i][5]
            for i in range(len(name),14):
                name=name+""
            for i in range(len(rm_tp),50):
                rm_tp=rm_tp+""
            for i in range(len(ck_in),14):
                ck_in=ck_in+""
            for i in range(len(ck_out),14):
                ck_out=ck_out+""
            for i in range(len(num),14):
                num=num+""
            for i in range(len(amt),14):
                amt=amt+""
            data.writelines(name+"\t"+rm_tp+"\t"+ck_in+"\t"+ck_out+"\t"+num+"\n")
        else:
            pass
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    data.close()  

def update(event):
    data=open('sketch.txt','r')
    phn_no=s6.get()
    data_list=[]
    j=0
    s=data.readlines()
    for i in s:
        l=s[j].split("\t")
        j+=1
        data_list.append(l)
    print(data_list)
    data.close()
    
    data=open('sketch.txt','w')
    name=s1.get()
    rm_tp=s2.get()
    ck_in=s3.get()
    ck_out=s4.get()
    num=s5.get()
    if name=="" or rm_tp=="" or ck_in=="" or ck_out=="" or num=="":
        error()
    else:
        for i in range(len(name),14):
            name=name+""
        for i in range(len(rm_tp),50):
            rm_tp=rm_tp+""
        for i in range(len(ck_in),14):
            ck_in=ck_in+""
        for i in range(len(ck_out),14):
            ck_out=ck_out+""
        for i in range(len(num),14):
            num=num+""
        for i in range(0,len(data_list)):
            if phn_no==data_list[i][-2]:
                data.writelines(name+"\t"+rm_tp+"\t"+ck_in+"\t"+ck_out+"\t"+num+"\n")
            else:
                name1=data_list[i][0]
                rm_tp1=data_list[i][1]
                ck_in1=data_list[i][2]
                ck_out1=data_list[i][3]
                num1=data_list[i][4]
                for i in range(len(name1),14):
                    name1=name1+""
                for i in range(len(rm_tp1),50):
                    rm_tp1=rm_tp1+""
                for i in range(len(ck_in1),14):
                    ck_in1=ck_in1+""
                for i in range(len(ck_out1),14):
                    ck_out1=ck_out1+""
                for i in range(len(num1),14):
                    num1=num1+""
                data.writelines(name1+"\t"+rm_tp1+"\t"+ck_in1+"\t"+ck_out1+"\t"+num1+"\n")            
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    s6.set("")
    updated()
    data.close()

def search(event):
    l8.grid(row=18,column=0)
    e6.grid(row=18,column=1)
    b5.bind('<Button-1>',ok)
    b7.bind('<Button-1>',delete)
    b8.bind('<Button-1>',update)

def ex(event):
    os._exit(0)
            
b1.bind('<Button-1>',display)
b2.bind('<Button-1>',add)
b3.bind('<Button-1>',display_first)
b4.bind('<Button-1>',display_last)
b5.bind('<Button-1>',search)
b7.bind('<Button-1>',search)
b8.bind('<Button-1>',search)
b9.bind('<Button-1>',ex)
root.mainloop()


