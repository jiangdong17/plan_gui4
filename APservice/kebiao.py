# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kebiao.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(961, 521)

        self.label_kejie = QtWidgets.QLabel(Form)
        self.label_kejie.setGeometry(QtCore.QRect(21, 41, 27, 19))
        self.label_kejie.setObjectName("label_kejie")

        self.label_time = QtWidgets.QLabel(Form)
        self.label_time.setGeometry(QtCore.QRect(121, 41, 27, 19))
        self.label_time.setObjectName("label_time")

        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(10, 80, 58, 16))
        self.label_19.setObjectName("label_19")

        self.layoutWidget_9 = QtWidgets.QWidget(Form)
        self.layoutWidget_9.setGeometry(QtCore.QRect(70, 70, 170, 23))
        self.layoutWidget_9.setObjectName("layoutWidget_9")

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.timeEditstart_0 = QtWidgets.QTimeEdit(self.layoutWidget_9)
        self.timeEditstart_0.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(7, 30, 0)))
        self.timeEditstart_0.setObjectName("timeEditstart_0")
        self.horizontalLayout_11.addWidget(self.timeEditstart_0)

        self.timeEditend_0 = QtWidgets.QTimeEdit(self.layoutWidget_9)
        self.timeEditend_0.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(7, 50, 0)))
        self.timeEditend_0.setObjectName("timeEditend_0")
        self.horizontalLayout_11.addWidget(self.timeEditend_0)

        self.pushButton_shoosetime = QtWidgets.QPushButton(Form)
        self.pushButton_shoosetime.setGeometry(QtCore.QRect(20, 10, 100, 32))
        self.pushButton_shoosetime.setObjectName("pushButton_shoosetime")

        self.pushButton_chooseDate = QtWidgets.QPushButton(Form)
        self.pushButton_chooseDate.setGeometry(QtCore.QRect(130, 10, 100, 32))
        self.pushButton_chooseDate.setObjectName("pushButton_chooseDate")

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 55, 351))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_ke1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ke1.setObjectName("label_ke1")
        self.verticalLayout.addWidget(self.label_ke1)

        self.label_ke2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ke2.setObjectName("label_ke2")
        self.verticalLayout.addWidget(self.label_ke2)

        self.label_ke3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ke3.setObjectName("label_ke3")
        self.verticalLayout.addWidget(self.label_ke3)

        self.label_ke4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ke4.setObjectName("label_ke4")
        self.verticalLayout.addWidget(self.label_ke4)

        self.label_ke5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ke5.setObjectName("label_ke5")
        self.verticalLayout.addWidget(self.label_ke5)

        self.label_ke6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ke6.setObjectName("label_ke6")
        self.verticalLayout.addWidget(self.label_ke6)

        self.label_ke7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ke7.setObjectName("label_ke7")
        self.verticalLayout.addWidget(self.label_ke7)

        self.label_ke8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ke8.setObjectName("label_ke8")
        self.verticalLayout.addWidget(self.label_ke8)

        self.label_ke9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ke9.setObjectName("label_ke9")
        self.verticalLayout.addWidget(self.label_ke9)

        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(280, 40, 631, 21))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_Mon = QtWidgets.QLabel(self.layoutWidget1)
        self.label_Mon.setObjectName("label_Mon")
        self.horizontalLayout.addWidget(self.label_Mon)

        self.label_Tue = QtWidgets.QLabel(self.layoutWidget1)
        self.label_Tue.setObjectName("label_Tue")
        self.horizontalLayout.addWidget(self.label_Tue)

        self.label_Wed = QtWidgets.QLabel(self.layoutWidget1)
        self.label_Wed.setObjectName("label_Wed")
        self.horizontalLayout.addWidget(self.label_Wed)

        self.label_THur = QtWidgets.QLabel(self.layoutWidget1)
        self.label_THur.setObjectName("label_THur")
        self.horizontalLayout.addWidget(self.label_THur)

        self.label_Fri = QtWidgets.QLabel(self.layoutWidget1)
        self.label_Fri.setObjectName("label_Fri")
        self.horizontalLayout.addWidget(self.label_Fri)

        self.label_Sat = QtWidgets.QLabel(self.layoutWidget1)
        self.label_Sat.setObjectName("label_Sat")
        self.horizontalLayout.addWidget(self.label_Sat)

        self.label_Sun = QtWidgets.QLabel(self.layoutWidget1)
        self.label_Sun.setObjectName("label_Sun")
        self.horizontalLayout.addWidget(self.label_Sun)

        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 100, 172, 351))
        self.layoutWidget2.setObjectName("layoutWidget2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.timeEditstart_1 = QtWidgets.QTimeEdit(self.layoutWidget2)

        self.timeEditstart_1.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(7, 55, 0)))
        self.timeEditstart_1.setObjectName("timeEditstart_1")
        self.horizontalLayout_2.addWidget(self.timeEditstart_1)

        self.timeEditend_1 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditend_1.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(8, 35, 0)))
        self.timeEditend_1.setObjectName("timeEditend_1")
        self.horizontalLayout_2.addWidget(self.timeEditend_1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.timeEditstart_2 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditstart_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(8, 45, 0)))
        self.timeEditstart_2.setObjectName("timeEditstart_2")
        self.horizontalLayout_3.addWidget(self.timeEditstart_2)

        self.timeEditend_2 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditend_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(9, 25, 0)))
        self.timeEditend_2.setObjectName("timeEditend_2")
        self.horizontalLayout_3.addWidget(self.timeEditend_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.timeEditstart_3 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditstart_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(9, 35, 0)))
        self.timeEditstart_3.setObjectName("timeEditstart_3")
        self.horizontalLayout_4.addWidget(self.timeEditstart_3)

        self.timeEditend_3 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditend_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(10, 15, 0)))
        self.timeEditend_3.setObjectName("timeEditend_3")

        self.horizontalLayout_4.addWidget(self.timeEditend_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.timeEditstart_4 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditstart_4.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(10, 25, 0)))
        self.timeEditstart_4.setObjectName("timeEditstart_4")
        self.horizontalLayout_5.addWidget(self.timeEditstart_4)

        self.timeEditend_4 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditend_4.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(11, 5, 0)))
        self.timeEditend_4.setObjectName("timeEditend_4")
        self.horizontalLayout_5.addWidget(self.timeEditend_4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.timeEditstart_5 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditstart_5.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(11, 10, 0)))
        self.timeEditstart_5.setObjectName("timeEditstart_5")
        self.horizontalLayout_6.addWidget(self.timeEditstart_5)

        self.timeEditend_5 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditend_5.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(11, 50, 0)))
        self.timeEditend_5.setObjectName("timeEditend_5")
        self.horizontalLayout_6.addWidget(self.timeEditend_5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.timeEditstart_6 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditstart_6.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(13, 0, 0)))
        self.timeEditstart_6.setObjectName("timeEditstart_6")
        self.horizontalLayout_7.addWidget(self.timeEditstart_6)

        self.timeEditend_6 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditend_6.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(13, 40, 0)))
        self.timeEditend_6.setObjectName("timeEditend_6")

        self.horizontalLayout_7.addWidget(self.timeEditend_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.timeEditstart_7 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditstart_7.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 1), QtCore.QTime(13, 55, 0)))
        self.timeEditstart_7.setObjectName("timeEditstart_7")
        self.horizontalLayout_8.addWidget(self.timeEditstart_7)

        self.timeEditend_7 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditend_7.setObjectName("timeEditend_7")
        self.horizontalLayout_8.addWidget(self.timeEditend_7)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        self.timeEditstart_8 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditstart_8.setObjectName("timeEditstart_8")
        self.horizontalLayout_9.addWidget(self.timeEditstart_8)

        self.timeEditend_8 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditend_8.setObjectName("timeEditend_8")
        self.horizontalLayout_9.addWidget(self.timeEditend_8)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.timeEditstart_9 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditstart_9.setObjectName("timeEditstart_9")
        self.horizontalLayout_10.addWidget(self.timeEditstart_9)

        self.timeEditend_9 = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEditend_9.setObjectName("timeEditend_9")
        self.horizontalLayout_10.addWidget(self.timeEditend_9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(540, 470, 330, 35))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")

        self.pushButton_kechengIN = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_kechengIN.setObjectName("pushButton_kechengIN")
        self.horizontalLayout_13.addWidget(self.pushButton_kechengIN)

        self.pushButton_kechengGAI = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_kechengGAI.setObjectName("pushButton_kechengGAI")
        self.horizontalLayout_13.addWidget(self.pushButton_kechengGAI)

        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_13.addWidget(self.pushButton_save)

        self.layoutWidget4 = QtWidgets.QWidget(Form)
        self.layoutWidget4.setGeometry(QtCore.QRect(260, 100, 631, 361))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.kecheng_11 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_11.setObjectName("kecheng_11")
        self.verticalLayout_3.addWidget(self.kecheng_11)

        self.kecheng_12 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_12.setObjectName("kecheng_12")
        self.verticalLayout_3.addWidget(self.kecheng_12)

        self.kecheng_13 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_13.setObjectName("kecheng_13")
        self.verticalLayout_3.addWidget(self.kecheng_13)

        self.kecheng_14 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_14.setObjectName("kecheng_14")
        self.verticalLayout_3.addWidget(self.kecheng_14)

        self.kecheng_15 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_15.setObjectName("kecheng_15")
        self.verticalLayout_3.addWidget(self.kecheng_15)

        self.kecheng_16 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_16.setObjectName("kecheng_16")
        self.verticalLayout_3.addWidget(self.kecheng_16)

        self.kecheng_17 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_17.setObjectName("kecheng_17")
        self.verticalLayout_3.addWidget(self.kecheng_17)

        self.kecheng_18 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_18.setObjectName("kecheng_18")
        self.verticalLayout_3.addWidget(self.kecheng_18)

        self.kecheng_19 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_19.setObjectName("kecheng_19")
        self.verticalLayout_3.addWidget(self.kecheng_19)

        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.kecheng_21 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_21.setObjectName("kecheng_21")
        self.verticalLayout_5.addWidget(self.kecheng_21)

        self.kecheng_22 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_22.setObjectName("kecheng_22")
        self.verticalLayout_5.addWidget(self.kecheng_22)

        self.kecheng_23 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_23.setObjectName("kecheng_23")
        self.verticalLayout_5.addWidget(self.kecheng_23)

        self.kecheng_24 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_24.setObjectName("kecheng_24")
        self.verticalLayout_5.addWidget(self.kecheng_24)

        self.kecheng_25 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_25.setObjectName("kecheng_25")
        self.verticalLayout_5.addWidget(self.kecheng_25)

        self.kecheng_26 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_26.setObjectName("kecheng_26")
        self.verticalLayout_5.addWidget(self.kecheng_26)

        self.kecheng_27 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_27.setObjectName("kecheng_27")
        self.verticalLayout_5.addWidget(self.kecheng_27)

        self.kecheng_28 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_28.setObjectName("kecheng_28")
        self.verticalLayout_5.addWidget(self.kecheng_28)

        self.kecheng_29 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_29.setObjectName("kecheng_29")
        self.verticalLayout_5.addWidget(self.kecheng_29)

        self.horizontalLayout_12.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.kecheng_31 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_31.setObjectName("kecheng_31")
        self.verticalLayout_4.addWidget(self.kecheng_31)

        self.kecheng_32 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_32.setObjectName("kecheng_32")
        self.verticalLayout_4.addWidget(self.kecheng_32)

        self.kecheng_33 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_33.setObjectName("kecheng_33")
        self.verticalLayout_4.addWidget(self.kecheng_33)

        self.kecheng_34 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_34.setObjectName("kecheng_34")
        self.verticalLayout_4.addWidget(self.kecheng_34)

        self.kecheng_35 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_35.setObjectName("kecheng_35")
        self.verticalLayout_4.addWidget(self.kecheng_35)

        self.kecheng_36 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_36.setObjectName("kecheng_36")
        self.verticalLayout_4.addWidget(self.kecheng_36)

        self.kecheng_37 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_37.setObjectName("kecheng_37")
        self.verticalLayout_4.addWidget(self.kecheng_37)

        self.kecheng_38 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_38.setObjectName("kecheng_38")
        self.verticalLayout_4.addWidget(self.kecheng_38)

        self.kecheng_39 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_39.setObjectName("kecheng_39")
        self.verticalLayout_4.addWidget(self.kecheng_39)

        self.horizontalLayout_12.addLayout(self.verticalLayout_4)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.kecheng_41 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_41.setObjectName("kecheng_41")
        self.verticalLayout_9.addWidget(self.kecheng_41)

        self.kecheng_42 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_42.setObjectName("kecheng_42")
        self.verticalLayout_9.addWidget(self.kecheng_42)

        self.kecheng_43 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_43.setObjectName("kecheng_43")
        self.verticalLayout_9.addWidget(self.kecheng_43)

        self.kecheng_44 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_44.setObjectName("kecheng_44")
        self.verticalLayout_9.addWidget(self.kecheng_44)

        self.kecheng_45 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_45.setObjectName("kecheng_45")
        self.verticalLayout_9.addWidget(self.kecheng_45)

        self.kecheng_46 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_46.setObjectName("kecheng_46")
        self.verticalLayout_9.addWidget(self.kecheng_46)

        self.kecheng_47 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_47.setObjectName("kecheng_47")
        self.verticalLayout_9.addWidget(self.kecheng_47)

        self.kecheng_48 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_48.setObjectName("kecheng_48")
        self.verticalLayout_9.addWidget(self.kecheng_48)

        self.kecheng_49 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_49.setObjectName("kecheng_49")
        self.verticalLayout_9.addWidget(self.kecheng_49)

        self.horizontalLayout_12.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.kecheng_51 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_51.setObjectName("kecheng_51")
        self.verticalLayout_8.addWidget(self.kecheng_51)

        self.kecheng_52 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_52.setObjectName("kecheng_52")
        self.verticalLayout_8.addWidget(self.kecheng_52)

        self.kecheng_53 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_53.setObjectName("kecheng_53")
        self.verticalLayout_8.addWidget(self.kecheng_53)

        self.kecheng_54 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_54.setObjectName("kecheng_54")
        self.verticalLayout_8.addWidget(self.kecheng_54)

        self.kecheng_55 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_55.setObjectName("kecheng_55")
        self.verticalLayout_8.addWidget(self.kecheng_55)

        self.kecheng_56 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_56.setObjectName("kecheng_56")
        self.verticalLayout_8.addWidget(self.kecheng_56)

        self.kecheng_57 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_57.setObjectName("kecheng_57")
        self.verticalLayout_8.addWidget(self.kecheng_57)

        self.kecheng_58 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_58.setObjectName("kecheng_58")
        self.verticalLayout_8.addWidget(self.kecheng_58)

        self.kecheng_59 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_59.setObjectName("kecheng_59")
        self.verticalLayout_8.addWidget(self.kecheng_59)

        self.horizontalLayout_12.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.kecheng_61 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_61.setObjectName("kecheng_61")
        self.verticalLayout_7.addWidget(self.kecheng_61)

        self.kecheng_62 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_62.setObjectName("kecheng_62")
        self.verticalLayout_7.addWidget(self.kecheng_62)

        self.kecheng_63 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_63.setObjectName("kecheng_63")
        self.verticalLayout_7.addWidget(self.kecheng_63)

        self.kecheng_64 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_64.setObjectName("kecheng_64")
        self.verticalLayout_7.addWidget(self.kecheng_64)

        self.kecheng_65 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_65.setObjectName("kecheng_65")
        self.verticalLayout_7.addWidget(self.kecheng_65)

        self.kecheng_66 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_66.setObjectName("kecheng_66")
        self.verticalLayout_7.addWidget(self.kecheng_66)

        self.kecheng_67 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_67.setObjectName("kecheng_67")
        self.verticalLayout_7.addWidget(self.kecheng_67)

        self.kecheng_68 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_68.setObjectName("kecheng_68")
        self.verticalLayout_7.addWidget(self.kecheng_68)

        self.kecheng_69 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_69.setObjectName("kecheng_69")
        self.verticalLayout_7.addWidget(self.kecheng_69)

        self.horizontalLayout_12.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.kecheng_71 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_71.setObjectName("kecheng_71")
        self.verticalLayout_6.addWidget(self.kecheng_71)

        self.kecheng_72 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_72.setObjectName("kecheng_72")
        self.verticalLayout_6.addWidget(self.kecheng_72)

        self.kecheng_73 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_73.setObjectName("kecheng_73")
        self.verticalLayout_6.addWidget(self.kecheng_73)

        self.kecheng_74 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_74.setObjectName("kecheng_74")
        self.verticalLayout_6.addWidget(self.kecheng_74)

        self.kecheng_75 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_75.setObjectName("kecheng_75")
        self.verticalLayout_6.addWidget(self.kecheng_75)

        self.kecheng_76 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_76.setObjectName("kecheng_76")
        self.verticalLayout_6.addWidget(self.kecheng_76)

        self.kecheng_77 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_77.setObjectName("kecheng_77")
        self.verticalLayout_6.addWidget(self.kecheng_77)

        self.kecheng_78 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_78.setObjectName("kecheng_78")
        self.verticalLayout_6.addWidget(self.kecheng_78)

        self.kecheng_79 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.kecheng_79.setObjectName("kecheng_79")
        self.verticalLayout_6.addWidget(self.kecheng_79)
        self.horizontalLayout_12.addLayout(self.verticalLayout_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_kejie.setText(_translate("Form", "课节"))
        self.label_time.setText(_translate("Form", "时间"))
        self.label_19.setText(_translate("Form", "晨会"))
        self.pushButton_shoosetime.setText(_translate("Form", "学期时间段"))
        self.pushButton_chooseDate.setText(_translate("Form", "选择日期"))
        self.label_ke1.setText(_translate("Form", "第一节课"))
        self.label_ke2.setText(_translate("Form", "第二节课"))
        self.label_ke3.setText(_translate("Form", "第三节课"))
        self.label_ke4.setText(_translate("Form", "第四节课"))
        self.label_ke5.setText(_translate("Form", "第五节课"))
        self.label_ke6.setText(_translate("Form", "第六节课"))
        self.label_ke7.setText(_translate("Form", "第七节课"))
        self.label_ke8.setText(_translate("Form", "第八节课"))
        self.label_ke9.setText(_translate("Form", "第九节课"))
        self.label_Mon.setText(_translate("Form", "星期一"))
        self.label_Tue.setText(_translate("Form", "星期二"))
        self.label_Wed.setText(_translate("Form", "星期三"))
        self.label_THur.setText(_translate("Form", "星期四"))
        self.label_Fri.setText(_translate("Form", "星期五"))
        self.label_Sat.setText(_translate("Form", "星期六"))
        self.label_Sun.setText(_translate("Form", "星期天"))
        self.pushButton_kechengIN.setText(_translate("Form", "录入课程"))
        self.pushButton_kechengGAI.setText(_translate("Form", "修改课程"))
        self.pushButton_save.setText(_translate("Form", "保存"))