from Domain.Task import *
from Repository.Repository import *
from Controller.TasksController import *
import copy
class UI:
    def __init__(self,controller):
        
        self.__controller=controller
    @staticmethod
    def printMenu():
        print('Available commands:')
        print('prev')
        print('next')
        print('filter <status>')
        print('add <text>')
        print('status <new_status>')
        
    def Menu(self):
        while(True):
            print(str(self.__controller.getCurrentTask()))
            print('Available commands:')
            print('prev')
            print('next')
            print('filter <status>')
            print('add <text>')
            print('status <new_status>')
            print('text <new_text>')
            print('remove')
            print('report')
            print('undo')
            print('redo')
        
            command=input("Please insert command \n")
            args=command.strip().split(' ')
            if args[0]=='prev' and len(args)==1:
                b=self.__controller.getCurrentTask()
                self.__controller.previous()
                if b==self.__controller.getCurrentTask():
                    print("There aren't any tasks before this one.")
                
            elif args[0]=='next' and len(args)==1:
                b=self.__controller.getCurrentTask()
               
                self.__controller.next()
                if b==self.__controller.getCurrentTask():
                    print("There aren't any tasks after this one.")
                
                
            elif args[0]=='filter' and len(args)==2:
                
                
                self.__controller.filter(args[1])
            elif args[0]=='add' and len(args)!=1:
                max=self.__controller.getMaxId()
                strng=''
                for i in range(1,len(args)):
                    strng+=' '
                    strng+=args[i]
                obj=Task(max,strng,'active')
                self.__controller.add(obj)
            elif args[0]=='status':
                if args[1]=='active' or args[1]=='archived' or args[1]=='done':
                    e=self.__controller.getCurrentTask()
                    obj=Task(e.getId(),e.getText(),args[1])
                    self.__controller.update(obj)
                    self.__controller.setCurrentTask(obj)
                else:
                    print("invalid status")
            elif args[0]=='text':
                e=self.__controller.getCurrentTask()
                obj=Task(e.getId(),args[1],e.getStatus())
                self.__controller.update(obj)
                self.__controller.setCurrentTask(obj)
            elif args[0]=='remove':
                try:
                    e=self.__controller.getCurrentTask()
                    self.__controller.next()
                    self.__controller.remove(e)
                except ValueError as w:
                    print(w)
            elif args[0]=='report':
                active=self.__controller.getActive()
                done=self.__controller.getDone()
                archived=self.__controller.getArchived()
                print('active: '+str(len(active)))
                print('archived: '+str(len(archived)))
                print('done: '+str(len(done)))
            elif args[0]=='undo':
                try:
                    self.__controller.undo()
                except ValueError:
                    print('Cannot undo only once')
            elif args[0]=='redo':
                try:
                    self.__controller.redo()
                except ValueError as v:
                    print(v)
            else:
                print('Invalid command. Try again')
            print('\n')
                
    