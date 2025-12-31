
import os

class Todo:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.description}"

class TodoListApp:
    def __init__(self):
        self.todos = []
        self.next_id = 1

    def add_todo(self, description):
        todo = Todo(self.next_id, description)
        self.todos.append(todo)
        self.next_id += 1
        print(f"Added: {todo}")

    def view_todos(self):
        if not self.todos:
            print("No todos yet!")
            return

        print("\n--- Your Todos ---")
        for todo in self.todos:
            print(todo)
        print("------------------")

    def update_todo(self, todo_id, new_description=None, new_completed_status=None):
        for todo in self.todos:
            if todo.id == todo_id:
                if new_description is not None:
                    todo.description = new_description
                if new_completed_status is not None:
                    todo.completed = new_completed_status
                print(f"Updated: {todo}")
                return
        print(f"Todo with ID {todo_id} not found.")

    def delete_todo(self, todo_id):
        initial_len = len(self.todos)
        self.todos = [todo for todo in self.todos if todo.id != todo_id]
        if len(self.todos) < initial_len:
            print(f"Deleted todo with ID {todo_id}.")
        else:
            print(f"Todo with ID {todo_id} not found.")

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def main():
    app = TodoListApp()

    while True:
        clear_screen()
        print("--- Console Todo List ---")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Mark Todo as Complete/Incomplete")
        print("5. Delete Todo")
        print("6. Exit")
        print("-------------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter todo description: ")
            app.add_todo(description)
            input("Press Enter to continue...")
        elif choice == '2':
            app.view_todos()
            input("Press Enter to continue...")
        elif choice == '3':
            try:
                todo_id = int(input("Enter ID of todo to update: "))
                new_description = input("Enter new description (leave blank to keep current): ")
                if new_description:
                    app.update_todo(todo_id, new_description=new_description)
                else:
                    print("No description provided, todo not updated.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
            input("Press Enter to continue...")
        elif choice == '4':
            try:
                todo_id = int(input("Enter ID of todo to mark: "))
                status_choice = input("Mark as (c)omplete or (i)ncomplete? ").lower()
                if status_choice == 'c':
                    app.update_todo(todo_id, new_completed_status=True)
                elif status_choice == 'i':
                    app.update_todo(todo_id, new_completed_status=False)
                else:
                    print("Invalid choice. Please enter 'c' or 'i'.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
            input("Press Enter to continue...")
        elif choice == '5':
            try:
                todo_id = int(input("Enter ID of todo to delete: "))
                app.delete_todo(todo_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
            input("Press Enter to continue...")
        elif choice == '6':
            print("Exiting Todo List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
