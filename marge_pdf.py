import customtkinter as ctk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter
import os

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

pdf_files = [] 
count = 0

def upload():
    global count
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File to Upload",
        filetypes=(("Select PDF", "*.pdf"), ("All files", "*.*"))
    )
    
    if file_path:
        try:
            filename = os.path.basename(file_path)
            
            pdf_files.append(file_path)
            
            file_label = ctk.CTkLabel(
                scrollable_frame, 
                text=f"{count + 1}. {filename}", 
                anchor="w", 
                fg_color=("gray85", "gray25"), 
                corner_radius=6,
                height=30
            )
            file_label.pack(fill="x", pady=2, padx=5)

            count += 1
            status_label.configure(text=f"{count} files ready to merge", text_color="blue")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error in selecting file: {e}")

def merge_save():
    if not pdf_files:
        messagebox.showwarning("Warning", "Please upload PDF files first!")
        return

    merger = PdfWriter()
    output_save = "" 
    
    try:
        for pdf in pdf_files:
            merger.append(pdf)
        
        output_save = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            title="Save Combined PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )

        if output_save:
            merger.write(output_save)
            messagebox.showinfo("Successful", "PDF Merged and Saved Successfully!")
            
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving file: {e}")
    finally:
        merger.close()


root = ctk.CTk()
root.geometry("500x550")
root.title("Modern PDF Merger")

label_title = ctk.CTkLabel(root, text="PDF Merger Tool", font=("Roboto Medium", 24))
label_title.pack(pady=20)

scrollable_frame = ctk.CTkScrollableFrame(root, label_text="Selected Files", width=400, height=250)
scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

button_frame = ctk.CTkFrame(root, fg_color="transparent")
button_frame.pack(pady=20)

btn_add = ctk.CTkButton(button_frame, text="Add PDF", command=upload, width=150, height=40)
btn_add.grid(row=0, column=0, padx=10)

btn_save = ctk.CTkButton(button_frame, text="Merge & Save", command=merge_save, width=150, height=40, 
                         fg_color="green", hover_color="darkgreen")
btn_save.grid(row=0, column=1, padx=10)

status_label = ctk.CTkLabel(root, text="No files selected", text_color="black")
status_label.pack(pady=(0, 20))

root.mainloop()