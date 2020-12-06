import sys

import numpy as np
from PyQt5 import QtWidgets

import interface
from radiotech.chirp import PulseChirp


# Описание класса основной программы
class LabWork(QtWidgets.QMainWindow, interface.Ui_mainLabWindow):
    """
    Класс лабораторной работы по исследованию импульсных ЛЧМ-сигналов.
    """

    def __init__(self) -> None:

        super().__init__()  # Вызов метода родительского класса
        self.setupUi(self)

        # Создание импульсного сигнала с ЛЧМ
        self.pulse_chirp = PulseChirp(
            self.durationDial.value() / 1000,
            self.deviationDial.value() * 1000,
            10000,  # TODO: добавить в настройки изменение частоты несущей
            100     # TODO: добавить в настройки изменение числа точек
        )

        # Свзязь изменения управляющих элементов и вызываемых методов
        self.durationDial.valueChanged.connect(self.update_all)
        self.deviationDial.valueChanged.connect(self.update_all)

    def update_all(self) -> None:
        """
        Обновление всех элементов вывода информации.

        :return: None.
        """
        self.update_lcd()
        self.update_graph()

    def update_lcd(self) -> None:
        """
        Обновление всех LCD-дисплеев.

        :return: None.
        """
        self.durationLCD.display(self.durationDial.value())
        self.deviationLCD.display(self.deviationDial.value())

    def update_graph(self) -> None:
        """
        Обновление всех графиков.

        :return: None.
        """

        # TODO: оптимизировать перерасчет графиков
        self.update_freq()
        self.update_phase()
        self.update_envelope()

    def update_freq(self) -> None:
        """
        Обновление графика мгновенной частоты.

        :return: None.
        """
        self.pulse_chirp.set_deviation(self.deviationDial.value())
        self.pulse_chirp.set_pulse_time(self.durationDial.value())

        pulse_time = self.pulse_chirp.get_time()
        pulse_freq = self.pulse_chirp.inst_freq_chirp()

        self.instFreqGraph.canvas.axes.clear()
        self.instFreqGraph.canvas.axes.plot(pulse_time, pulse_freq)
        self.instFreqGraph.canvas.axes.set_title('Мгновенная частота')
        # self.instFreqGraph.canvas.axes.draw()

    def update_phase(self) -> None:
        """
        Обновление графика мгновенной фазы.

        :return: None.
        """
        self.pulse_chirp.set_deviation(self.deviationDial.value())
        self.pulse_chirp.set_pulse_time(self.durationDial.value())

        pulse_time = self.pulse_chirp.get_time()
        pulse_phase = self.pulse_chirp.inst_phase_chirp()

        self.instPhaseGraph.canvas.axes.clear()
        self.instPhaseGraph.canvas.axes.plot(pulse_time, pulse_phase)
        self.instPhaseGraph.canvas.axes.set_title('Мгновенная фаза')
        # self.instFreqGraph.canvas.axes.draw()

    def update_envelope(self) -> None:
        """
        Обновление графика огибающей.

        :return: None.
        """
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LabWork()
    window.show()
    app.exec_()
