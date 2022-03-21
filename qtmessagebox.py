import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Exception_Notification(QWidget):


    def show_messagebox(self, purpose, message):

        if purpose == 'c':
            return QMessageBox.critical(self,'Critical', message, QMessageBox.Ok)

        elif purpose == 'q':
            return QMessageBox.question(self,'Question', message, QMessageBox.Ok | QMessageBox.No)

        elif purpose == 'w':
            return QMessageBox.warning(self, 'Warning', message, QMessageBox.Ok)

        elif purpose == 'i':
            return QMessageBox.information(self, 'Information', message, QMessageBox.Ok)





if __name__ == '__main__':
    app = QApplication(sys.argv)

    noti = Exception_Notification()
    result = noti.show_messagebox('q', 'question')
    sys.exit(app.exec_())
