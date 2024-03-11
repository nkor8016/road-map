import svgwrite
import pandas as pd
from datetime import datetime
import calendar

# Create a sample DataFrame
data = {
    'Task': ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5'],
    'Start Date': ['2023-04-01', '2023-04-10', '2023-04-15', '2023-05-01', '2023-05-15'],
    'End Date': ['2023-04-15', '2023-04-25', '2023-05-05', '2023-05-20', '2023-06-01'],
    'Team': ['Team A', 'Team B', 'Team A', 'Team C', 'Team B']
}

df = pd.DataFrame(data)

# Convert date strings to datetime objects
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Define the dimensions of the SVG image
width, height = 800, 400

# Create a new SVG drawing
dwg = svgwrite.Drawing('gantt_chart.svg', size=(width, height))

# Add a white background rectangle
dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='white'))

# Define the chart properties
chart_start = df['Start Date'].min()
chart_end = df['End Date'].max()
bar_height = 20
padding = 10
label_padding = 30  # Increased padding for task labels

# Draw the month rectangles and labels
month_width = (width - 2 * padding) // 12
month_height = 30
x = padding
y = padding + month_height + padding * 2

# Draw the year label
year = chart_start.year
dwg.add(dwg.text(str(year), insert=(width // 2, y - month_height // 2 - padding), font_size=20, text_anchor='middle'))

# Draw the SCM - team label
dwg.add(dwg.text("SCM - team", insert=(width // 2, y - month_height // 2 + padding), font_size=16, text_anchor='middle'))

for month in range(1, 13):
    month_x = x
    month_y = y

    # Draw the month rectangle
    dwg.add(dwg.rect(insert=(month_x, month_y), size=(month_width, month_height), fill='lightgray', stroke='black', stroke_width=1, opacity=0.5))
    dwg.add(dwg.rect(insert=(month_x, month_y * 1.5 + 10), size=(month_width, height - month_y * 2), fill='lightgray', stroke='black', stroke_width=1, opacity=0.25))
    dwg.add(dwg.rect(insert=(month_x + month_width / 2, month_y * 1.5 + 10), size=(month_width, height - month_y * 2), fill='lightgray', stroke='black', stroke_width=1, opacity=0.05))
    dwg.add(dwg.text(calendar.month_abbr[month], insert=(month_x + month_width // 2, month_y + month_height // 2), font_size=12, text_anchor='middle'))

    # Draw the vertical slice
    slice_x = month_x + month_width
    dwg.add(dwg.line(start=(slice_x, month_y), end=(slice_x, month_y + month_height), stroke='black', stroke_width=1))

    x += month_width

# Draw the task bars
bar_y = y + month_height + padding
for _, row in df.iterrows():
    task = row['Task']
    start_date = row['Start Date']
    end_date = row['End Date']
    team = row['Team']

    # Calculate the x-coordinates based on the start and end dates
    start_x = padding + (start_date - datetime(start_date.year, 1, 1)).total_seconds() / (365.25 * 24 * 60 * 60) * (width - 2 * padding)
    end_x = padding + (end_date - datetime(end_date.year, 1, 1)).total_seconds() / (365.25 * 24 * 60 * 60) * (width - 2 * padding)

    # Draw the task bar
    dwg.add(dwg.rect(insert=(start_x + 3, bar_y), size=((end_x - start_x + 3), bar_height), fill='lightblue', stroke='black', stroke_width=1))

    # Draw the task label
    label_x = start_x + (end_x - start_x) / 2
    dwg.add(dwg.text(f"{task} ({team})", insert=(label_x, bar_y + bar_height + label_padding), font_size=12, text_anchor='middle'))

    bar_y += bar_height + padding + label_padding

# Save the SVG image
dwg.save()