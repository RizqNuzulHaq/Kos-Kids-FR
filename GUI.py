import os
import tkinter as tk
import tkinter as ttk
from tkinter import filedialog
from tkinter import messagebox
import shutil
from PIL import ImageTk
from tkPDFViewer import tkPDFViewer as pdf
import CNN

def moveDir(original, folder):
    target = r'' + CNN.directory + folder
    if os.path.isdir(target):
        shutil.rmtree(target)

    shutil.copytree(original, target)
    button1["state"] = "disable"

def moveDataset(original):
    target = r'dataset'
    if os.path.isdir(target):
        shutil.rmtree(target)

    shutil.copytree(original, target)
    button1["state"] = "disable"


def runTrain():
    isExist = os.path.exists(CNN.directory)
    if isExist == False:
        messagebox.showerror("Error", "You dont have dataset")
    else:
        CNN.cnn(CNN.directory)
        button1["state"] = "normal"

def runMain():
    isExist = os.path.exists(CNN.directory)
    if isExist == False:
        messagebox.showerror("Error", "You dont have dataset")
    else:
        CNN.tes(CNN.directory)


root = tk.Tk()
root.title("Face Recognizer")
root.resizable(False, False)
root.geometry("300x650")
root.configure(bg="#17161b")

#Image frame
imageFrame = ttk.Frame(root,bg="#17161b")
#penempatan
imageFrame.pack(padx=10,pady=10,fill="x",expand=True)

#Komponen
label = tk.Label(imageFrame, text="Face Recognition",font=("CONSOLAS BOLD", 16), fg="WHITE",bg="#17161b")
label.pack(padx=10,pady=10,fill="x",expand=True)
render = ImageTk.PhotoImage(file='facial-recognition.png')
img = tk.Label(imageFrame, image=render,bg="#17161b")
img.pack(padx=10,pady=10,fill="x",expand=True)

def add():
    def open():
        top.filename = filedialog.askdirectory(initialdir="D:", title="Select A Folder")
        if top.filename != "":
            response = messagebox.askyesno("Alert", "Are you sure?")
            if response == 1:
                if e.get() == "":
                    messagebox.showerror("Error", "Name field cant be empty")
                    top.destroy()

                moveDir(top.filename,e.get())
                top.destroy()
                messagebox.showinfo("Info", "Dont forget to retrain the dataset")
            else:
                top.destroy()


    top = ttk.Toplevel()
    top.title("Add Face")
    top.resizable(True, True)
    top.geometry("350x170")
    top.configure(bg="#17161b")
    label = tk.Label(top,text="Faces List\n____", font=("CONSOLAS BOLD", 8), fg="WHITE", bg="#17161b").pack(pady=5, padx=5)
    info = tk.Label(top, text=os.listdir(CNN.directory), font=("CONSOLAS BOLD", 8), fg="WHITE", bg="#17161b")
    info.pack(pady=5, padx=5)
    label = tk.Label(top, text="Name\n____", font=("CONSOLAS BOLD", 8), fg="WHITE", bg="#17161b")
    label.pack(pady=5, padx=5)
    e = tk.Entry(top, width=50)
    e.pack()
    buttonOpen =  tk.Button(top, text="Add Face", command =open , font=("CONSOLAS",10,"bold"),bg="#2a2d36", fg="WHITE")
    buttonOpen.pack(pady=5,padx=5)

def Change():

    def open():
        filename = filedialog.askdirectory(initialdir="D:", title="Select A Folder")
        if filename != "":
            response = messagebox.askyesno("Alert", "Are you sure?")

            if response == 1:
                CNN.directory = filename + "/"
                moveDataset(filename)
                print(CNN.directory)
                top.destroy()
                button2["state"] = "normal"
                
                messagebox.showinfo("Info", "Dont forget to retrain the dataset")
            else:
                top.destroy()

    top = ttk.Toplevel()
    top.title("Change Dataset")
    top.resizable(True, False)
    top.geometry("300x150")
    top.configure(bg="#17161b")
    info = tk.Label(top, text="Dataset Directory :", font=("CONSOLAS BOLD", 8), fg="WHITE",
                    bg="#17161b")
    info.pack(pady=5, padx=5)
    label = tk.Label(top, text=CNN.directory, font=("CONSOLAS BOLD", 8), fg="WHITE", bg="#17161b")
    label.pack(pady=5, padx=5)
    buttonOpen = tk.Button(top, text="Open File", command=open, font=("CONSOLAS", 10, "bold"), bg="#2a2d36", fg="WHITE")
    buttonOpen.pack(pady=5, padx=5)

def showManual():
    top = ttk.Toplevel()
    top.title("Manual")
    top.resizable(True, True)
    top.geometry("550x750")
    top.configure(bg="#17161b")
    v1 = pdf.ShowPdf()
    v2 = v1.pdf_view(top,
                     pdf_location=open(r"Manual/Manual.pdf"),
                     width=70, height=100)
    v2.pack()

button1 = tk.Button(imageFrame, text="Start", command =runMain , font=("CONSOLAS",10,"bold"),bg="#2a2d36", fg="WHITE", state="normal")
button2 = tk.Button(imageFrame, text="Add Face", command =add, font=("CONSOLAS",10,"bold"),bg="#2a2d36", fg="WHITE", state="normal")
button3 = tk.Button(imageFrame, text="Train", command =runTrain, font=("CONSOLAS",10,"bold"),bg="#2a2d36", fg="WHITE")
button4 = tk.Button(imageFrame, text="Change/Add Dataset", command =Change, font=("CONSOLAS",10,"bold"),bg="#2a2d36", fg="WHITE")
button6 = tk.Button(imageFrame, text="Manual", command =showManual, font=("CONSOLAS",10,"bold"),bg="#2a2d36", fg="WHITE")
button5 = tk.Button(imageFrame, text="Exit",command=root.quit,font=("CONSOLAS",10,"bold"),bg="#2a2d36", fg="WHITE")
button1.pack(padx=10,pady=10,fill="x",expand=True)
button2.pack(padx=10,pady=10,fill="x",expand=True)
button4.pack(padx=10,pady=10,fill="x",expand=True)
button3.pack(padx=10,pady=10,fill="x",expand=True)
button6.pack(padx=10,pady=10,fill="x",expand=True)
button5.pack(padx=10,pady=10,fill="x",expand=True)


if os.path.exists(CNN.directory) == True:
    button3["state"] = "normal"
    button2["state"] = "normal"
    button1["state"] = "normal"
else:
    button3["state"] = "disabled"
    button2["state"] = "disabled"
    button1["state"] = "disabled"

root.wm_iconphoto(False,render)
root.mainloop()