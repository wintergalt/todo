'''
Created on Oct 21, 2011

@author: dromoli
'''

from elixir import Entity, Field, Unicode, DateTime, Integer, \
    setup_all, create_all, OneToMany, ManyToOne, using_options, Boolean
from PySide.QtCore import * #@UnusedWildImport
from PySide.QtGui import * #@UnusedWildImport
import datetime

class Task(Entity):
    using_options(tablename='tasks')
    title = Field(Unicode(30))
    description = Field(Unicode(255))
    date_added = Field(DateTime, default=datetime.datetime.now)
    date_due = Field(DateTime)
    priority = Field(Integer)
    completed = Field(Boolean,default=False)
    taskList = ManyToOne('List')
    primary_key = True
    
    def __repr__(self):
        return '<Task "{0}" with priority {1} due {2} is {3} completed.>'.format(self.title, self.priority, self.date_due, '' if self.completed else 'not')
    
    
class List(Entity):
    ''' The container for tasks (you can have many lists of tasks)'''
    using_options(tablename='lists')
    primary_key = True
    name = Field(Unicode(30))
    tasks = OneToMany('Task')