from tkinter import *
window = Tk()
window.title("BMI CALCULATOR")
window.geometry("380x400")
window.configure(bg="lightcyan")
def calculatebmi():
    weight=int(weightentry.get())
    height=int(heightentry.get())/100
    bmi=weight/height*height
    bmi=round(bmi,1)
    name=username.get()
    resultlabel.destroy()
    message={}
    if bmi<18.5:
        message="You are underweighted"
    elif bmi>18.5 and bmi<=24.9:
        message="You are in normal range"
    elif bmi>25 and bmi<=29.9:
        message="You are over weighted"
    elif bmi>30:
        message="Obesity"
    else:
        message="Something went wrong"
    outputmessage=Label(resultframe,text=f"{name}Your BMI is {bmi} and {message}",bg="lightcyan",font=("Calibri",12),width=42)
    outputmessage.place(x=20,y=40)
    outputmessage.pack()


applabel=Label(window,text="BMI CALCULATOR",fg="black",bg="lightcyan",font=("Calibri",20),bd=5)
applabel.place(x=50,y=20)

namelabel=Label(window,text="Name",fg="black",bg="lightcyan",font=("Calibri",10),bd=5)
namelabel.place(x=20,y=90)

username=Entry(window,text="",bd=2,width=22)
username.place(x=150,y=92)

heightlabel=Label(window,text="Enter Your Height",fg="black",bg="lightcyan",font=("Calibri",10),bd=5)
heightlabel.place(x=20,y=140)

heightentry=Entry(window,text="",bd=2,width=22)
heightentry.place(x=150,y=142)

weightlabel=Label(window,text="Enter Your Weight",fg="black",bg="lightcyan",font=("Calibri",10),bd=5)
weightlabel.place(x=20,y=185)

weightentry=Entry(window,text="",bd=2,width=22)
weightentry.place(x=150,y=187)

calculatebutton=Button(window,text="Calculate",fg="black",bg="cyan",font=("Calibri",10),bd=5,command=calculatebmi)
calculatebutton.place(x=20,y=250)

resultframe=LabelFrame(window,text="Result",fg="black",bg="lightcyan",font=("Calibri",10))
resultframe.pack(padx=20,pady=20)
resultframe.place(x=20,y=300)

resultlabel=Label(resultframe,text="",fg="black",bg="lightcyan",font=("Calibri",10),width=33)
resultlabel.place(x=20,y=20)
resultlabel.pack()


window.mainloop()

