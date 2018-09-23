import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# create our window
app = QApplication(sys.argv)
w =QMainWindow()
w.setWindowTitle('TA')
w.resize(640, 200)


#labels2
nameLabel2 = QLabel(w)
nameLabel2.setText('Project')
line2 = QLineEdit()
line2.move(60,20)
line2.resize(200,32)
nameLabel2.move(20,20)

# Create combobox
combo2 = QComboBox(w)
combo2.addItems(["C","P"])
combo2.move(80,20)


#labels3
nameLabel3 = QLabel(w)
nameLabel3.setText('WB')
line3 = QLineEdit()
line3.move(20,80)
line3.resize(200,32)
nameLabel3.move(20,60)


# Create textbox
textbox = QLineEdit(w)
textbox.move(90,60)
textbox.resize(210, 30)

# Create a button in the window
button = QPushButton('Publish', w)
button.move(90, 100)

#Exit
button2 = QtGui.QPushButton('Exit', w)
button2.move(210, 100)

#Browse
button3 = QtGui.QPushButton('Browse', w)
button3.move(310, 60)


def browse():
    filename = QFileDialog.getOpenFileName(w, 'Open File', 'C:\\')
    return filename

input = []

# Browse Create the actions
@pyqtSlot()
def on_click3():
    result2 = browse()
    textbox.setText(result2)
    input.append(result2)

# Browse Create the actions
@pyqtSlot()
def on_click2():
    project_name = combo2.currentText()
    print(project_name)
    if (len(input) == 0):
        print ("Please select the workbook")
    else:
        print(input[0])

        







def window_open():
    # connect the signals to the slots
    button2.clicked.connect(QtCore.QCoreApplication.instance().quit)
    button.clicked.connect(on_click2)
    button3.clicked.connect(on_click3)
    w.show()
    app.exec_()


window_open()
