# main.py

# 🚀 Your first Pro-Level Python Script Starts Here!

# Let's build a simple CLI-based "Task Manager"
# This teaches you:
# - Reading user input
# - Writing to files
# - Lists, loops, and conditions

tasks = []

def show_menu():
    print("\n📝 Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Save and Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("✅ Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        with open("tasks.txt", "w") as f:
            for t in tasks:
                f.write(t + "\n")
        print("💾 Tasks saved. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
