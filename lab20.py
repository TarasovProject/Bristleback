from PyQt5 import QtWidgets, QtCore 
import sys 

app = QtWidgets.QApplication(sys.argv) 
window = QtWidgets.QWidget() 
window.setWindowTitle("Первая программа на PyQt") 
window.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
window.setFixedSize(300, 400)

label = QtWidgets.QLabel("<center>Привет, мир!</center>") 

btnQuit = QtWidgets.QPushButton("&Закрыть окно") 
vbox = QtWidgets.QVBoxLayout() 
vbox.addWidget(label) 
vbox.addWidget(btnQuit) 
window.setLayout(vbox) 

btnQuit.clicked.connect(app.quit) 

window.show() 
sys.exit(app.exec_())
print('z t,e fkb,f,e')
