from tkinter import *
from tkinter import messagebox
import pymysql


class homepage:
    def __init__(self,root):
        self.root=root 
        self.root.title("home page")
        self.root.geometry("810x590+100+50")
        self.root.resizable(False,False)
        
        
        self.bg=PhotoImage(file="D:\programming\python\program\project\images\home1.png")
        self.bg_image=Label(self.root,image=self.bg)
        self.bg_image.place(x=0,y=0, relwidth=1, relheight=1)

        frame_head=Frame(self.root,bg="dark blue")
        frame_head.place(x=0,y=0,height=40,width=810)

        heading=Label(frame_head,text="HOSPITAL MANAGEMT SYSTEM",font=("times new roman",15),fg="white",bg="dark blue" ).place(x=10,y=4,height=30)

        butt_logout=Button(frame_head,text="LOG OUT",bg="red",fg="white",cursor="hand2",font=("times new roman",10),command=self.logout)
        butt_logout.place(x=740,y=5,height=30)


        frame_butt=Frame(self.root,bg="light blue")
        frame_butt.place(x=0,y=40,width=100,height=550)

        men=Label(frame_butt,text="MENU",font=("times new roman",15),bg="white").place(x=0,y=0,width=100,height=40)
        
        butt_home=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2").place(x=0,y=41,width=100,height=90)
        self.bg_home=PhotoImage(file="D:\programming\python\program\project\images\home2.png")
        self.bg_homeimage=Label(frame_butt,image=self.bg_home)
        self.bg_homeimage.place(x=28,y=50, width=45, height=45)
        self.home_head=Label(frame_butt,text="HOME",font=("times new roman",11)).place(x=25,y=105,height=10)


        butt_doctor=Button(frame_butt,font=("times new roman",13),bg="white",cursor="hand2",command=self.doctor).place(x=0,y=131,width=100,height=90)
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
        frame_admin.place(x=100,y=40,width=710,height=40)
        admin_dash=Label(frame_admin,text="Admin Dashboard",font=("times new roman",15,"bold"),bg="light grey").place(x=0,y=3,width=150,height=40)

        self.a=0
        specialization=Button(self.root,bg="red",fg="white",cursor="hand2").place(x=120,y=100,width=150,height=85)
        self.specialization_val=Label(self.root,text="Specialization",bg="red",fg="white",font=("times new roman",15)).place(x=135,y=116,width=120,height=25)
        self.specialization_valint=Label(self.root,text=self.a,bg="red",fg="white",font=("times new roman",15)).place(x=175,y=140,width=30,height=25)
        self.specialization_brack1=Label(self.root,text="(",bg="red",fg="white",font=("times new roman",15)).place(x=176,y=140,width=10,height=25)
        self.specialization_brack2=Label(self.root,text=")",bg="red",fg="white",font=("times new roman",15)).place(x=194,y=140,width=10,height=25)

        self.b=0
        Doctor=Button(self.root,bg="red",fg="white",cursor="hand2").place(x=290,y=100,width=150,height=85)
        self.doctor_val=Label(self.root,text="DOCTOR",bg="red",fg="white",font=("times new roman",15)).place(x=305,y=116,width=120,height=25)
        self.specialization_valint=Label(self.root,text=self.b,bg="red",fg="white",font=("times new roman",15)).place(x=345,y=140,width=30,height=25)
        self.specialization_brack1=Label(self.root,text="(",bg="red",fg="white",font=("times new roman",15)).place(x=346,y=140,width=10,height=25)
        self.specialization_brack2=Label(self.root,text=")",bg="red",fg="white",font=("times new roman",15)).place(x=364,y=140,width=10,height=25)

        self.c=0
        patient=Button(self.root,bg="red",fg="white",cursor="hand2").place(x=460,y=100,width=150,height=85)
        self.doctor_val=Label(self.root,text="PATIENT",bg="red",fg="white",font=("times new roman",15)).place(x=475,y=116,width=120,height=25)
        self.doctor_valint=Label(self.root,text=self.c,bg="red",fg="white",font=("times new roman",15)).place(x=515,y=140,width=30,height=25)
        self.doctor_brack1=Label(self.root,text="(",bg="red",fg="white",font=("times new roman",15)).place(x=516,y=140,width=10,height=25)
        self.doctor_brack2=Label(self.root,text=")",bg="red",fg="white",font=("times new roman",15)).place(x=534,y=140,width=10,height=25)

        self.d=0
        todayappoint=Button(self.root,bg="red",fg="white",cursor="hand2").place(x=630,y=100,width=150,height=85)
        self.todayappoint_val=Label(self.root,text="TODAY APPOINTMENT",bg="red",fg="white",font=("times new roman", 10)).place(x=635,y=116,width=140,height=25)
        self.todayappoint_valint=Label(self.root,text=self.d,bg="red",fg="white",font=("times new roman",15)).place(x=700,y=140,width=30,height=25)
        self.todayappoint_brack1=Label(self.root,text="(",bg="red",fg="white",font=("times new roman",15)).place(x=701,y=140,width=10,height=25)
        self.todayappoint_brack2=Label(self.root,text=")",bg="red",fg="white",font=("times new roman",15)).place(x=719,y=140,width=10,height=25)


        frame_changepass=Frame(self.root,bg="white",borderwidth=1,relief=SOLID)
        frame_changepass.place(x=480,y=230,height=310,width=320)
        self.title_changepass=Label(self.root,text="Change password",font=("times new roman" ,10,"bold"),bd=0,bg="white").place(x=485,y=222)


        user=Label(frame_changepass,text="Username",font=("Goudy old style",15,"bold"),fg="black",bg="white",bd=0).place(x=18,y=36)
        self.txt_user=Entry(frame_changepass,font=("times new roman",15),bg="lightgrey",borderwidth=3,relief=RIDGE)
        self.txt_user.place(x=135,y=36,width=150, height=30)

        password=Label(frame_changepass,text="Old Password",font=("Goudy old style",15,"bold"),bd=0,fg="black",bg="white").place(x=12,y=92)
        self.txt_pass=Entry(frame_changepass,font=("times new roman",15),bg="lightgrey",borderwidth=3,relief=RIDGE)
        self.txt_pass.place(x=140,y=90,width=150, height=30)

        newpassword=Label(frame_changepass,text="New Password",font=("Goudy old style",15,"bold"),bd=0,fg="black",bg="white").place(x=12,y=150)
        self.txt_newpass=Entry(frame_changepass,font=("times new roman",15),bg="lightgrey",borderwidth=3,relief=RIDGE)
        self.txt_newpass.place(x=145,y=140,width=154, height=30)

        bttn_change=Button(frame_changepass,text="change password",font=("Goudy old style",15,"bold"),command=self.changepass,borderwidth=10,relief=RIDGE,bd=0,fg="white",bg="blue",cursor="hand2").place(x=65,y=220,width=200)

    
    def logout(self):
        self.msgbox=messagebox.askquestion("warning","ARE YOU SURE",parent=self.root)
        if self.msgbox=='yes':
            self.root.destroy()
            import login

        else:
            messagebox.showinfo('Return','You will now return to the application screen',parent=self.root)

    def exit_home(self):
        self.root.destroy()


    
    def changepass(self):

        cur.execute("select * from login where username=%s and password=%s",(self.txt_user.get(),self.txt_pass.get()) )
        row=cur.fetchone()
        if self.txt_user.get()=="" or self.txt_pass.get()=="" or self.txt_newpass.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required", parent=self.root)

        elif row==None:
            messagebox.showerror("ERROR","INVALID USERNAME AND PASSWORD",parent=self.root)
            self.txt_user.delete(0, END)
            self.txt_pass.delete(0, END)
            self.txt_newpass.delete(0, END)

        else:
            cur.execute("update login SET password=%s where username=%s ",(self.txt_newpass.get(),self.txt_user.get()))
            messagebox.showinfo("information","your password is change")
            self.txt_user.delete(0, END)
            self.txt_pass.delete(0, END)
            self.txt_newpass.delete(0, END)
            conn.commit()


    def doctor(self):
        self.root.destroy()
        import doctor

    def patient(self):
        self.root.destroy()
        import patient

    def appointment(self):
        self.root.destroy()
        import appointment

    

        

        


conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
cur=conn.cursor()
root=Tk()
obj=homepage(root)
root.mainloop()