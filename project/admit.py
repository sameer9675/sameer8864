from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import pymysql

class admit:
    def __init__(self,root):
        self.root=root
        self.root.title("login systenm")
        self.root.geometry("1000x630+100+50")
        self.root.resizable(False,False)
        self.root.configure(bg="light green")

        frame_head=Frame(self.root,bg="dark blue")
        frame_head.place(x=0,y=0,height=40,width=1000)

        heading=Label(frame_head,text="HOSPITAL MANAGEMT SYSTEM",font=("times new roman",15),fg="white",bg="dark blue" ).place(x=10,y=4,height=30)


        frame_butt=Frame(self.root,bg="light blue")
        frame_butt.place(x=0,y=40,width=100,height=590)

        men=Label(frame_butt,text="MENU",font=("times new roman",18,"bold"),bg="white").place(x=0,y=0,width=100,height=52)
        
        butt_home=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.home).place(x=0,y=52,width=100,height=94)
        self.bg_home=PhotoImage(file="D:\programming\python\program\project\images\home2.png")
        self.bg_homeimage=Label(frame_butt,image=self.bg_home)
        self.bg_homeimage.place(x=28,y=65, width=45, height=45)
        self.home_head=Label(frame_butt,text="HOME",font=("times new roman",11)).place(x=25,y=120,height=10)


        butt_doctor=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.doctor).place(x=0,y=146,width=100,height=94)
        self.bg_doctoricon=PhotoImage(file="D:\programming\python\program\project\images\doctoricon.png")
        self.bg_doctoriconimage=Label(frame_butt,image=self.bg_doctoricon)
        self.bg_doctoriconimage.place(x=28,y=160, width=45, height=45)
        self.doctor_head=Label(frame_butt,text="DOCTOR",font=("times new roman",11)).place(x=20,y=218,height=10)
        
        butt_patient=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.patient).place(x=0,y=240,width=100,height=94)
        self.bg_patienticon=PhotoImage(file="D:\programming\python\program\project\images\patienticon.png")
        self.bg_patienticonimage=Label(frame_butt,image=self.bg_patienticon)
        self.bg_patienticonimage.place(x=28,y=250, width=45, height=45)
        self.patient_head=Label(frame_butt,text="PATIENT",font=("times new roman",11)).place(x=20,y=310,height=10)

        butt_appointment=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.appointment).place(x=0,y=334,width=100,height=94)
        self.bg_appointmenticon=PhotoImage(file="D:\programming\python\program\project\images\calendericon.png")
        self.bg_appointmenticonimage=Label(frame_butt,image=self.bg_appointmenticon)
        self.bg_appointmenticonimage.place(x=28,y=345, width=45, height=45)
        self.appointment_head=Label(frame_butt,text="APPOINTMENT",font=("times new roman",10)).place(x=2,y=400,height=10)

        butt_admitinfo=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2").place(x=0,y=428,width=100,height=94)
        self.bg_admiticon=PhotoImage(file="D:\programming\python\program\project\images\dmiticon.png")
        self.bg_admiticonimage=Label(frame_butt,image=self.bg_admiticon)
        self.bg_admiticonimage.place(x=28,y=436, width=45, height=45)
        self.admit_head=Label(frame_butt,text="ADMIT INFO",font=("times new roman",11)).place(x=2,y=498,height=10)
        
        
        butt_exit=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.exit_home).place(x=0,y=522,width=100,height=69)
        self.bg_exiticon=PhotoImage(file="D:\programming\python\program\project\images\exiticon.png")
        self.bg_exiticonimage=Label(frame_butt,image=self.bg_exiticon)
        self.bg_exiticonimage.place(x=28,y=525, width=45, height=65)
        #self.admit_head=Label(frame_butt,text="EXIT",font=("times new roman",11)).place(x=8,y=540,height=10)

        frame_admin=Frame(self.root,bg="light grey")
        frame_admin.place(x=100,y=40,width=900,height=52)
        admin_dash=Label(frame_admin,text="Admit Patient/Information",font=("times new roman",17,"bold"),bg="light grey").place(x=2,y=5,width=280,height=40)


        self.id=Label(self.root,text="Input Patient's ID",font=("times new roaman",11,"bold"),bg="light green").place(x=115,y=110)
        self.entry_id=Entry(self.root,font=("times new roaman",11,"bold"),borderwidth=4,relief=GROOVE)
        self.entry_id.place(x=102,y=140,width=180,height=26)
        self.butt_id_search=Button(self.root,text="SEARCH",font=("times new roaman",11,"bold"),cursor="hand2",bg="light blue",command=self.idcheck).place(x=115,y=180,width=140,height=35)

        
        self.idtext=StringVar()
        self.idrandom=Label(self.root,text="Patient ID:",font=("times new roaman",11,"bold"),bg="light green").place(x=370,y=110)
        self.entry_idrandom=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.idtext,borderwidth=4,relief=GROOVE)
        self.entry_idrandom.place(x=470,y=110,width=180,height=26)

        self.nametext=StringVar()
        self.name=Label(self.root,text="NAME:",font=("times new roaman",11,"bold"),bg="light green").place(x=370,y=172)
        self.entry_name=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.nametext,borderwidth=4,relief=GROOVE)
        self.entry_name.place(x=470,y=170,width=180,height=26)

        self.gender=Label(self.root,text="GENDER:",font=("times new roaman",11,"bold"),bg="light green").place(x=370,y=243)
        self.options=[
            "Gender                                ",
            "Male",
            "Female",
            "Other"
        ]
        self.clicked=StringVar()
        self.clicked.set(self.options[0])
        self.drop=OptionMenu(self.root,self.clicked,*self.options).place(x=470,y=240,width=180)

        self.agetext=StringVar()
        self.age=Label(self.root,text="AGE:",font=("times new roaman",11,"bold"),bg="light green").place(x=370,y=314)
        self.entry_age=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.agetext,borderwidth=4,relief=GROOVE)
        self.entry_age.place(x=470,y=310,width=180,height=26)


        self.contacttext=StringVar()
        self.contact=Label(self.root,text="Contact No. :",font=("times new roaman",11,"bold"),bg="light green").place(x=370,y=383)
        self.entry_contact=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.contacttext,borderwidth=4,relief=GROOVE)
        self.entry_contact.place(x=470,y=380,width=180,height=26)

        
        self.addresstext=StringVar()
        self.address=Label(self.root,text="Address:",font=("times new roaman",11,"bold"),bg="light green").place(x=370,y=454)
        self.entry_address=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.addresstext,borderwidth=4,relief=GROOVE)
        self.entry_address.place(x=470,y=450,width=180,height=26)

        
        self.diseasetext=StringVar()
        self.address=Label(self.root,text="Disease:",font=("times new roaman",11,"bold"),bg="light green").place(x=370,y=525)
        self.entry_address=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.diseasetext,borderwidth=4,relief=GROOVE)
        self.entry_address.place(x=470,y=520,width=180,height=26)

        
        self.checkintext=StringVar()
        self.check=Label(self.root,text="Check In:",font=("times new roaman",11,"bold"),bg="light green").place(x=370,y=596)
        self.entry_check=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.checkintext,borderwidth=4,relief=GROOVE)
        self.entry_check.place(x=470,y=590,width=180,height=26)


        
        self.bloodtext=StringVar()
        self.blood=Label(self.root,text="Blood group:",font=("times new roaman",11,"bold"),bg="light green").place(x=800,y=110)
        self.entry_blood=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.bloodtext,borderwidth=4,relief=GROOVE)
        self.entry_blood.place(x=765,y=140,width=180,height=26)


        
        self.docnametext=StringVar()
        self.docname=Label(self.root,text="Doctor Name:",font=("times new roaman",11,"bold"),bg="light green").place(x=800,y=190)
        self.entry_docname=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.docnametext,borderwidth=4,relief=GROOVE)
        self.entry_docname.place(x=765,y=220,width=180,height=26)


        
        self.checkouttext=StringVar()
        self.checkout=Label(self.root,text="Check Out:",font=("times new roaman",11,"bold"),bg="light green").place(x=800,y=270)
        self.entry_checkout=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.checkouttext,borderwidth=4,relief=GROOVE)
        self.entry_checkout.place(x=765,y=300,width=180,height=26)

        
        self.roomtext=StringVar()
        self.room=Label(self.root,text="Room No.:",font=("times new roaman",11,"bold"),bg="light green").place(x=800,y=350)
        self.entry_room=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.roomtext,borderwidth=4,relief=GROOVE)
        self.entry_room.place(x=765,y=380,width=180,height=26)


        
        self.pricetext=StringVar()
        self.price=Label(self.root,text="Price:",font=("times new roaman",11,"bold"),bg="light green").place(x=800,y=430)
        self.entry_price=Entry(self.root,font=("times new roaman",11,"bold"),textvariable=self.pricetext,borderwidth=4,relief=GROOVE)
        self.entry_price.place(x=765,y=460,width=180,height=26)

        self.butt_add=Button(self.root,text="ADD",font=("times new roaman",11,"bold"),cursor="hand2",bg="light blue",command=self.add).place(x=786,y=520,width=140,height=35)







    def idcheck(self):
        self.c=self.entry_id.get().isalpha()
        if len(self.entry_id.get())!=4:
            messagebox.showerror("Error","ID SHOULD BE OF 8 DIGIT")

        elif self.c==TRUE:
            messagebox.showerror("Error","ID SHOULD BE IN DIGIT")


    def add(self):
        self.d=random.randint(1001,9999)
        c=self.contacttext.get().isalpha()
        conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
        cur=conn.cursor()
        if  (self.nametext.get()=="" or self.contacttext.get()=="" or self.addresstext.get()=="" or self.diseasetext.get()=="" or self.checkintext.get()=="" or self.bloodtext.get()=="" or self.docnametext.get()=="" or self.checkouttext.get()=="" or self.roomtext.get()=="" or self.pricetext.get()=="" or self.agetext.get()==""):
            messagebox.showerror("ERROR","All Fields Are Required", parent=self.root)

        elif c==TRUE or len(self.contacttext.get())!=10:
             messagebox.showerror("ERROR","Invalid Contact No.", parent=self.root)  
             
        else:
            cur.execute("insert into admit values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.d,
                                                                                       self.nametext.get(),
                                                                                       self.clicked.get(),
                                                                                       self.contacttext.get(),
                                                                                       self.addresstext.get(),
                                                                                       self.diseasetext.get(),
                                                                                       self.checkintext.get(),
                                                                                       self.bloodtext.get(),
                                                                                       self.docnametext.get(),
                                                                                       self.checkouttext.get(),
                                                                                       self.roomtext.get(),
                                                                                       self.pricetext.get(),
                                                                                       self.agetext.get()
                                                                                       ))
            conn.commit()
            self.idtext.set(self.d)
            conn.close()



    def home(self):
        self.root.destroy()
        import home

    def doctor(self):
        self.root.destroy()
        import doctor

    def appointment(self):
        self.root.destroy()
        import appointment

    def patient(self):
        self.root.destroy()
        import patient





        




        














    def exit_home(self):
        self.root.destroy()






root=Tk()
obj=admit(root)
root.mainloop()