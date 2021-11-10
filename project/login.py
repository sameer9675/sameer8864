from tkinter import *
from tkinter import messagebox
import pymysql #pip install pymysql

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("login systenm")
        self.root.geometry("810x550+100+50")
        self.root.resizable(False,False)
        #BG image

        self.bg=PhotoImage(file="D:\programming\python\program\project\images\doctor4.png")
        self.bg_image=Label(self.root,image=self.bg)
        self.bg_image.place(x=0,y=0, relwidth=1, relheight=1)

        #login frame

        frame_login=Frame(self.root,bg="white")
        frame_login.place(x=100,y=100,height=400,width=440)

        title=Label(frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=120,y=30)
        info=Label(frame_login,text="Login Page for ADMIN",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=130,y=100)
        user=Label(frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=150)
        self.txt_user=Entry(frame_login,font=("times new roman",15),bg="lightgrey")
        self.txt_user.place(x=50,y=180,width=320, height=25)

        password=Label(frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=210)
        self.txt_pass=Entry(frame_login,font=("times new roman",15),bg="lightgrey",show="*")
        self.txt_pass.place(x=50,y=240,width=320, height=25)

        forget=Button(frame_login,text="forget password?",cursor="hand2",font=("times new roman",12),bd=0,fg="#d25d17",bg="white").place(x=50,y=270,height=25)

        log_button=Button(frame_login,text="LOG IN",command=self.login,cursor="hand2",font=("times new roman",16),fg="white",bg="#d25d17").place(x=160,y=300,width=140,height="30")

        patient=Button(self.root,text="PATIENT \n LOG IN",cursor="hand2",font=("times new roman",13),fg="white",bg="#d25d17").place(x=110,y=480,width=100,height="40")

        patient=Button(self.root,text="DOCTOR \n LOG IN",cursor="hand2",font=("times new roman",13),fg="white",bg="#d25d17").place(x=420,y=480,width=100,height="40")


        

    def login(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required", parent=self.root)

        else:
            try:
                
                cur.execute("select * from login where username=%s and password=%s",(self.txt_user.get(),self.txt_pass.get()))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("ERROR","INVALID USERNAME AND PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("success","WELCOME",parent=self.root)
                    self.root.destroy()
                    import home
                    

                    conn.close()

            except Exception as es:
                 messagebox.showerror("ERROR","ERROR DUE TO: {str(es)}",parent=self.root)

conn=pymysql.connect(host="localhost",user="root",password="sameer",database="hospital")
cur=conn.cursor()
root=Tk()
obj=login(root)
root.mainloop()

