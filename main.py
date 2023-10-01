import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QStackedWidget, QVBoxLayout, \
    QLineEdit
from PyQt5.QtGui import QFont
from crypto import Cryptography
from keygen import keygen

font = QFont()
font.setFamily('Ubuntu')
font.setPointSize(24)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.filename = None
        self.setGeometry(0, 0, 720, 480)
        self.layout = QVBoxLayout(self)
        self.stacked_widget = QStackedWidget(self)
        self.window1 = QWidget()
        self.window2 = QWidget()

        self.stacked_widget.addWidget(self.window1)
        self.stacked_widget.addWidget(self.window2)

        self.layout.addWidget(self.stacked_widget)

        self.own_name = QLabel('Welcome to Pass Saver', self.window1)
        self.own_name.setGeometry(200, 100, 350, 60)
        self.own_name.setFont(font)
        self.own_name.setStyleSheet('color: #A0A0A0')
        self.create_base_button = QPushButton('Create new password base', self.window1)
        self.create_base_button.setGeometry(250, 170, 250, 30)
        self.create_base_button.setStyleSheet("color: #FFFFFF; background-color: #424355; border-radius: 15px;")
        self.open_base_button = QPushButton('Open existing pass base', self.window1)
        self.open_base_button.setGeometry(250, 220, 250, 30)
        self.open_base_button.setStyleSheet("color: #FFFFFF; background-color: #424355; border-radius: 15px;")
        self.open_base_button.clicked.connect(self.open_file_dialog)
        self.setStyleSheet("background-color: #2F2F34;")

        self.input_key_label = QLabel('Input Base Key below', self.window2)
        self.input_key_label.setGeometry(260, 170, 200, 30)
        self.input_key_label.setStyleSheet('color: #FFFFFF')
        font.setPointSize(14)
        self.input_key_label.setFont(font)
        self.key_input = QLineEdit(self.window2)
        self.key_input.setGeometry(200, 200, 300, 30)
        self.key_input.setStyleSheet('color:#FFFFFF')

        self.key_input_submit = QPushButton('Open existing pass base', self.window2)
        self.key_input_submit.setGeometry(225, 240, 250, 30)
        self.key_input_submit.setStyleSheet('color: #FFFFFF; background-color: #424355')
        self.key_input_submit.clicked.connect(lambda: self.openbase(self.key_input.text()))

        self.stacked_widget.setCurrentWidget(self.window1)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose File", "", "All Files (*.passv)",
                                                   options=options)

        if file_name:
            self.filename = file_name
            self.stacked_widget.setCurrentWidget(self.window2)

    def openbase(self,password):
        key = keygen(password)
        crt = Cryptography(key)
        result = crt.decrypt(self.filename)
        print(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
