from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import pymysql

class managedoctor:
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
        frame_admin.place(x=100,y=40,width=850,height=40)
        admin_dash=Label(frame_admin,text="Doctor Dashboard",font=("times new roman",15,"bold"),bg="light grey").place(x=2,y=3,width=150,height=40)


        butt_managespecial=Button(frame_admin,text="Manage Specialization",cursor="hand2",command=self.managespecial).place(x=160,y=5,height=30,width=150)
        butt_managedoctor=Button(frame_admin,text="Manage Doctor",cursor="hand2").place(x=320,y=5,height=30,width=150)

        frame_adddoctor=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_adddoctor.place(x=140,y=100,height=460,width=310)
        self.adddoctor_head=Label(self.root,text="Add Doctor",font=("times new roman",11)).place(x=145,y=89)

        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select distinct specialization from specialization")
        rows=cur.fetchall()
        
        self.options=[
            "specilization              "
            
        ]

        for i in rows:
            self.options.insert(1,i[0])
        
        
        conn.commit()
        conn.close()

        self.specil=Label(frame_adddoctor,text="specialization",font=("times new roman",13)).place(x=4,y=28)
        
        self.clicked=StringVar()
        self.clicked.set(self.options[0])
        self.drop=OptionMenu(frame_adddoctor,self.clicked,*self.options).place(x=132,y=24,width=150)

        self.name=Label(frame_adddoctor,text="Name",font=("times new roman",13)).place(x=20,y=80)
        self.name_entry=Entry(frame_adddoctor,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.name_entry.place(x=132,y=78,width=150)

        self.fee=Label(frame_adddoctor,text="Consultancy Fees",font=("times new roman",13)).place(x=4,y=132)
        self.fee_entry=Entry(frame_adddoctor,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.fee_entry.place(x=132,y=132,width=150)

        self.contact=Label(frame_adddoctor,text="Contace No.",font=("times new roman",13)).place(x=4,y=194)
        self.contact_entry=Entry(frame_adddoctor,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.contact_entry.place(x=132,y=194,width=150)

        self.email=Label(frame_adddoctor,text="Email",font=("times new roman",13)).place(x=20,y=246)
        self.email_entry=Entry(frame_adddoctor,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.email_entry.place(x=132,y=246,width=150)

        self.address=Label(frame_adddoctor,text="Address",font=("times new roman",13)).place(x=4,y=298)
        self.address_entry=Entry(frame_adddoctor,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.address_entry.place(x=102,y=298,width=200,height=70)


        butt_add=Button(frame_adddoctor,text="Add",cursor="hand2",bg="sky blue",fg="white",command=self.add).place(x=18,y=388,height=30,width=80)
        butt_update=Button(frame_adddoctor,text="Update",cursor="hand2",bg="green",fg="white",command=self.update).place(x=109,y=388,height=30,width=80)
        butt_clear=Button(frame_adddoctor,text="Clear",cursor="hand2",bg="dark orange",fg="white",command=self.clear).place(x=200,y=388,height=30,width=80)
        butt_delete=Button(frame_adddoctor,text="Delete",cursor="hand2",bg="purple",fg="white",command=self.delete1).place(x=109,y=425,height=30,width=80)


        frame_docdetails=Frame(self.root,borderwidth=1,relief=SOLID)
        frame_docdetails.place(x=455,y=100,height=460,width=485)
        self.docdetails_head=Label(self.root,text="Doctor Details",font=("times new roman",11)).place(x=460,y=89)

        self.docname=Label(frame_docdetails,text="Enter Doctor Name",font=("times new roman",14)).place(x=15,y=25)
        butt_search=Button(frame_docdetails,text="Search",cursor="hand2",bg="dark blue",fg="white",command=self.search1).place(x=320,y=25,height=30,width=70)
        butt_showall=Button(frame_docdetails,text="Show All",cursor="hand2",bg="dark orange",fg="white",command=self.showall).place(x=400,y=25,height=30,width=70)
        self.docname_entry=Entry(frame_docdetails,font=("times new roman",15),borderwidth=4,relief=GROOVE)
        self.docname_entry.place(x=165,y=25,height=30,width=150)

        frame_docdetailsdesc=Frame(frame_docdetails,borderwidth=1,relief=SOLID)
        frame_docdetailsdesc.place(x=2,y=70,height=387,width=480)


        scroll_x=ttk.Scrollbar(frame_docdetailsdesc,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame_docdetailsdesc,orient=VERTICAL)
        

        self.doctor_table=ttk.Treeview(frame_docdetailsdesc,column=("id","specialization","docname","address","fee","contactno","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.doctor_table.xview)
        scroll_y=ttk.Scrollbar(command=self.doctor_table.yview)


        self.doctor_table.heading("id",text="ID")
        self.doctor_table.heading("specialization",text="specialization")
        self.doctor_table.heading("docname",text="Doctor name")
        self.doctor_table.heading("address",text="Address")
        self.doctor_table.heading("fee",text="Fee")
        self.doctor_table.heading("contactno",text="Contact No.")
        self.doctor_table.heading("email",text="Email")

        self.doctor_table["show"]="headings"

        self.doctor_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        


        self.doctor_table.column("id",width=30)
        self.doctor_table.column("specialization",width=80)
        self.doctor_table.column("docname",width=80)
        self.doctor_table.column("address",width=70)
        self.doctor_table.column("fee",width=60)
        self.doctor_table.column("contactno",width=70)
        self.doctor_table.column("email",width=70)


    def add(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        if self.name_entry.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required", parent=self.root)

        else:
            cur.execute("insert into doctor values(%s,%s,%s,%s,%s,%s,NOW())",(self.clicked.get(),self.name_entry.get(),self.address_entry.get(),self.fee_entry.get(),self.contact_entry.get(),self.email_entry.get()))
            
            conn.commit()
            self.clear()
            self.fetch_data()
            conn.close()


    def delete1(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("delete from doctor where email=%s",(self.email_entry.get()))
        
        
        conn.commit()
        self.clear()
        self.fetch_data()
        conn.close()


    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select ROW_NUMBER() over(order by specialization) as ID,specialization,doctor_name,address,fee,contact_no,email from doctor;")
        rows=cur.fetchall()
        if len(rows)!=0 or len(rows)==0:
            self.doctor_table.delete(*self.doctor_table.get_children())
            for i in rows:
                self.doctor_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def clear(self):
        #self.clicked.delete(0,END)
        self.name_entry.delete(0,END)
        self.fee_entry.delete(0,END)
        self.address_entry.delete(0,END)
        self.contact_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.docname_entry.delete(0,END)

    def search1(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("select ROW_NUMBER() over(order by specialization) as ID,specialization,doctor_name,address,fee,contact_no,email from doctor where doctor_name=%s",(self.docname_entry.get()))
        rows=cur.fetchall()
        if len(rows)!=0 or len(rows)==0:
            self.doctor_table.delete(*self.doctor_table.get_children())
            for i in rows:
                self.doctor_table.insert("",END,values=i)

            conn.commit()
            self.clear()
        conn.close()



    def update(self):
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        cur.execute("update doctor set doctor_name=%s,address=%s,fee=%s,contact_no=%s,email=%s where specialization=%s",(self.name_entry.get(),self.address_entry.get(),self.fee_entry.get(),self.contact_entry.get(),self.email_entry.get(),self.clicked.get()))
        conn.commit()
        self.clear()
        self.fetch_data()
        conn.close()


    
    
    
    
    def showall(self):
        self.fetch_data()


    def home(self):
        self.root.destroy()
        import home

    def patient(self):
        self.root.destroy()
        import patient

    def appointment(self):
        self.root.destroy()
        import appointment



    def exit_home(self):
        self.root.destroy() 

    def managespecial(self):
        self.root.destroy()
        import doctor



root=Tk()
obj=managedoctor(root)
root.mainloop()