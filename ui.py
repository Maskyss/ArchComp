import json


def open_json():
    with open('tasks.json') as jsonfile:
        return json.load(jsonfile)


tasks = open_json()


def print_tasks():
    print(json.dumps(tasks, indent=2, sort_keys=True))


def write_tasks():
    with open('tasks.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(tasks, indent=2))


def add_tasks():
    id_task = 1
    for x in tasks:
        if x['id'] == id_task:
            id_task += 1
        else:
            break

    title = input("title: ")
    description = input("done: ")
    day = input("day: ")
    month = input("month: ")
    year = input("year: ")

    additional_task = {"id": id_task, "title": title, "done": description,
                       "day": day, "month": month, "year": year}

    tasks.append(additional_task)

    write_tasks()


def delete_tasks():
    id_del = input("id:")
    i=-1
    for x in tasks:
        i+=1
        if x['id'] == int(id_del):
            del tasks[i]

    write_tasks()


def update_tasks():
    id_del = input("id:")
    for x in tasks:
        if x['id'] == int(id_del):
            x['done'] = True

    write_tasks()
