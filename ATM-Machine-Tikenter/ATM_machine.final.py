bal=0
amt=0
from tkinter import *
import tkinter.messagebox
steev=Tk()
steev.geometry("2000x1000")
steev.title("NightWalker")

from PIL import ImageTk,Image
p=Image.open("D:/hello4.jpg")
p=p.resize((1300,900))
p=ImageTk.PhotoImage(p)
pic=tkinter.Label(steev,image=p)
pic.place(x=0,y=0)
attachments=[]
import pymysql
import smtplib
import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.application import MIMEApplication
Label(steev,text="Welcome to SBI ATM",fg="white",bg="#326ba8",font=("Helvetica",35,"bold")).place(x=400,y=100)
def pinno():
    import pymysql
    con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
    c = con.cursor()
    phoneno=pin.get()
    q=('select * from sbi where phoneno = %s')
    c.execute(q,(phoneno))
    d = c.fetchone()
    print("result:",d)
    if d!=None:
        tkinter.messagebox.showinfo('loged',"you are welcome")
        p=pin.get()
        if p == '' :
           tkinter.messagebox.showwarning('error','check your fields') 
    
        elif p==phoneno:
        
            tkinter.messagebox.showinfo("valid","Comming feild click your choice")
            p=Image.open("D:/hello4.jpg")
            p=p.resize((1300,900))
            p=ImageTk.PhotoImage(p)
            pic=tkinter.Label(steev,image=p)
            pic.place(x=1,y=1)
            con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
            c = con.cursor()
            na=('select name from sbi where phoneno = %s')
            c.execute(na ,(phoneno))
            n= c.fetchone()
           
          
         
            Label(steev,text=(f"welcome",n),fg="white",bg="#326ba8",font=("Helvetica",25,"bold") ).place(x=450,y=50)
            Label(steev,text=" Enter your choice",fg="white",bg="#326ba8",font=("Helvetica",25,"bold") ).place(x=450,y=100)
            Button(steev,text="1.Deposit",fg="white",bg="#326ba8",font=("Helvetica",22,"bold"),command=deposit).place(x=50,y=250)
            Button(steev,text="2.withdraw",fg="white",bg="#326ba8",font=("Helvetica",22,"bold"),command=withdraw).place(x=50,y=350)
            Button(steev,text="3.Balance",fg="white",bg="#326ba8",font=("Helvetica",22,"bold"),command=Balance).place(x=50,y=450)
            Button(steev,text="4.Create Account",fg="white",bg="#326ba8",font=("Helvetica",22,"bold"),command=create).place(x=900,y=250)
            Button(steev,text="5.Recipt",fg="white",bg="#326ba8",font=("Helvetica",22,"bold"),command=recipt).place(x=900,y=350)
            Button(steev,text="6.Mini-statment",fg="white",bg="#326ba8",font=("Helvetica",22,"bold"),command=mini).place(x=900,y=450)
        else:
            tkinter.messagebox.showinfo("Invalid","your pin is incorrect")
         
    else:
        yn=tkinter.messagebox.askyesno('Error',"you don't have an account")
        print(yn)
        if yn==True:
            Button(steev,text="4.Create Account",fg="white",bg="#326ba8",font=("Helvetica",22,"bold"),command=create).place(x=900,y=250)
            
            
    
 
       
   

def deposit():
    def add():
  
       
        yn=tkinter.messagebox.askyesno("Deposit Amount","Do yo want to Deposit money")
        if yn==True:
           
            global amt
            amt=int(deposit.get())
            phoneno=pin.get()
            con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
            c = con.cursor()
            na=('select name from sbi where phoneno =%s')
            c.execute(na ,(phoneno))
            n=c.fetchone()
            n=list(n)
            nam=n[0]
            na=('select amount from sbi where phoneno = %s')
            c.execute(na ,(phoneno))
            bal= c.fetchone()
            b=bal[0]
            bal= amt + b
            import datetime
            time=datetime.datetime.now()
            time.strftime(" %A %X%p %d/%B/%Y ")
        
            ###mini_statment####
            recipt=f" \n your Deposited amount= {amt} and current balance= {bal}, last banking time and date={time}"
            file=open(f"D:/ATM_{nam}_mini_statment.txt","a")
            file.write(recipt)
            ################
            recipt=f" hello {nam} \n phone number={phoneno} \n your balance=${bal}\n your last banking time and date={time}"
            file=open(f"D:/ATM_{nam} onlyrecipt.txt","w")
            file.write(recipt)
           
            con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
            c = con.cursor()
            phoneno=pin.get()
            ba=phoneno
            a=bal
            u=('update sbi set amount =%s where phoneno =%s')
            values=a,ba
            c.execute(u,values)
            con.commit()
            
           
            
            if amt =="" :
                tkinter.messagebox.showwarning("Feild is Empty","Enter your amount")
        
           
            else:
               ask=tkinter.messagebox.askyesno("Deposit", f"Deposited ${amt}")
               if ask==True:
                   
                   tkinter.messagebox.showwarning("Thankyou","Thankyou for Banking with us..")
                   Label(steev,text=f"your amount  deposited:= {amt}, your current balance is:= {bal}",fg="white",bg="#326ba8",font=("Helvetica",15)).place(x=150,y=550)         
                   Button(steev,text="Back to menu",fg="white",bg="#326ba8",font=("Helvetica",15,"bold"),command=pinno).place(x=550,y=450)
                   sender_email="steevson9090@gmail.com"
                   con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
                   c = con.cursor()
                   phoneno=pin.get()
                  
                   
                   na=('select name from sbi where phoneno =%s')
                   c.execute(na ,(phoneno))
                   n=c.fetchone()
                   n=list(n)
                   nam=n[0]
                   
                
                   
                   em=('select email from sbi where phoneno =%s')
                   c.execute(em ,(phoneno))
                   e= c.fetchone()
                   e=list(e)
                   mil=e[0]
                   receiver_email=mil
                   subject="Welcome to SBI"
                   message=f"Hello {nam}\n you have deposited rupeess {amt}\n your current balance is:= ${bal} \n thankyou for banking with us "
                   password="mmqb gayl abdr aaco"
                   port=587
       
                   context=ssl.create_default_context()

                   server= smtplib.SMTP("smtp.gmail.com",port)
                   server.starttls(context=context)
                   server.login(sender_email,password)
                   msg=MIMEMultipart()
                   msg["from"]=formataddr(("State bank of india",sender_email))
                   msg["to"]=receiver_email
                   msg["subject"]=subject
                   msg.attach(MIMEText(message,"plain"))
                   server.sendmail(sender_email,receiver_email,msg.as_string())
                   filename=f"D:/ATM_{nam} onlyrecipt.txt"
                   with open(filename,'rb') as f:
                       file_data=f.read()
                       file_name=f.name
                       
                       
                       msg.attach(MIMEApplication(file_data, maintype='application', subtype='txt', filename=file_name))
                      
             
                  
                       
                   print("email send sucessfully")
                   Label(steev,text=(f"Hai",n),fg="black",bg="green",font=("Helvetica",20)).place(x=150,y=650)
                   Label(steev,text="please Check your mail for more information",fg="black",bg="green",font=("Helvetica",20)).place(x=320,y=650)
                   
               
                         
            
                  
                   
                   
            
                                     
                  
               return bal
       
      
    
   
    p=Image.open("D:/hello4.jpg")
    p=p.resize((1300,900))
    p=ImageTk.PhotoImage(p)
    pic=tkinter.Label(steev,image=p)
    pic.place(x=0,y=0)
  
   
    Label(steev,text="Enter the amount you want to Deposit  ",fg="white",bg="#326ba8",font=("Helvetica",15)).place(x=150,y=350)
    deposit=Entry(steev)
    deposit.place(x=550,y=350) 

   
   
    Button(steev,text="Back to menu",fg="white",bg="#326ba8",font=("Helvetica",15,"bold"),command=pinno).place(x=550,y=450)
    Button(steev,text="Deposit",fg="white",bg="#326ba8",font=("Helvetica",10,"bold"),command=add).place(x=700,y=350)
    

   
    
def withdraw():
    def sub():
        ak=tkinter.messagebox.askyesno("Withdraw Amount","Do yo want to Withdraw money")
        if ak==True:
            global amt
            amt=int(withdraw.get())
            con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
            c = con.cursor()
            phoneno=pin.get()
            na=('select amount from sbi where phoneno = %s')
            c.execute(na ,(phoneno))
            bal = c.fetchone()
            b=bal[0]
            am=tkinter.messagebox.askyesno("Withdraw", f"Withdraw ${amt}")
            if am==True:
                if b>=amt:
                    bal= b-amt
                    con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
                    c = con.cursor()
                    na=('select name from sbi where phoneno =%s')
                    c.execute(na ,(phoneno))
                    n=c.fetchone()
                    n=list(n)
                    nam=n[0]
                    phoneno=pin.get()
                    ba=phoneno
                    a=bal
                    u=('update sbi set amount =%s where phoneno =%s')
                    values=a,ba
                    c.execute(u,values)
                    con.commit()
               
                    Label(steev,text=f"your amount  withdrawed:= {amt}, your current balance is:= {bal}",fg="white",bg="#326ba8",font=("Helvetica",15)).place(x=150,y=550)
                    sender_email="steevson9090@gmail.com"
                    con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
                    c = con.cursor()
                    phoneno=pin.get()
                    import datetime
                    time=datetime.datetime.now()
                    time.strftime(" %A %X%p %d/%B/%Y ")
        
                    ###mini_statment####
                    recipt=f"\n your withdrawed amount= {amt} and current balance= {bal}, last banking time and date={time}"
                    file=open(f"D:/ATM_{nam}_mini_statment.txt","a")
                    file.write(recipt)
                    ################
                    recipt=f" hello {nam} \n phone number= {phoneno} \n your balance= {bal}\n your last banking time and date={time}"
                    file=open(f"D:/ATM_{nam} onlyrecipt.txt","w")
                    file.write(recipt)
                    file.close()
                    na=('select name from sbi where phoneno =%s')
                    c.execute(na ,(phoneno))
                    n=c.fetchone()
                    n=list(n)
                    nam=n[0]
                   
                    
                    em=('select email from sbi where phoneno =%s')
                    c.execute(em ,(phoneno))
                    e= c.fetchone()
                    e=list(e)
                    mil=e[0]
                    receiver_email=mil
                    subject="Welcome to SBI"
                    message=f"Hello {nam}\n you have withdraw rupeess {amt}\n your current balance is:= ${bal} \n thankyou for banking with us "
                    password="mmqb gayl abdr aaco"
                    port=587
       
                    context=ssl.create_default_context()

                    server= smtplib.SMTP("smtp.gmail.com",port)
                    server.starttls(context=context)
                    server.login(sender_email,password)
                    msg=MIMEMultipart()
                    msg["from"]=formataddr(("State bank of india",sender_email))
                    msg["to"]=receiver_email
                    msg["subject"]=subject
                    msg.attach(MIMEText(message,"plain"))
                    server.sendmail(sender_email,receiver_email,msg.as_string())
                    filename=f"D:/ATM_{nam} onlyrecipt.txt"
                    with open(filename,'rb') as f:
                        file_data=f.read()
                        file_name=f.name
                       
                       
                    msg.attach(MIMEApplication(file_data, maintype='application', subtype='txt', filename=file_name))
                      
             
                  
                       
                    print("email send sucessfully")
                    Label(steev,text=(f"Hai",n),fg="black",bg="green",font=("Helvetica",20)).place(x=150,y=650)
                    Label(steev,text="please Check your mail for more information",fg="black",bg="green",font=("Helvetica",20)).place(x=320,y=650)

                                      
                else:
                    Label(steev,text="insufficent balance" , fg="white",bg="#326ba8",font=("Helvetica",15)).place(x=150,y=450)
            
                
            if amt=="" :
                tkinter.messagebox.showwarning("Feild is Empty","Enter your amount")
            
               
            else:
                
                tkinter.messagebox.showwarning("Thankyou","Thankyou for Banking with us..")
                         
                Button(steev,text="Back to menu",fg="white",bg="#326ba8",font=("Helvetica",15,"bold"),command=pinno).place(x=550,y=450)
                return bal
      
    
   
    p=Image.open("D:/hello4.jpg")
    p=p.resize((1300,900))
    p=ImageTk.PhotoImage(p)
    pic=tkinter.Label(steev,image=p)
    pic.place(x=0,y=0)
   
    Label(steev,text="Enter the amount you want to withdraw  ",fg="white",bg="#326ba8",font=("Helvetica",15)).place(x=150,y=350)
    withdraw=Entry(steev)
    withdraw.place(x=550,y=350) 

   
   
    Button(steev,text="Back to menu",fg="white",bg="#326ba8",font=("Helvetica",15,"bold"),command=pinno).place(x=550,y=450)
    Button(steev,text="Withdraw",fg="white",bg="#326ba8",font=("Helvetica",10,"bold"),command=sub).place(x=700,y=350)
    

    
   
    
def Balance():
    
    he=tkinter.messagebox.showinfo("Balance enquire","check your balance")
    p=Image.open("D:/hello4.jpg")
    p=p.resize((1300,900))
    p=ImageTk.PhotoImage(p)
    pic=tkinter.Label(steev,image=p)
    pic.place(x=0,y=0)
    con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
    c = con.cursor()
    phoneno=pin.get()
    ba=phoneno
    na=('select amount from sbi where phoneno = %s')
    c.execute(na ,(phoneno))
    bal= c.fetchone()
    b=bal[0]
   
    
   
    Label(steev,text=f"Your balance is = {b} ",fg="white",bg="#326ba8",font=("Helvetica",25)).place(x=150,y=350)
    Button(steev,text="Back to menu",fg="white",bg="#326ba8",font=("Helvetica",15,"bold"),command=pinno).place(x=500,y=450)
    return bal
    #for update amount...............pro
 
    
  
 

    
def create():
    tkinter.messagebox.showinfo("Create Account","Do you want to create account")
    p=Image.open("D:/hello.jpg")
    p=p.resize((1300,900))
    p=ImageTk.PhotoImage(p)
    pic=tkinter.Label(steev,image=p)
    pic.place(x=0,y=0)
    import pymysql
    Label(steev,text="Enter your name",fg="white",bg="#326ba8",font=("Helvetica",20)).place(x=150,y=150)
    n=Entry(steev)
    n.place(x=450,y=150)
    Label(steev,text="Enter phone number",fg="white",bg="#326ba8",font=("Helvetica",20)).place(x=150,y=250)
    ph=Entry(steev)
    ph.place(x=450,y=250)
    Label(steev,text="Enter your username",fg="white",bg="#326ba8",font=("Helvetica",20)).place(x=150,y=350)
    u=Entry(steev)
    u.place(x=450,y=350)
    Label(steev,text="Enter your password",fg="white",bg="#326ba8",font=("Helvetica",20)).place(x=150,y=450)
    pas=Entry(steev)
    pas.place(x=450,y=450)
    Label(steev,text="Enter your Email ID",fg="white",bg="#326ba8",font=("Helvetica",20)).place(x=150,y=550)
    m=Entry(steev)
    m.place(x=450,y=550)
    def acces():
       
        name=n.get()
        phoneno=ph.get()
        username=u.get()
        password=pas.get()
        email=m.get()
        if name=="" or phoneno=="" or username=="" or password=="" or email=="":
            tkinter.messagebox.showwarning("Error","Complete the feild buddy")
        else:
            import pymysql
            con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
            c=con.cursor()
            va=("insert into sbi( name , phoneno , username ,password , email, amount) values (%s ,%s ,%s ,%s ,%s,%s)")
            values=name,phoneno,username,password,email, bal
            c.execute(va,values)
            con.commit()
            
        
            con.close()
            
            tkinter.messagebox.showwarning("valid","Feild is completed")
            Button(steev,text="Back to menu",fg="white",bg="#326ba8",font=("Helvetica",15,"bold"),command=pinno).place(x=550,y=650)
    Button(steev,text='okay',font=("Helvetica",15),command=acces).place(x=450,y=650)
    Button(steev,text="Back to menu",fg="white",bg="#326ba8",font=("Helvetica",15,"bold"),command=pinno).place(x=550,y=650)


    steev.mainloop()

def recipt():
    he=tkinter.messagebox.askokcancel("Recipt","Do yo want recipt")
    if he==True:
        p=Image.open("D:/hello.jpg")
        p=p.resize((1300,900))
        p=ImageTk.PhotoImage(p)
        pic=tkinter.Label(steev,image=p)
        pic.place(x=0,y=0)
      
        
        import datetime
        time=datetime.datetime.now()
        time.strftime(" %A %X%p %d/%B/%Y ")
        
        con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
        c = con.cursor()
        phoneno=pin.get()
        na=('select amount from sbi where phoneno = %s')
        c.execute(na ,(phoneno))
        bal= c.fetchone()
        b=bal[0]
        na=('select name from sbi where phoneno =%s')
        c.execute(na ,(phoneno))
        n=c.fetchone()
        n=list(n)
        nam=n[0]
        q=('select * from sbi where phoneno = %s')
        c.execute(q,(phoneno))
        d = c.fetchall()
        Label(steev,text=f" hello {nam} \n phone number={phoneno} \n your balance={b}\n your last banking time and date={time}",fg="white",bg="#326ba8",font=("Helvetica",20)).place(x=350,y=250)
        recipt=f" hello {nam} \n phone number={phoneno} \n your balance=${bal}\n your last banking time and date={time}"
        file=open(f"D:/ATM_{nam} onlyrecipt.txt","w")
        file.write(recipt)
        file.close()
        Button(steev,text="Back to menu",fg="white",bg="#326ba8",font=("Helvetica",15,"bold"),command=pinno).place(x=550,y=650)

def mini():
    
    she=tkinter.messagebox.askokcancel("Mini-statment","Do yo want Mini-Statment")
    if she==True:
        p=Image.open("D:/hello.jpg")
        p=p.resize((1300,900))
        p=ImageTk.PhotoImage(p)
        pic=tkinter.Label(steev,image=p)
        pic.place(x=0,y=0)
        con=pymysql.connect(host='localhost',user='root',password='1234',db='bank')
        c = con.cursor()
        
        phoneno=pin.get()
        na=('select name from sbi where phoneno =%s')
        c.execute(na ,(phoneno))
        n=c.fetchone()
        n=list(n)
        nam=n[0]
        
        import datetime
        time=datetime.datetime.now()
        time.strftime(" %A %X%p %d/%B/%Y ")
        
        recipt=f"your balance=${bal}\nyour last banking time and date={time}"
        Label(steev,text=(f"\n  Please open D:Data file: \n 'D:/ ATM_{nam}_mini_statment.txt' \n acess your mini-statment "),fg="white",bg="#326ba8",font=("Helvetica",20)).place(x=350,y=250)
        file=open(f"D:/ATM_{nam}_mini_statment.txt","a")
        file.write(recipt)
        
        file.close()
        Button(steev,text="Back to menu",fg="white",bg="#326ba8",font=("Helvetica",15,"bold"),command=pinno).place(x=550,y=650)
    
    
    

                

Label(steev,text="Enter your phone number",fg="white",bg="#326ba8",font=("Helvetica",12,"bold")).place(x=500,y=200)
pin=Entry(steev)
pin.place(x=710,y=200)
Button(steev,text="check",fg="white",bg="#326ba8",font=("Helvetica",10,"bold"),command=pinno).place(x=850,y=200)



steev.mainloop()
