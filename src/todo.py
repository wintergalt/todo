'''
Created on Oct 21, 2011

@author: dromoli
'''

from PySide.QtCore import * #@UnusedWildImport
from PySide.QtGui import * #@UnusedWildImport
from model.bo import Task, List
from ui.mainwindow import Ui_MainWindow
from ui.editor import Editor
from elixir import * #@UnusedWildImport
import sys, os
from datetime import datetime
import logging

dbdir = os.path.join(os.path.expanduser("~"),".todo")
dbfile = os.path.join(dbdir,"tasks.sqlite")

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)
        self.current_list = session.query(List).filter_by(name=u'Default').one()
        self.load_data()
        self.editor = Editor(self)
        self.editor.hide()
        logging.basicConfig(level=logging.DEBUG)
        
        
    def load_data(self):
        tasks = session.query(Task).filter_by(taskList=self.current_list)
        tv = self.mainwindow.treeView
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Task', 'Description', 'Date due'])
        
        for task in tasks:
            items = []

            it = QStandardItem(QIcon('ui/priority-{0}.png'.format(task.priority)),task.title)
            it.setData(task.title, Qt.DisplayRole)
            it.task = task
            it.column_name = 'title'
            it.setCheckable(True)
            if task.completed:
                it.setCheckState(Qt.CheckState.Checked)
            else:
                it.setCheckState(Qt.CheckState.Unchecked)
            items.append(it)
            
            it = QStandardItem()
            it.setData(task.description, Qt.DisplayRole)
            it.task = task
            it.column_name = 'description'
            items.append(it)
            
            it = QStandardItem()
            it.setData(str(task.date_due), Qt.DisplayRole)
            it.task = task
            it.column_name = 'date_due'
            items.append(it)
            
            model.appendRow(items)
            
        tv.setModel(model)
        tv.sortByColumn(2, Qt.SortOrder.AscendingOrder)
        tv.setColumnWidth(0, 120)
        tv.setColumnWidth(1, 300)
        tv.setColumnWidth(2, 165)
        tv.setIndentation(0)
        model.dataChanged.connect(self.item_data_changed)
        tv.selectionModel().currentChanged.connect(self.task_selection_changed)
        self.mainwindow.actionDelete_Task.triggered.connect(self.delete_task_action)
        self.mainwindow.actionEdit_Task.triggered.connect(self.edit_task_action)
        self.mainwindow.actionNew_Task.triggered.connect(self.new_task_action)
        self.mainwindow.action_Exit.triggered.connect(self.exit_action)
        
        
    def item_data_changed(self, item):
        if item.column() == 0:
            print('Ignoring item_data_changed... column was 0')
            return
        
        item = self.mainwindow.treeView.model().itemFromIndex(self.mainwindow.treeView.currentIndex())
        if item.checkState():
            item.task.completed = True
        else:
            item.task.completed = False
        setattr(item.task, item.column_name, item.data(Qt.DisplayRole))
        self.mainwindow.treeView.model().item(item.row(), 0).setIcon(QIcon('ui/priority-{0}.png'.format(item.task.priority)))
        session.commit()
        
    def delete_task_action(self,checked=None):
        idx = self.mainwindow.treeView.currentIndex()
        # First, get the 'current' task
        item = self.mainwindow.treeView.model().itemFromIndex(idx)
        # if none selected, do nothing
        if not item:
            logging.debug('No item selected, returning...')
            return
        # Delete the task
        item.task.delete()
        session.commit()
        self.mainwindow.treeView.model().removeRow(idx.row())
        
    def new_task_action(self,checked=None):
        # Open the task in the editor
        self.editor.action = 'new_task'
        self.editor.edit(Task(taskList=self.current_list), self.mainwindow.treeView.model())
        
    def number_of_tasks(self):
        return session.query(Task).count()
        
    def edit_task_action(self,checked=None):
        # Open the task in the editor
        self.editor.action = 'edit_task'
        currentItem = self.mainwindow.treeView.model().itemFromIndex(self.mainwindow.treeView.currentIndex())
        self.editor.edit(currentItem.task, self.mainwindow.treeView.model())
        
    def exit_action(self):
        sys.exit()
        
    def task_selection_changed(self, current, previous):
        self.mainwindow.actionDelete_Task.setEnabled(True if current else False) 
        
            
def init_db():
    if not os.path.isdir(dbdir):
        os.mkdir(dbdir)
    metadata.bind = 'sqlite:///{0}'.format(dbfile)
    metadata.bind.echo = True
    setup_all()
    if not os.path.exists(dbfile):
        create_all()
        
    # clear tables
#    session.query(List).delete()
#    session.query(Task).delete()
#    
#    defaultList = List(name=u'Default')
#    taskOne = Task(title=u'Task 1', 
#                   date_due=datetime(2011, 12, 25), 
#                   priority=1,taskList=defaultList,completed=True,
#                   description='First task')
#    taskTwo = Task(title=u'Task 2', 
#                   date_due=datetime(2012, 12, 25), 
#                   priority=2,taskList=defaultList,completed=False,
#                   description='This is the second task')
#    
#    session.commit()
    
                
if __name__ == '__main__':
    init_db()
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
    
