class Task:
    def __init__(self,id,text,status):
        self.__id=id
        self.__text=text
        self.__status=status
        
    def getId(self):
        return self.__id
    def getText(self):
        return self.__text
    def getStatus(self):
        return self.__status
    def __str__(self):
        return str(self.__id)+' '+self.__text+' '+self.__status
    
def testTask():
    tsk=Task(1,'caca','active')
    assert tsk.getId()==1
    assert tsk.getText()=='caca'
    assert tsk.getStatus()=='active'
    
if __name__=='__main__':
    testTask()
    