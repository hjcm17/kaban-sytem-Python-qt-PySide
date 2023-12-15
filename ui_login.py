# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_tela_login(object):
    def setupUi(self, tela_login):
        if not tela_login.objectName():
            tela_login.setObjectName(u"tela_login")
        tela_login.resize(1124, 726)
        tela_login.setStyleSheet(u"")
        self.frame = QFrame(tela_login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(310, 150, 511, 481))
        self.frame.setStyleSheet(u"background-color: rgba(7, 125, 15, 0.2);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.usuario_input = QLineEdit(self.frame)
        self.usuario_input.setObjectName(u"usuario_input")
        self.usuario_input.setGeometry(QRect(130, 210, 261, 31))
        self.usuario_input.setStyleSheet(u"background-color: rgb(191, 191, 191);\n"
"\n"
"font: 9pt \"Tahoma\";")
        self.senha_input = QLineEdit(self.frame)
        self.senha_input.setObjectName(u"senha_input")
        self.senha_input.setGeometry(QRect(130, 270, 261, 31))
        self.senha_input.setStyleSheet(u"background-color: rgb(191, 191, 191);\n"
"\n"
"font: 9pt \"Tahoma\";")
        self.senha_input.setEchoMode(QLineEdit.Password)
        self.btn_acessar = QPushButton(self.frame)
        self.btn_acessar.setObjectName(u"btn_acessar")
        self.btn_acessar.setGeometry(QRect(160, 340, 211, 31))
        self.btn_acessar.setStyleSheet(u"QPushButton:pressed\n"
"    { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);}")
        self.btn_cadastro = QPushButton(self.frame)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setGeometry(QRect(160, 390, 211, 31))
        self.btn_cadastro.setStyleSheet(u"QPushButton:pressed\n"
"    { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);}")
        self.logon_label = QLabel(tela_login)
        self.logon_label.setObjectName(u"logon_label")
        self.logon_label.setGeometry(QRect(440, 90, 251, 251))
        self.logon_label.setPixmap(QPixmap(u"../../../../Downloads/kanbanLogo.png"))
        self.logon_label.setScaledContents(True)

        self.retranslateUi(tela_login)

        QMetaObject.connectSlotsByName(tela_login)
    # setupUi

    def retranslateUi(self, tela_login):
        tela_login.setWindowTitle(QCoreApplication.translate("tela_login", u"Form", None))
        self.usuario_input.setPlaceholderText(QCoreApplication.translate("tela_login", u"Usu\u00e1rio:", None))
        self.senha_input.setPlaceholderText(QCoreApplication.translate("tela_login", u"Senha:", None))
        self.btn_acessar.setText(QCoreApplication.translate("tela_login", u"ENTRAR", None))
        self.btn_cadastro.setText(QCoreApplication.translate("tela_login", u"CRIAR CONTA", None))
        self.logon_label.setText("")
    # retranslateUi

