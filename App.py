from Domain.Task import *
from Repository.Repository import *
from Controller.TasksController import *
from UI.UI import *


repo=Repository()

ctrl=tasksController(repo)
ui=UI(ctrl)
ui.Menu()