import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import editcheck
import os


# create our window
app = QApplication(sys.argv)
w =QMainWindow()
w.setWindowTitle('EDM')
# Set window size.
w.resize(640, 200)


# Create textbox
textbox = QLineEdit(w)
textbox.move(80,80)
textbox.resize(210, 30)

# Create textbox2
textbox2 = QLineEdit(w)
textbox2.move(80,110)
textbox2.resize(210, 30)


# Set window size.
#w.resize(320, 150)

# Create a button in the window
button = QPushButton('Generate', w)
button.move(90, 150)

#Exit
button2 = QtGui.QPushButton('Exit', w)
button2.move(200, 150)

#Browse
button3 = QtGui.QPushButton('Browse', w)
button3.move(290, 80)

#Browse
button4 = QtGui.QPushButton('Browse', w)
button4.move(290, 110)

# Create combobox
combo = QComboBox(w)
combo.addItems(["H", "p","o"])
combo.move(80, 20)


# Create combobox
combo2 = QComboBox(w)
combo2.addItems(["C","P"])
combo2.move(80, 50)

#labels
nameLabel = QLabel(w)
nameLabel.setText('Sc')
line = QLineEdit()
line.move(60,20)
line.resize(200,32)
nameLabel.move(20,20)

#labels2
nameLabel2 = QLabel(w)
nameLabel2.setText('Qua')
line2 = QLineEdit()
line2.move(20,80)
line2.resize(200,32)
nameLabel2.move(20,50)


#labels3
nameLabel3 = QLabel(w)
nameLabel3.setText('Input')
line3 = QLineEdit()
line3.move(20,80)
line3.resize(200,32)
nameLabel3.move(20,80)

result4 = textbox.text()
print(result4)
textbox.setText("")

#labels3
nameLabel4 = QLabel(w)
nameLabel4.setText('Output')
line4 = QLineEdit()
line4.move(20,80)
line4.resize(200,32)
nameLabel4.move(20,110)

result4 = textbox.text()
print(result4)
textbox.setText("")



def browse():
    filename = QFileDialog.getOpenFileName(w, 'Open File', 'C:\\')
    return filename



# Generate Create the actions
@pyqtSlot()
def on_click():
    #result = textbox.text()
    #print(result)
    #textbox.setText("")
    result2 = combo.currentText()
    print(result2)

# Browse Create the actions
@pyqtSlot()
def on_click2():
    #result = textbox.text()
    #print(result)
    #textbox.setText("")
    result2 = combo2.currentText()
    print(result2)


input = []

# Browse Create the actions
@pyqtSlot()
def on_click3():
    #result = textbox.text()
    #print(result)
    #textbox.setText("")
    result2 = browse()
    textbox.setText(result2)
    print(result2)
    input.append(result2)


# Browse Create the actions
@pyqtSlot()
def on_click4():
    #result = textbox.text()
    #print(result)
    #textbox.setText("")
    result2 = browse()
    textbox2.setText(result2)
    print(result2)
    output = result2
    edc.edc_s(str(input[0]),str(output))





# connect the signals to the slots
button.clicked.connect(on_click)
button2.clicked.connect(QtCore.QCoreApplication.instance().quit)
button.clicked.connect(on_click2)
button3.clicked.connect(on_click3)
button4.clicked.connect(on_click4)
# Show the window and run the app

w.show()

app.exec_()

