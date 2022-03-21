import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Exception_Notification(QWidget):


    def show_messagebox(self, purpose, message):

        if purpose == 'c':
            QMessageBox.Ok == QMessageBox.critical(self,'Critical', message, QMessageBox.Ok)

        elif purpose == 'q':
            result = QMessageBox.question(self,'Question', message, QMessageBox.Ok | QMessageBox.Cancel)
            if result == QMessageBox.Ok:
                print('OK')
            elif result == QMessageBox.Cancel:
                print('Cancel')
            else:
                print('condition exception raise')
        elif purpose == 'w':
            QMessageBox.warning(self, 'Warning', message, QMessageBox.Ok)

        elif purpose == 'i':
            QMessageBox.information(self, 'Information', message, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    noti = Exception_Notification()
    result = noti.show_messagebox('q','TEST')
    sys.exit(app.exec_())
