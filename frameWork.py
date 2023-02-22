from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
import os

master = Tk()

class App(Tk):

    def __init__(self, *args, **kwargs):

        master.title("Note Application")

        self.img = PhotoImage(file="note-icon.png")
        master.iconphoto(False,self.img)

        self.canvas = Canvas(master,height=750,width=500)
        self.canvas.pack()

        self.top_frame = Frame(master,bg="#b6facc")
        self.top_frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.15)

        self.middle_frame = Frame(master,bg="#b6facc")
        self.middle_frame.place(relx=0.05,rely=0.22,relwidth=0.9,relheight=0.4)

        self.bottom_frame = Frame(master,bg="#b6facc")
        self.bottom_frame.place(relx=0.05,rely=0.64,relwidth=0.9,relheight=0.31)

        self.main_title_label = Label(self.top_frame,font=("Verdana",20,"bold"),text="Note Application",bg="#b6facc")
        self.main_title_label.place(x=100,y=35)

        self.empty_text = "Please write your note down here..."
        self.text_field = Text(self.middle_frame,height=18,width=49,font=("Verdana",10,"bold"))
        self.text_field.place(x=5,y=5)
        self.text_field.tag_configure('style',foreground="#bfbfbf",font=("Verdana",7,"bold"))
        self.text_field.insert(END,self.empty_text,'style')

        self.file_button = Button(self.bottom_frame,text="Select File",font=("Verdana",7,"bold"),height=2,width=20,command=self.ask_directory)
        self.file_button.pack(padx=5,pady=5,anchor="n")

        self.file_dir_label = Label(self.bottom_frame,text="...",font=("Verdana",7,"bold"),bg="#b6facc")
        self.file_dir_label.pack(padx=5,pady=5,anchor="n")

        self.file_name_field = Entry(self.bottom_frame,font=("Verdana",7,"bold"),width=30)
        self.file_name_field.pack(padx=5,pady=5,anchor="n")

        self.save_button = Button(self.bottom_frame,text="Save",font=("Verdana",15,"bold"),height=2,width=15,command=self.save)
        self.save_button.pack(padx=5,pady=20,anchor="n")

        self.now = datetime.now()

    def ask_directory(self):

        self.file_path = filedialog.askdirectory()
        self.file_dir_label.config(text=self.file_path)

    def save(self):

        try:

            self.file_name = self.file_name_field.get()
            self.note = self.text_field.get("1.0","end")

            self.full_file_name = os.path.join(self.file_path,self.file_name) + ".txt"

            with open(self.full_file_name,"a",encoding="utf-8") as file:
                file.write(f"Date: {self.now}\nNote:\n{self.note}\n")

            message = "Your note has been saved!"
            messagebox.showinfo("Success!",message)

        except Exception as err:

            message = "Please be sure that all blanks are filled!"
            messagebox.showerror("Failed!",message)
        
        finally:

            master.destroy()

note_app = App()
master.mainloop()