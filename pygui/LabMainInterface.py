# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LabMainInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from pygui.MplWidget import MplWidget

class Ui_mainLabWindow(object):
    def setupUi(self, mainLabWindow):
        mainLabWindow.setObjectName("mainLabWindow")
        mainLabWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainLabWindow.sizePolicy().hasHeightForWidth())
        mainLabWindow.setSizePolicy(sizePolicy)
        mainLabWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.mainLabWidget = QtWidgets.QWidget(mainLabWindow)
        self.mainLabWidget.setObjectName("mainLabWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainLabWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLab = QtWidgets.QLabel(self.mainLabWidget)
        self.titleLab.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLab.setObjectName("titleLab")
        self.verticalLayout.addWidget(self.titleLab)
        self.workHorizontalLayout = QtWidgets.QHBoxLayout()
        self.workHorizontalLayout.setObjectName("workHorizontalLayout")
        self.graphLayout = QtWidgets.QVBoxLayout()
        self.graphLayout.setObjectName("graphLayout")
        self.graphGroupBox = QtWidgets.QGroupBox(self.mainLabWidget)
        self.graphGroupBox.setObjectName("graphGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.graphGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphLayouts = QtWidgets.QVBoxLayout()
        self.graphLayouts.setObjectName("graphLayouts")
        self.graphTabWidget = QtWidgets.QTabWidget(self.graphGroupBox)
        self.graphTabWidget.setObjectName("graphTabWidget")
        self.signalTab = QtWidgets.QWidget()
        self.signalTab.setObjectName("signalTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.signalTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.signalGridLayout = QtWidgets.QGridLayout()
        self.signalGridLayout.setObjectName("signalGridLayout")
        self.instFreqGraph = MplWidget(self.signalTab)
        self.instFreqGraph.setStyleSheet("")
        self.instFreqGraph.setObjectName("instFreqGraph")
        self.signalGridLayout.addWidget(self.instFreqGraph, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.signalGridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.instPhaseGraph = MplWidget(self.signalTab)
        self.instPhaseGraph.setStyleSheet("")
        self.instPhaseGraph.setObjectName("instPhaseGraph")
        self.signalGridLayout.addWidget(self.instPhaseGraph, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.signalGridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.signalGridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.signalGraph = MplWidget(self.signalTab)
        self.signalGraph.setStyleSheet("")
        self.signalGraph.setObjectName("signalGraph")
        self.signalGridLayout.addWidget(self.signalGraph, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.signalGridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.envelopeGraph = MplWidget(self.signalTab)
        self.envelopeGraph.setAutoFillBackground(False)
        self.envelopeGraph.setStyleSheet("")
        self.envelopeGraph.setObjectName("envelopeGraph")
        self.signalGridLayout.addWidget(self.envelopeGraph, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.signalGridLayout, 0, 0, 1, 1)
        self.graphTabWidget.addTab(self.signalTab, "")
        self.envelopeTab = QtWidgets.QWidget()
        self.envelopeTab.setObjectName("envelopeTab")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.envelopeTab)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.envelopeVertLayouts = QtWidgets.QVBoxLayout()
        self.envelopeVertLayouts.setObjectName("envelopeVertLayouts")
        self.ampRangeGraph = MplWidget(self.envelopeTab)
        self.ampRangeGraph.setObjectName("ampRangeGraph")
        self.envelopeVertLayouts.addWidget(self.ampRangeGraph)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.envelopeVertLayouts.addItem(spacerItem4)
        self.autoCorrelationGraph = MplWidget(self.envelopeTab)
        self.autoCorrelationGraph.setObjectName("autoCorrelationGraph")
        self.envelopeVertLayouts.addWidget(self.autoCorrelationGraph)
        self.verticalLayout_15.addLayout(self.envelopeVertLayouts)
        self.graphTabWidget.addTab(self.envelopeTab, "")
        self.ambiguityTab = QtWidgets.QWidget()
        self.ambiguityTab.setObjectName("ambiguityTab")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.ambiguityTab)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.ambigutyLayout = QtWidgets.QVBoxLayout()
        self.ambigutyLayout.setObjectName("ambigutyLayout")
        self.ambigutyLayout3D = QtWidgets.QVBoxLayout()
        self.ambigutyLayout3D.setObjectName("ambigutyLayout3D")
        self.ambigutyGraph3D = MplWidget(self.ambiguityTab)
        self.ambigutyGraph3D.setObjectName("ambigutyGraph3D")
        self.ambigutyLayout3D.addWidget(self.ambigutyGraph3D)
        self.ambigutyLayout.addLayout(self.ambigutyLayout3D)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.ambigutyLayout.addItem(spacerItem5)
        self.projectionLayouts = QtWidgets.QGridLayout()
        self.projectionLayouts.setObjectName("projectionLayouts")
        self.tauProjectionGraph = MplWidget(self.ambiguityTab)
        self.tauProjectionGraph.setObjectName("tauProjectionGraph")
        self.projectionLayouts.addWidget(self.tauProjectionGraph, 0, 0, 1, 1)
        self.freqProjectionGraph = MplWidget(self.ambiguityTab)
        self.freqProjectionGraph.setObjectName("freqProjectionGraph")
        self.projectionLayouts.addWidget(self.freqProjectionGraph, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.projectionLayouts.addItem(spacerItem6, 0, 1, 1, 1)
        self.ambigutyLayout.addLayout(self.projectionLayouts)
        self.verticalLayout_17.addLayout(self.ambigutyLayout)
        self.graphTabWidget.addTab(self.ambiguityTab, "")
        self.graphLayouts.addWidget(self.graphTabWidget)
        self.verticalLayout_5.addLayout(self.graphLayouts)
        self.graphLayout.addWidget(self.graphGroupBox)
        self.workHorizontalLayout.addLayout(self.graphLayout)
        self.settingLayout = QtWidgets.QVBoxLayout()
        self.settingLayout.setObjectName("settingLayout")
        self.settingGroupBox = QtWidgets.QGroupBox(self.mainLabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingGroupBox.sizePolicy().hasHeightForWidth())
        self.settingGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.settingGroupBox.setFont(font)
        self.settingGroupBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.settingGroupBox.setObjectName("settingGroupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.settingGroupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.settingBoxLayout = QtWidgets.QVBoxLayout()
        self.settingBoxLayout.setObjectName("settingBoxLayout")
        self.envelopeSetBox = QtWidgets.QGroupBox(self.settingGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.envelopeSetBox.sizePolicy().hasHeightForWidth())
        self.envelopeSetBox.setSizePolicy(sizePolicy)
        self.envelopeSetBox.setObjectName("envelopeSetBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.envelopeSetBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.envelopeSetGrid = QtWidgets.QGridLayout()
        self.envelopeSetGrid.setObjectName("envelopeSetGrid")
        self.envelopeTriangle = QtWidgets.QRadioButton(self.envelopeSetBox)
        self.envelopeTriangle.setObjectName("envelopeTriangle")
        self.envelopeSetGrid.addWidget(self.envelopeTriangle, 1, 0, 1, 1)
        self.envelopeRectangle = QtWidgets.QRadioButton(self.envelopeSetBox)
        self.envelopeRectangle.setObjectName("envelopeRectangle")
        self.envelopeSetGrid.addWidget(self.envelopeRectangle, 0, 0, 1, 1)
        self.envelopeGauss = QtWidgets.QRadioButton(self.envelopeSetBox)
        self.envelopeGauss.setObjectName("envelopeGauss")
        self.envelopeSetGrid.addWidget(self.envelopeGauss, 0, 1, 1, 1)
        self.envelopeExp = QtWidgets.QRadioButton(self.envelopeSetBox)
        self.envelopeExp.setObjectName("envelopeExp")
        self.envelopeSetGrid.addWidget(self.envelopeExp, 1, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.envelopeSetGrid)
        self.settingBoxLayout.addWidget(self.envelopeSetBox)
        self.durationSetBox = QtWidgets.QGroupBox(self.settingGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durationSetBox.sizePolicy().hasHeightForWidth())
        self.durationSetBox.setSizePolicy(sizePolicy)
        self.durationSetBox.setObjectName("durationSetBox")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.durationSetBox)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.durationLayout = QtWidgets.QHBoxLayout()
        self.durationLayout.setObjectName("durationLayout")
        self.durationDial = QtWidgets.QDial(self.durationSetBox)
        self.durationDial.setMinimumSize(QtCore.QSize(0, 0))
        self.durationDial.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));")
        self.durationDial.setInputMethodHints(QtCore.Qt.ImhNone)
        self.durationDial.setMinimum(1)
        self.durationDial.setMaximum(10)
        self.durationDial.setWrapping(False)
        self.durationDial.setNotchesVisible(False)
        self.durationDial.setObjectName("durationDial")
        self.durationLayout.addWidget(self.durationDial)
        self.durationLayoutLCD = QtWidgets.QVBoxLayout()
        self.durationLayoutLCD.setObjectName("durationLayoutLCD")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.durationLayoutLCD.addItem(spacerItem7)
        self.durationLCD = QtWidgets.QLCDNumber(self.durationSetBox)
        self.durationLCD.setMinimumSize(QtCore.QSize(108, 40))
        self.durationLCD.setStyleSheet("")
        self.durationLCD.setObjectName("durationLCD")
        self.durationLayoutLCD.addWidget(self.durationLCD)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.durationLayoutLCD.addItem(spacerItem8)
        self.durationLayout.addLayout(self.durationLayoutLCD)
        self.verticalLayout_11.addLayout(self.durationLayout)
        self.settingBoxLayout.addWidget(self.durationSetBox)
        self.deviationSetBox = QtWidgets.QGroupBox(self.settingGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviationSetBox.sizePolicy().hasHeightForWidth())
        self.deviationSetBox.setSizePolicy(sizePolicy)
        self.deviationSetBox.setObjectName("deviationSetBox")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.deviationSetBox)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.deviationLayout = QtWidgets.QHBoxLayout()
        self.deviationLayout.setObjectName("deviationLayout")
        self.deviationDial = QtWidgets.QDial(self.deviationSetBox)
        self.deviationDial.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));")
        self.deviationDial.setMinimum(1)
        self.deviationDial.setMaximum(250)
        self.deviationDial.setObjectName("deviationDial")
        self.deviationLayout.addWidget(self.deviationDial)
        self.deviationLayoutLCD = QtWidgets.QVBoxLayout()
        self.deviationLayoutLCD.setObjectName("deviationLayoutLCD")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.deviationLayoutLCD.addItem(spacerItem9)
        self.deviationLCD = QtWidgets.QLCDNumber(self.deviationSetBox)
        self.deviationLCD.setMinimumSize(QtCore.QSize(0, 40))
        self.deviationLCD.setObjectName("deviationLCD")
        self.deviationLayoutLCD.addWidget(self.deviationLCD)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.deviationLayoutLCD.addItem(spacerItem10)
        self.deviationLayout.addLayout(self.deviationLayoutLCD)
        self.verticalLayout_13.addLayout(self.deviationLayout)
        self.settingBoxLayout.addWidget(self.deviationSetBox)
        self.verticalLayout_7.addLayout(self.settingBoxLayout)
        self.settingLayout.addWidget(self.settingGroupBox)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.settingLayout.addItem(spacerItem11)
        self.workHorizontalLayout.addLayout(self.settingLayout)
        self.verticalLayout.addLayout(self.workHorizontalLayout)
        mainLabWindow.setCentralWidget(self.mainLabWidget)
        self.menubar = QtWidgets.QMenuBar(mainLabWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.setting = QtWidgets.QMenu(self.menubar)
        self.setting.setObjectName("setting")
        self.info = QtWidgets.QMenu(self.menubar)
        self.info.setObjectName("info")
        mainLabWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainLabWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        mainLabWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.setting.menuAction())
        self.menubar.addAction(self.info.menuAction())

        self.retranslateUi(mainLabWindow)
        self.graphTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainLabWindow)

    def retranslateUi(self, mainLabWindow):
        _translate = QtCore.QCoreApplication.translate
        mainLabWindow.setWindowTitle(_translate("mainLabWindow", "Исследование импульсных сигналов с частотной модуляцией"))
        self.titleLab.setText(_translate("mainLabWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Лабораторная работа №5</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Исследование импульсных сигналов с частотной модуляцией</span></p></body></html>"))
        self.graphGroupBox.setTitle(_translate("mainLabWindow", "Графики"))
        self.graphTabWidget.setTabText(self.graphTabWidget.indexOf(self.signalTab), _translate("mainLabWindow", "Радиосигнал"))
        self.graphTabWidget.setTabText(self.graphTabWidget.indexOf(self.envelopeTab), _translate("mainLabWindow", "Комплексная огибающая"))
        self.graphTabWidget.setTabText(self.graphTabWidget.indexOf(self.ambiguityTab), _translate("mainLabWindow", "Функция неопределённости"))
        self.settingGroupBox.setTitle(_translate("mainLabWindow", "Параметры сигнала"))
        self.envelopeSetBox.setTitle(_translate("mainLabWindow", "Огибающая"))
        self.envelopeTriangle.setText(_translate("mainLabWindow", "Треугольная"))
        self.envelopeRectangle.setText(_translate("mainLabWindow", "Прямоугольная"))
        self.envelopeGauss.setText(_translate("mainLabWindow", "Гауссова"))
        self.envelopeExp.setText(_translate("mainLabWindow", "Экспоненциальная"))
        self.durationSetBox.setTitle(_translate("mainLabWindow", "Длительность, мс"))
        self.deviationSetBox.setTitle(_translate("mainLabWindow", "Девиация частоты, КГц"))
        self.setting.setTitle(_translate("mainLabWindow", "Настройки"))
        self.info.setTitle(_translate("mainLabWindow", "Информация"))
