class Task:
    def __init__(self, desc):
        self.desc = desc
        self.done = False

    def __str__(self):
        return f"[{'✓' if self.done else '✗'}] {self.desc}"


tasks = []

def addTask():
    tasks.append(Task(input("Enter task: ")))

def markDone():
    listTasks("all")
    try:
        i = int(input("Task number to mark as done: "))
        if 0 <= i < len(tasks):
            tasks[i].done = True
            print("Marked as done.")
    except:
        print("Invalid input.")

def listTasks(filter_by="all"):
    print("\n--- Tasks ---")
    for i, t in enumerate(tasks):
        if filter_by == "done" and not t.done: continue
        if filter_by == "pending" and t.done: continue
        print(f"{i}. {t}")
    print("-------------\n")

def searchTask():
    keyword = input("Keyword: ").lower()
    print("\n--- Search ---")
    found = False
    for i, t in enumerate(tasks):
        if keyword in t.desc.lower():
            print(f"{i}. {t}")
            found = True
    if not found:
        print("No match found.")
    print("-------------\n")

while True:
    print("1.Add  2.Done  3.All  4.Done Only  5.Pending Only  6.Search  7.Exit")
    choice = input("Choice: ")
    if choice == "1": addTask()
    elif choice == "2": markDone()
    elif choice == "3": listTasks()
    elif choice == "4": listTasks("done")
    elif choice == "5": listTasks("pending")
    elif choice == "6": searchTask()
    elif choice == "7": break
    else: print("Invalid.")
