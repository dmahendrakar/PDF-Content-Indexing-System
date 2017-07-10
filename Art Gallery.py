from Tkinter import *

class CIF:
    
    def __init__(self,master):
        #frame = Frame(master)
        self.root=Tk()
        
        self.root.button1= Button(self.root,text="SUBMIT",command=self.Submit)
	
        self.root.title("Content Indexing System")
    
        DOI=Label(self.root,text="Enter your question: ")
        NOI=Label(self.root,text="Search parameter: ")

        #self.v=StringVar()
                    
        self.entry1=Entry(self.root,textvariable=self.v)
        self.entry2=Entry(self.root)


        q.grid(row=0,sticky=E)
        p.grid(row=0,column=3)
        

        self.entry1.grid(row=0,column=1)
        self.entry2.grid(row=0,column=4)
        self.root.button1.grid(row=27,column=4)

       
    def Submit(self):
        question=self.q.get()
        param=int(self.p.get())
        self.root.quit()
        self.root.destroy()


class AWIF:
    
    def __init__(self,master):
        #frame = Frame(master)
        self.root=Tk()
        
        self.root.button1= Button(self.root,text="SUBMIT",command=self.Submit)
        #button1.bind("<Button-1>",Submit)
        

	
        self.root.title("ARTWORK INFORMATION FORM")
    
        ALN=Label(self.root,text="Artist Last Name")
        AFN=Label(self.root,text="Artist First Name")
        TITLE = Label(self.root,text="Title")
        YC=Label(self.root,text="Year Completed")
        TYPE=Label(self.root,text="Type")
        MED=Label(self.root,text="Medium")
        STYLE=Label(self.root,text="Style")
        SIZE=Label(self.root,text="Size")

        OLN = Label(self.root,text="Owner Last Name")
        OFN = Label(self.root,text="Owner First Name")
        ST=Label(self.root,text="Street")
        CITY=Label(self.root,text="City")
        STATE=Label(self.root,text="State")
        ZIP=Label(self.root,text="Zip")
        TEL=Label(self.root,text="Telephone  :")
        AREA=Label(self.root,text="Area Code")
        NUM=Label(self.root,text="Number")
        OSN=Label(self.root,text="Owner Security Number")

        DL = Label(self.root,text="Date Listed")
        AP = Label(self.root,text="Asking Price")
        
        
        self.v=StringVar()
                    
        self.entry1=Entry(self.root)
        self.entry2=Entry(self.root)
        self.entry3=Entry(self.root)
        self.entry4=Entry(self.root)
        self.entry5=Entry(self.root,width=50)
        self.entry6=Entry(self.root)
        self.entry7=Entry(self.root)
        self.entry8=Entry(self.root)
        self.entry9=Entry(self.root)
        self.entry10=Entry(self.root)
        self.entry11=Entry(self.root)
        self.entry12=Entry(self.root)
        self.entry13=Entry(self.root)
        self.entry14=Entry(self.root)
        self.entry15=Entry(self.root)
        self.entry16=Entry(self.root)
        self.entry17=Entry(self.root)
        self.entry18=Entry(self.root)
        self.entry19=Entry(self.root)



        ALN.grid(row=0,sticky=E)
        AFN.grid(row=0,column=3)
        TITLE.grid(row=2,sticky=E)
        YC.grid(row=4,sticky=E)
        TYPE.grid(row=6,sticky=E)
        MED.grid(row=8,sticky=E)
        STYLE.grid(row=10,sticky=E)
        SIZE.grid(row=12,sticky=E)
        OLN.grid(row=14,sticky=E)
        OFN.grid(row=14,column=3)
        ST.grid(row=16,sticky=E)
        CITY.grid(row=18,sticky=E)
        STATE.grid(row=18,column=3)
        ZIP.grid(row=18,column=5)
        TEL.grid(row=20,sticky=E)
        AREA.grid(row=20,column=1,sticky=E)
        NUM.grid(row=20,column=3)
        OSN.grid(row=22,sticky=E)
        DL.grid(row=24,sticky=E)
        AP.grid(row=24,column=3)
        
        self.entry1.grid(row=0,column=1)
        self.entry2.grid(row=0,column=4)
        self.entry3.grid(row=2,column=1)
        self.entry3.config(width=50)
        self.entry4.grid(row=4,column=1)
        self.entry5.grid(row=6,column=1)
        self.entry6.grid(row=8,column=1)
        self.entry7.grid(row=10,column=1)
        self.entry8.grid(row=12,column=1)
        self.entry9.grid(row=14,column=1)
        self.entry10.grid(row=14,column=4)
        self.entry11.grid(row=16,column=1)
        self.entry12.grid(row=18,column=1)
        self.entry13.grid(row=18,column=4)
        self.entry14.grid(row=18,column=6)
        self.entry15.grid(row=20,column=2)
        self.entry16.grid(row=20,column=4)
        self.entry17.grid(row=22,column=1)
        self.entry18.grid(row=24,column=1)
        self.entry19.grid(row=24,column=4)
        
        self.root.button1.grid(row=27,column=4)
       
    def Submit(self):
        cr.execute("INSERT INTO Artwork(artistId,workTitle,askingPrice,dateListed,dateReturned,dateShown,status,workMedium,workSize,workStyle,workType,workYearCompleted,collectorSocialSecurityNumber) VALUES(1,'"+self.entry3.get()+"'," +self.entry19.get()+",'"+self.entry18.get()+"','2014-7-21',null,'for sale','"+self.entry6.get()+"','"+self.entry8.get()+"','"+self.entry7.get()+"','"+self.entry5.get()+"','"+self.entry4.get()+" ','"+self.entry17.get()+"')")
        cnx.commit()
        self.root.destroy()
        print  self.entry1.get()
        print  self.entry2.get()
        print  self.entry3.get()
        print  self.entry4.get()
        print  self.entry5.get()
        print  self.entry6.get()
        print  self.entry7.get()
        print  self.entry8.get()
        print  self.entry9.get()
        print  self.entry10.get()
        print  self.entry11.get()
        print  self.entry12.get()
        print  self.entry13.get()
        print  self.entry14.get()
        print  self.entry15.get()
        print  self.entry16.get()
        print  self.entry17.get()
        print  self.entry18.get()
        print  self.entry19.get()
    

class AIF:
    
    def __init__(self,master):
        #frame = Frame(master)
        self.root=Tk()
        
        self.root.button1= Button(self.root,text="SUBMIT",command=self.Submit)
        #button1.bind("<Button-1>",Submit)
	
        self.root.title("ARTIST INFORMATION FORM")
    
        DOI=Label(self.root,text="Date of Interview")
        NOI=Label(self.root,text="Name of Interviewer")
        ALN=Label(self.root,text="Artist Last Name")
        AFN=Label(self.root,text="Artist First Name")
        ST=Label(self.root,text="Street")
        CITY=Label(self.root,text="City")
        STATE=Label(self.root,text="State")
        ZIP=Label(self.root,text="Zip")
        TEL=Label(self.root,text="Telephone  :")
        AREA=Label(self.root,text="Area Code")
        NUM=Label(self.root,text="Number")
        SSN=Label(self.root,text="Social Security Number")
        UTYPE=Label(self.root,text="Usual Type")
        UMED=Label(self.root,text="Usual Medium")
        USTYLE=Label(self.root,text="Usual Style")
         
        self.entry1=Entry(self.root)
        self.entry2=Entry(self.root)
        self.entry3=Entry(self.root)
        self.entry4=Entry(self.root)
        self.entry5=Entry(self.root,width=50)
        self.entry6=Entry(self.root)
        self.entry7=Entry(self.root)
        self.entry8=Entry(self.root)
        self.entry9=Entry(self.root)
        self.entry10=Entry(self.root)
        self.entry11=Entry(self.root)
        self.entry12=Entry(self.root)
        self.entry13=Entry(self.root)
        self.entry14=Entry(self.root)
        self.entry15=Entry(self.root)

        DOI.grid(row=0,sticky=E)
        NOI.grid(row=0,column=3)
        ALN.grid(row=2,sticky=E)
        AFN.grid(row=2,column=3)
        ST.grid(row=4,sticky=E)
        CITY.grid(row=6,sticky=E)
        STATE.grid(row=6,column=2)
        ZIP.grid(row=6,column=6)
        TEL.grid(row=8,sticky=E)
        AREA.grid(row=8,column=1)
        NUM.grid(row=8,column=3)
        SSN.grid(row=10,sticky=E)
        UTYPE.grid(row=12,sticky=E)
        UMED.grid(row=14,sticky=E)
        USTYLE.grid(row=16,sticky=E)

        self.entry1.grid(row=0,column=1)
        self.entry2.grid(row=0,column=4)
        self.entry3.grid(row=2,column=1)
        self.entry4.grid(row=2,column=4)
        self.entry5.grid(row=4,column=1)
        self.entry6.grid(row=6,column=1)
        self.entry7.grid(row=6,column=3,columnspan=2)
        self.entry8.grid(row=6,column=7,columnspan=2)
        self.entry9.grid(row=8,column=2)
        self.entry10.grid(row=8,column=4)
        self.entry11.grid(row=10,column=1)
        self.entry12.grid(row=12,column=1)
        self.entry13.grid(row=14,column=1)
        self.entry14.grid(row=16,column=1)
        
        self.root.button1.grid(row=17,column=4)

        
       
    def Submit(self):
        cr.execute("INSERT INTO Artist(firstName,lastName,interviewDate,interviewerName,areaCode,telephoneNumber,street,zip,salesLastYear,salesYearToDate,socialSecurityNumber,usualMedium,usualStyle,usualType) VALUES('"+self.entry4.get()+"', '"+self.entry3.get()+"', '"+self.entry1.get()+"', '"+self.entry2.get()+"', '"+self.entry9.get()+"','"+self.entry10.get()+"','"+self.entry5.get()+"', '"+self.entry8.get()+"', 9000, 4500,'"+self.entry11.get()+"', '"+self.entry13.get()+"', '"+self.entry14.get()+"', '"+self.entry12.get()+"')")
        cnx.commit()
        self.root.destroy()
        print  self.entry1.get()
        print  self.entry2.get()
        print  self.entry3.get()
        print  
        print  self.entry5.get()
        print  self.entry6.get()
        print  self.entry7.get()
        print  self.entry8.get()
        print  self.entry9.get()
        print  self.entry10.get()
        print  self.entry11.get()
        print  self.entry12.get()
        print  self.entry13.get()
        print  self.entry14.get()

root=Tk()
root.title("WELCOME TO ART GALLERY")
#imgf=open("C:\\Users\\Win\\Desktop\\the-milky-way-over-the-mountains-31955-1920x1200.jpg")
#img=PhotoImage(imgf)
#label0=Label(root,image=img)
#label0.pack()
label1=Label(root,text="WHO ARE YOU?")
label1.pack(side=TOP)
label2=Label(root,text="WHAT DO YOU WANT TO DO?")
label2.pack(side=TOP)

def aif(event):
    obj=AIF(root)


def cif(event):
    obj=CIF(root)


def awif(event):
    obj=AWIF(root)

button1= Button(root,text="Artist")
button1.bind("<Button-1>",aif)
button2= Button(root,text="Collector")
button2.bind("<Button-1>",cif)
button3= Button(root,text="Artwork")
button3.bind("<Button-1>",awif)
button4= Button(root,text="Queries")
button4.pack(side=TOP)
button1.pack(side=BOTTOM)
button2.pack(side=BOTTOM)
button3.pack(side=BOTTOM)
button1.config(height=5,width=30)
button2.config(height=5,width=30)
button3.config(height=5,width=30)
#root.destroy()
#obj=CIF(root)

root.geometry("500x500")
root.mainloop()
