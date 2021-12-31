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
      
    
class threadedGUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.gui.quit()

    def run(self):
        self.gui = tk.Tk()
        self.gui.geometry("300x300")
        self.gui.title("pdf2png")
        self.gui.protocol("WM_DELETE_WINDOW", self.callback)

        #LABEL
        self.label = tk.Label(text="Conversione in corso")
        self.label.place(x=100, y=100)

        self.gui.mainloop()
