from tkinter import*  
import math,random,os
from tkinter import messagebox

class Restraunt:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x860")
        self.root.title("Chinees Corner")
        bg_color="#FF7F50"
        bg_color1= "#074463"
        bg_color2="#00FFFF"
        title=Label(self.root,text="China Bowl",bd=8,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",25,"bold"),pady=2).pack(fill=X)

        # ==============Variables====================
        # -------menu variable---------
        self.chilli=IntVar()
        self.noodel=IntVar()
        self.manchu=IntVar()
        self.frice=IntVar()
        self.rolls=IntVar()
        self.chopse=IntVar()
        self.coke=IntVar()
        self.pepsi=IntVar()
        self.dew=IntVar()

        # --------------customer variable-----------
        self.cname=StringVar()
        self.cnum=StringVar()
        self.cbillid=StringVar()
        x=random.randint(10000,99999)
        self.cbillid.set(str(x))
        self.csearch=StringVar()

        # ----------action Variable--------------------
        self.total_amount=StringVar()
        self.tax=StringVar()



        # customer Details frame
        cust=LabelFrame(self.root,text="Customer Details",font=("times",20,"bold"),fg="gold",bg=bg_color1,bd=5,relief=GROOVE)
        cust.place(x=0,y=70,relwidth=1)

        cname=Label(cust,text="Customer Name",font=("times 16 bold"),fg="black",bg=bg_color1).grid(row=0,column=0,padx=15,pady=5)
        cname_txt=Entry(cust,width=15,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.cname).grid(row=0,column=1,padx=15,pady=7)

        cphno=Label(cust,text="Mobile No.",font=("times 16 bold"),fg="black",bg=bg_color1).grid(row=0,column=2,padx=15,pady=5)
        cphno_txt=Entry(cust,width=15,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.cnum).grid(row=0,column=3,padx=15,pady=7)

        cbill=Label(cust,text="Bill Id",font=("times 16 bold"),fg="black",bg=bg_color1).grid(row=0,column=4,padx=15,pady=5)
        cbill_txt=Entry(cust,width=15,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.csearch).grid(row=0,column=5,padx=15,pady=7)

        bill_srch=Button(cust,text="Search",width=10,bd=5,font="arial 12 bold",command=self.find_bill).grid(row=0,column=6,padx=75,pady=10)

        # ------------MENU-------------


        menu=LabelFrame(self.root,text="MENU",font=("times",24,"bold"),fg="red",bg=bg_color2)
        menu.place(x=20,y=180,relwidth=.40)

        item=Label(menu,text="Items",font=("times 18 bold"),fg="black",bg=bg_color2).grid(row=0,column=0,padx=30,pady=4)
        prc=Label(menu,text="Price",font=("times 18 bold"),fg="black",bg=bg_color2).grid(row=0,column=1,padx=40,pady=4)
        quant=Label(menu,text="Quantity",font=("times 18 bold"),fg="black",bg=bg_color2).grid(row=0,column=2,padx=40,pady=4)

        item1=Label(menu,text="Chilli potato",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=1,column=0,padx=15,pady=10)
        p1=Label(menu,text="90/-",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=1,column=1,padx=15,pady=10)
        q1_txt=Entry(menu,width=3,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.chilli).grid(row=1,column=2,padx=15,pady=5)

        item2=Label(menu,text="Noodels",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=2,column=0,padx=15,pady=10)
        p2=Label(menu,text="70/-",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=2,column=1,padx=15,pady=10)
        q2_txt=Entry(menu,width=3,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.noodel).grid(row=2,column=2,padx=15,pady=5)

        item3=Label(menu,text="Manchurian",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=3,column=0,padx=15,pady=10)
        p3=Label(menu,text="120/-",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=3,column=1,padx=15,pady=10)
        q3_txt=Entry(menu,width=3,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.manchu).grid(row=3,column=2,padx=15,pady=5)

        item4=Label(menu,text="Fried Rice",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=4,column=0,padx=15,pady=10)
        p4=Label(menu,text="100/-",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=4,column=1,padx=15,pady=10)
        q4_txt=Entry(menu,width=3,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.frice).grid(row=4,column=2,padx=15,pady=5)

        item5=Label(menu,text="Spring roll",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=5,column=0,padx=15,pady=10)
        p5=Label(menu,text="60/-",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=5,column=1,padx=15,pady=10)
        q5_txt=Entry(menu,width=3,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.rolls).grid(row=5,column=2,padx=15,pady=5)

        item6=Label(menu,text="Chopsee",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=6,column=0,padx=15,pady=10)
        p6=Label(menu,text="130/-",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=6,column=1,padx=15,pady=10)
        q6_txt=Entry(menu,width=3,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.chopse).grid(row=6,column=2,padx=15,pady=5)

        item7=Label(menu,text="Coke",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=7,column=0,padx=15,pady=10)
        p7=Label(menu,text="40/-",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=7,column=1,padx=15,pady=10)
        q7_txt=Entry(menu,width=3,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.coke).grid(row=7,column=2,padx=15,pady=5)

        item8=Label(menu,text="Pepsi",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=8,column=0,padx=15,pady=10)
        p8=Label(menu,text="35/-",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=8,column=1,padx=15,pady=10)
        q8_txt=Entry(menu,width=3,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.pepsi).grid(row=8,column=2,padx=15,pady=5)

        item9=Label(menu,text="Mountain Dew",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=9,column=0,padx=15,pady=10)
        p9=Label(menu,text="45/-",font=("times 16 bold"),fg="black",bg=bg_color2).grid(row=9,column=1,padx=15,pady=10)
        q9_txt=Entry(menu,width=3,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.dew).grid(row=9,column=2,padx=15,pady=5)

        


        # ---------------Bill Area-------------

        bill=Frame(self.root,bd=7,relief=GROOVE)
        bill.place(x=600,y=180,relwidth=.50,relheight=.57)
        bill_titel=Label(bill,text="Bill",font="arial 18 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(bill,orient=VERTICAL)
        self.billarea=Text(bill,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.billarea.yview)
        self.billarea.pack(fill=BOTH,expand=1)


        #-----------bill Action------------------
        act=LabelFrame(self.root,text="Action",font=("times",24,"bold"),fg="red",bg=bg_color1,bd=7,relief=GROOVE)
        act.place(x=0,y=700,relwidth=1,relheight=.15)

        tot_p=Label(act,text="Total Amount",font=("times 16 bold"),fg="White",bg=bg_color1).grid(row=0,column=0,padx=15,pady=10)
        tot_p_txt=Entry(act,width=8,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.total_amount).grid(row=0,column=1,padx=15,pady=5)

        tax=Label(act,text="Tax Amount",font=("times 16 bold"),fg="White",bg=bg_color1).grid(row=0,column=2,padx=15,pady=10)
        tax_txt=Entry(act,width=8,font="arial 15",bd=3,relief=SUNKEN,textvariable=self.tax).grid(row=0,column=3,padx=15,pady=5)
        
        
        ord_btn=Button(act,text="order Now",command=self.total,width=10,bd=5,font="arial 12 bold").grid(row=0,column=4,padx=20,pady=10)
        gbill_btn=Button(act,text="Generate bill",command=self.bill_area,width=10,bd=5,font="arial 12 bold").grid(row=0,column=5,padx=20,pady=10)
        clear_btn=Button(act,text="Clear All",width=10,bd=5,font="arial 12 bold",command=self.clear_data).grid(row=0,column=6,padx=20,pady=10)
        exit_btn=Button(act,text="EXIT",width=10,bd=5,font="arial 12 bold",command=self.Exit_shop).grid(row=0,column=7,padx=20,pady=10)

        

    def total(self):
        self.i1=self.chilli.get()*90
        self.i2=self.noodel.get()*70
        self.i3=self.manchu.get()*120
        self.i4=self.frice.get()*100
        self.i5=self.rolls.get()*60
        self.i6=self.chopse.get()*130
        self.i7=self.coke.get()*40
        self.i8=self.pepsi.get()*35
        self.i9=self.dew.get()*45
        self.total_price=float(
            (self.i1)+
            (self.i2)+
            (self.i3)+
            (self.i4)+
            (self.i5)+
            (self.i6)+
            (self.i7)+
            (self.i8)+
            (self.i9)
        )
        self.total_amount.set("Rs. "+str(round(self.total_price,2)))
        self.tot_tx=round(self.total_price*0.10,2)
        self.tax.set("Rs. "+str(self.tot_tx))

        self.total_bill="Rs. "+str(float(self.total_price + self.tot_tx))

    
    def welcome_bill(self):
        self.billarea.delete('1.0',END)
        self.billarea.insert(END,"\t\t\t\tWelcome to Chinees Corner\n")
        self.billarea.insert(END,f"\n Bill Id :       {self.cbillid.get()}")
        self.billarea.insert(END,f"\n Customer Name : {self.cname.get()}")
        self.billarea.insert(END,f"\n Mobile Number : {self.cnum.get()}")
        self.billarea.insert(END,f"\n================================================================================")
        self.billarea.insert(END,f"\nITEMS                      quantiy                            Amount")
        self.billarea.insert(END,f"\n================================================================================")


    def bill_area(self):
        if self.cname.get()=="" or self.cnum.get()=="":
            messagebox.showerror("error","Customer Details Are Must")
        elif self.total_amount.get()=="Rs. 0.0":
            messagebox.showerror("error","No Product is Purchased")
        else:
            self.welcome_bill()
            if self.chilli.get()!=0:
                self.billarea.insert(END,f"\n Chilli Potato                 {self.chilli.get()}                               {self.i1}")
            if self.noodel.get()!=0:
                self.billarea.insert(END,f"\n    Noodels                    {self.noodel.get()}                               {self.i2}")
            if self.manchu.get()!=0:
                self.billarea.insert(END,f"\n  Manchurian                   {self.manchu.get()}                               {self.i3}")
            if self.frice.get()!=0:
                self.billarea.insert(END,f"\n  Fried Rice                   {self.frice.get()}                               {self.i4}")
            if self.rolls.get()!=0:
                self.billarea.insert(END,f"\n  Spring Roll                  {self.rolls.get()}                               {self.i5}")
            if self.chopse.get()!=0:
                self.billarea.insert(END,f"\n    Chopsee                    {self.chopse.get()}                               {self.i6}")
            if self.coke.get()!=0:
                self.billarea.insert(END,f"\n     Coke                      {self.coke.get()}                               {self.i7}")
            if self.pepsi.get()!=0:
                self.billarea.insert(END,f"\n     Pepsi                     {self.pepsi.get()}                               {self.i8}")
            if self.dew.get()!=0:
                self.billarea.insert(END,f"\n  Mountain Dew                 {self.dew.get()}                               {self.i9}")
            self.billarea.insert(END,f"\n--------------------------------------------------------------------------------")
            if self.tax.get()!="Rs. 0.0":
                self.billarea.insert(END,f"\n   Total Tax                                                {self.tax.get()}")

            self.billarea.insert(END,f"\n--------------------------------------------------------------------------------")   
            self.billarea.insert(END,f"\n   Total Amount                                            {self.total_bill}")
            self.billarea.insert(END,f"\n================================================================================")
            self.save_bill()
    
    def save_bill(self):
        op=messagebox.askyesno("Save bill","Do you want to save bill?")
        if op>0:
            self.bill_data=self.billarea.get('1.0',END)
            f1=open("Restraunt billing System/Bills/"+ str(self.cbillid.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved","Bill Saved Successfully")
        else:
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("Restraunt billing System/Bills/"):
            if i.split('.')[0]==self.csearch.get():
                f1=open(f"Restraunt billing System/Bills/{i}","r")
                self.billarea.delete('1.0',END)
                for d in f1:
                    self.billarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("error","Invalid Bill Id!")
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to Clear Data?")
        if op>0:
            self.chilli.set(0)
            self.noodel.set(0)
            self.manchu.set(0)
            self.frice.set(0)
            self.rolls.set(0)
            self.chopse.set(0)
            self.coke.set(0)
            self.pepsi.set(0)
            self.dew.set(0)

            # --------------customer variable-----------
            self.cname.set("")
            self.cnum.set("")
            self.cbillid.set("")
            x=random.randint(10000,99999)
            self.cbillid.set(str(x))
            self.csearch.set("")
            self.total_amount.set("")
            self.tax.set("")
            self.welcome_bill()
    def Exit_shop(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()


root=Tk()
shop= Restraunt(root)
root.mainloop()
