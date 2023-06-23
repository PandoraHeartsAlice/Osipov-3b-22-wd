class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                tasks = f.read().splitlines()
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            f.write('\n'.join(self.tasks))

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()

    def display_tasks(self):
        print("List of household chores:")
        for task in self.tasks:
            print(task)


todo_list = ToDoList('my_todo_list.txt')

todo_list.add_task("To wash the dishes")
todo_list.add_task("Do the cleaning")

todo_list.remove_task("Do the cleaning")

todo_list.display_tasks()
