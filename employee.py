from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

class Employee :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee management system")

        self.department=StringVar()
        self.name=StringVar()
        self.phone=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.address=StringVar()
        self.married=StringVar()
        self.dob=StringVar()
        self.doj=StringVar()
        self.idType=StringVar()
        self.idProof=StringVar()
        self.salary=StringVar()
        self.country=StringVar()
        self.searchBy =StringVar()
        self.searchText = StringVar()

        lbl_title = Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",
                          font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1330,height=50)
        
        # logo
        img_logo = Image.open('images/icon.jpg')
        img_logo = img_logo.resize((50,50))
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root,image=self.photo_logo)
        self.logo.place(x=170,y=0,width=50,height=50)

        #image frame
        img_frame = Frame(self.root,bd=2,relief='ridge',bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1st image
        img1 = Image.open('images/img1.png')
        img1 = img1.resize((440,160))
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=440,height=160)

        # 2nd image
        img2 = Image.open('images/img3.png')
        img2 = img2.resize((440,160))
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame,image=self.photo2)
        self.img_2.place(x=420,y=0,width=440,height=160)

        # 3rd image
        img3 = Image.open('images/img2.png')
        img3 = img3.resize((440,160))
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame,image=self.photo3)
        self.img_3.place(x=850,y=0,width=440,height=160)

        # main frame
        Main_frame=Frame(self.root,bd=2,relief='ridge',bg='white')
        Main_frame.place(x=0,y=200,width=1350,height=560)

        # upper frame
        upper_frame = LabelFrame(Main_frame,bd=2,relief="ridge",bg='white',
                                 text='Employee Management Information',
                                 font=('arial',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1240,height=220)

        #label for combo field for dep
        lbl_dep = Label(upper_frame,text="Department",font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,sticky=W)

        lbl_combo = ttk.Combobox(upper_frame,textvariable=self.department,font=('arial',11,'bold'),width=20,state='readonly')
        lbl_combo['value'] =("Select Department","Software Engineer","Manager","Team Lead","HR")
        lbl_combo.current(0)
        lbl_combo.grid(row=0,column=1,padx=2,sticky=W)
        
        #label for entry field for name
        lbl_name = Label(upper_frame,text="Name",font=('arial',11,'bold'),bg='white')
        lbl_name.grid(row=0,column=2,sticky=W)

        entry_name = Entry(upper_frame,textvariable=self.name,font=('arial',11,'bold'),width=20)
        entry_name.grid(row=0,column=3,padx=2,sticky=W)

        #label for entry field for phone
        lbl_phone = Label(upper_frame,text="Phone",font=('arial',11,'bold'),bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W)

        entry_phone = Entry(upper_frame,textvariable=self.phone,font=('arial',11,'bold'),width=20)
        entry_phone.grid(row=0,column=5,padx=2,sticky=W)

        #label for entry field for email
        lbl_email = Label(upper_frame,text="Email",font=('arial',11,'bold'),bg='white')
        lbl_email.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        entry_email = Entry(upper_frame,textvariable=self.email,font=('arial',11,'bold'),width=20)
        entry_email.grid(row=1,column=1,padx=2,pady=7,sticky=W)

         #label for entry field for address
        lbl_address = Label(upper_frame,text="Address",font=('arial',11,'bold'),bg='white')
        lbl_address.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        entry_address = Entry(upper_frame,textvariable=self.address,font=('arial',11,'bold'),width=20)
        entry_address.grid(row=1,column=3,padx=2,pady=7,sticky=W)

         #label for entry field for country
        lbl_country = Label(upper_frame,text="Country",font=('arial',11,'bold'),bg='white')
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        entry_country = Entry(upper_frame,textvariable=self.country,font=('arial',11,'bold'),width=20)
        entry_country.grid(row=1,column=5,padx=2,pady=7,sticky=W)

         #label for entry field for DOB
        lbl_DOB = Label(upper_frame,text="DOB",font=('arial',11,'bold'),bg='white')
        lbl_DOB.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        entry_DOB = Entry(upper_frame,textvariable=self.dob,font=('arial',11,'bold'),width=20)
        entry_DOB.grid(row=2,column=1,padx=2,pady=7,sticky=W)

         #label for entry field for DOJ
        lbl_DOJ = Label(upper_frame,text="DOJ",font=('arial',11,'bold'),bg='white')
        lbl_DOJ.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        entry_DOJ= Entry(upper_frame,textvariable=self.doj,font=('arial',11,'bold'),width=20)
        entry_DOJ.grid(row=2,column=3,padx=2,pady=7,sticky=W)

         #label for entry field for Salary (CTC)
        lbl_CTC = Label(upper_frame,text="CTC",font=('arial',11,'bold'),bg='white')
        lbl_CTC.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        entry_CTC= Entry(upper_frame,textvariable=self.salary,font=('arial',11,'bold'),width=20)
        entry_CTC.grid(row=2,column=5,padx=2,pady=7,sticky=W)


        
        #label for combo field for Married Status
        lbl_Married_status = Label(upper_frame,text="Married Status",font=('arial',11,'bold'),bg='white')
        lbl_Married_status.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        lbl_combo = ttk.Combobox(upper_frame,textvariable=self.married,font=('arial',11,'bold'),width=20,state='readonly')
        lbl_combo['value'] =("Married","Un Married")
        lbl_combo.current(0)
        lbl_combo.grid(row=3,column=1,padx=2,pady=7,sticky=W)

         #label for combo field for gender
        lbl_gender = Label(upper_frame,text="Gender",font=('arial',11,'bold'),bg='white')
        lbl_gender.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        lbl_combo = ttk.Combobox(upper_frame,textvariable=self.gender,font=('arial',11,'bold'),width=20,state='readonly')
        lbl_combo['value'] =("Male","Female")
        lbl_combo.current(0)
        lbl_combo.grid(row=3,column=3,padx=2,pady=7,sticky=W)

         #label for combo field for id_proof
        lbl_id_type = ttk.Combobox(upper_frame,textvariable=self.idType,font=('arial',11,'bold'),width=20,state='readonly')
        lbl_id_type['value'] =("Aadhar No.","PAN No.")
        lbl_id_type.current(0)
        lbl_id_type.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        entry_id_proof =Entry(upper_frame,textvariable=self.idProof,font=('arial',11,'bold'),width=20)
        entry_id_proof.grid(row=4,column=1,padx=2,pady=7,sticky=W)


        #Add Employee Image
        employeeImg= Image.open('images/employeeImage.png')
        employeeImg= employeeImg.resize((220,190))
        self.employeePhoto = ImageTk.PhotoImage(employeeImg)

        self.imgEmp = Label(upper_frame,image=self.employeePhoto)
        self.imgEmp.place(x=870,y=0,width=220,height=190)


        #Add four button Update, Save, Delete, Reset

        button_frame = Frame(upper_frame,bd=2,relief='ridge',bg='white')
        button_frame.place(x=1100,y=4,width=125,height=190)

        btn_save = Button(button_frame,text="Save",command=self.AddData,font=('arial',12,'bold'),fg='white',bg='blue',width=12)
        btn_save.grid(row=0,column=0,pady=7,sticky=W)

        btn_update = Button(button_frame,command=self.updateData,text="Update",font=('arial',12,'bold'),fg='white',bg='blue',width=12)
        btn_update.grid(row=1,column=0,pady=7,sticky=W)

        btn_delete = Button(button_frame,text="Delete",command=self.deleteData,font=('arial',12,'bold'),fg='white',bg='blue',width=12)
        btn_delete.grid(row=2,column=0,pady=7,sticky=W)

        btn_reset = Button(button_frame,text="Reset",command=self.resetEmployeeInfo,font=('arial',12,'bold'),fg='white',bg='blue',width=12)
        btn_reset.grid(row=3,column=0,pady=7,sticky=W)

        # down frame
        down_frame = LabelFrame(Main_frame,bd=2,relief="ridge",bg='white',
                                 text='Employee Management Information Table',
                                 font=('arial',11,'bold'),fg='violet')
        down_frame.place(x=10,y=230,width=1240,height=240)

        #searh Frame
        search_frame= LabelFrame(down_frame,text="Search Employee Information",relief='ridge',bd=2,font=('arial',11,'bold'),fg='violet', bg='white')
        search_frame.place(x=0,y=0,width=1220,height=55)

        search_lbl = Label(search_frame,text="Search By:",font=('arial',12,'bold'),bg='red',fg='white')
        search_lbl.grid(row=0,column=0,padx=4,pady=2,sticky=W)

        lbl_combo = ttk.Combobox(search_frame,textvariable=self.searchBy,font=('arial',11,'bold'),width=20,state='readonly')
        lbl_combo['value'] =("Select option","IdProof","Phone")
        lbl_combo.current(0)
        lbl_combo.grid(row=0,column=1,padx=4,pady=2,sticky=W)

        search_entry = Entry(search_frame,textvariable=self.searchText,bg='white',font=('arial',12,'bold'),bd=2,width=30)
        search_entry.grid(row=0,column=2,padx=4,pady=2,sticky=W)

        btn_search = Button(search_frame,command=self.searchEmployeeInfo,text="Search",font=('arial',12,'bold'),fg='white',bg='blue',width=12)
        btn_search.grid(row=0,column=3,padx=4,pady=2,sticky=W)

        btn_showAll = Button(search_frame,text="Show All",command=self.ShowAll,font=('arial',12,'bold'),fg='white',bg='blue',width=12)
        btn_showAll.grid(row=0,column=4,padx=4,pady=2,sticky=W)

        #searh Frame
        table_frame= Frame(down_frame,relief='ridge',bd=2, bg='white')
        table_frame.place(x=0,y=55,width=1220,height=180)

        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)
    
        self.employee_table = ttk.Treeview(table_frame,column=("dep","name","phone",'email',"dob",'doj','salary','idProof','idType','married','gender','address','country',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idProof',text='ID Proof')
        self.employee_table.heading('idType',text='ID Type')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')
        
        self.employee_table['show'] ='headings'
        self.employee_table.pack(fill=BOTH,expand=1)

        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('address',width=100)

        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idType',width=100)
        self.employee_table.column('idProof',width=100)
        self.employee_table.column('salary',width=100)
        self.employee_table.column('country',width=100)

        self.employee_table.bind("<ButtonRelease>",self.setDataIntoUpperFrame)
        self.ShowAll()


        ########### function declaration for data ##########################
    def AddData(self):
        if(self.idProof.get() == "" or self.phone.get() == ''):
            messagebox.showerror("Error","All fields are required", parent= self.root)
        conn = mysql.connector.connect(host="localhost",user="root",password="root",database="employeedata")
        cursor = conn.cursor()
        try:
            cursor.execute("insert into employee values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.department.get(),
                self.name.get(),
                self.phone.get(),
                self.email.get(),
                self.dob.get(),
                self.doj.get(),
                self.salary.get(),
                self.idProof.get(),
                self.idType.get(),
                self.married.get(),
                self.gender.get(),
                self.address.get(),
                self.country.get()
            ))
            conn.commit()
            messagebox.showinfo("Success","Data Added Successfully",parent = self.root)
            self.resetEmployeeInfo()
            self.ShowAll()
        except Exception as ex:
            messagebox.showinfo("Error",str(ex),parent = self.root)
        conn.close()

    def ShowAll(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="root",database="employeedata")
        cursor = conn.cursor()
        try:
            cursor.execute("select * from employee")
            data = cursor.fetchall()
            if(len(data) != 0):
                self.employee_table.delete(*self.employee_table.get_children())
                for i in data:
                    self.employee_table.insert("",END,values=i)
        except Exception as ex:
            messagebox.showerror("Error",str(ex),parent= self.root)
        conn.close()

    def setDataIntoUpperFrame(self,event = ""):
        curr_row =self.employee_table.focus()
        data = self.employee_table.item(curr_row)['values']
        self.department.set(data[0])
        self.name.set(data[1])
        self.phone.set(data[2])
        self.email.set(data[3])
        self.dob.set(data[4])
        self.doj.set(data[5])
        self.salary.set(data[6])
        self.idProof.set(data[7])
        self.idType.set(data[8])
        self.married.set(data[9])
        self.gender.set(data[10])
        self.address.set(data[11])
        self.country.set(data[12])

    def resetEmployeeInfo(self):
        self.department.set("Select Department")
        self.name.set("")
        self.phone.set("")
        self.email.set("")
        self.dob.set("")
        self.doj.set("")
        self.salary.set("")
        self.idProof.set("")
        self.idType.set("Aadhar No.")
        self.married.set("Married")
        self.gender.set("Male")
        self.address.set("")
        self.country.set("")

    def deleteData(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="employeedata")
        cursor= conn.cursor()
    
        try:
            cursor.execute("delete from employee where IdProof= %s",(self.idProof.get(),))
            conn.commit()
            messagebox.showinfo("Success","Data deleted Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",str(ex),parent = self.root)
        conn.close()

    def searchEmployeeInfo(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="employeedata")
        cursor = conn.cursor()
        try:
            cursor.execute("select * from employee where "+ str(self.searchBy.get()) + " LIKE %s",(self.searchText.get(),))
            data= cursor.fetchall()
            print(data,self.searchBy.get(),self.searchText.get())
            
            self.employee_table.delete(*self.employee_table.get_children())
            if(len(data) != 0):
                for i in data:
                    self.employee_table.insert("",END,values=i)
            conn.commit()
        except Exception as ex:
            messagebox.showerror("Error",str(ex),parent= self.root)
        conn.close()
    def updateData(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="employeedata")
        cursor = conn.cursor()
        try:
            cursor.execute("update employee set Department=%s,Name=%s,Phone=%s,Email=%s,DOB=%s,DOJ=%s,Salary=%s,IdProof=%s,IdType=%s,Married=%s,Gender=%s,Address=%s,Country=%s ",(
                self.department.get(),
                self.name.get(),
                self.phone.get(),
                self.email.get(),
                self.dob.get(),
                self.doj.get(),
                self.salary.get(),
                self.idProof.get(),
                self.idType.get(),
                self.married.get(),
                self.gender.get(),
                self.address.get(),
                self.country.get()
            ))
            conn.commit()
            self.resetEmployeeInfo()
            self.ShowAll()
        except Exception as ex:
            messagebox.showerror("Error",str(ex),parent= self.root)
        conn.close()


if __name__ == "__main__" :
    root = Tk()
    obj = Employee(root)
    root.mainloop()