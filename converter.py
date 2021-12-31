import pathGUI
import pdf2png as convTool

view = pathGUI.GUI()
path = view.address

if(path != "")
    ui2 = pathGUI.threadedGUI()
    p = convTool.pdf2png(path).replace("/", "\\")

    subprocess.Popen(r'explorer /select, {}'.format(p))    #open dialog w/ original file & folder w/ splitted pages
    ui2.gui.destroy()
