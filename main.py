import json


def get_tasks():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    return tasks


def commit(tasks, config_path="tasks.json"):
    with open(config_path, "w") as file:
        json.dump(tasks, file)


def add_task(tasks, task, status, notes):
    task_dict = {'name': task, 'status': status, 'notes': notes}

    tasks["tasks"].append(task_dict)

    commit(tasks)


def change_task(tasks, idx, task, status, notes):
    if task:
        tasks["tasks"][idx]["name"] = task
    if status:
        tasks["tasks"][idx]["status"] = status
    if notes:
        tasks["tasks"][idx]["notes"] = notes

    commit(tasks)


def remove_task(tasks, idx):
    tasks["tasks"].pop(idx)

    commit(tasks)


def main():
    while True:
        action = input("add, list, change, or remove tasks: ")
        tasks = get_tasks()

        match action.lower():
            case "list":
                for idx, task in enumerate(tasks["tasks"]):
                    print(f"---TASK {idx + 1}---")
                    print(f"Name: {task["name"]}\nStatus: {task["status"]}\nNotes: {task["notes"]}")

            case "add":
                task = input("Task name: ")
                status = input("Status: ")
                notes = input("Notes: ")
                add_task(tasks, task, status, notes)

            case "change":
                idx = int(input("Enter task number to change: ")) - 1

                task = input("Task name: ")
                status = input("Status: ")
                notes = input("Notes: ")

                change_task(tasks, idx, task, status, notes)

            case "remove":
                idx = int(input("Enter task number to remove: ")) - 1

                remove_task(tasks, idx)
            case "quit":
                exit("Bye!")
            case _:
                print("Please enter a valid command.")
                continue


if __name__ == "__main__":
    main()
