import customtkinter as ctk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

current_qr_image = None


def generate_qr():
    global current_qr_image
    text = entry.get()

    if text.strip() == "":
        messagebox.showerror("Error", "Please enter some text!")
        return

    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    current_qr_image = img

    ctk_img = ctk.CTkImage(light_image=img.get_image(), dark_image=img.get_image(), size=(200, 200))
    
    qr_label.configure(image=ctk_img, text="") 
    print("QR Generated")

def save_qr():
    global current_qr_image
    
    if current_qr_image is None:
        messagebox.showerror("Error", "Generate a QR Code first!")
        return

    file_path = filedialog.asksaveasfilename(
        initialfile="my_qr_code",
        defaultextension=".png",
        filetypes=[("PNG file", "*.png"), ("JPEG file", "*.jpg")],
        title="Save QR Code"
    )

    if file_path:
        try:
            current_qr_image.save(file_path)
            messagebox.showinfo("Success", "QR Code Saved Successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save: {e}")


app = ctk.CTk()
app.geometry("400x550")
app.title("QR Generator Pro")
app.resizable(False, False)


title_label = ctk.CTkLabel(app, text="QR Code Generator", font=("Roboto Medium", 24))
title_label.pack(pady=(30, 20))


entry = ctk.CTkEntry(app, placeholder_text="Enter text or URL here...", width=300, height=40, font=("Roboto", 14))
entry.pack(pady=10)


btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=10)


btn_generate = ctk.CTkButton(
    btn_frame, 
    text="Generate", 
    command=generate_qr, 
    width=140, height=35,
    font=("Roboto", 14, "bold"),
    fg_color="#3B8ED0", hover_color="#1F6AA5"
)
btn_generate.pack(side="left", padx=10)


btn_save = ctk.CTkButton(
    btn_frame, 
    text="Save Image", 
    command=save_qr, 
    width=140, height=35,
    font=("Roboto", 14, "bold"),
    fg_color="#2CC985", hover_color="#1FA468"
)
btn_save.pack(side="left", padx=10)


qr_frame = ctk.CTkFrame(app, width=220, height=220, corner_radius=10)
qr_frame.pack(pady=30)
qr_frame.pack_propagate(False) 

qr_label = ctk.CTkLabel(qr_frame, text="QR will appear here")
qr_label.pack(expand=True, fill="both", padx=10, pady=10)

app.mainloop()