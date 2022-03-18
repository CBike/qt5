import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class App(QWidget):

    def show_QMessagebox(self,purpose,message):

        if purpose == 'c':
            QMessageBox.critical(self,'Critical', message, QMessageBox.Ok)

        elif purpose == 'q':
            QMessageBox.question(self,'Question', message, QMessageBox.Ok | QMessageBox.No)

        elif purpose == 'w':
            QMessageBox.warning(self, 'Warning', message, QMessageBox.Ok)

        elif purpose == 'i':
            QMessageBox.information(self, 'Information', message, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    ex.show_QMessagebox('c','critical')
    ex.show_QMessagebox('i', 'information')
    ex.show_QMessagebox('w', 'warning')
    ex.show_QMessagebox('q', 'question')
    sys.exit(app.exec_())
