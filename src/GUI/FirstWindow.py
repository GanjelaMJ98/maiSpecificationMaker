
from .forms import FirstWindowForm
from PyQt5 import QtWidgets
import sys
answer = None

class FirstWindowApp(QtWidgets.QMainWindow, FirstWindowForm.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.StartCreateButton.clicked.connect(self.on_clicked)
        self.StartUpdateButton.clicked.connect(self.on_clicked)
        self.StartPrintButton.clicked.connect(self.on_clicked)

    def on_clicked(self):
        global answer
        button = self.sender()
        answer = button.text()
        self.close()



def FirstWindow():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = FirstWindowApp()  # Создаём объект класса FirstWindowApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

    if answer is None:
        return 0
    else:
        return answer

def main():
    print(FirstWindow())

if __name__ == "__main__":
   main()