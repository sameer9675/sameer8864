from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import pymysql

class patient:
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


        butt_doctor=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.doctor).place(x=0,y=131,width=100,height=90)
        self.bg_doctoricon=PhotoImage(file="D:\programming\python\program\project\images\doctoricon.png")
        self.bg_doctoriconimage=Label(frame_butt,image=self.bg_doctoricon)
        self.bg_doctoriconimage.place(x=28,y=136, width=45, height=45)
        self.doctor_head=Label(frame_butt,text="DOCTOR",font=("times new roman",11)).place(x=20,y=190,height=10)
        
        butt_patient=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2").place(x=0,y=221,width=100,height=90)
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
        frame_admin.place(x=100,y=40,width=850,height=40)
        admin_dash=Label(frame_admin,text="Manage Patient",font=("times new roman",15,"bold"),bg="light grey").place(x=2,y=3,width=150,height=40)


        frame_patientdetail=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_patientdetail.place(x=105,y=100,height=270,width=320)
        self.patientdetail_head=Label(self.root,text="Patient Details",font=("times new roman",10)).place(x=110,y=90)


        self.patient_name=Label(self.root,text="Patient Name",font=("times new roman",13)).place(x=116,y=118)
        self.patient_name_entry=Entry(frame_patientdetail,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.patient_name_entry.place(x=135,y=15,width=158)
        
        self.options=[
            "Gender                        ",
            "Male",
            "Female",
            "Other"
        ]
        self.clicked=StringVar()
        self.clicked.set(self.options[0])
        self.drop=OptionMenu(frame_patientdetail,self.clicked,*self.options).place(x=135,y=52,width=158)
        self.patient_gender=Label(self.root,text="Gender",font=("times new roman",13)).place(x=125,y=155)

        self.patient_DOB=Label(self.root,text="D.O.B",font=("times new roman",13)).place(x=125,y=192)
        self.patient_DOB_entry=Entry(frame_patientdetail,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.patient_DOB_entry.place(x=135,y=89,width=158)

        self.patient_contact=Label(self.root,text="Contact No.",font=("times new roman",13)).place(x=116,y=229)
        self.patient_contact_entry=Entry(frame_patientdetail,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.patient_contact_entry.place(x=135,y=126,width=158)

        self.patient_email=Label(self.root,text="Email",font=("times new roman",13)).place(x=125,y=266)
        self.patient_email_entry=Entry(frame_patientdetail,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.patient_email_entry.place(x=135,y=163,width=158)

        self.patient_address=Label(self.root,text="Address",font=("times new roman",13)).place(x=125,y=303)
        self.patient_address_entry=Entry(frame_patientdetail,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.patient_address_entry.place(x=135,y=200,width=165,height=60)



        frame_appoint=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_appoint.place(x=430,y=100,height=270,width=510)
        self.appoint_head=Label(self.root,text="Appoint Doctor",font=("times new roman",10)).place(x=438,y=90)


        self.symptom=Label(frame_appoint,text="Symptoms",font=("times new roman",13)).place(x=15,y=20)
        self.symptom_entry=Entry(frame_appoint,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.symptom_entry.place(x=130,y=15,width=165,height=90)



        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select distinct specialization from specialization")
        rows=cur.fetchall()
        
        self.options1=[
            "specification               "
            
        ]

        for i in rows:
            self.options1.insert(1,i[0])
        
        
        conn.commit()
        conn.close()
        
        
        self.appointdoc=Label(frame_appoint,text="Select to appoint doctor",font=("times new roman",13)).place(x=310,y=20)
        self.clicked1=StringVar()
        self.clicked1.set(self.options1[0])
        self.drop=OptionMenu(frame_appoint,self.clicked1,*self.options1).place(x=320,y=48,width=158)


        
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select doctor_name from doctor where specialization=%s",(self.clicked1.get()))
        rows=cur.fetchall()
        self.options2=[
            "Doctor                          ",
            
        ]
        for i in rows:
            self.options2.insert(1,i[0])
        conn.commit()
        conn.close()
        self.clicked2=StringVar()
        self.clicked2.set(self.options2[0])
        self.drop=OptionMenu(frame_appoint,self.clicked2,*self.options2).place(x=320,y=76,width=158)

        
        
        
        
        self.date=Label(frame_appoint,text="Enter Date (DD//MM//YYYY)",font=("times new roman",13)).place(x=15,y=130)
        self.date_entry=Entry(frame_appoint,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.date_entry.place(x=15,y=160,width=215,height=30)


        self.time=Label(frame_appoint,text="Enter Time (HH/MM/SS)",font=("times new roman",13)).place(x=270,y=130)
        self.time_entry=Entry(frame_appoint,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.time_entry.place(x=270,y=160,width=215,height=30)

        butt_add=Button(frame_appoint,text="Add",cursor="hand2",bg="sky blue",fg="white",command=self.add).place(x=15,y=210,height=30,width=100)
        butt_update=Button(frame_appoint,text="Update",cursor="hand2",bg="green",fg="white",command=self.update).place(x=135,y=210,height=30,width=100)
        butt_clear=Button(frame_appoint,text="Clear",cursor="hand2",bg="dark orange",fg="white",command=self.clear).place(x=260,y=210,height=30,width=100)
        butt_delete=Button(frame_appoint,text="Delete",cursor="hand2",bg="purple",fg="white",command=self.delete1).place(x=390,y=210,height=30,width=100)

        frame_dis=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_dis.place(x=105,y=385,height=200,width=835)
        self.appoint_head=Label(self.root,text="Patient Details",font=("times new roman",10)).place(x=110,y=373)

        self.name=Label(frame_dis,text="Enter Patient Name",font=("times new roman",13)).place(x=12,y=15)
        self.name_entry=Entry(frame_dis,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.name_entry.place(x=170,y=12,width=190,height=35)

        butt_search=Button(frame_dis,text="Search",cursor="hand2",bg="sky blue",fg="white",command=self.search1).place(x=380,y=12,height=32,width=80)
        butt_clear_search=Button(frame_dis,text="Clear",cursor="hand2",bg="green",fg="white",command=self.clear).place(x=470,y=12,height=32,width=80)
        butt_showall=Button(frame_dis,text="Show All",cursor="hand2",bg="dark orange",fg="white",command=self.showall).place(x=565,y=12,height=32,width=80)

        frame_table=Frame(frame_dis,borderwidth=1,relief=SOLID)
        frame_table.place(x=1,y=55,height=142,width=830)


        scroll_x=ttk.Scrollbar(frame_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame_table,orient=VERTICAL)
        

        self.patient_table=ttk.Treeview(frame_table,column=("id","patient_name","Gender","DOB","Contact","email","Address","Symptoms","Specification","Doctor","Apt_date","Apt_time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.patient_table.xview)
        scroll_y=ttk.Scrollbar(command=self.patient_table.yview)


        self.patient_table.heading("id",text="ID")
        self.patient_table.heading("patient_name",text="Patient Name")
        self.patient_table.heading("Gender",text="Gender")
        self.patient_table.heading("DOB",text="DOB")
        self.patient_table.heading("Contact",text="Contact")
        self.patient_table.heading("email",text="Email")
        self.patient_table.heading("Address",text="Address")
        self.patient_table.heading("Symptoms",text="Symptoms")
        self.patient_table.heading("Specification",text="Specification")
        self.patient_table.heading("Doctor",text="Doctor")
        self.patient_table.heading("Apt_date",text="Apt Date")
        self.patient_table.heading("Apt_time",text="Apt Time")

        self.patient_table["show"]="headings"

        self.patient_table.pack(fill=BOTH,expand=1)
        self.fetch_data()


        self.patient_table.column("id",width=30)
        self.patient_table.column("patient_name",width=80)
        self.patient_table.column("Gender",width=60)
        self.patient_table.column("DOB",width=80)
        self.patient_table.column("Contact",width=80)
        self.patient_table.column("email",width=80)
        self.patient_table.column("Address",width=80)
        self.patient_table.column("Symptoms",width=80)
        self.patient_table.column("Specification",width=60)
        self.patient_table.column("Doctor",width=60)
        self.patient_table.column("Apt_date",width=70)
        self.patient_table.column("Apt_time",width=70)



    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select ROW_NUMBER() over(order by patient_name) as ID,patient_name,Gender,DOB,Contact,email,Address,Symptoms,Specification,doctor,Apt_date,Apt_time from patient")
        rows=cur.fetchall()
        if len(rows)!=0 or len(rows)==0:
            self.patient_table.delete(*self.patient_table.get_children())
            for i in rows:
                self.patient_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def add(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        if self.patient_name_entry.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required", parent=self.root)

        else:
            cur.execute("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.patient_name_entry.get(),
                                                                                       self.clicked.get(),
                                                                                       self.patient_DOB_entry.get(),
                                                                                       self.patient_contact_entry.get(),
                                                                                       self.patient_email_entry.get(),
                                                                                       self.patient_address_entry.get(),
                                                                                       self.symptom_entry.get(),
                                                                                       self.clicked1.get(),
                                                                                       self.clicked2.get(),
                                                                                       self.date_entry.get(),
                                                                                       self.time_entry.get()
                                                                                       ))
            
            conn.commit()
            self.clear()
            self.fetch_data()
            conn.close()


    def delete1(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("delete from patient where email=%s",(self.patient_email_entry.get()))
        
        
        conn.commit()
        self.clear()
        self.fetch_data()
        conn.close()


    def clear(self):
        #self.clicked.delete(0,END)
        self.patient_name_entry.delete(0,END)
        self.patient_DOB_entry.delete(0,END)
        self.patient_contact_entry.delete(0,END)
        self.patient_email_entry.delete(0,END)
        self.patient_address_entry.delete(0,END)
        self.symptom_entry.delete(0,END)
        self.date_entry.delete(0,END)
        self.time_entry.delete(0,END)
        self.name_entry.delete(0,END)


    def search1(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select ROW_NUMBER() over(order by patient_name) as ID,patient_name,Gender,DOB,Contact,email,Address,Symptoms,Specification,doctor,Apt_date,Apt_time from patient where patient_name=%s",(self.patient_name_entry.get()))
        rows=cur.fetchall()
        if len(rows)!=0 or len(rows)==0:
            self.patient_table.delete(*self.patient_table.get_children())
            for i in rows:
                self.patient_table.insert("",END,values=i)

            conn.commit()
            self.clear()
        conn.close()



    def update(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("update patient set patient_name=%s,Gender=%s,DOB=%s,Contact=%s,email=%s,Address=%s,Symptoms=%s,specification=%s,doctor=%s,Apt_date=%s,Apt_time=%s where patient_name=%s",(self.patient_name_entry.get(),
                                                                                                                                                                      self.clicked.get(),
                                                                                                                                                                      self.patient_DOB_entry.get(),
                                                                                                                                                                      self.patient_contact_entry.get(),
                                                                                                                                                                      self.patient_email_entry.get(),
                                                                                                                                                                      self.patient_address_entry.get(),
                                                                                                                                                                      self.symptom_entry.get(),
                                                                                                                                                                      self.clicked1.get(),
                                                                                                                                                                      self.clicked2.get(),
                                                                                                                                                                      self.date_entry.get(),
                                                                                                                                                                      self.time_entry.get(),
                                                                                                                                                                      self.patient_name_entry.get()
                                                                                                                                                                      ))
        conn.commit()
        self.clear()
        self.fetch_data()
        conn.close()


    
    
    def showall(self):
        self.fetch_data()

    def home(self):
        self.root.destroy()
        import home

    def doctor(self):
        self.root.destroy()
        import doctor

    def appointment(self):
        self.root.destroy()
        import appointment

    



    
    
    def exit_home(self):
        self.root.destroy()






root=Tk()
obj=patient(root)
root.mainloop()