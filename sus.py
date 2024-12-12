class ToDoList:
    def init(self):
        self.tasks = []

    def viewtasks(self):
        if not self.tasks:
            print("No tasks found")
        else:
            print("\nTasks:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "\u2713" if task["done"] else "\u2717"
                print(f"{idx}. {task['task']} [{status}]")


if name == "_main":
    main(