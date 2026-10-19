import argparse
import json
import datetime
from pathlib import Path

USER_DATA_DIR = Path.home() / ".task-cli"
DATA_FILE = USER_DATA_DIR / "tasks.json"


def ensure_data_dir():
    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    ensure_data_dir()
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return {"all_tasks": [], "in_progress": [], "done": []}


def save_data():
    ensure_data_dir()
    data = {
        "all_tasks": all_tasks,
        "in_progress": in_progress,
        "done": done,
    }
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


data = load_data()
all_tasks = data["all_tasks"]
in_progress = data["in_progress"]
done = data["done"]

def add_task(task):
    if task in all_tasks:
        print("Task already exists")
        return
    created_at = datetime.datetime.now()
    created_at = created_at.strftime("createdAt: %H:%M:%S, %d-%m-%Y")
    all_tasks.append(task + ", " + created_at)
    print(f"Task added succesfully (ID: {len(all_tasks)})")


def update_task(task_id, task):
    if (task_id - 1) not in range(len(all_tasks)):
        return
    elif len(task) < 1:
        return
    updated_at = datetime.datetime.now()
    updated_at = updated_at.strftime("updatedAt: %H:%M:%S, %d-%m-%Y")
    all_tasks[task_id - 1] = task + ", " + updated_at
    print(f"Task has been updated (ID: {len(all_tasks)})")


def delete_task(task_id):
    if (task_id - 1) not in range(len(all_tasks)):
        return
    task = all_tasks[task_id - 1]
    if task in all_tasks:
        all_tasks.remove(task)
    elif task in in_progress:
        in_progress.remove(task)
    elif task in done:
        done.remove(task)
    print("Task has been deleted")


def delete_all():
    all_tasks.clear()
    in_progress.clear()
    done.clear()
    print("All tasks have been deleted")


def mark_in_progress(mip_id):
    if (mip_id - 1) not in range(len(all_tasks)):
        return
    if (mip_id - 1) in range(len(in_progress)):
        print("Task is already in progress")
        return
    task = all_tasks[mip_id - 1]
    if task in done:
        return
    in_progress.append(task)
    print("Task updated to in-progress")


def mark_done(done_id):
    if (done_id - 1) not in range(len(all_tasks)):
        return
    if (done_id - 1) in range(len(done)):
        print("Task is already done")
        return
    task = all_tasks[done_id - 1]
    if task in in_progress:
        in_progress.remove(task)
    done.append(task)
    print("Task updated to done")


def list_tasks():
    print("\nAll tasks:\n")
    for task in all_tasks:
        print(f"{task} (ID:{all_tasks.index(task) + 1})")
    print("")


def list_todo():
    to_do = all_tasks.copy()
    to_do_copy = to_do.copy()
    print("\nTasks to-do:\n")
    for task in to_do_copy:
        if task in in_progress or task in done:
            to_do.remove(task)
        else:
            print(f"{task} (ID:{all_tasks.index(task) + 1})")
    print("")


def list_in_progress():
    print("\nTasks in-progress:\n")
    for task in in_progress:
        print(f"{task} (ID:{all_tasks.index(task) + 1})")
    print("")


def list_done():
    print("\nTasks done:\n")
    for task in done:
        print(f"{task} (ID:{all_tasks.index(task) + 1})")
    print("")


parser = argparse.ArgumentParser(prog="task-cli")


commands = parser.add_subparsers(dest="command", required=True)

add_parser = commands.add_parser("add", help="add task")
add_parser.add_argument("task")

update_parser = commands.add_parser("update", help="update task")
update_parser.add_argument("task_id", type=int)
update_parser.add_argument("task")

delete_parser = commands.add_parser("delete", help="delete task")
delete_parser.add_argument("task_id", type=int)

delete_all_parser = commands.add_parser("delete-all", help="delete all tasks")

mark_in_progress_parser = commands.add_parser("mark-in-progress", help="mark task as in progress")
mark_in_progress_parser.add_argument("mip_id", type=int)

mark_done_parser = commands.add_parser("mark-done", help="mark task as done")
mark_done_parser.add_argument("done_id", type=int)

list_all_parser = commands.add_parser("list", help="list all")
list_all_parser.add_argument("status", nargs="?", choices=["todo", "in-progress", "done"])

args = parser.parse_args()

if args.command == "add":
    add_task(args.task)
    save_data()
elif args.command == "update":
    update_task(args.task_id, args.task)
    save_data()
elif args.command == "delete":
    delete_task(args.task_id)
    save_data()
elif args.command == "delete-all":
    delete_all()
    save_data()
elif args.command == "mark-in-progress":
    mark_in_progress(args.mip_id)
    save_data()
elif args.command == "mark-done":
    mark_done(args.done_id)
    save_data()
elif args.command == "list" and args.status == None:
    list_tasks()
elif args.command == "list" and args.status == "todo":
    list_todo()
elif args.command == "list" and args.status == "in-progress":
    list_in_progress()
elif args.command == "list" and args.status == "done":
    list_done()
