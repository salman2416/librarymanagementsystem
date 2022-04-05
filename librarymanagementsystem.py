


        # # from tkinter import*#######################
from tkinter import*
from tkinter import ttk
class Student():

     def __init__(self,root):
        self.root=root

        self.root.title("Library management system")
        self.root.geometry("1000x700+0+0")

        title=Label(self.root,text="Student management system",font=("times new roman",50,"bold"),bd=9,relief=GROOVE,bg="orange",fg="white")
        title.pack(side=TOP,fill=X)

        ################## Mnage Frame ###############
        Manage_frame= Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_frame.place(x=20,y=100,width=450,height=585)

        m_title=Label(Manage_frame,text="Manage Student",bg="yellow",fg="black",font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_frame,text="Roll No.",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll=Entry(Manage_frame,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_frame,text="Name",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(Manage_frame,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_frame,text="Email",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_email=Entry(Manage_frame,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(Manage_frame,text="Gender",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        combo_gender=ttk.Combobox(Manage_frame,font=("times new roman",10,"bold"),state="readonly")
        combo_gender['values'] = ('Male','Female','Other')
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_Contact=Label(Manage_frame,text="Contact No.",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_Contact=Entry(Manage_frame,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_Dob=Label(Manage_frame,text="Date Of Birth",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_Dob=Entry(Manage_frame,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Address=Label(Manage_frame,text="Address",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.txt_Address=Text(Manage_frame,width=30,height=3,font=("times new roman",10,"bold"))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=10,sticky="w")


        ############# Btn Frame ######################
        Btn_frame= Frame(Manage_frame,bd=3,relief=RIDGE,bg="black")
        Btn_frame.place(x=15,y=525,width=420)

        Add_btn=Button(Btn_frame,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        Update_btn=Button(Btn_frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        Delete_btn=Button(Btn_frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        Clear_btn=Button(Btn_frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)


        ################## Details Frame ###############
        Detail_frame= Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Detail_frame.place(x=500,y=100,width=600,height=585)

        lbl_search=Label(Detail_frame,text="Search By",bg="blue",fg="white",font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,pady=5,padx=5,sticky="w")

        combo_search=ttk.Combobox(Detail_frame,font=("times new roman",10,"bold"),width=8,state="readonly")
        combo_search['values'] = ('Roll No.','Name','Contact')
        combo_search.grid(row=0,column=1,pady=5,padx=5,sticky="w")

        txt_search=Entry(Detail_frame,font=("times new roman",10,"bold"),width=15,bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=5,padx=5,sticky="w")

        Search_btn=Button(Detail_frame,text="Search",width=8).grid(row=0,column=3,padx=5,pady=5)
        Showall_btn=Button(Detail_frame,text="Show All",width=10).grid(row=0,column=4,padx=5,pady=5)




        ################## Table Frame ###############
        Table_frame= Frame(Detail_frame,bd=4,relief=RIDGE,bg="white")
        Table_frame.place(x=30,y=50,width=450,height=501)

        scroll_x= Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y= Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table =ttk.Treeview(Table_frame,column=('roll','name','gmail','gender','contact','dob','Address'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading('roll',text="Roll no.")
        self.student_table.heading('name',text="Name")
        self.student_table.heading('gmail',text="Email")
        self.student_table.heading('gender',text="Gender")
        self.student_table.heading('contact',text="Contact")
        self.student_table.heading('dob',text="DOB")
        self.student_table.heading('Address',text="Address")


        self.student_table['show']='headings'
        self.student_table.column('roll',width=50)
        self.student_table.column('name',width=50)
        self.student_table.column('gmail',width=50)
        self.student_table.column('gender',width=50)
        self.student_table.column('contact',width=50)
        self.student_table.column('dob',width=50)
        self.student_table.column('Address',width=50)

        self.student_table.pack(fill=BOTH,expand=1)





if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()

