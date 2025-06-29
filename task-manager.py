import json
import os

FILE_PATH = "files/task-file"

class Task():

    def __init__(self, title, completed=False, date=None, topic=None):
        self.title = title
        self.completed = completed
        self.date = date
        self.topic = topic

    def __str__(self):
        return f"Task {self.title} due for {self.date} and topic: {self.topic}"

    def to_dict(self):
        return {"title" : self.title,
                "completed" : self.completed,
                "date" : self.date,
                "topic" : self.topic}
    @staticmethod
    def from_dict(dict):
        return Task(title=dict['title'], 
                    completed=dict['completed'], 
                    date=dict['date'], 
                    topic=dict['topic'])


class TaskManager():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def complete_task(self, title):
        for target in self.tasks:
            if target.title == title:
                target.completed = True
                return f"Task with title {title} marked as completed with success" 
        return f"Couldn't find a task with the title {title}"
    
    def export_tasks(self):
        return [task.to_dict() for task in self.tasks]


    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.export_tasks(), f, indent=4)


    def load_from_file(self, filename):
        if not os.path.exists(filename):
            print("No JSON file was found, empty list initialized")
            self.tareas = []
            return
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
                print("Tasks loaded successfuly")
            except json.JSONDecodeError:
                print("Error: archivo JSON malformado.")
                self.tasks = []
                

    def __str__(self):
        return "\n".join(str(task) for task in self.tasks)

    


manager = TaskManager()    
manager.load_from_file(FILE_PATH)
print(manager)






