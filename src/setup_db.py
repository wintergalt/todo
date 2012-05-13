'''
Created on Oct 21, 2011

@author: dromoli
'''

from model.bo import List, Task
from datetime import datetime
from elixir import *

if __name__ == '__main__':
    setup_all(True)
    # clear tables
    session.query(List).delete()
    session.query(Task).delete()
    
    defaultList = List(name=u'Default')
    taskOne = Task(title=u'Task 1', 
                   date_due=datetime(2011, 12, 25), 
                   priority=1,taskList=defaultList,completed=True)
    taskTwo = Task(title=u'Task 2', 
                   date_due=datetime(2012, 12, 25), 
                   priority=2,taskList=defaultList,completed=False)
    session.commit()
