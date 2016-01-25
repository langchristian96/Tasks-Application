from Domain.Task import *

class tasksController:
    def __init__(self,repo):
        self.__repo=repo
        self.__status='active'
        for e in self.__repo.getAll():
            if e.getStatus()=='active':
                self.__currentTask=e
                break
    def getCurrentTask(self):
        return self.__currentTask
    def getActive(self):
        list=[]
        for e in self.__repo.getAll():
            if e.getStatus()=='active':
                list.append(e)
        return list
                
    def getDone(self):
        list=[]
        for e in self.__repo.getAll():
            if e.getStatus()=='done':
                list.append(e)
        return list
    def getArchived(self):
        list=[]
        for e in self.__repo.getAll():
            if e.getStatus()=='archived':
                list.append(e)
        return list
    def setCurrentTask(self,obj):
        self.__currentTask=obj
    def add(self,obj):
        self.__repo.add(obj)
    def remove(self,obj):
        self.__repo.remove(obj)
    def update(self,obj):
        self.__repo.update(obj)
    def updatee(self):
        self.__repo.store()
    def filter(self,status):
        self.__status=status
        for e in self.__repo.getAll():
            if e.getStatus()==status:
                self.__currentTask=e
                break
    def next(self):
        for e in self.__repo.getAll():
            if e.getId()>self.__currentTask.getId() and e.getStatus()==self.__status:
                self.__currentTask=e
                break   
    def undo(self):
        self.__repo.undo()
    def redo(self):
        self.__repo.redo()
    def previous(self):
        list=self.__repo.getAll()
        
        idx=list.index(self.__currentTask)
        for idx in range(idx,-1,-1):
            if list[idx].getId()<self.__currentTask.getId() and list[idx].getStatus()==self.__status:
                self.__currentTask=list[idx]
                break
    def getMaxId(self):
        max=0
        for e in self.__repo.getAll():
            if e.getId()>max:
                max=e.getId()
        return max+1
    
        
    