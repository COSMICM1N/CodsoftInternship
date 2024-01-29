class ToDoCLI:
    def __init__(self):
        self.tasks=[]
        
    def add_task(self,task):
        self.tasks.append(task)
        print("Task added successfully")
        
    def update_task(self,index,updated_task):
        if 0<=index<len(self.tasks):
            self.tasks[index]=updated_tasks
            print("Task updated successfully")
        else:
            print("Invalid Index")
            
    def delete_task(self,index):
        if 0<=index<len(self.tasks):
            deleted_tasks=self.tasks.pop(index)
            print(f"Task '{deleted_task} deleted successfully")
        else:
            print("Invalid index")
            
    def list_task(self):
        print("Task List:")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}.{task}")
            
if __name__ == "__main__":
    todo_app=ToDoCLI()
    
    while True:
        print("\nOptions:")
        print("1.Add Task")
        print("2.Update Task")
        print("3.Delete Task")
        print("4.List Tasks")
        print("5.Exit")
        
        option=input("Enter your option(1-5):")
        
        if option=="1":
            task=input("Enter the task:")
            todo_app.add_task(task)
        elif option=="2":
            index=int(input("Enter the task index to update:"))
            updated_task=input("Enter the uodated task:")
            todo_app.update_task(index -1,updated_task)
        elif option=="3":
            index=int(input("Enter the task index to delete:"))
            todo_app.delete_task(index -1)
        elif option=="4":
            todo_app.list_task()
        elif option=="5":
            break
        else:
            print("Invalid option")