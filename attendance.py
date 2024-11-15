import numpy as np
import pandas as pd
from tkinter import messagebox
from tkinter import*
from pytube import YouTube 
import os 
from tkinter import ttk
import tkinter as tk

class Youtube_vid_aud:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance")
        self.root.geometry("1100x2130+0+0")
        self.root.resizable(False,False)
        self.root.configure(bg='cyan')
        self.root.overrideredirect(True)
        self.data = {'Rollno': ['105001','105002','105003'],'Name': ['Aditya','Brijesh','Ravi']}
        
        self.txt_var1=StringVar()
        self.txt_var2=StringVar()
        self.txt_var3=StringVar()
        self.txt_var4=StringVar()
        
        self.count=0
        
        
        self.lbl=Label(self.root,text='Attendance',bg="cyan",fg='blue',font=("Arial",18,'bold','underline'))
        self.lbl.place(x=300,y=100)
        self.lbl=Label(self.root,text=' Date :- ',bg="cyan",font=("Georgia",7,'bold'))
        self.lbl.place(x=50,y=350)
        self.lbl=Label(self.root,text=' Name :- ',bg="cyan",font=("Georgia",7,'bold'))
        self.lbl.place(x=50,y=500)
        self.lbl=Label(self.root,text=' Roll no. :- ',bg="cyan",font=("Georgia",7,'bold'))
        self.lbl.place(x=50,y=650)
        self.lbl=Label(self.root,text=' Attendance :- ',bg="cyan",font=("Georgia",7,'bold'))
        self.lbl.place(x=600,y=650)
        
        self.entry1=Entry(self.root,bg='yellow',bd=5,textvariable=self.txt_var1)
        self.entry1.place(x=240,y=500,width=800)
        self.entry2=Entry(self.root,bg='yellow',bd=5,textvariable=self.txt_var2)
        self.entry2.place(x=240,y=650,width=300)
        self.entry3=Entry(self.root,bg='yellow',bd=5,textvariable=self.txt_var3)
        self.entry3.place(x=870,y=650,width=150)
        self.entry4=Entry(self.root,bg='yellow',bd=5,textvariable=self.txt_var4)
        self.entry4.place(x=240,y=350,width=300)
        
        self.btn1=Button(self.root,text='Del',bg='lime',bd=5,font=('Georgia',5,'bold'),command=self.delete)
        self.btn1.place(x=100,y=850)
        
        self.btn1=Button(self.root,text='Add',bg='lime',bd=5,font=('Georgia',5,'bold'),command=self.add)
        self.btn1.place(x=300,y=850)
        
        self.btn1=Button(self.root,text='P',bg='lime',bd=5,font=('Georgia',5,'bold'),command=self.present)
        self.btn1.place(x=520,y=850)
        
        self.btn1=Button(self.root,text='A',bg='lime',bd=5,font=('Georgia',5,'bold'),command=self.absent)
        self.btn1.place(x=700,y=850)
        
        self.btn1=Button(self.root,text='Back',bg='lime',bd=5,font=('Georgia',5,'bold'),command=self.back)
        self.btn1.place(x=880,y=850)
        
        self.btn1=Button(self.root,text='Start',bg='lime',bd=5,font=('Georgia',5,'bold'),command=self.start)
        self.btn1.place(x=700,y=350)
        
        self.btn1=Button(self.root,text='Search',bg='lime',bd=5,font=('Georgia',5,'bold'),command=self.search)
        self.btn1.place(x=450,y=1000)
        
    def start(self):
        self.df =pd.read_excel('output.xlsx')
        a=self.txt_var4.get()
        self.df.insert(len(self.df.columns),a,'')
        #self.df = pd.DataFrame(self.data)
        self.df.to_excel('output.xlsx',sheet_name='ravi',index=False)
        
        self.txt_var1.set(self.df.loc[0,self.df.columns[1]])
        self.txt_var3.set(self.df.loc[0,self.df.columns[-1]])
        #self.txt_var4.set(self.df.columns[-1])
        self.txt_var2.set(self.df.loc[0,self.df.columns[0]])
    def delete(self):
    	pass
    	
    def add(self):
    	df =pd.read_excel('output.xlsx')
    	row=len(df.index)
    	
    	if row != self.count:
    		roll=self.txt_var2.get()
    		rollno=int(roll)+1
    		self.txt_var2.set(rollno)
    		self.txt_var1.set(df.loc[self.count,df.columns[1]])
    		self.txt_var3.set('')
    		df.to_excel('output.xlsx',sheet_name='ravi',index=False)
    	else:
    		print("done")
    	
    	
    	pass
    	
    def present(self):
    	self.txt_var3.set('')
    	df =pd.read_excel('output.xlsx')
    	df.loc[self.count,df.columns[-1]]='P'
    	df.to_excel('output.xlsx',sheet_name='ravi',index=False)
    	self.txt_var3.set(df.loc[self.count,df.columns[-1]])
    	self.count+=1
    	
    	pass
    	
    def absent(self):
    	df =pd.read_excel('output.xlsx')
    	df.loc[self.count,df.columns[-1]]='A'
    	df.to_excel('output.xlsx',sheet_name='ravi',index=False)
    	self.txt_var3.set(df.loc[self.count,df.columns[-1]])
    	self.count+=1
    	pass
    	
    def back(self):
    	df =pd.read_excel('output.xlsx')
    	self.count-=1
    	self.txt_var3.set(df.loc[self.count,df.columns[-1]])
    	pass
    	
    def search(self):
    	df =pd.read_excel('output.xlsx')
    	date=self.txt_var4.get()
    	name=self.txt_var1.get()
    	attendance=self.txt_var3.get()
    	roll=self.txt_var2.get()
    	rollno=int(roll)-105001
    	self.txt_var1.set(df.loc[rollno,df.columns[1]])
    	self.txt_var3.set(df.loc[rollno,df.columns[-1]])
    	self.txt_var4.set(df.columns[-1])
    	pass
    	
root=tk.Tk()
obj=Youtube_vid_aud(root)
root.mainloop()








#data3=data3.split(',')

#print(data3)
#df =pd.read_excel('output.xlsx')
#df.loc[1,'Rollno']=677867

#index=len(df.columns)
#newrow=[]
#for i in range(5):
#	row=input()
#	newrow.append(row)

#df.loc[len(df.rows)]=newrow

#df.insert(index,col,data3)

#data = {'Rollno': ['105001','105002','105003'],'Name': ['Aditya','Brijesh','Ravi']}
#df = pd.DataFrame(data)



#print(df)
#df.to_excel('output.xlsx',sheet_name='ravi',index=False)

