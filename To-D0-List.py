class TodoItem:
    def __init__(self, task):
        self.task = task
        self.completed = False
    def mark_completed(self):
        self.completed = True
    def __str__(self):
        status = "✓" if self.completed else "✘"
        return f"[{status}] {self.task}"
class TodoList:
    def __init__(self):
        self.items = []
    def add_task(self, task):
        self.items.append(TodoItem(task))
    def update_task(self, index, new_task):
        if 0 <= index < len(sel.items):
            self.items[index].task = new_task
        else:
            print("Invalid task index.")
    def mark_task_completed(self, index):
        if 0 <= index < len(self.items):
            self.items[index].mark_completed()
        else:
            print("Invalid task index")
    def display_tasks(self):
        if not self.items:
            print("No tasks in the list.")
        else:
            for idx, item in enumerate(self.items):
                print(f"{idx + 1}.{item}")
def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Mark Task Complted")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Choose an option(1-5):")
        if choice == '1':
            task = input("Enter the task:")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
            index =  int(input("Enter task number to update:"))-1
            new_task =  int(input("Enter new task:"))
            todo_list.update_task(index, new_task)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Enter task number to mark as completed"))-1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Existing the To-Do List.")
            break
        else:
            print("Invalid option. Please choose again.")
if __name__=="__main__":
    main()
