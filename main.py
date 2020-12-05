import sys

import numpy as np
from PyQt5 import QtWidgets

import interface
from radiotech import chirp


# Описание класса основной программы
class LabWork(QtWidgets.QMainWindow, interface.Ui_mainLabWindow):
    def __init__(self) -> None:

        super().__init__()  # Вызов метода родительского класса
        self.setupUi(self)

        # Свзяь изменения управляющих элементов и вызываемых методов
        self.durationDial.valueChanged.connect(self.update_all)
        self.deviationDial.valueChanged.connect(self.update_all)

    def update_all(self):
        self.durationLCD.display(self.durationDial.value())
        self.deviationLCD.display(self.deviationDial.value())


        # self.instFreqGraph.canvas.axes.clear()
        # self.instFreqGraph.canvas.axes.plot(np.linspace(0, 1, 50), np.linspace(0, 10, 50))
        # self.instFreqGraph.canvas.axes.set_title('Мгновенная фаза сигнала')
        # self.instFreqGraph.canvas.axes.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LabWork()
    window.show()
    app.exec_()

