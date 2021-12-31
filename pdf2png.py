import PyPDF2
import pngify
import os.path
from os import PathLike

"""
TODO:
·(V) Decidere path di output
·(V) Conversione pdf -> png
· Restituire tutto in zip
"""

# 1 pdf -> n pdf, n = #pagine
def splitPDF(path):
    filename = pngify.getNameFromPath(path)
    pdfRead = PyPDF2.PdfFileReader(path)

    for page in range(pdfRead.getNumPages()):
        pdfWrite = PyPDF2.PdfFileWriter()                                    #all'interno di ciclo -> file vuoto ad ogni iterazione
        pdfWrite.addPage(pdfRead.getPage(page))


        output = f"\page{page+1}.pdf"                                        #nome pagina
        directory = os.path.split(path)[0]                                   #directory 
        outputFileName = directory + output                                  #path completo

        with open(outputFileName, "wb") as out:
            pdfWrite.write(out)
    
        print(f"Created: {outputFileName}")
    

def pdf2png(path: PathLike):
    """
      Divide pdf in pagine in formato png

    Parameters
    ----------
    path: path-like object
        path del documento pdf
    """
    filename = pngify.getNameFromPath(path)
    pdfRead = PyPDF2.PdfFileReader(path)

    directory = os.path.split(path)[0]                                      #directory
    extraFolder = f"\{filename}_Split"
    os.mkdir(directory + extraFolder)    #crea cartella dove inserire file
    

    for page in range(pdfRead.getNumPages()):
        pdfWrite = PyPDF2.PdfFileWriter()  #all'interno di ciclo -> file vuoto ad ogni iterazione
        pdfWrite.addPage(pdfRead.getPage(page))


        output = f"\{filename}_page{page+1}.pdf"                             #numero pagina
        outputFileName = directory + extraFolder + output                    #path completo
    
        with open(outputFileName, "wb") as out:
            pdfWrite.write(out)
            
        pngify.pngify(outputFileName, directory+extraFolder)
        os.remove(outputFileName)

        print(f"Created: {outputFileName}")
        
    return path
