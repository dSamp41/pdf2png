import pathGUI
import pdf2png as convTool

view = pathGUI.GUI()
path = view.address
#print(path)

if(path != ""):
    print(path) 
    convTool.pdf2png(path)