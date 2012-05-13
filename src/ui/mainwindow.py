# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Nov  4 12:22:53 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 425)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/accessories-text-editor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setAutoFillBackground(True)
        self.treeView.setAlternatingRowColors(False)
        self.treeView.setSortingEnabled(True)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(True)
        self.horizontalLayout.addWidget(self.treeView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 23))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Tasks = QtGui.QMenu(self.menubar)
        self.menu_Tasks.setObjectName("menu_Tasks")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Todo_Help = QtGui.QAction(MainWindow)
        self.action_Todo_Help.setObjectName("action_Todo_Help")
        self.actionA_bout_Todo = QtGui.QAction(MainWindow)
        self.actionA_bout_Todo.setObjectName("actionA_bout_Todo")
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.actionDelete_Task = QtGui.QAction(MainWindow)
        self.actionDelete_Task.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_Task.setIcon(icon1)
        self.actionDelete_Task.setObjectName("actionDelete_Task")
        self.actionNew_Task = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/list-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Task.setIcon(icon2)
        self.actionNew_Task.setObjectName("actionNew_Task")
        self.actionEdit_Task = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/stock_search-and-replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Task.setIcon(icon3)
        self.actionEdit_Task.setObjectName("actionEdit_Task")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Help.addAction(self.action_Todo_Help)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionA_bout_Todo)
        self.menu_Tasks.addAction(self.actionNew_Task)
        self.menu_Tasks.addAction(self.actionEdit_Task)
        self.menu_Tasks.addSeparator()
        self.menu_Tasks.addAction(self.actionDelete_Task)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Tasks.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionNew_Task)
        self.toolBar.addAction(self.actionEdit_Task)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDelete_Task)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Tasks!", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Tasks.setTitle(QtGui.QApplication.translate("MainWindow", "&Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Todo_Help.setText(QtGui.QApplication.translate("MainWindow", "&Todo Help...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_bout_Todo.setText(QtGui.QApplication.translate("MainWindow", "A&bout Todo...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Task.setText(QtGui.QApplication.translate("MainWindow", "Delete Task", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Task.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Task.setText(QtGui.QApplication.translate("MainWindow", "New Task", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Task.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Task.setText(QtGui.QApplication.translate("MainWindow", "Edit Task", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Task.setShortcut(QtGui.QApplication.translate("MainWindow", "Return", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc