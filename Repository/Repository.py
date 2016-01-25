from Domain.Task import *
import copy
class Repository:
    _fName='tasks.txt'
    def __init__(self):
        self.__data=[]
        self.__undo=None
        self.__redo=None
        self.__loadFromFile()
    def add(self,obj):
        self.__undo=copy.copy(self.__data)
        self.__redo=None
        if self.find(obj.getId())==None:
            self.__data.append(obj)
            self.__storeToFile()
        else:
            raise ValueError("The object already exists")
    def find(self,id):
        for e in self.__data:
            if e.getId()==id:
                return e
        return None
    
    def remove(self,obj):
        self.__undo=copy.copy(self.__data)
        self.__redo=None
        if self.find(obj.getId())!=None:
            self.__data.remove(obj)
            self.__storeToFile()
        else:
            raise ValueError("Object does not exist")
    def undo(self):
        if self.__undo==None:
            raise ValueError("Cannot undo")
        else:
            self.__redo=self.__data
            self.__data=self.__undo
            self.__undo=None
            self.__storeToFile()
    def redo(self):
        if self.__redo==None:
            raise ValueError("Cannot redo")
        else:
            self.__undo=self.__data
            self.__data=self.__redo
            self.__redo=None
            self.__storeToFile()
    def update(self,obj):
        self.__undo=copy.copy(self.__data)
        self.__redo=None
        e=self.find(obj.getId())
        if e!=None:
            idx=self.__data.index(e)
            self.__data.remove(e)
            self.__data.insert(idx,obj)
            self.__storeToFile()
        else:
            raise ValueError("The object does not exist")
    def getAll(self):
        return self.__data;
    def store(self):
        self.__storeToFile()
    def __storeToFile(self):
        try:
            f=open(self._fName,'w')
            list=copy.copy(self.__data)
            for e in list:
                string=''
                string+=str(e.getId())
                string+=','
                string+=e.getText()
                string+=','
                string+=e.getStatus()
                string+='\n'
                f.write(string)
            f.close()
        except IOError:
            return
    def __loadFromFile(self):
        try:
            f=open(self._fName,'r')
        except IOError:
            return
        
        t=f.readline().strip()
        while t!='':
            args=t.split(',')
            tsk=Task(int(args[0]),args[1],args[2])
            self.__data.append(tsk)
            t=f.readline().strip()
        f.close()
            
            