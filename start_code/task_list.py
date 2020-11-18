tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
  ]
# Print a list of uncompleted tasks
# Print a list of completed tasks
# Print a list of all task descriptions
# Print a list of tasks where time_taken is at least a given time
# Print any task with a given description

# def task_status(list):
#     uncompleted_task = []
#     completed_task = []
#     for task in list:
#         while task["completed"] == False:
#             uncompleted_task.append(task), 
#             completed_task.append(task)
#     print(uncompleted_task)
#     print(completed_task)

# task_status(tasks)


def uncompleted(list):
    uncompleted_task = []
    for task in list:
        if task["completed"] == False:
            uncompleted_task.append(task)
    #print(uncompleted_task)

uncompleted(tasks)

def completed(list):
    completed_task = []
    for task in list:
        if task["completed"] == True:
            completed_task.append(task)
    #print(completed_task)

completed(tasks)

def get_task_description(task_order):
    task_description = []
    for task in tasks:
        task_description.append(task["description"])
    print(task_description)

get_task_description(tasks)





