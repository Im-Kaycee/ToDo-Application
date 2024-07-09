"""TO-DO list app
Should be able to:
1. Take in input
2. Save input
3. Output content
4. Delete content
Usage:
Add task todo.py --task "task"
Delete task todo.py --delete_task id
Show tasks todo.py --show_tasks showtasks
"""

import argparse
import sqlite3


def create_table():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, tasks TEXT)""")
    conn.commit()
    conn.close()


def insert_task(tasks):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (tasks) VALUES (?)', (tasks,))
    conn.commit()
    conn.close()


def show_tasks():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    print("It is working")
    data = cur.execute('SELECT * FROM tasks')
    for row in data:
        print(row)


def delete_tasks(id):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Helps you manage your tasks")
    parser.add_argument('--task', '-t', help='This is the task to be added')
    parser.add_argument('--show_tasks', '-s', help='This shows all tasks')
    #parser.add_argument('--priority', '-p', help='This is used to set priority')
    parser.add_argument('--delete_task', '--d', help='This is used to delete a task')

    args = parser.parse_args()
    task = args.task
    create_table()
    if args.task:
        insert_task(task)
        print(f"Task '{task}' has been added")
    elif args.show_tasks:
        show_tasks()
    elif args.delete_task:
        delete_tasks(args.delete_task)
        print(f"Task '{task}' has been deleted")


if __name__ == "__main__":
    main()
