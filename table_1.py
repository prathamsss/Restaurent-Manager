from tkinter import *
from tkinter import Label
import time
import pandas as pd
import ttk
from PIL import ImageTk, Image
import os
import csv
from datetime import date

window = Tk()
window.title(" table 1")
window.geometry('850x1000')



class Christina(Frame): 
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.btn = Button(self, text="Start",bd=23,borderwidth= 23,height=2,font=("Arial bold", 20),relief='solid', width=10,command=self.clicked)
        self.btn.place(x=0, y=0)
        self.btn.pack()
        self.lbl = Label(self,bd=1,relief='solid',text="  OFF ",font=("Arial", 40), bg="green3")
        self.lbl.place(x=0, y=0)
        self.lbl.pack()
        
    global nm,pm,nx,ny,total,start_time,end_time,time_lapsed,bucket_nm,total_cart
    def numb(self,n,x,y):        
        self.nm=n
        self.nx=x
        self.ny=y
        
    def clicked(self):
        if self.btn['text'] == "Start":
            self.entry()
            self.start()
            self.btn.configure(text="Stop")
            self.lbl.configure(text="  ON  ", bg="red")
            
            f_l=Label(window,text="Total = 0    ",bd=3,relief='solid',font=("Arial", 40),bg='gold')
            f_l.place(x=570,y=0)
            
            tree = ttk.Treeview(window)
            tree["columns"]=("one")
            tree.column("#0", width=150, minwidth=150, stretch=NO)
            tree.column("one", width=50, minwidth=50, stretch=NO)
            tree.heading("#0",text="Items",anchor=W)
            tree.heading("one",text="Prize",anchor=W)
            for i in range(50):
                folder1=tree.insert("", i, "", text="     ", values="  ")
                
            tree.place(x=350,y=0)   
    
            # print("Table NO =",self.nm)
            self.menu(0)
           
        else:
            self.btn.configure(text="Start")
            self.stop()
            self.menu(1)
            self.lbl.configure(text="  OFF ", bg="green3")
    global gmm    
    def start(self):
        global start_time
        self.start_time = time.time() 


    def stop(self):
        global end_time , tot
        self.end_time = time.time()
        self.time_convert()
       

        #pm = self.to()
    def time_convert(self):
        self.sec = self.end_time - self.start_time
        global mins
        self.mins =self.sec // 60 
        global s
        self.s =  self.sec % 60
        global hours
        self.hours =   self.mins // 60
        self.mins =  self.mins % 60
        t=("Time = {0}:{1}:{2}".format(int(self.hours),int(self.mins),round(self.s)))
        print(t)
        t_pass=str(self.hours)+str(self.mins)
        self.xh=float(self.hours)*100
        self.ymin=float(self.mins)*(100/60)
        global total
        self.total=self.xh+self.ymin
        print("\t\n")
        if 0<=self.mins<=59 and self.hours==0:
            self.total=100
        elif self.mins==0 and self.hours==0:
            self.total=00
        t1='Time Total ='+str(self.total)    
      
        
        l_t=Label(window,text=int(self.total),bd=3,relief='solid',font=("Arial", 20),bg='orange')
        l_t.place(x=self.nx+40,y=self.ny)
        
        lt_d=Label(window,text=t,bg='orange',font=("Helvetica", 15),width=9)
        lt_d.place(x=self.nx-55,y=self.ny)
        
        lt_d1=Label(window,text='Time Total ->',bg='pink',font=("Helvetica", 13),width=10)
        lt_d1.place(x=self.nx-55,y=self.ny+30)
        
        return self.total
 
    def menu(self,c):
        self.data_m = pd.read_csv("/Users/prathamesh/Desktop/cafe/menu.csv") 
        self.colnames = ['Items', 'Prize']
        self.data_m = pd.read_csv('/Users/prathamesh/Desktop/cafe/menu.csv', names=self.colnames)
        self.prize_col = self.data_m.Prize.tolist()
        self.prize_col.pop(0)
        self.but_nm = self.data_m.Items.tolist()
        self.but_nm.pop(0) 
        #************             MENU 1 ***************
        self.data_m_1 = pd.read_csv("/Users/prathamesh/Desktop/cafe/menu_1.csv") 
        self.colnames = ['Items', 'Prize']
        self.data_m_1 = pd.read_csv('/Users/prathamesh/Desktop/cafe/menu_1.csv', names=self.colnames)
        self.prize_col_1 = self.data_m_1.Prize.tolist()
        self.prize_col_1.pop(0)
        self.but_nm_1 = self.data_m_1.Items.tolist()
        self.but_nm_1.pop(0) 
                #************             MENU 2 ***************
        self.data_m_2 = pd.read_csv("/Users/prathamesh/Desktop/cafe/menu_2.csv") 
        self.colnames = ['Items', 'Prize']
        self.data_m_2 = pd.read_csv('/Users/prathamesh/Desktop/cafe/menu_2.csv', names=self.colnames)
        self.prize_col_2 = self.data_m_2.Prize.tolist()
        self.prize_col_2.pop(0)
        self.but_nm_2 = self.data_m_2.Items.tolist()
        self.but_nm_2.pop(0) 

                #************             MENU 3 ***************
        self.data_m_3 = pd.read_csv("/Users/prathamesh/Desktop/cafe/menu_3.csv") 
        self.colnames = ['Items', 'Prize']
        self.data_m_3 = pd.read_csv('/Users/prathamesh/Desktop/cafe/menu_3.csv', names=self.colnames)
        self.prize_col_3 = self.data_m_3.Prize.tolist()
        self.prize_col_3.pop(0)
        self.but_nm_3 = self.data_m_3.Items.tolist()
        self.but_nm_3.pop(0) 
        
                #************             MENU 4 ***************
        self.data_m_4 = pd.read_csv("/Users/prathamesh/Desktop/cafe/menu_4.csv") 
        self.colnames = ['Items', 'Prize']
        self.data_m_4 = pd.read_csv('/Users/prathamesh/Desktop/cafe/menu_4.csv', names=self.colnames)
        self.prize_col_4 = self.data_m_4.Prize.tolist()
        self.prize_col_4.pop(0)
        self.but_nm_4 = self.data_m_4.Items.tolist()
        self.but_nm_4.pop(0) 
        
        
        
        
        #print(self.but_nm)
        for i in range(0,int(len(self.but_nm))):   
            self.b_1=Button(text=self.but_nm[i],command= lambda i= i:cal_m(self.prize_col[i],self.but_nm[i]))
            self.b_1.place(x=0,y=210+25*i)


        for i in range(0,int(len(self.but_nm_1))):   
            self.b_1_1=Button(text=self.but_nm_1[i],command= lambda i= i:cal_m(self.prize_col_1[i],self.but_nm_1[i]))
            self.b_1_1.place(x=100,y=210+25*i)


        for i in range(0,int(len(self.but_nm_2))):   
            self.b_1_2=Button(text=self.but_nm_2[i],command= lambda i= i:cal_m(self.prize_col_2[i],self.but_nm_2[i]))
            self.b_1_2.place(x=220,y=210+25*i)

        for i in range(0,int(len(self.but_nm_3))):   
            self.b_1_3=Button(text=self.but_nm_3[i],command= lambda i= i:cal_m(self.prize_col_3[i],self.but_nm_3[i]))
            self.b_1_3.place(x=370,y=210+25*i)

        for i in range(0,int(len(self.but_nm_4))):   
            self.b_1_4=Button(text=self.but_nm_4[i],command= lambda i= i:cal_m(self.prize_col_4[i],self.but_nm_4[i]))
            self.b_1_4.place(x=560,y=210+25*i)


            if c==1:
                lc=Label(window,text='  ',bg='white',height=50,width=200)
                lc.place(x=0,y=200)
            bucket_p=[]
            global bucket_nm
            bucket_nm=[]
            global total_cart
            def cal_m(x_m,item_nm):
                  x_m=int(x_m)
                  bucket_p.append(x_m)
                  global bucket_nm
                  bucket_nm.append(item_nm)
                  print(bucket_nm)
                  total_cart=(sum(bucket_p))
                  print(total_cart)      
                  dict = {'Name':bucket_nm,'Total': bucket_p} 
                  df = pd.DataFrame(dict) 
                  df.to_csv('table_1.csv') 
                  return bucket_nm 

        total_but=Button(window,text='MENU TOTAL',width=15,font=("times bold", 20),command=lambda :self.to(bucket_nm,bucket_p,1))
        total_but.place(x=0,y=112) 
        lbtm=Label(window,text='* Press MENU TOTAL before pressing STOP',bg='black',fg='red')
        lbtm.place(x=0,y=145)
        
        reset_button=Button(window,text='RESET Menu',relief=RAISED,width=15,font=("arial", 15),fg='firebrick1',command= lambda:self.to(bucket_nm,bucket_p,0)) 
        reset_button.place(x=0,y=180)   
        
        
    
    
    def to(self,lis,prize,x_m):
        tree = ttk.Treeview(window)
        tree["columns"]=("one")
        tree.column("#0", width=150, minwidth=150, stretch=NO)
        tree.column("one", width=50, minwidth=50, stretch=NO)
        tree.heading("#0",text="Items",anchor=W)
        tree.heading("one",text="Prize",anchor=W)
        for i in range(int(len(lis))):
            text_m=str(i)+str(')  ')+str(lis[i])
            folder1=tree.insert("", i, "", text=text_m, values=(prize[i]))
        tree.insert("" ,int(len(lis)), "",text="Total",value=sum(prize))
        tree.place(x=350,y=0)   
        global pm
        pm=sum(prize)
        global pmm
        pmm=int(pm)
        print("Menu total = ",pm)
        self.bt=Button(window,text="FINAL TOTAL",bd=23,borderwidth= 23,height=2,font=("Arial bold", 20),relief='solid', width='13',command=lambda :self.tf(pmm))
        self.bt.place(x=680,y=86)
        self.lbt=Label(window,text='* Press STOP before pressing FINAL TOTAL',bg='black',fg='red')
        self.lbt.place(x=560,y=57)


        if x_m==0:
            lis.clear()
            prize.clear()
            tree.pack_forget()
        print("pmm=",pmm)    
        return pmm
        
    
    
    def tf(self,pm):
        total=self.time_convert()
        f_t=int(total)+int(pm)
        if f_t<=0:
            f_t=0
        ft='Total = '+str(f_t)+"    "   
        f_l=Label(window,text=ft,bd=3,relief='solid',font=("Arial", 40),bg='gold')
        f_l.place(x=570,y=0)
        today = date.today()

        nm,cont=self.details()
        with open(r'/Users/prathamesh/Desktop/cafe/history.csv', 'a', newline='') as csvfile:
             fieldnames = ['Name','Contact','Total','Date']
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
             writer.writerow({'Name':nm,'Contact':cont,'Total':total,'Date':today})
       
        
        
    def entry(self):
        global nm,contact,name,cont
        name =StringVar(window)
        contact =StringVar(window)
        b_s=Button(window,text="Submit",relief='solid',width=7,font=("times bold", 20),command=lambda :self.details())
        b_s.place(x=565,y=110)
        nm=Entry(window,textvariable = name,bd=5)
        nm.place(x=565,y=135)
        cont=Entry(window,textvariable = contact,bd=5)
        cont.place(x=565,y=170)
        return nm,cont
        
    def details(self):
        nm=(name.get())
        cont=(contact.get())
            # with open(r'history.csv', 'a', newline='') as csvfile:
            #     fieldnames = ['Name','Contact','Time']
            #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
            #     writer.writerow({'Name':nm, 'Contact':cont})
        return nm,cont
        
    lb1= Label(window,text='1',bd=5,relief='solid',font=("Arial", 70) ,bg='yellow')
    lb1.place(x=1,y=0)
    
        

        
    
    
    
    
        
table_1 = Christina(window)
table_1.numb(1,250,0)
table_1.place(x=70,y=0)
window.resizable(True, True) 




window.mainloop()

