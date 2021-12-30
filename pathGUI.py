import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

'''
TODO:
· responsive size
· radio button ZIP: se attivo restituisci archivio ZIP
'''

class GUI():
    def __init__(self):
        self.address = ""
        self.gui = tk.Tk()
        self.gui.geometry("300x300")
        self.gui.title("pdf2png")


        #LABEL
        self.l1 = tk.Label(text="Path:")
        self.l1.place(x=80, y=100)

        #BUTTON
        self.button = tk.Button(text="Scegli", command=self.browseFile)
        self.button.place(x=130, y=100)

        self.gui.mainloop()


    def browseFile(self):
        """
        Seleziona file da explorer

        Parameters
        ----------
        """
        self.address = filedialog.askopenfilename(filetypes = (("PDF files", "*.pdf"), ("All files", "*")))
        self.gui.destroy()
      
