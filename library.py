from tkinter import *

class TimetableGenerator:
    def __init__(self,root):
        self.root=root
        self.root.title("Timetable Generator")
        self.root.geometry("1520x800+0+0")

        lbltitle=Label(self.root,text="Automated Timetable Generator",bg="cyan",fg="black",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)



if __name__=="__main__":
    root=Tk()
    obj=TimetableGenerator(root)
    root.mainloop()
