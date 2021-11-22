from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import pymysql

class doctor:
    def __init__(self,root):
        self.root=root
        self.root.title("login systenm")
        self.root.geometry("900x590+100+50")
        self.root.resizable(False,False)

        frame_head=Frame(self.root,bg="dark blue")
        frame_head.place(x=0,y=0,height=40,width=900)

        heading=Label(frame_head,text="HOSPITAL MANAGEMT SYSTEM",font=("times new roman",15),fg="white",bg="dark blue" ).place(x=10,y=4,height=30)


        frame_butt=Frame(self.root,bg="light blue")
        frame_butt.place(x=0,y=40,width=100,height=550)

        men=Label(frame_butt,text="MENU",font=("times new roman",15),bg="white").place(x=0,y=0,width=100,height=40)
        
        butt_home=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.home).place(x=0,y=41,width=100,height=90)
        self.bg_home=PhotoImage(file="D:\programming\python\program\project\images\home2.png")
        self.bg_homeimage=Label(frame_butt,image=self.bg_home)
        self.bg_homeimage.place(x=28,y=50, width=45, height=45)
        self.home_head=Label(frame_butt,text="HOME",font=("times new roman",11)).place(x=25,y=105,height=10)


        butt_doctor=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2").place(x=0,y=131,width=100,height=90)
        self.bg_doctoricon=PhotoImage(file="D:\programming\python\program\project\images\doctoricon.png")
        self.bg_doctoriconimage=Label(frame_butt,image=self.bg_doctoricon)
        self.bg_doctoriconimage.place(x=28,y=136, width=45, height=45)
        self.doctor_head=Label(frame_butt,text="DOCTOR",font=("times new roman",11)).place(x=20,y=190,height=10)
        
        butt_patient=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.patient).place(x=0,y=221,width=100,height=90)
        self.bg_patienticon=PhotoImage(file="D:\programming\python\program\project\images\patienticon.png")
        self.bg_patienticonimage=Label(frame_butt,image=self.bg_patienticon)
        self.bg_patienticonimage.place(x=28,y=226, width=45, height=45)
        self.patient_head=Label(frame_butt,text="PATIENT",font=("times new roman",11)).place(x=20,y=278,height=10)

        butt_appointment=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.appointment).place(x=0,y=311,width=100,height=90)
        self.bg_appointmenticon=PhotoImage(file="D:\programming\python\program\project\images\calendericon.png")
        self.bg_appointmenticonimage=Label(frame_butt,image=self.bg_appointmenticon)
        self.bg_appointmenticonimage.place(x=28,y=316, width=45, height=45)
        self.appointment_head=Label(frame_butt,text="APPOINTMENT",font=("times new roman",10)).place(x=2,y=369,height=10)

        butt_admitinfo=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2").place(x=0,y=401,width=100,height=90)
        self.bg_admiticon=PhotoImage(file="D:\programming\python\program\project\images\dmiticon.png")
        self.bg_admiticonimage=Label(frame_butt,image=self.bg_admiticon)
        self.bg_admiticonimage.place(x=28,y=406, width=45, height=45)
        self.admit_head=Label(frame_butt,text="ADMIT INFO",font=("times new roman",11)).place(x=2,y=460,height=10)
        
        
        butt_exit=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.exit_home).place(x=0,y=491,width=100,height=59)
        self.bg_exiticon=PhotoImage(file="D:\programming\python\program\project\images\exiticon.png")
        self.bg_exiticonimage=Label(frame_butt,image=self.bg_exiticon)
        self.bg_exiticonimage.place(x=28,y=496, width=45, height=45)
        self.admit_head=Label(frame_butt,text="ERROR",font=("times new roman",11)).place(x=2,y=551,height=10)


        frame_admin=Frame(self.root,bg="light grey")
        frame_admin.place(x=100,y=40,width=800,height=40)
        admin_dash=Label(frame_admin,text="Doctor Dashboard",font=("times new roman",15,"bold"),bg="light grey").place(x=2,y=3,width=150,height=40)


        butt_managespecial=Button(frame_admin,text="Manage Specialization",cursor="hand2").place(x=160,y=5,height=30,width=150)
        butt_managedoctor=Button(frame_admin,text="Manage Doctor",cursor="hand2",command=self.managedoctor).place(x=320,y=5,height=30,width=150)


        frame_doctorspecial=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_doctorspecial.place(x=140,y=110,height=240,width=310)
        self.doctorspecial_head=Label(self.root,text="Doctor Specialization",font=("times new roman",14,"bold")).place(x=145,y=97)
        self.doctorspecial_entry=Label(frame_doctorspecial,text="Enter Doctor Specialization",font=("times new roman",12)).place(x=4,y=26)
        self.doctorspecial_entryblock=Entry(frame_doctorspecial,bg="lightgrey",font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.doctorspecial_entryblock.place(x=8,y=65,height=35,width=280)

        butt_add=Button(frame_doctorspecial,text="Add",cursor="hand2",bg="sky blue",fg="white",command=self.addspecialization).place(x=8,y=130,height=30,width=140)
        butt_update=Button(frame_doctorspecial,text="Update",cursor="hand2",bg="green",fg="white").place(x=160,y=130,height=30,width=140)
        butt_clear=Button(frame_doctorspecial,text="Clear",cursor="hand2",bg="dark orange",fg="white",command=self.clear).place(x=8,y=175,height=30,width=140)
        butt_delete=Button(frame_doctorspecial,text="Delete",cursor="hand2",bg="purple",fg="white",command=self.delete1).place(x=160,y=175,height=30,width=140)

        frame_allspecial=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_allspecial.place(x=470,y=110,height=460,width=423)
        self.allspceial_head=Label(self.root,text="All Specialization",font=("times new roman",14,"bold")).place(x=475,y=97)
        self.allspecial_search=Label(frame_allspecial,text="Search",font=("times new roman",14)).place(x=15,y=25)
        self.search_entry=Entry(frame_allspecial,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.search_entry.place(x=85,y=25,height=30,width=150)
        butt_search=Button(frame_allspecial,text="Search",cursor="hand2",bg="dark blue",fg="white", command=self.search1).place(x=250,y=25,height=30,width=80)
        butt_showall=Button(frame_allspecial,text="Show All",cursor="hand2",bg="dark orange",fg="white",command=self.showall).place(x=340,y=25,height=30,width=70)
       
       
        frame_allspecialdesc=Frame(frame_allspecial,borderwidth=1,relief=SOLID)
        frame_allspecialdesc.place(x=2,y=70,height=387,width=418)

        scroll_x=ttk.Scrollbar(frame_allspecialdesc,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame_allspecialdesc,orient=VERTICAL)
        

        self.doctor_table=ttk.Treeview(frame_allspecialdesc,column=("id","specialization","creation_date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.doctor_table.xview)
        scroll_y=ttk.Scrollbar(command=self.doctor_table.yview)


        self.doctor_table.heading("id",text="ID")
        self.doctor_table.heading("specialization",text="specialization")
        self.doctor_table.heading("creation_date",text="creation date")

        self.doctor_table["show"]="headings"

        self.doctor_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        


        self.doctor_table.column("id",width=40)
        self.doctor_table.column("specialization",width=70)
        self.doctor_table.column("creation_date",width=70)


    def addspecialization(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        if self.doctorspecial_entryblock.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required", parent=self.root)

        else:
            cur.execute("insert into specialization values(%s,NOW())",(self.doctorspecial_entryblock.get()))
            
            conn.commit()
            self.clear()
            self.fetch_data()
            conn.close()

    

    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select ROW_NUMBER() over(order by specialization) as ID,specialization,creation_date from specialization;")
        rows=cur.fetchall()
        if len(rows)!=0 or len(rows)==0:
            self.doctor_table.delete(*self.doctor_table.get_children())
            for i in rows:
                self.doctor_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    def delete1(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("delete from specialization where specialization=%s",(self.doctorspecial_entryblock.get()))
        
        
        conn.commit()
        self.clear()
        self.fetch_data()
        conn.close()


    def search1(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select ROW_NUMBER() over(order by specialization) as ID,specialization,creation_date from specialization where specialization=%s",(self.search_entry.get()))
        rows=cur.fetchall()
        if len(rows)!=0 or len(rows)==0:
            self.doctor_table.delete(*self.doctor_table.get_children())
            for i in rows:
                self.doctor_table.insert("",END,values=i)

            conn.commit()
            self.clear()
        conn.close()

    def showall(self):
        self.fetch_data()


    def clear(self):
        self.doctorspecial_entryblock.delete(0,END)
        self.search_entry.delete(0,END)


    

    
   
        
    
    def exit_home(self):
        self.root.destroy()

    def home(self):
        self.root.destroy()
        import home

    def patient(self):
        self.root.destroy()
        import patient

    def appointment(self):
        self.root.destroy()
        import appointment

    def managedoctor(self):
        self.root.destroy()
        import manage_doctor



root=Tk()
obj=doctor(root)
root.mainloop()



#If the entry field contains some calculation, then entry field declaration and place value must be separate.