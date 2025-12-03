import customtkinter as ctk
import tkinter.messagebox as tmsg
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
def click(text_value):
    global scvalue
    text = text_value
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
            screen.configure(text_color="#ff4444") 
        else:
            try:
                value = eval(screen.get())
                screen.configure(text_color="#ff4444") 
            except Exception as e:
                tmsg.showinfo("Alert", "Input Error")
                value = "Error"
                screen.configure(text_color="#ff4444")
        
        scvalue.set(value)
        
    elif text == "C":
        scvalue.set("")
        screen.configure(text_color="#3B8ED0") 
        
    elif text == "⌫":
        current_val = scvalue.get()
        scvalue.set(current_val[:-1])
        screen.configure(text_color="#3B8ED0") 
        
    else:
        screen.configure(text_color="#3B8ED0")
        scvalue.set(scvalue.get() + text)

# --- Keyboard Binding Function ---
def key_event(event):
    key = event.keysym
    char = event.char
    if key == "Return":
        click("=")
    elif key == "BackSpace":
        click("⌫")
    elif key == "Escape":
        click("C")
    else:
        if char in "0123456789./*-+":
            click(char)

# --- GUI Setup ---
root = ctk.CTk()
root.geometry("350x450")
root.minsize(350, 450)
root.title("CALCULATOR --suraj😎")
root.configure(fg_color="#000000")
root.bind("<Key>", key_event)

scvalue = ctk.StringVar()
scvalue.set("")

# --- Screen ---
screen = ctk.CTkEntry(root, textvariable=scvalue, font=("Arial", 35, "bold"), 
                      justify="right", fg_color="#101010", text_color="#3B8ED0", 
                      border_color="#3B8ED0", border_width=2)
screen.pack(fill="x", ipadx=8, padx=15, pady=20)

main_frame = ctk.CTkFrame(root, fg_color="transparent")
main_frame.pack(expand=True)

px = 5
py = 5
btn_width = 70
btn_height = 55

def frame(b1, b2, b3, b4):
    l = [b1, b2, b3, b4]
    f = ctk.CTkFrame(main_frame, fg_color="transparent")
    
    for i in l:
        if i in ["*", "-", "+", "/"]:
            btn_color = "#1f6aa5" 
            hover_c = "#144870"
        else:
            btn_color = "#1f1f1f" 
            hover_c = "#333333"

        b = ctk.CTkButton(f, text=i, font=("Arial", 22, "bold"), 
                          width=btn_width, height=btn_height, 
                          fg_color=btn_color, hover_color=hover_c,
                          command=lambda x=i: click(x)) 
        
        b.pack(side="left", padx=px, pady=py)
        
    f.pack(anchor="center", pady=2) 

frame("7", "8", "9", "/")
frame("4", "5", "6", "*")
frame("1", "2", "3", "-")
frame("C", "0", ".", "+")

f1 = ctk.CTkFrame(main_frame, fg_color="transparent")

b_eq = ctk.CTkButton(f1, text="=", font=("Arial", 22, "bold"), 
                     width=230, height=btn_height, 
                     fg_color="#1f6aa5", hover_color="#144870",
                     command=lambda: click("="))
b_eq.pack(side="left", padx=px, pady=py)

b_back = ctk.CTkButton(f1, text="⌫", font=("Arial", 22, "bold"), 
                       width=btn_width, height=btn_height, 
                       fg_color="#c42b1c", hover_color="#8a1c11",
                       command=lambda: click("⌫"))
b_back.pack(side="left", padx=px, pady=py)

f1.pack(anchor="center", pady=2)

root.mainloop()