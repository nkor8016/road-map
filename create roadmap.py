import matplotlib.pyplot as plt

from task import calculate_duration, tasks


# Function to visualize and save roadmap
def save_roadmap_image(tasks):
    durations = calculate_duration(tasks)
    fig, ax = plt.subplots()
    y_pos = range(len(tasks))
    durations_list = [durations[task.name] for task in tasks]

    ax.barh(y_pos, durations_list, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels([task.name for task in tasks])
    ax.invert_yaxis()  # Invert y-axis to have tasks listed from top to bottom
    ax.set_xlabel('Duration (days)')
    ax.set_title('Project Roadmap')

    plt.savefig('roadmap.png', bbox_inches='tight')  # Save the plot as an image
    plt.show()


# Call the function to save roadmap to image
save_roadmap_image(tasks)
