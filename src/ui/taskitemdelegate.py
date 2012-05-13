'''
Created on Nov 3, 2011

@author: dromoli
'''
from PySide.QtGui import QItemDelegate
from PySide.QtCore import * #@UnusedWildImport

class TaskItemDelegate(QItemDelegate):
    
    def __init__(self, parent=None):
        super(TaskItemDelegate, self).__init__(parent)
        self.rowColors = {1:Qt.GlobalColor.red, 2:Qt.GlobalColor.darkYellow,3:Qt.GlobalColor.yellow,4:Qt.GlobalColor.green,5:Qt.GlobalColor.blue }
        print('----------- Finished initializing delegate')
        
    def drawBackground(self, painter, option, index):
        QItemDelegate.drawBackground(self,painter,option,index)
        item = index.model().itemFromIndex(index)
        print('----------- About to paint item with priority {0}'.format(item.task.priority))
        item.setBackground(self.rowColors[item.task.priority])
        painter.save()
        #painter.restore()