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


def replace_column():
    import pandas as pd

    # Assuming 'data' is your dictionary
    data = {
        'Task': ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5'],
        'Start Date': ['2023-04-01', '2023-04-10', '2023-04-15', '2023-05-01', '2023-05-15'],
        'End Date': ['2023-04-15', '2023-04-25', '2023-05-05', '2023-05-20', '2023-06-01'],
        'Product / Initiative': ['Sub Team A 1', 'Sub Team B', 'Sub Team A 2', 'Sun Team C 1', 'Sub Team B 2'],
        'Team': ['Team A', 'Team B', 'Team A', 'Team C', 'Team B']
    }

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Replace 'Team A' in 'Team' column with corresponding values from 'Product / Initiative' column
    replace_team_name = "Team A"
    column_to_replace = 'Team'
    replacing_values_column = 'Product / Initiative'
    df.loc[df[column_to_replace] == replace_team_name, column_to_replace] = df.loc[
        df[column_to_replace] == replace_team_name, replacing_values_column]

    print(df)
