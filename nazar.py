from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
app=QApplication([])

window=QWidget()
window.setWindowIcon(QIcon('image_d57cb43b-f514-462d-ae54-d703e1737b96.png'))
window.resize(200,1000)
window.move(100,56)
window.setStyleSheet('background-color: #000000')
window.show()

app.exec_()