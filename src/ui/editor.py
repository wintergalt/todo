'''
Created on Oct 23, 2011

@author: diego
'''

from PySide.QtGui import QWidget
from PySide.QtCore import QDate,QTime,QDateTime,Qt
from ui.edittask import Ui_Form
from elixir import *
from model.bo import Task
from datetime import datetime

class Editor(QWidget):
    def __init__(self,parent,task=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.btnCancel.clicked.connect(self.cancel_edit_task)
        self.ui.btnOk.clicked.connect(self.confirm_edit_task)
        
        for i in range(1, 4):
            self.ui.cmbPriority.addItem(str(i),i)
        
        self.action = None
        
        
    def edit(self,task, tree):
        """ Takes a task, loads the widget with its contents and shows the widget """
        self.task = task
        self.tree = tree
        self.ui.txtTaskTitle.setText(self.task.title)
        self.ui.chkCompleted.setChecked(True if self.task.completed else False)
        dt = self.task.date_due
        if dt:
            self.ui.datDueDate.setDate(QDate(dt.year,dt.month,dt.day))
            self.ui.datDueDate.setTime(QTime(dt.hour,dt.minute))
        else:
            self.ui.datDueDate.setDateTime(QDateTime())
        self.ui.txtTaskDescription.setPlainText(self.task.description)
        self.move(50,50)
        self.setWindowTitle('Edit task')
        self.setWindowFlags(Qt.Dialog)
        self.show()
        
    def cancel_edit_task(self):
        self.item = None
        self.hide()
        
    def confirm_edit_task(self):
        cp = self.ui.cmbPriority
        self.task.title = self.ui.txtTaskTitle.text()
        self.task.description = self.ui.txtTaskDescription.document().toPlainText()
        self.task.priority = cp.itemData(cp.currentIndex())
        self.task.date_due = datetime.strptime(self.ui.datDueDate.textFromDateTime(self.ui.datDueDate.dateTime()),'%d/%m/%Y %H:%M')
        self.task.completed = self.ui.chkCompleted.isChecked()
        session.commit()
        self.tree.model().itemFromIndex(self.tree.currentIndex()).setData(self.task)
        self.hide()
        