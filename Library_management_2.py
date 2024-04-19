from tkinter import  *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime



class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
    

        #==================================================Variable===================================================================================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.title_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.actualprice_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturn_var=StringVar()
        self.dateoverdue_var=StringVar()



        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green", bd=20, relief=RIDGE,font=("times new roman",50,"bold"),padx=2, pady=6)
        lbltitle.pack(side=TOP,fill=X)



        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        #=============================================DataFrameLeft=====================================================================================================


        DataFrameLeft=LabelFrame(frame,text="Library membership information",bg="powder blue",fg="black", bd=12, relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("arial",12,"bold"),padx=2 , pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.member_var,width= 27, state="readonly")
        comMember["value"]=("Admin staff", "student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)



        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN NO",font=("aril",12,"bold"),padx=2 , pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=27)
        txtPRN_NO.grid(row=1,column=1)


        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID NO:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)  
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.title_var,width=27)
        txtTitle.grid(row=2,column=1)


        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=27)
        txtFirstName.grid(row=3,column=1)


        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=27)
        txtLastName.grid(row=4,column=1)


        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Adress 1:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=27)
        txtAddress1.grid(row=5,column=1)


        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address 2:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=27)
        txtAddress2.grid(row=6,column=1)
        

     
        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code:",font=("arial",12,"bold"),padx= 2, pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=27)
        txtPostCode.grid(row=7,column=1)


        lblMobileNo=Label(DataFrameLeft,bg="powder blue",text="Mobile No:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblMobileNo.grid(row=8,column=0,sticky=W)
        txtMobileNo=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=27)
        txtMobileNo.grid(row=8,column=1)


        lblBookID=Label(DataFrameLeft,bg="powder blue",text="Book ID:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=27)
        txtBookID.grid(row=0,column=3)


        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=27)
        txtBookTitle.grid(row=1,column=3)


        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author Name:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.author_var,width=27)
        txtAuthor.grid(row=2,column=3)


        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Data Borrowed:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDataBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=27)
        txtDataBorrowed.grid(row=3,column=3)


        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=27)
        txtDateDue.grid(row=4,column=3)


        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook_var,width=27)
        txtDaysOnBook.grid(row=5,column=3)


        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.latereturn_var,width=27)
        txtLateReturnFine.grid(row=6,column=3)


        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateoverdue_var,width=27)
        txtDateOverDue.grid(row=7,column=3)


        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("arial",12,"bold"),padx=2 , pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.actualprice_var,width=27)
        txtActualPrice.grid(row=8,column=3)

        #***************************************Data Frame right************************************************************************************

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="black", bd=12, relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)


        self.textbox=Text(DataFrameRight,font=("arial",12,"bold"),width=32, height=16, padx=2, pady=6)
        self.textbox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Operating System','Network Theory','DataBase Management System','Engineering Mathematic','Digital Logic','Internet of Things','Software Engineering',
                 'Image Processing','Data science','Data Structure','Formal Language Automata','Web Technology','Design Analysis and Algorithm','Cyber Security',
                 'OOPs','Programing Problem Solving','Data Mining','Higher Physic','Enviormental Science','Python Programming','HTML','Advance in Java',
                 'Aptitude Mathematics','Logical Mathematic','Machine larning','Cloud Computing','Computer Orginazation and Architecture'
                 
                 ]
        def selectBook():
            value=str(listbox.get(listbox.curselection()))
            x=value

        
            if (x == "Operating System"):
                    self.bookid_var.set("BKID6501")
                    self.booktitle_var.set("Concept of Operating System")
                    self.author_var.set("Tanenbaum")
                    pass
            
                
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")

            elif (x == "Network Theory"):
                    self.bookid_var.set("BKID6502")
                    self.booktitle_var.set("Computer Network")
                    self.author_var.set("William H.Hayt")
            
                    
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                
            elif (x == "DataBase Management System"):
                    self.bookid_var.set("BKID6503")
                    self.booktitle_var.set("DBMS")
                    self.author_var.set("Henry F.Kort")
            
                
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                
            elif x == "Engineering Mathematic":
                    self.bookid_var.set("BKID6504")
                    self.booktitle_var.set("Higher Mathematic")
                    self.author_var.set("B.S. Grewal")
            
                
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Digital Logic":
                    self.bookid_var.set("BKID6505")
                    self.booktitle_var.set("DELD")
                    self.author_var.set("Kollisol")
            
                
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Internet of Things":
                    self.bookid_var.set("BKID6506")
                    self.booktitle_var.set("IOT")
                    self.author_var.set("Arshdeep Bahga")
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Software Engineering":
                    self.bookid_var.set("BKID6507")
                    self.booktitle_var.set("Software Engieering")
                    self.author_var.set("lan Sommerville")
        
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Image Processing":
                    self.bookid_var.set("BKID6508")
                    self.booktitle_var.set("Image Processing")
                    self.author_var.set("Tanenbam")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.500")
                

            elif x == "Data science":
                    self.bookid_var.set("BKID6509")
                    self.booktitle_var.set("Data Science")
                    self.author_var.set("Tanenbaum")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1232")
                
            elif x == "Data Structure":
                    self.bookid_var.set("BKID6510")
                    self.booktitle_var.set("Data Structure")
                    self.author_var.set("Willy")
        
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.2300")
                

            elif x == "Formal Language Automata":
                    self.bookid_var.set("BKID6511")
                    self.booktitle_var.set("TOC")
                    self.author_var.set("Michiel Smid")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Web Technology":
                    self.bookid_var.set("BKID6512")
                    self.booktitle_var.set("Web Technology")
                    self.author_var.set("Michelly")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Design Analysis and Algorithm":
                    self.bookid_var.set("BKID6513")
                    self.booktitle_var.set("DAA")
                    self.author_var.set("Ellis horowitz")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Cyber Security":
                    self.bookid_var.set("BKID6515")
                    self.booktitle_var.set("Cyber Security")
                    self.author_var.set("Tanenbaum")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "OOPs":
                    self.bookid_var.set("BKID6584")
                    self.booktitle_var.set("OOPs")
                    self.author_var.set("Barney")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Programing Problem Solving":
                    self.bookid_var.set("BKID6516")
                    self.booktitle_var.set("PPS")
                    self.author_var.set("William H.Hayt")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Data Mining":
                    self.bookid_var.set("BKID6517")
                    self.booktitle_var.set("Data Minning")
                    self.author_var.set("Henery. Kort")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15) 
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Higher Physic":
                    self.bookid_var.set("BKID6518")
                    self.booktitle_var.set("Higher Education Physic")
                    self.author_var.set("S.Chand")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Enviormental Science":
                    self.bookid_var.set("BKID6519")
                    self.booktitle_var.set("Enviormental Science")
                    self.author_var.set("Kollisol")
    
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif    x == "Python Programming":
                    self.bookid_var.set("BKID6520")
                    self.booktitle_var.set("Python Programing")
                    self.author_var.set("W3School")
            
                    pass
                
                
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "HTML":
                    self.bookid_var.set("BKID6521")
                    self.booktitle_var.set("HTML")
                    self.author_var.set("GreekofGeeks")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Advance in Java":
                    self.bookid_var.set("BKID6522")
                    self.booktitle_var.set("Advance Java")
                    self.author_var.set("E Balagurusamy")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Aptitude Mathematics":
                    self.bookid_var.set("BKID6523")
                    self.booktitle_var.set("Mathemaic")
                    self.author_var.set("RS Aggarwal")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Logical Mathematic":
                    self.bookid_var.set("BKID6524")
                    self.booktitle_var.set("Logic Math")
                    self.author_var.set("Tanenbaum")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Machine larning":
                    self.bookid_var.set("BKID6525")
                    self.booktitle_var.set("ML")
                    self.author_var.set("William H.Hayt")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Cloud Computing":
                    self.bookid_var.set("BKID6526")
                    self.booktitle_var.set("Cloud Computing")
                    self.author_var.set("Tanserflow")
            
                    pass
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

            elif x == "Computer Orginazation and Architecture":
                    self.bookid_var.set("BKID6527")
                    self.booktitle_var.set("COA")
                    self.author_var.set("Tanenbaum")
            
                
    
            
                    d1=datetime.date.today()
                    d2=datetime.timedelta(days=15)
                    d3=d1+d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook_var.set(15)
                    self.latereturn_var.set("Rs.50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs.1000")
                

                

        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listbox.bind("<<ListboxSelect>>",selectBook)
        pass

        listbox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listbox.yview)

        for item in listBooks:
            listbox.insert(END,item)


        #**************************************Buttons Frame****************************************************************************************
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=0)


        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=2)


        btnAddData=Button(Framebutton,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=4)


        btnAddData=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="White")
        btnAddData.grid(row=0,column=5)


        #**************************************Information Button**********************************************************************************

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=195)

        Table_Frame=Frame(FrameDetails,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Table_Frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        Yscroll=ttk.Scrollbar(Table_Frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_Frame,columns=("membertype","prnno","title","firstname","lastname","address1","address2"
                                                             ,"postcode","mobile","bookid","booktitle","author","dateborrow","dateonDue",
                                                             "days","latereturnfine","dateoverdue","actualprice"),xscrollcommand=xscroll.set,yscrollcommand=Yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        Yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        Yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN ")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postcode",text="Post code")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrow",text="Date Borrow")
        self.library_table.heading("dateonDue",text="Date on Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("actualprice",text="Actual Price")


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("membertype",width="100")
        self.library_table.column("prnno",width="100")
        self.library_table.column("title",width="100")
        self.library_table.column("firstname",width="100")
        self.library_table.column("lastname",width="100")
        self.library_table.column("address1",width="100")
        self.library_table.column("address2",width="100")
        self.library_table.column("postcode",width="100")
        self.library_table.column("mobile",width="100")
        self.library_table.column("bookid",width="100")
        self.library_table.column("booktitle",width="100")
        self.library_table.column("author",width="100")
        self.library_table.column("dateborrow",width="100")
        self.library_table.column("dateonDue",width="100")
        self.library_table.column("days",width="100")
        self.library_table.column("latereturnfine",width="100")
        self.library_table.column("dateoverdue",width="100")
        self.library_table.column("actualprice",width="100")

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor )


    def adda_data(self):
            conn = mysql.connector.connect(host="localhost",username="root",password="Swarup@0204",database="project")            

            my_cursor=conn.cursor()
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(

                                                                                                                        self.member_var.get(),
                                                                                                                        self.prn_var.get(),
                                                                                                                        self.title_var.get(),
                                                                                                                        self.firstname_var.get(),
                                                                                                                        self.lastname_var.get(),
                                                                                                                        self.address1_var.get(),
                                                                                                                        self.address2_var.get(),
                                                                                                                        self.postcode_var.get(),
                                                                                                                        self.mobile_var.get(),
                                                                                                                        self.bookid_var.get(),
                                                                                                                        self.booktitle_var.get(),
                                                                                                                        self.author_var.get(),
                                                                                                                        self.dateborrowed_var.get(),
                                                                                                                        self.dateoverdue_var.get(),
                                                                                                                        self.daysonbook_var.get(),
                                                                                                                        self.latereturn_var.get(),
                                                                                                                        self.dateoverdue_var.get(),
                                                                                                                        self.actualprice_var.get(),                                                                                                           
                                                                                                                                                ))


            conn.commit()
            self.fatch_data()
            conn.close()                                                                                                      
                                                                                                                                                
            messagebox.showinfo("success","member has been inserted sucessfully")


    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Swarup@0204",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from project")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
                conn.commit()
                conn.close()
    def get_cursor(self,Event=""):
        cursor_rows=self.library_table.focus()
        content=self.library_table.item(cursor_rows)
        row=content['values']

        self.member_var(row[0])
        self.prn_var(row[1])
        self.title_var(row[2])
        self.firstname_var(row[3])
        self.lastname_var(row[4])
        self.address1_var(row[5])
        self.address2_var(row[6])
        self.postcode_var(row[7])
        self.mobile_var(row[8])
        self.bookid_var(row[9])
        self.booktitle_var(row[10])
        self.author_var(row[11])
        self.dateborrowed_var(row[12])
        self.datedue_var(row[13])
        self.daysonbook_var(row[14])
        self.latereturn_var(row[15])
        self.dateborrowed_var(row[16])
        self.actualprice_var(row[17])

    def showData(self):
        self.textbox.insert(END,"Member Type:\t\t"+ self.member_var().get()+"\n")
        self.textbox.insert(END,"PRN NO:\t\t"+ self.prn_var().get()+"\n")
        self.textbox.insert(END,"Title:\t\t"+ self.title_var().get()+"\n")
        self.textbox.insert(END,"First Name :\t\t"+ self.firstname_var().get()+"\n")
        self.textbox.insert(END,"Last Name:\t\t"+ self.lastname_var().get()+"\n")
        self.textbox.insert(END,"Address1:\t\t"+ self.address1_var().get()+"\n")
        self.textbox.insert(END,"Address2:\t\t"+ self.address2_var().get()+"\n")
        self.textbox.insert(END,"Postcode:\t\t"+ self.postcode_var().get()+"\n")
        self.textbox.insert(END,"mobile:\t\t"+ self.mobile_var().get()+"\n")
        self.textbox.insert(END,"Book id:\t\t"+ self.bookid_var().get()+"\n")
        self.textbox.insert(END,"book Title:\t\t"+ self.booktitle_var().get+"\n")
        self.textbox.insert(END,"Author:\t\t"+ self.author_var().get()+"\n")
        self.textbox.insert(END,"Date Borrowed:\t\t"+ self.datedue_var().get()+"\n")
        self.textbox.insert(END,"Date Due:\t\t"+ self.member_var().get()+"\n")
        self.textbox.insert(END,"Days on Book:\t\t"+ self.daysonbook_var().get()+"\n")
        self.textbox.insert(END,"Late Return Fine:\t\t"+ self.latereturn_var().get()+"\n")
        self.textbox.insert(END,"date Borrowed:\t\t"+ self.dateoverdue_var().get()+"\n")
        self.textbox.insert(END,"Actual price:\t\t"+ self.actualprice_var().get()+"\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.title_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturn_var.set(""),
        self.dateoverdue_var.set(""),
        self.actualprice_var.set(""),
        self.textbox.delete("1.0",END)


    




    

if __name__ == "__main__":
    root = tk.Tk()
    obj=LibraryManagementSystem(root)
    label = tk.Label(root)
    label.pack()

    root.mainloop()




    