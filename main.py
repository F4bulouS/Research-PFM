import sys

from PyQt5 import QtWidgets
import numpy as np

from pygui import LabMainInterface
from radiotech.chirp import PulseChirp, EnvelopeType


# Описание класса основной программы
class LabWork(QtWidgets.QMainWindow, LabMainInterface.Ui_mainLabWindow):
    """
    Класс лабораторной работы по исследованию импульсных ЛЧМ-сигналов.
    """

    # Базовые параметры сигнала
    BASE_DURATION = 0.001
    BASE_DEVIATION = 1000
    BASE_CARRIER = 10000
    BASE_POINTS = 10000

    env_type = EnvelopeType.RECTANGLE

    def __init__(self) -> None:

        super().__init__()  # Вызов метода родительского класса
        self.setupUi(self)

        # Создание базового импульсного сигнала с ЛЧМ
        self.pulse_chirp = PulseChirp(
            self.BASE_DURATION,
            self.BASE_DEVIATION,
            # TODO: добавить в настройки изменение частоты несущей
            self.BASE_CARRIER,
            self.env_type,
            # TODO: добавить в настройки изменение числа точек
            self.BASE_POINTS
        )

        # Установка стандартных значений элементов
        self.durationLCD.display(self.BASE_DURATION * 1000)
        self.deviationLCD.display(self.BASE_DEVIATION / 1000)
        self.envelopeRectangle.click()

        # Изменение значений управляющих элементов
        self.durationDial.valueChanged.connect(
            lambda: self.update_all(self.env_type)
        )
        self.deviationDial.valueChanged.connect(
            lambda: self.update_all(self.env_type)
        )

        # Построение графиков после запуска программы
        self.update_all(self.env_type)

        # TODO: оптимизировать
        # Изменение огибающей
        self.envelopeRectangle.clicked.connect(
            lambda: self.update_all(EnvelopeType.RECTANGLE)
        )
        self.envelopeGauss.clicked.connect(
            lambda: self.update_all(EnvelopeType.GAUSS)
        )
        self.envelopeTriangle.clicked.connect(
            lambda: self.update_all(EnvelopeType.TRIANGLE)
        )
        self.envelopeExp.clicked.connect(
            lambda: self.update_all(EnvelopeType.EXPONENTIAL)
        )

    def update_all(self, env_type: EnvelopeType) -> None:
        """
        Обновление всех элементов вывода информации.

        :param env_type: тип огибающей

        :return: None.
        """
        # Сохранение огибающей
        self.env_type = env_type

        # Считывание управляющих элементов
        duration = self.durationDial.value()
        deviation = self.deviationDial.value()

        # Обновление дисплеев с информацией
        self.durationLCD.display(duration)
        self.deviationLCD.display(deviation)

        # Изменение параметров радиосигнала
        self.pulse_chirp.duration = duration * 0.001
        self.pulse_chirp.deviation = deviation * 1000
        self.pulse_chirp.envelope_type = self.env_type

        # Перерасчет времени (ось X)
        pulse_time = self.pulse_chirp.time

        # TODO: оптимизировать обновление графиков
        # Обновление графиков
        self.update_freq(pulse_time)
        self.update_phase(pulse_time)
        self.update_envelope(pulse_time)
        self.update_radio_signal(pulse_time)

    def update_freq(self, pulse_time: np.ndarray) -> None:
        """
        Обновление графика мгновенной частоты.

        :return: None.
        """
        # TODO: повторящийся блок кода во всех функциях обновления графиков
        self.instFreqGraph.canvas.axes.clear()
        self.instFreqGraph.canvas.axes.plot(
            pulse_time,
            self.pulse_chirp.inst_freq_chirp()
        )
        self.instFreqGraph.canvas.axes.set_title('Мгновенная частота')
        self.instFreqGraph.canvas.draw()

    def update_phase(self, pulse_time: np.ndarray) -> None:
        """
        Обновление графика мгновенной фазы.

        :return: None.
        """
        self.instPhaseGraph.canvas.axes.clear()
        self.instPhaseGraph.canvas.axes.plot(
            pulse_time,
            self.pulse_chirp.inst_phase_chirp()
        )
        self.instPhaseGraph.canvas.axes.set_title('Мгновенная фаза')
        self.instPhaseGraph.canvas.draw()

    def update_envelope(self, pulse_time: np.ndarray) -> None:
        """
        Обновление графика огибающей.

        :return: None.
        """
        self.envelopeGraph.canvas.axes.clear()
        self.envelopeGraph.canvas.axes.plot(
            pulse_time,
            self.pulse_chirp.envelope()
        )
        self.envelopeGraph.canvas.axes.set_title('Огибающая')
        self.envelopeGraph.canvas.draw()

    def update_radio_signal(self, pulse_time: np.ndarray) -> None:
        """
        Обновление графика радиосигнала.

        :return: None.
        """
        self.signalGraph.canvas.axes.clear()
        self.signalGraph.canvas.axes.plot(
            pulse_time,
            self.pulse_chirp.radio_signal()
        )
        self.signalGraph.canvas.axes.set_title('Радиосигнал')
        self.signalGraph.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LabWork()
    window.show()
    app.exec_()
