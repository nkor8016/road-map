# Sample code to create a basic roadmap

class Task:
    def __init__(self, name, duration, dependencies=None):
        self.name = name
        self.duration = duration
        self.dependencies = dependencies or []


# Define tasks
tasks = [
    Task("Task A", 5),
    Task("Task B", 7, dependencies=["Task A"]),
    Task("Task C", 4, dependencies=["Task A"]),
    Task("Task D", 6, dependencies=["Task B", "Task C"]),
]


# Function to calculate total duration
def calculate_duration(tasks):
    durations = {task.name: task.duration for task in tasks}
    for task in tasks:
        for dep in task.dependencies:
            durations[task.name] += durations[dep]
    return durations


# Function to print roadmap
def print_roadmap(tasks):
    durations = calculate_duration(tasks)
    for task in tasks:
        print(f"{task.name}: {durations[task.name]} days")


# Print the roadmap
print_roadmap(tasks)
