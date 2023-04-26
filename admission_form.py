from tkinter import *
from tkinter import messagebox

def admission():
    kk = Tk()
    kk.geometry("500x500")
    kk.title("Admission Form")
    kk.config(bg="grey")

    l=Label(kk,text="Admission Form",bg="grey",font=("Arial",30,"bold"))
    l.place(x=500,y=0)

    l1=Label(kk,text="Admission No. : ",bg="grey",font=("Arial",13,"bold"))
    l1.place(x=400,y=60)
    e1=Entry(kk,width=40)
    e1.place(x=600,y=60)

    l2=Label(kk,text="Full Name : ",bg="grey",font=("Arial",13,"bold"))
    l2.place(x=400,y=90)
    e2=Entry(kk,width=40)
    e2.place(x=600,y=90)

    l3=Label(kk,text="Date of Birth : ",bg="grey",font=("Arial",13,"bold"))
    l3.place(x=400,y=120)
    e3=Entry(kk,width=40)
    e3.place(x=600,y=120)

    l4 = Label(kk,text="Gender",bg="grey",font=("Arial",13,"bold"))
    l4.place(x=400,y=150)
    var = IntVar()
    Radiobutton(kk,text="Male",bg="grey",font=("Arial",10,"bold"),variable=var,value=1).place(x=600,y=150)
    Radiobutton(kk,text="Female",bg="grey",font=("Arial",10,"bold"),variable=var,value=2).place(x=680,y=150)
    Radiobutton(kk,text="Other",bg="grey",font=("Arial",10,"bold"),variable=var,value=3).place(x=760,y=150)
    
    l3=Label(kk,text="Phone No. : ",bg="grey",font=("Arial",13,"bold"))
    l3.place(x=400,y=180)
    e3=Entry(kk,width=40)
    e3.place(x=600,y=180)

    l4=Label(kk,text="Address : ",bg="grey",font=("Arial",13,"bold"))
    l4.place(x=400,y=210)
    e4=Entry(kk,width=40)
    e4.place(x=600,y=210)

    l5=Label(kk,text="Course : ",bg="grey",font=("Arial",13,"bold"))
    l5.place(x=400,y=240)
    options_list = ["Python","C++", "Java", "Perl","Php","Kotlin"]
    clicked = StringVar(kk)
    clicked.set("            Select your course :            ")
    course_menu = OptionMenu(kk, clicked, *options_list)
    course_menu.place(x=600,y=240)

    var1=StringVar()
    var1.set(False)
    var2=StringVar()
    var2.set(False)
    var3=StringVar()
    var3.set(False)

    l6=Label(kk,text="Language : ",bg="grey",font=("Arial",13,"bold"))
    l6.place(x=400,y=280)
    c1=Checkbutton(kk, text="Hindi", variable=var1, onvalue="Hindi",font=("Arial",13))
    c1.place(x=600,y=280)
    c2=Checkbutton(kk, text="English", variable=var2, onvalue="English",font=("Arial",13))
    c2.place(x=700,y=280)
    c3=Checkbutton(kk, text="Gujrati", variable=var3, onvalue="Gujrati",font=("Arial",13))
    c3.place(x=800,y=280)

    var4=StringVar()
    var4.set(False)
    ch=Checkbutton(kk, text="*Terms & Conditions Apply",bg="grey", variable=var4, onvalue="*Terms & Conditions Apply",font=("Arial",8))
    ch.place(x=550,y=320)

    b1=Button(kk,text="Submit",bg="yellow",fg="black",activebackground="red",font=("Arial",13,"bold"))
    b1.place(x=600,y=340)

    b2=Button(kk,text="Click me to close Admission Form",bg="red",fg="black",activebackground="yellow",command=kk.destroy)
    b2.place(x=550,y=380)

    kk.mainloop()

admission()






















    
    
