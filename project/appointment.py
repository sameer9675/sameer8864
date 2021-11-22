from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import pymysql

class appoint:
    def __init__(self,root):
        self.root=root
        self.root.title("login systenm")
        self.root.geometry("950x590+100+50")
        self.root.resizable(False,False)

        frame_head=Frame(self.root,bg="dark blue")
        frame_head.place(x=0,y=0,height=40,width=950)

        heading=Label(frame_head,text="HOSPITAL MANAGEMT SYSTEM",font=("times new roman",15),fg="white",bg="dark blue" ).place(x=10,y=4,height=30)


        frame_butt=Frame(self.root,bg="light blue")
        frame_butt.place(x=0,y=40,width=100,height=550)

        men=Label(frame_butt,text="MENU",font=("times new roman",15),bg="white").place(x=0,y=0,width=100,height=40)
        
        butt_home=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.home).place(x=0,y=41,width=100,height=90)
        self.bg_home=PhotoImage(file="D:\programming\python\program\project\images\home2.png")
        self.bg_homeimage=Label(frame_butt,image=self.bg_home)
        self.bg_homeimage.place(x=28,y=50, width=45, height=45)
        self.home_head=Label(frame_butt,text="HOME",font=("times new roman",11)).place(x=25,y=105,height=10)


        butt_doctor=Button(frame_butt,font=("times new roman",13),command=self.doctor,bg="white",cursor="hand2").place(x=0,y=131,width=100,height=90)
        self.bg_doctoricon=PhotoImage(file="D:\programming\python\program\project\images\doctoricon.png")
        self.bg_doctoriconimage=Label(frame_butt,image=self.bg_doctoricon)
        self.bg_doctoriconimage.place(x=28,y=136, width=45, height=45)
        self.doctor_head=Label(frame_butt,text="DOCTOR",font=("times new roman",11)).place(x=20,y=190,height=10)
        
        butt_patient=Button(frame_butt,font=("times new roman",13),command=self.patient,bg="white",cursor="hand2").place(x=0,y=221,width=100,height=90)
        self.bg_patienticon=PhotoImage(file="D:\programming\python\program\project\images\patienticon.png")
        self.bg_patienticonimage=Label(frame_butt,image=self.bg_patienticon)
        self.bg_patienticonimage.place(x=28,y=226, width=45, height=45)
        self.patient_head=Label(frame_butt,text="PATIENT",font=("times new roman",11)).place(x=20,y=278,height=10)

        butt_appointment=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2").place(x=0,y=311,width=100,height=90)
        self.bg_appointmenticon=PhotoImage(file="D:\programming\python\program\project\images\calendericon.png")
        self.bg_appointmenticonimage=Label(frame_butt,image=self.bg_appointmenticon)
        self.bg_appointmenticonimage.place(x=28,y=316, width=45, height=45)
        self.appointment_head=Label(frame_butt,text="APPOINTMENT",font=("times new roman",10)).place(x=2,y=369,height=10)

        butt_admitinfo=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.admit).place(x=0,y=401,width=100,height=90)
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
        frame_admin.place(x=100,y=40,width=850,height=40)
        admin_dash=Label(frame_admin,text="Patient | Appointment History",font=("times new roman",15,"bold"),bg="light grey").place(x=2,y=3,width=260,height=40)


        frame_appoint=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_appoint.place(x=105,y=100,height=70,width=835)
        self.appoint_head=Label(self.root,text="Search Appointment",font=("times new roman",11)).place(x=110,y=88)


        self.patient_name=Label(frame_appoint,text="Patient Name:",font=("times new roman",15,"bold")).place(x=18,y=20)
        self.patient_name_entry=Entry(frame_appoint,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.patient_name_entry.place(x=160,y=20,width=200)


        butt_search=Button(frame_appoint,text="Search",cursor="hand2",bg="sky blue",fg="white",command=self.search1).place(x=380,y=20,height=30,width=100)
        butt_clear=Button(frame_appoint,text="Clear",cursor="hand2",bg="green",fg="white",command=self.clear).place(x=500,y=20,height=30,width=100)


        frame_butt=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_butt.place(x=105,y=183,height=65,width=835)
        self.appointmenu_head=Label(self.root,text="Appointment Menu",font=("times new roman",11)).place(x=110,y=172)


        butt_showtoday=Button(frame_butt,text="Show Today's Appointment",cursor="hand2",bg="dark blue",fg="white",command=self.todayapp,font=("times new roman",12)).place(x=5,y=20,height=35,width=190)
        butt_showallappoint=Button(frame_butt,text="Show All Appointment",cursor="hand2",bg="green",fg="white", command=self.showall,font=("times new roman",12)).place(x=210,y=20,height=35,width=190)
        butt_deleteall=Button(frame_butt,text="Delete All",cursor="hand2",bg="Red",fg="white",command=self.deleteall).place(x=425,y=20,height=35,width=190)
        butt_deletetoday=Button(frame_butt,text="Delete Today's History",cursor="hand2",bg="dark grey",fg="white",command=self.delete1).place(x=640,y=20,height=35,width=190)


        frame_table=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_table.place(x=105,y=255,height=330,width=835)


        scroll_x=ttk.Scrollbar(frame_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame_table,orient=VERTICAL)
        

        self.patient_table=ttk.Treeview(frame_table,column=("id","patient_name","Gender","Contact","Symptoms","Specification","Doctor","Apt_date","Apt_time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.patient_table.xview)
        scroll_y=ttk.Scrollbar(command=self.patient_table.yview)


        self.patient_table.heading("id",text="Patient ID")
        self.patient_table.heading("patient_name",text="Patient Name")
        self.patient_table.heading("Gender",text="Gender")
        self.patient_table.heading("Contact",text="Patient Contact")
        self.patient_table.heading("Symptoms",text="Symptoms")
        self.patient_table.heading("Specification",text="Specification")
        self.patient_table.heading("Doctor",text="Doctor")
        self.patient_table.heading("Apt_date",text="Apt Date")
        self.patient_table.heading("Apt_time",text="Apt Time")

        self.patient_table["show"]="headings"

        self.patient_table.pack(fill=BOTH,expand=1)
        self.fetch_data()


        self.patient_table.column("id",width=40)
        self.patient_table.column("patient_name",width=100)
        self.patient_table.column("Gender",width=60)
        self.patient_table.column("Contact",width=80)
        self.patient_table.column("Symptoms",width=80)
        self.patient_table.column("Specification",width=80)
        self.patient_table.column("Doctor",width=60)
        self.patient_table.column("Apt_date",width=70)
        self.patient_table.column("Apt_time",width=70)


    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select ROW_NUMBER() over(order by patient_name) as ID,patient_name,Gender,Contact,Symptoms,Specification,doctor,Apt_date,Apt_time from patient")
        rows=cur.fetchall()
        if len(rows)!=0 or len(rows)==0:
            self.patient_table.delete(*self.patient_table.get_children())
            for i in rows:
                self.patient_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def search1(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select ROW_NUMBER() over(order by patient_name) as ID,patient_name,Gender,Contact,Symptoms,Specification,doctor,Apt_date,Apt_time from patient where patient_name=%s",(self.patient_name_entry.get()))
        rows=cur.fetchall()
        if len(rows)!=0 or len(rows)==0:
            self.patient_table.delete(*self.patient_table.get_children())
            for i in rows:
                self.patient_table.insert("",END,values=i)

            conn.commit()
            self.clear()
        conn.close()


    def todayapp(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select ROW_NUMBER() over(order by patient_name) as ID,patient_name,Gender,Contact,Symptoms,Specification,doctor,Apt_date,Apt_time from patient where Apt_date=current_date")
        rows=cur.fetchall()
        if len(rows)!=0 or len(rows)==0:
            self.patient_table.delete(*self.patient_table.get_children())
            for i in rows:
                self.patient_table.insert("",END,values=i)

            conn.commit()
            self.clear()
        conn.close()

    
    def delete1(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("delete from patient where apt_date=current_date")
        
        
        conn.commit()
        self.clear()
        self.fetch_data()
        conn.close()

    def deleteall(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("delete from patient")
        
        
        conn.commit()
        self.clear()
        self.fetch_data()
        conn.close()


    def clear(self):
        self.patient_name_entry.delete(0,END)




    def showall(self):
        self.fetch_data()

        








    

    def exit_home(self):
        self.root.destroy()

    def home(self):
        self.root.destroy()
        import home

    def home(self):
        self.root.destroy()
        import home

    def doctor(self):
        self.root.destroy()
        import doctor

    def patient(self):
        self.root.destroy()
        import patient
    
    def admit(self):
        self.root.destroy()
        import admit















root=Tk()
obj=appoint(root)
root.mainloop()