from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
                    def __init__(self,root):
                                        self.root = root
                                        self.root.title("Library Management System")
                                        self.root.geometry("1550x800+0+0")
                                        
                                        # =========================================variable =================================================
                                        self.member_var=StringVar()
                                        self.prn_var=StringVar()
                                        self.id_var=StringVar()
                                        self.firstname_var=StringVar()
                                        self.lastname_var=StringVar()
                                        self.address1_var=StringVar()
                                        self.address2_var=StringVar()
                                        self.postid_var=StringVar()
                                        self.mobile_var=StringVar()
                                        self.bookid_var=StringVar()
                                        self.booktitle_var=StringVar()
                                        self.auther_var=StringVar()
                                        self.databorrowed_var=StringVar()
                                        self.datedue_var=StringVar()
                                        self.daysonbook_var=StringVar()
                                        self.latereturnfine_var=StringVar()
                                        self.dateoverdue_var=StringVar()
                                        self.finallprice_var=StringVar()

                                        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
                                        lbltitle.pack(side=TOP,fill=X)
    
                                        fram=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
                                        fram.place(x=0,y=130,width=1530,height=400) 
                                        
                                        # =======================================DataFramLeft======================================
                                        DataFrameLeft=LabelFrame(fram,text="Library Membership Information",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold")) 
                                        DataFrameLeft.place(x=0,y=5,width=860,height=350)  
                                        
                                        lblMember=Label(DataFrameLeft,font=("arial",12,"bold"),text="Member Type",padx=2,pady=6,bg="powder blue")
                                        lblMember.grid(row=0,column=0,sticky=W)
                                        
                                        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=30,state="readonly")
                                        comMember["values"]=("Admin Staff","Student","Lecturer")
                                        comMember.current(0)
                                        comMember.grid(row=0,column=1)
                                        
                                        lblPRN_No=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No:",padx=2,bg="powder blue")
                                        lblPRN_No.grid(row=1,column=0,sticky=W)
                                        txtPRN_No=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
                                        txtPRN_No.grid(row=1,column=1)
                                        
                                        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,bg="powder blue")
                                        lblTitle.grid(row=2,column=0,sticky=W)
                                        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
                                        txtTitle.grid(row=2,column=1)
                                        
                                        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName:",padx=2,bg="powder blue")
                                        lblFirstName.grid(row=3,column=0,sticky=W)
                                        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
                                        txtFirstName.grid(row=3,column=1)
                                        
                                        lblLastname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lastname:",padx=2,bg="powder blue")
                                        lblLastname.grid(row=4,column=0,sticky=W)
                                        txtLastname=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
                                        txtLastname.grid(row=4,column=1)
                                        
                                        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1:",padx=2,bg="powder blue")
                                        lblAddress1.grid(row=5,column=0,sticky=W)
                                        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
                                        txtAddress1.grid(row=5,column=1)
                                        
                                        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2:",padx=2,bg="powder blue")
                                        lblAddress2.grid(row=6,column=0,sticky=W)
                                        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
                                        txtAddress2.grid(row=6,column=1)
                                        
                                        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post ID:",padx=2,bg="powder blue")
                                        lblPostCode.grid(row=7,column=0,sticky=W)
                                        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postid_var,width=29)
                                        txtPostCode.grid(row=7,column=1)
                                        
                                        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile:",padx=2,bg="powder blue")
                                        lblMobile.grid(row=8,column=0,sticky=W)
                                        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
                                        txtMobile.grid(row=8,column=1)
                                        
                                        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book ID:",padx=2,bg="powder blue")
                                        lblBookId.grid(row=0,column=2,sticky=W)
                                        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
                                        txtBookId.grid(row=0,column=3)
                                        
                                        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,bg="powder blue")
                                        lblBookTitle.grid(row=1,column=2,sticky=W)
                                        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
                                        txtBookTitle.grid(row=1,column=3)
                                        
                                        lblAutherName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name:",padx=2,bg="powder blue")
                                        lblAutherName.grid(row=2,column=2,sticky=W)
                                        txtAutherName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.auther_var,width=29)
                                        txtAutherName.grid(row=2,column=3)
                                        
                                        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Data Borrowed:",padx=2,bg="powder blue")
                                        lblDateBorrowed.grid(row=3,column=2,sticky=W)
                                        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.databorrowed_var,width=29)
                                        txtDateBorrowed.grid(row=3,column=3)
                                        
                                        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,bg="powder blue")
                                        lblDateDue.grid(row=4,column=2,sticky=W)
                                        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
                                        txtDateDue.grid(row=4,column=3)
                                        
                                        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Books:",padx=2,bg="powder blue")
                                        lblDaysOnBook.grid(row=5,column=2,sticky=W)
                                        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook_var,width=29)
                                        txtDaysOnBook.grid(row=5,column=3)
                                        
                                        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,bg="powder blue")
                                        lblLateReturnFine.grid(row=6,column=2,sticky=W)
                                        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.latereturnfine_var,width=29)
                                        txtLateReturnFine.grid(row=6,column=3)
                                        
                                        lblDateOverDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,bg="powder blue")
                                        lblDateOverDue.grid(row=7,column=2,sticky=W)
                                        txtDateOverDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue_var,width=29)
                                        txtDateOverDue.grid(row=7,column=3)
                                        
                                        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Finall Price:",padx=2,bg="powder blue")
                                        lblActualPrice.grid(row=8,column=2,sticky=W)
                                        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finallprice_var,width=29)
                                        txtActualPrice.grid(row=8,column=3)
                                        
                                        for widget in DataFrameLeft.winfo_children():
                                           widget.grid_configure(padx=4, pady=4)
                                        # ======================================= DataFram Right =================================== 
                                        self.DataFrameRight=LabelFrame(fram,text="Book Details",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",12,"bold")) 
                                        self.DataFrameRight.place(x=870,y=5,width=580,height=350) 
                                        
                                        self.textBox=Text(self.DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
                                        self.textBox.grid(row=0,column=2)
                                        
                                        self.listScrollbar=Scrollbar(self.DataFrameRight)
                                        self.listScrollbar.grid(row=0,column=1,sticky="ns")
                                        
                                        self.listBooks = ["Computer Fundamentals","Programming in C","Data Structures Using C","Database System Concepts",
                                        "Operating System Concepts","Computer Networks","Object Oriented Programming with C++","Java Programming","Head First Java",
                                        "Python Crash Course","Software Engineering","Web Technologies","HTML and CSS","JavaScript","Computer Graphics",
                                        ]
                                        self.listBox=Listbox(self.DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
                                        self.listBox.bind("<<ListboxSelect>>",self.SelectBook)
                                        self.listBox.grid(row=0,column=0,padx=4)
                                        self.listScrollbar.config(command=self.listBox.yview)
                                        for item in self.listBooks:
                                                            self.listBox.insert(END,item)
                                        # =========================================Button Frame=====================================
                                        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
                                        Framebutton.place(x=0,y=530,width=1530,height=70)
                                        
                                        btnAddData=Button(Framebutton,text="Add Data",command=self.add_data,font=("arial",12,"bold"),width=23,bg="blue",fg="White")
                                        btnAddData.grid(row=0,column=0)
                                        
                                        btnAddData=Button(Framebutton,text="Show Data",command=self.showData,font=("arial",12,"bold"),width=23,bg="blue",fg="White")
                                        btnAddData.grid(row=0,column=1)
                                        
                                        btnAddData=Button(Framebutton,text="Update",command=self.update,font=("arial",12,"bold"),width=23,bg="blue",fg="White")
                                        btnAddData.grid(row=0,column=2)
                                        
                                        btnAddData=Button(Framebutton,text="Delete",command=self.delete,font=("arial",12,"bold"),width=23,bg="blue",fg="White")
                                        btnAddData.grid(row=0,column=3)
                                        
                                        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=23,bg="blue",fg="White")
                                        btnAddData.grid(row=0,column=4)
                                        
                                        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=23,bg="blue",fg="White")
                                        btnAddData.grid(row=0,column=5)
                                        # =========================================Information Frame===============================
                                        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
                                        FrameDetails.place(x=0,y=600,width=1530,height=195)   
                                        
                                        Table_frame=Frame(FrameDetails,bd=12,relief=RIDGE,padx=20,bg="powder blue")
                                        Table_frame.place(x=0,y=2,width=1460,height=190)
                                        
                                        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
                                        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
                                        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","title","firstname","Lastname",
                                                                                          "address1","address2","postid","mobile","bookid","booktitle",
                                                                                          "auther","databorrowed","datedue","daysonbooks","latereturnfine",
                                                                                          "dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
                                        xscroll.pack(side=BOTTOM,fill=X)
                                        yscroll.pack(side=RIGHT,fill=Y)
                                        
                                        xscroll.config(command=self.library_table.xview)
                                        yscroll.config(command=self.library_table.yview)

                                        self.library_table.heading("membertype",text="Member Type")              
                                        self.library_table.heading("prnno",text="PRN NO")              
                                        self.library_table.heading("title",text="Title")              
                                        self.library_table.heading("firstname",text="First Name")              
                                        self.library_table.heading("Lastname",text="Last Name")              
                                        self.library_table.heading("address1",text="Address1")              
                                        self.library_table.heading("address2",text="Address2")              
                                        self.library_table.heading("postid",text="Post ID")              
                                        self.library_table.heading("mobile",text="Mobile")              
                                        self.library_table.heading("bookid",text="Book ID")              
                                        self.library_table.heading("booktitle",text="Booktitle")              
                                        self.library_table.heading("auther",text="Auther")              
                                        self.library_table.heading("databorrowed",text="Data of Borrowed") 
                                        self.library_table.heading("datedue",text="Date Due") 
                                        self.library_table.heading("daysonbooks",text="Days On Book") 
                                        self.library_table.heading("latereturnfine",text="Late Return Fine") 
                                        self.library_table.heading("dateoverdue",text="Date Over Due") 
                                        self.library_table.heading("finalprice",text="Final Price") 
                                        
                                        self.library_table["show"]="headings"
                                        self.library_table.pack(fill=BOTH,expand=1) 
                                        
                                        self.library_table.column("membertype",width=100) 
                                        self.library_table.column("prnno",width=100) 
                                        self.library_table.column("title",width=100) 
                                        self.library_table.column("firstname",width=100) 
                                        self.library_table.column("Lastname",width=100) 
                                        self.library_table.column("address1",width=100) 
                                        self.library_table.column("address2",width=100) 
                                        self.library_table.column("postid",width=100) 
                                        self.library_table.column("mobile",width=100) 
                                        self.library_table.column("bookid",width=100) 
                                        self.library_table.column("booktitle",width=100) 
                                        self.library_table.column("auther",width=100) 
                                        self.library_table.column("databorrowed",width=100) 
                                        self.library_table.column("datedue",width=100) 
                                        self.library_table.column("daysonbooks",width=100) 
                                        self.library_table.column("latereturnfine",width=100) 
                                        self.library_table.column("dateoverdue",width=100) 
                                        self.library_table.column("finalprice",width=100)
                                        
                                        self.fatch_data()
                                        self.library_table.bind("<ButtonRelease-1>",self.get_cursor) 
                                        
                    def SelectBook(self,even=""):
                                        value=str(self.listBox.get(self.listBox.curselection()))
                                        x=value
                                        if (x=="Computer Fundamentals"):
                                                            self.bookid_var.set("BHJK2345")
                                                            self.booktitle_var.set("Computer Fundamentals")
                                                            self.auther_var.set("Charles Babbage")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.300")
                                        elif (x=="Programming in C"):
                                                            self.bookid_var.set("BHDG2445")
                                                            self.booktitle_var.set("Programming in C")
                                                            self.auther_var.set("Dennis Ritchie")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.400")
                                        elif (x=="Data Structures Using C"):
                                                            self.bookid_var.set("NJMK3445")
                                                            self.booktitle_var.set("Data Structures Using C")
                                                            self.auther_var.set("Niklaus Wirth")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.500")
                                        elif (x=="Database System Concepts"):
                                                            self.bookid_var.set("NHJK2345")
                                                            self.booktitle_var.set("Database System Concepts")
                                                            self.auther_var.set("S. Sudarshan")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.600")
                                        elif (x=="Operating System Concepts"):
                                                            self.bookid_var.set("KLJK2565")
                                                            self.booktitle_var.set("Operating System Concepts")
                                                            self.auther_var.set("Peter Baer Galvin")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.700")
                                        elif (x=="Computer Networks"):
                                                            self.bookid_var.set("NFUK2345")
                                                            self.booktitle_var.set("Computer Networks")
                                                            self.auther_var.set("Andrew S. Tanenbaum")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.800")
                                        elif (x=="Object Oriented Programming with C++"):
                                                            self.bookid_var.set("NDKL9845")
                                                            self.booktitle_var.set("Object Oriented Programming with C++")
                                                            self.auther_var.set("Bjarne Stroustrup")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.900")
                                        elif (x=="Java Programming"):
                                                            self.bookid_var.set("BHNF9845")
                                                            self.booktitle_var.set("Java Programming")
                                                            self.auther_var.set("James Gosling")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.1000")
                                        elif (x=="Head First Java"):
                                                            self.bookid_var.set("BHKN2985")
                                                            self.booktitle_var.set("Head First Java")
                                                            self.auther_var.set("Kathy Sierra")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.1200")
                                        elif (x=="Python Crash Course"):
                                                            self.bookid_var.set("BKLM2655")
                                                            self.booktitle_var.set("Python Crash Course")
                                                            self.auther_var.set("Eric Matthes")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.1300")
                                        elif (x=="Software Engineering"):
                                                            self.bookid_var.set("BHMK2398")
                                                            self.booktitle_var.set("Software Engineering")
                                                            self.auther_var.set("Winston W. Royce")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.1400")
                                        elif (x=="Web Technologies"):
                                                            self.bookid_var.set("BLUK2045")
                                                            self.booktitle_var.set("Web Technologies")
                                                            self.auther_var.set("Tim Berners-Lee")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.1500")
                                        elif (x=="HTML and CSS "):
                                                            self.bookid_var.set("BHLI2395")
                                                            self.booktitle_var.set("HTML and CSS ")
                                                            self.auther_var.set("Tim Berners-Lee")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.1600")
                                        elif (x=="JavaScript"):
                                                            self.bookid_var.set("BHLE60045")
                                                            self.booktitle_var.set("JavaScript")
                                                            self.auther_var.set("Brendan Eich")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.1700")
                                        elif (x=="Computer Graphics"):
                                                            self.bookid_var.set("BHMJ2345")
                                                            self.booktitle_var.set("Computer Graphics")
                                                            self.auther_var.set("Ivan Sutherland")
                                                                                
                                                            d1=datetime.date.today()
                                                            d2=datetime.timedelta(days=15)
                                                            d3=d1+d2
                                                            self.databorrowed_var.set(d1)
                                                            self.datedue_var.set(d3)
                                                            self.daysonbook_var.set(15)
                                                            self.latereturnfine_var.set("Rs.50")
                                                            self.dateoverdue_var.set("NO")
                                                            self.finallprice_var.set("Rs.1800")
                                                                                                    
                    def add_data(self):
                                        con=mysql.connector.connect(host="localhost",username="root",password="Brijesh@12",database="Mydata")                   
                                        my_cursor=con.cursor()
                                        my_cursor.execute("insert into library value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                               self.member_var.get(),
                                                                                                                                               self.prn_var.get(),
                                                                                                                                               self.id_var.get(),
                                                                                                                                               self.firstname_var.get(),
                                                                                                                                               self.lastname_var.get(),
                                                                                                                                               self.address1_var.get(),
                                                                                                                                               self.address2_var.get(),
                                                                                                                                               self.postid_var.get(),
                                                                                                                                               self.mobile_var.get(),
                                                                                                                                               self.bookid_var.get(),
                                                                                                                                               self.booktitle_var.get(),
                                                                                                                                               self.auther_var.get(),
                                                                                                                                               self.databorrowed_var.get(),
                                                                                                                                               self.datedue_var.get(),
                                                                                                                                               self.daysonbook_var.get(),
                                                                                                                                               self.latereturnfine_var.get(),
                                                                                                                                               self.dateoverdue_var.get(),
                                                                                                                                               self.finallprice_var.get()
                                                                                                                                            ))
                                        con.commit()
                                        self.fatch_data()
                                        con.close()
                                        messagebox.showinfo("Success","Member Has been inserted successfully")
                    
                    def update(self):
                                        con=mysql.connector.connect(host="localhost",username="root",password="Brijesh@12",database="Mydata")                   
                                        my_cursor=con.cursor()
                                        my_cursor.execute("update library set Member=%s,ID=%s,Firstname=%s,Lastname=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,Bookid=%s,Booktitle=%s,Auther=%s,Databorrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s WHERE PRN_NO=%s",(
                                                                                                                                                                self.member_var.get(),
                                                                                                                                                                self.id_var.get(),
                                                                                                                                                                self.firstname_var.get(),
                                                                                                                                                                self.lastname_var.get(),
                                                                                                                                                                self.address1_var.get(),
                                                                                                                                                                self.address2_var.get(),
                                                                                                                                                                self.postid_var.get(),
                                                                                                                                                                self.mobile_var.get(),
                                                                                                                                                                self.bookid_var.get(),
                                                                                                                                                                self.booktitle_var.get(),
                                                                                                                                                                self.auther_var.get(),
                                                                                                                                                                self.databorrowed_var.get(),
                                                                                                                                                                self.datedue_var.get(),
                                                                                                                                                                self.daysonbook_var.get(),
                                                                                                                                                                self.latereturnfine_var.get(),
                                                                                                                                                                self.dateoverdue_var.get(),
                                                                                                                                                                self.finallprice_var.get(),
                                                                                                                                                                self.prn_var.get()
                                                                                                                                            ))
                                         
                                        con.commit()
                                        self.fatch_data()
                                        con.close()
                                        messagebox.showinfo("Success","Member has been Updated")                  
                    def fatch_data(self):
                                        con=mysql.connector.connect(host="localhost",username="root",password="Brijesh@12",database="Mydata")                   
                                        my_cursor=con.cursor()
                                        my_cursor.execute("select * from library")
                                        rows=my_cursor.fetchall()
                                        
                                        if len(rows)!=0:
                                                            self.library_table.delete(*self.library_table.get_children())
                                                            for i in rows:
                                                                                self.library_table.insert("",END,values=i)
                                                            con.commit()
                                        con.close() 
                                                           
                    def get_cursor(self,event=""):
                                        cursor_row=self.library_table.focus()
                                        content=self.library_table.item(cursor_row)
                                        row=content['values']
                                        self.member_var.set(row[0]),                  
                                        self.prn_var.set(row[1]),                
                                        self.id_var.set(row[2]),                  
                                        self.firstname_var.set(row[3]),                  
                                        self.lastname_var.set(row[4]),                  
                                        self.address1_var.set(row[5]),                  
                                        self.address2_var.set(row[6]),                  
                                        self.postid_var.set(row[7]),                  
                                        self.mobile_var.set(row[8]),                  
                                        self.bookid_var.set(row[9]),                  
                                        self.booktitle_var.set(row[10]),                  
                                        self.auther_var.set(row[11]),                  
                                        self.databorrowed_var.set(row[12]),                  
                                        self.datedue_var.set(row[13]),                  
                                        self.daysonbook_var.set(row[14]),                  
                                        self.latereturnfine_var.set(row[15]),                  
                                        self.dateoverdue_var.set(row[16]),                  
                                        self.finallprice_var.set(row[17])                  
                     
                    def showData(self):
                        self.textBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
                        self.textBox.insert(END,"PRN NO:\t\t"+ self.prn_var.get() + "\n")
                        self.textBox.insert(END,"ID NO:\t\t"+ self.id_var.get() + "\n")
                        self.textBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")
                        self.textBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")
                        self.textBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
                        self.textBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
                        self.textBox.insert(END,"Post Id:\t\t"+ self.postid_var.get() + "\n")
                        self.textBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
                        self.textBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
                        self.textBox.insert(END,"Book Title\t\t"+ self.booktitle_var.get() + "\n")
                        self.textBox.insert(END,"Auther:\t\t"+ self.auther_var.get() + "\n")
                        self.textBox.insert(END,"DataBorrowed:\t\t"+ self.databorrowed_var.get() + "\n")
                        self.textBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
                        self.textBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get() + "\n")
                        self.textBox.insert(END,"LateReturnFine:\t\t"+ self.dateoverdue_var.get() + "\n")
                        self.textBox.insert(END,"DateOverDue\t\t"+ self.dateoverdue_var.get() + "\n")
                        self.textBox.insert(END,"FinallPrice:\t\t"+ self.finallprice_var.get() + "\n")
                    
                    def reset(self):
                                        self.member_var.set("")           
                                        self.prn_var.set("")   
                                        self.id_var.set("")   
                                        self.firstname_var.set("")   
                                        self.lastname_var.set("")   
                                        self.address1_var.set("")   
                                        self.address2_var.set("")   
                                        self.postid_var.set("")   
                                        self.mobile_var.set("")   
                                        self.bookid_var.set("")   
                                        self.booktitle_var.set("")   
                                        self.auther_var.set("")   
                                        self.databorrowed_var.set("")   
                                        self.datedue_var.set("")   
                                        self.daysonbook_var.set("")   
                                        self.latereturnfine_var.set("")
                                        self.dateoverdue_var.set("")   
                                        self.finallprice_var.set("")
                                        self.textBox.delete("1.0",END)      
                     
                    def iExit(self):
                                        iExit=tkinter.messagebox.askyesno("Library management System","Do you want to exit")
                                        if iExit>0:
                                                            self.root.destroy()
                                                            return 
                                        
                    def delete(self):
                                        if self.prn_var.get()=="" or self.id_var.get()=="":
                                                            messagebox.showerror("Error","First Select the Mumber")
                                        else:
                                                             con=mysql.connector.connect(host="localhost",username="root",password="Brijesh@12",database="Mydata")                   
                                                             my_cursor=con.cursor()
                                                             query="delete from library where PRN_NO=%s"
                                                             value=(self.prn_var.get(),)
                                                             my_cursor.execute(query,value)
                                                             
                                        con.commit()
                                        self.fatch_data()
                                        self.reset()
                                        con.close()                                         
                                        
                                        messagebox.showinfo("Success","Member has been Deleted")
                                                                 
if __name__ == "__main__":                                                              
                    root=Tk()
                    obj=LibraryManagementSystem(root)
                    root.mainloop()                                        
                                        