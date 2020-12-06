from typing import Union

import numpy as np
from scipy import signal


class PulseChirp:
    """
    Класс импульсных сигналов с линейной частотной модуляцией.

    В данном классе описаны сигналы с различными огибающими, а также некоторые их
    характеристики.

    Атрибуты:
    Нет.
    """

    def __init__(
            self,
            pulse_time: Union[int, float],
            deviation: Union[int, float],
            carrier: Union[int, float],
            points: int = 1000
    ) -> None:
        """
        Констуктор класса с одним именованным параметром.

        :param pulse_time: конечное временное значение
        :param deviation: наибольшее отколнение частоты
        :param carrier: несущая частота
        :param points: количество точек, которое устанавливается для каждого
         последующего вычисления

        :return: None.
        """
        self.pulse_time = pulse_time
        self.deviation = deviation
        self.carrier = carrier
        self.points = points

    def set_pulse_time(self, pulse_time: Union[int, float]) -> None:
        """
        Метод изменения конечного времени.

        :param pulse_time: длительность импульса
        :return: None.
        """
        self.pulse_time = pulse_time

    def set_deviation(self, deviation: Union[int, float]) -> None:
        """
        Метод изменения девиации.

        :param deviation: наибольшее отклоение частоты
        :return: None.
        """
        self.deviation = deviation

    def set_carrier(self, carrier: Union[int, float]) -> None:
        """
        Метод установки новой несущей частоты.

        :param carrier: несущая частота
        :return: None.
        """
        self.carrier = carrier

    def set_points(self, points: int) -> None:
        """
        Метод установки нового числа точек для каждого вычисления.

        :param points: количество точек,
        которое устанавливается для каждого последующего вычисления
        :return: None.
        """
        self.points = points

    def get_time(self) -> np.ndarray:
        """
        Метод расчета времени (ось OX).

        Данный метод рассчитывает временной массив numpy.ndarray с учетом
        количества периодов сигнала.

        :return: массив numpy.ndarray временных значений .
        """
        return np.linspace(0, self.pulse_time, self.points)

    def inst_freq_chirp(self) -> np.ndarray:
        """
        Метод расчета мгновенной частоты ЛЧМ сигнала.

        :return: Массив numpy.ndarray со значениями мгновенных
         частот в каждый момент времени.
        """
        # Базовая "пила" имеет диапазон от -1 до 1, поэтому вводится
        # масштабирование на 0,5 и смещение на 0,5
        return self.deviation * (0.5 * signal.sawtooth(
            2 * np.pi * (1 / self.pulse_time) * self.get_time()
        ) + 0.5) + self.carrier

    # FIXME: исправить ошибку в расчете фазы
    def inst_phase_chirp(self) -> np.ndarray:
        """
        Метод расчета мгновенной фазы ЛЧМ сигнала.

        :return: Массив numpy.ndarray со значениями мгновенных
         фаз в каждый момент времени.
        """
        # Создание нулевого массира размерностью points x 1
        phase = np.zeros(self.points)

        # Фиксирование времени
        t = self.get_time()

        # Расчет мгновенной фазы
        for i in range(len(t)):
            phase[i] = (self.deviation * t[i]**2) / (
                        2 * self.pulse_time) + self.carrier * t[i]**2

        return phase


    # # Уравнение огибающей
    # def envelope_eq(self, forms: int) -> np.ndarray:
    #     pass
    #
    # # Уравнение радиосигнала (модулированного)
    # def radio_signal_eq(self) -> np.ndarray:
    #     pass
