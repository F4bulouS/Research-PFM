from typing import Union
from enum import Enum, auto

import numpy as np
from scipy import signal


class EnvelopeType(Enum):
    """
    Тип огибающих радиосигнала.
    """

    RECTANGLE = auto()
    TRIANGLE = auto()
    EXPONENTIAL = auto()
    GAUSS = auto()


class PulseChirp:
    """
    Класс импульсных сигналов с линейной частотной модуляцией.

    В данном классе описаны сигналы с различными огибающими, а также некоторые
    их характеристики.

    Публичные атрибуты: нет.
    """
    def __init__(
            self,
            duration: Union[int, float],
            deviation: Union[int, float],
            carrier: Union[int, float],
            envelope_type: EnvelopeType,
            points: int = 1000
    ) -> None:
        """
        Констуктор класса с одним именованным параметром.

        :param duration: конечное временное значение импульса
        :param deviation: наибольшее отколнение частоты
        :param carrier: несущая частота
        :param envelope_type: тип огибающей
        :param points: количество точек, которое устанавливается для каждого
         последующего вычисления

        :return: None.
        """
        self._duration = duration
        self._deviation = deviation
        self._carrier = carrier
        self.envelope_type: EnvelopeType = envelope_type
        self._points = points

    # Геттеры и сеттеры для атрибутов, которым нужна проверка
    @property
    def duration(self) -> Union[int, float]:
        return self._duration

    @duration.setter
    def duration(self, duration) -> None:
        if duration <= 0:
            raise Exception('Длительность импульса должна быть положительной!')
        self._duration = duration

    @property
    def deviation(self) -> Union[int, float]:
        return self._deviation

    @deviation.setter
    def deviation(self, deviation: Union[int, float]) -> None:
        if deviation <= 0:
            raise Exception('Девиация должна быть положительной!')
        self._deviation = deviation

    @property
    def carrier(self) -> Union[int, float]:
        return self._carrier

    @carrier.setter
    def carrier(self, carrier: Union[int, float]) -> None:
        if carrier <= 0:
            raise Exception('Частота несущей должна быть положительной!')
        self._carrier = carrier

    @property
    def points(self) -> int:
        return self._points

    @points.setter
    def points(self, points: int) -> None:
        if points <= 0:
            raise Exception('Количество точек должно быть положительным!')
        self._points = points

    @property
    def time(self) -> np.ndarray:
        """
        Массив временных значений.

        :return: Временные значения с фиксированным шагом, равным отношению
        длительности импульса к число точек.
        """
        return np.linspace(0, self._duration, self._points)

    def inst_freq_chirp(self) -> np.ndarray:
        """
        Метод расчета мгновенной частоты ЛЧМ сигнала.

        :return: Массив numpy.ndarray со значениями мгновенных
         частот в каждый момент времени.
        """
        # Базовая "пила" имеет диапазон от -1 до 1, поэтому вводится
        # масштабирование на 0,5 и смещение на 0,5
        return self._deviation * (0.5 * signal.sawtooth(
            2 * np.pi * (1 / self._duration) * self.time
        ) + 0.5) + self._carrier

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
        t = self.time

        # Расчет мгновенной фазы
        for i in range(0, self.points):
            phase[i] = (self.deviation * t[i]**2) / (
                        2 * self._duration) + self.carrier * t[i]**2

        return phase

    def envelope(self) -> np.ndarray:
        """
        Метод расчёта огибающей.

        :return: Массив numpy.ndarray со значениями огибающей
        """
        # TODO: оптимизировать построение огибающей
        # Массив значений огибающей
        envelope_values = np.zeros(self._points)

        # Массив времени
        t = self.time

        # Прямоугольный импульс
        if self.envelope_type == EnvelopeType.RECTANGLE:
            # Чтобы не было прямой линии, крайние точки импульса
            # приравнены к нулю
            envelope_values[0] = 0
            envelope_values[self.points - 1] = 0

            for point in range(1, self.points - 1):
                envelope_values[point] = 1

        # Гауссов импульс
        elif self.envelope_type == EnvelopeType.GAUSS:
            for point in range(0, self.points):
                # Чисто эмпирическая формула, рассчитанная в Mathcad 15.0 M045
                envelope_values[point] =\
                    np.exp((- (t[point] - (self._duration / 2)) ** 2) /
                           (2 * (self._duration / 6) ** 2))

        # Треугольный импульс
        elif self.envelope_type == EnvelopeType.TRIANGLE:
            for point in range(0, self.points):
                if t[point] < self._duration / 2:
                    envelope_values[point] = (1 / self._duration) * t[point]
                else:
                    envelope_values[point] = \
                        1 - (1 / self._duration * t[point])

        # Экспоненциальный импульс
        elif self.envelope_type == EnvelopeType.EXPONENTIAL:
            envelope_values[0] = 0
            for point in range(1, self.points):
                envelope_values[point] = np.exp(
                    -1 * t[point] / (self._duration / 5))

        # На всякий случай, если вдруг формат огибающей будет неверным
        else:
            Exception("Неверный формат огибающей!")

        return envelope_values

    def radio_signal(self) -> np.ndarray:
        """
        Метод построения радиосигнала.

        :return: Массив numpy.ndarray со значениями огибающей
        """
        return self.envelope() * np.cos(
            2 * np.pi * self.carrier *
            self.inst_freq_chirp() * self.time / 1000
        )
