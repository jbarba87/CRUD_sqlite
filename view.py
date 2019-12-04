# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import Alumno    
import Controller



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(985, 683)
        MainWindow.resize(1200, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)

        #self.tableWidget.setGeometry(QtCore.QRect(60, 50, 861, 281))
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 1100, 281))

        #self.tableWidget.setMinimumSize(QtCore.QSize(861, 0))
        self.tableWidget.setMinimumSize(QtCore.QSize(1100, 0))

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.btnCerrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCerrar.setGeometry(QtCore.QRect(820, 600, 84, 28))
        self.btnCerrar.setObjectName("btnCerrar")
        self.btnLeer = QtWidgets.QPushButton(self.centralwidget)
        self.btnLeer.setGeometry(QtCore.QRect(690, 600, 84, 28))
        self.btnLeer.setObjectName("btnLeer")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 380, 371, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtCodigo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtCodigo.setObjectName("txtCodigo")
        self.gridLayout.addWidget(self.txtCodigo, 0, 0, 1, 1)
        self.txtCorreo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtCorreo.setObjectName("txtCorreo")
        self.gridLayout.addWidget(self.txtCorreo, 4, 0, 1, 1)
        self.txtHorario = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtHorario.setObjectName("txtHorario")
        self.gridLayout.addWidget(self.txtHorario, 2, 0, 1, 1)
        self.txtNombre_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtNombre_2.setObjectName("txtNombre_2")
        self.gridLayout.addWidget(self.txtNombre_2, 1, 0, 1, 1)
        self.txtEspecialidad = QtWidgets.QLabel(self.gridLayoutWidget)
        self.txtEspecialidad.setObjectName("txtEspecialidad")
        self.gridLayout.addWidget(self.txtEspecialidad, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.btnIngresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnIngresar.setGeometry(QtCore.QRect(530, 400, 84, 28))
        self.btnIngresar.setObjectName("btnIngresar")
        self.btnActualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btnActualizar.setGeometry(QtCore.QRect(530, 450, 84, 28))
        self.btnActualizar.setObjectName("btnActualizar")
        self.btnBorrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBorrar.setGeometry(QtCore.QRect(530, 510, 84, 28))
        self.btnBorrar.setObjectName("btnBorrar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # Conexiones ingresadas
        self.btnCerrar.clicked.connect(self.Cerrar)
        self.btnIngresar.clicked.connect(self.procesar_ingreso)
        self.btnActualizar.clicked.connect(self.procesar_actualizacion)
        self.btnBorrar.clicked.connect(self.procesar_borrado)
        self.btnLeer.clicked.connect(self.leer)
        self.tableWidget.cellClicked.connect(self.table_clicked)

    def procesar_ingreso(self):
        self.procesar(0)
    def procesar_actualizacion(self):
        self.procesar(1)
    def procesar_borrado(self):
        self.procesar(2)

    def Cerrar(self):
        sys.exit()


    def procesar(self, opcion):

        al = Alumno.Alumno()

        if (self.lineEdit.text() == "" ):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("El Casillero del Codigo no puede estar vacio.")
            msgBox.exec()
            return

        al.setcodigo( self.lineEdit.text())
        al.setnombre( self.lineEdit_2.text())
        al.sethorario( self.lineEdit_3.text())
        al.setespecialidad( self.lineEdit_4.text())
        al.setcorreo( self.lineEdit_5.text())


        if (opcion == 0):
            Controller.Controller.ingresar_alumno(al)
        if (opcion == 1):
            Controller.Controller.actualizar_alumno(al)
        if (opcion == 2):
            Controller.Controller.borrar_alumno(al)

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

        self.leer()


    def leer(self):
        lista = Controller.Controller.listar_alumnos()

        row = 0

        self.tableWidget.setRowCount( len(lista) )

        # print(lista)

        for al in lista:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(al[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(al[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(al[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(al[3]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(al[4]))

            row = row + 1

        # Estableciendo ancho de columnas
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 60)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 400)

        
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(" ")
        msgBox.setText("Mostrando " + str(row) + " columnas.")
        msgBox.exec()



    def table_clicked(self, row, col):

        self.lineEdit.setText( self.tableWidget.item(row, 0).text() )
        self.lineEdit_2.setText( self.tableWidget.item(row, 1).text() )
        self.lineEdit_3.setText( self.tableWidget.item(row, 2).text() )
        self.lineEdit_4.setText( self.tableWidget.item(row, 3).text() )
        self.lineEdit_5.setText( self.tableWidget.item(row, 4).text() )



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conectar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Horario"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Especialidad"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Correo"))
        self.btnCerrar.setText(_translate("MainWindow", "Cerrar"))
        self.btnLeer.setText(_translate("MainWindow", "Leer datos"))
        self.txtCodigo.setText(_translate("MainWindow", "Codigo"))
        self.txtCorreo.setText(_translate("MainWindow", "Correo"))
        self.txtHorario.setText(_translate("MainWindow", "Horario"))
        self.txtNombre_2.setText(_translate("MainWindow", "Nombre"))
        self.txtEspecialidad.setText(_translate("MainWindow", "Especialidad"))
        self.btnIngresar.setText(_translate("MainWindow", "Ingresar"))
        self.btnActualizar.setText(_translate("MainWindow", "Actualizar"))
        self.btnBorrar.setText(_translate("MainWindow", "Borrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

