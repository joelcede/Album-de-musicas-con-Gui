from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.insert(0, '../conectordb')
sys.path.insert(0, '../css')
from Conectordb import Conexion
from estilos import Estilos
import pymysql

class Editorxd:

    def mensaje(self,titulo,mensaje):
        mensj = QtWidgets.QMessageBox()
        mensj.setWindowTitle(titulo)
        mensj.setText(mensaje)
        mensj.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mensj.exec_()

    def __init__(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(752, 314)
        Editor.setMinimumSize(QtCore.QSize(752, 314))
        Editor.setMaximumSize(QtCore.QSize(752, 314))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imagenes/HaYC9-S7.ico"))#, QtGui.QIcon.Normal, QtGui.QIcon.Offb
        Editor.setWindowIcon(icon)
        #Esto va en otro archivo
        css = Estilos()
        css.estilo_editar(Editor)
        #Esto va en otro archivo
        self.centralwidget = QtWidgets.QWidget(Editor)
        self.centralwidget.setObjectName("centralwidget")
        self.tabla_db = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_db.setGeometry(QtCore.QRect(10, 110, 511, 192))
        self.tabla_db.setObjectName("tabla_db")
        self.tabla_db.setColumnCount(5)
        self.tabla_db.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_db.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        #
        self.buscar()
        conectarx = Conexion()
        conectarx.conectar(self.datos,self.tabla_db)     
        #
        self.tabla_db.setHorizontalHeaderItem(4, item)
        self.btn_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscar.setGeometry(QtCore.QRect(230, 60, 75, 31))
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 10, 431, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.escr_buscar = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.escr_buscar.setObjectName("escr_buscar")
        self.horizontalLayout_2.addWidget(self.escr_buscar)
        self.cbox_buscar_por = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cbox_buscar_por.setObjectName("cbox_buscar_por")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        self.cbox_buscar_por.addItem("")
        self.horizontalLayout_2.addWidget(self.cbox_buscar_por)
        self.edt_nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_nombre.setGeometry(QtCore.QRect(540, 20, 201, 31))
        self.edt_nombre.setObjectName("edt_nombre")
        self.edt_autor = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_autor.setGeometry(QtCore.QRect(540, 70, 201, 31))
        self.edt_autor.setObjectName("edt_autor")
        self.edt_genero = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_genero.setGeometry(QtCore.QRect(540, 120, 201, 31))
        self.edt_genero.setObjectName("edt_genero")
        self.edt_ano = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_ano.setGeometry(QtCore.QRect(540, 170, 201, 31))
        self.edt_ano.setObjectName("edt_ano")
        self.editar_duracion = QtWidgets.QLineEdit(self.centralwidget)
        self.editar_duracion.setGeometry(QtCore.QRect(540, 220, 201, 31))
        self.editar_duracion.setObjectName("editar_duracion")
        self.btn_guardar_editado = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guardar_editado.setGeometry(QtCore.QRect(600, 270, 81, 31))
        self.btn_guardar_editado.setObjectName("btn_guardar_editado")
        self.btn_guardar_editado.clicked.connect(self.editar)
        Editor.setCentralWidget(self.centralwidget)
        self.texto_transparente(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def texto_transparente(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "Editar musica"))
        item = self.tabla_db.horizontalHeaderItem(0)
        item.setText(_translate("Editor", "Nombre"))
        item = self.tabla_db.horizontalHeaderItem(1)
        item.setText(_translate("Editor", "Autor"))
        item = self.tabla_db.horizontalHeaderItem(2)
        item.setText(_translate("Editor", "Genero"))
        item = self.tabla_db.horizontalHeaderItem(3)
        item.setText(_translate("Editor", "Año"))
        item = self.tabla_db.horizontalHeaderItem(4)
        item.setText(_translate("Editor", "Duracion"))
        self.btn_buscar.setText(_translate("Editor", "Buscar"))
        self.escr_buscar.setPlaceholderText(_translate("Editor", "Buscar"))
        self.cbox_buscar_por.setItemText(0, _translate("Editor", "Nombre "))
        self.cbox_buscar_por.setItemText(1, _translate("Editor", "Autor"))
        self.cbox_buscar_por.setItemText(2, _translate("Editor", "Genero"))
        self.edt_nombre.setPlaceholderText(_translate("Editor", "Editar nombre"))
        self.edt_autor.setPlaceholderText(_translate("Editor", "Editar autor"))
        self.edt_genero.setPlaceholderText(_translate("Editor", "Editar genero"))
        self.edt_ano.setPlaceholderText(_translate("Editor", "Editar año"))
        self.editar_duracion.setPlaceholderText(_translate("Editor", "Editar duracion"))
        self.btn_guardar_editado.setText(_translate("Editor", "Editar"))

    def buscar(self):
        buscar = Conexion()
        self.datos = []
        buscar.buscar_datos(self.datos)

    def editar(self):
        editar = Conexion()
        nombre_buscado = self.escr_buscar.text()
        nombre = self.edt_nombre.text()
        autor = self.edt_autor.text()
        genero = self.edt_genero.text()
        año = self.edt_ano.text()
        duracion = self.editar_duracion.text()
        msg = self.mensaje("Alerta","Se a editado un contacto a travez de su nombre") 
        editar.editar_datos(nombre_buscado,nombre,autor,genero,año,duracion,msg)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QMainWindow()
    ventana = Editorxd(Editor)
    Editor.show()
    sys.exit(app.exec_())
