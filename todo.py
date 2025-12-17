import customtkinter as ctk
import json
from tkinter import messagebox
import os
from PIL import Image
file_path = "todo.json"

def read_json():
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def write_json(new_data):
    with open(file_path, "w") as f:
        json.dump(new_data, f, indent=4)

def main():

    if taskval.get() !="":
          datas=read_json()
          datas["tasks"].append(taskval.get())
          write_json(datas)
          taskval.set("")

    for widget in f22.winfo_children():
            widget.destroy()
            

    data1=read_json()

    for task in data1.get("tasks"):
        var=ctk.BooleanVar() 

        def on_check(t=task, v=var):
                    if v.get():
                        data1["tasks"].remove(t)
                        write_json(data1)
                        messagebox.showinfo("Congratulation",f"🎉 {t} completed")
                        main()
                        root.update()

        cd=ctk.CTkCheckBox(f22,text=task,variable=var,onvalue=True,offvalue=False,
                           command=lambda t=task, v=var: on_check(t, v),)
        cd.pack(anchor="w", pady=5, padx=10)



if __name__=="__main__":

    if not os.path.exists(file_path):
         with open(file_path,"w",encoding="utf-8") as f:
              json.dump({"tasks":[]},f,indent=4)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root=ctk.CTk()
    root.iconbitmap("logo.ico")
    root.geometry("350x450")
    root.title("📋 To-Do-List")
    mainframe=ctk.CTkFrame(root,fg_color="#000000",bg_color="#000000")
    mainframe.pack(fill="both",expand=True)
    f1=ctk.CTkFrame(mainframe,height=70,fg_color="#000000")
    f1.pack(side="top",fill="x",padx=10,pady=5)

    f2=ctk.CTkFrame(mainframe,height=350,fg_color="#000000")
    f2.pack(fill="both",padx=10,pady=10)

    f21=ctk.CTkFrame(f2,height=50,fg_color="#000000")
    f21.pack(fill="both",padx=10,pady=10)

    f22=ctk.CTkScrollableFrame(f2,height=350,width=350,fg_color="#000000")
    f22.pack(fill="both",padx=10,pady=10,expand=True)

    l1=ctk.CTkLabel(f1,text="To-Do-List",font=("Algerian",30,"bold","underline"))
    l1.pack(pady=2)

    taskval=ctk.StringVar()

    e1=ctk.CTkEntry(f21,width=200,textvariable=taskval)
    e1.pack(side="left")
    e1.bind("<Return>",lambda event:b1.invoke())
    b1=ctk.CTkButton(f21,text="add",width=100,command=main)
    b1.pack(side="right")

    main()

    root.mainloop()