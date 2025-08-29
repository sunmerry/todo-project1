
class Todo:
  def __init__(self):
    self.task = input("Enter your task: ")
    self.task_description = input("task description: ")
    self.task_deadline = input("when to complete: ")
    self.task_completion = False
    self.reminder = {1: False, 2: False, 3: False}
  def __str__(self):
    return f'A task : {self.task}'
  

print("Create a new task")
todo = Todo()



