# CLI Task Tracker

## Quick start

1. Open a terminal in the repository folder.
2. Add the repository folder to your Windows `PATH` so the command works from anywhere.
3. Run:

   task-cli add "Buy groceries"

## Example commands

task-cli add "Buy groceries"
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete-all
task-cli list done

Text in parentheses is your input. Text in square brackets is a description.

Before using the task tracker, add the repository folder to your `PATH` so you can run the command without typing `python` first.

## Commands

- `add (task to be added)`
- `update (task ID to be updated + updated task)`
- `delete (task ID to be deleted)`
- `delete-all` [delete all tasks]
- `mark-in-progress (task ID to be marked as in-progress)`
- `mark-done (task ID to be marked as done)`
- `list` [list all tasks]
- `list todo` [list tasks that are todo]
- `list in-progress` [list tasks that are in progress]
- `list done` [list tasks that are done]

Project URL: <https://roadmap.sh/projects/task-tracker>
