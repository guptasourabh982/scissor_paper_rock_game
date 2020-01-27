from tkinter import *
import random


comp_score = 0
user_score = 0

def update(inp):
    Comp = random.randint(1, 3)
    global comp_score
    global user_score

    if inp == 1:
        user1["image"] = None
        user1.configure(image=u1)
        user2["text"] = ""
        user2.configure(text="Scissor")

    elif inp == 2:
        user1["image"] = None
        user1.configure(image=u2)
        user2["text"] = ""
        user2.configure(text="Paper")
    elif inp == 3:
        user1["image"] = None
        user1.configure(image=u3)
        user2["text"] = ""
        user2.configure(text="Rock")

    if Comp == 1:
        comp1["image"] = None
        comp1.configure(image=u1)
        comp2["text"] = ""
        comp2.configure(text="Scissor")
    elif Comp == 2:
        comp1["image"] = None
        comp1.configure(image=u2)
        comp2["text"] = ""
        comp2.configure(text="Paper")

    elif Comp == 3:
        comp1["text"] = None
        comp1.configure(image=u3)
        comp2["text"] = ""
        comp2.configure(text="Rock")



    if (Comp == 1 and inp == 2) or (Comp == 2 and inp == 3) or (Comp == 3 and inp == 1):
        comp_score += 1
        l3.config(text=comp_score)
    elif (Comp == 2 and inp == 1) or (Comp == 3 and inp == 2) or (Comp == 1 and inp == 3):
        user_score += 1
        l4.config(text=user_score)
    elif (Comp == 1 and inp == 1) or (Comp == 2 and inp == 2) or (Comp == 3 and inp == 3):
        pass

def reset():
    l3.configure(text="0")
    l4.configure(text="0")
    user1.configure(image="")
    comp1.configure(image="")
    user2.configure(text="")
    comp2.configure(text="")

def exit():
    root.destroy()

root = Tk()
root.title("SPC_game")
root.geometry("700x680+300+0")
root.config(bg="white")


u1 = PhotoImage(file="scisor.png" )
u2 = PhotoImage(file="pap.png" )
u3 = PhotoImage(file="rok.png" )



root.resizable(0, 0)

Label(root,bg="white", fg="brown", font="TimesNewRoman 20 bold", text="Scissor/Paper/Rock").place(x=210,y=0)

l1 = Label(root, bg="white", fg="black", font="TimesNewRoman 18 bold", text="Computer score:")
l1.place(x=10, y=60)
l3 = Label(root, bg="white", fg="black", font="TimesNewRoman 18 bold", text="0")
l3.place(x=220, y=60)
l2 = Label(root, bg="white", fg="black", font="TimesNewRoman 18 bold", text="User score:")
l2.place(x=450, y=60)
l4 = Label(root,bg="white", fg="black", font="TimesNewRoman 18 bold", text="0")
l4.place(x=600, y=60)

comp = Label(root, bg="white", fg="darkblue", font="TimesNewRoman 18 bold", text="Computer's choice:")
comp.place(x=10, y=150)
comp1 = Label(root,bg="white")
comp1.place(x=30, y=200)
comp2 = Label(root,bg="white", fg="blue", font="TimesNewRoman 16 bold")
comp2.place(x=50, y=400)
user = Label(root,bg="white", fg="darkblue", font="TimesNewRoman 16 bold", text="User's choice:")
user.place(x=450, y=150)
user1 = Label(root,bg="white")
user1.place(x=455, y=200)
user2 = Label(root,bg="white", fg="blue", font="TimesNewRoman 15 bold")
user2.place(x=480, y=400)


b1 = Button(root, bg="white", fg="grey", border="0", font="TimesNewRoman 18 bold", text="Scissors", command=lambda:update(1) )
b1.place(x=140, y=450)
b2 = Button(root, bg="white", fg="grey", border="0", font="TimesNewRoman 18 bold", text="Paper", command=lambda:update(2) )
b2.place(x=285, y=450)
b3 = Button(root, bg="white", fg="grey", border="0", font="TimesNewRoman 18 bold", text="Rock", command=lambda:update(3) )
b3.place(x=440, y=450)

b2 = Button(root, bg="white", fg="red", border="0", font="TimesNewRoman 13 bold", text="Reset", height=1, width=5, command=reset )
b2.place(x=200, y=600)
b3 = Button(root, bg="white", fg="red", border="0", font="TimesNewRoman 13 bold", text="Exit", height=1, width=5, command=exit )
b3.place(x=375, y=600)
root.mainloop()
