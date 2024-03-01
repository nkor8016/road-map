# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script:

# dataset = pandas.DataFrame(Title, Year, Quarter, Month, Day, Year.1, Quarter.1, Month.1, Day.1)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
from datetime import datetime
import pandas as pd
from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

dataset['Start Date'] = pd.to_datetime(dataset['Start Date']).dt.strftime("%Y-%m-%d")
dataset['End Date'] = pd.to_datetime(dataset['End Date']).dt.strftime("%Y-%m-%d")

roadmap = Roadmap(2000, 5000, colour_theme="GREYWOOF")
roadmap.set_title("Roadmap")
roadmap.set_subtitle("SCM")
roadmap.set_timeline(TimelineMode.MONTHLY, start="2023-06-01", number_of_items=12
                     # , year_fill_colour= "Lightblue"
                     # , item_fill_colour="Lightblue"
                     )

group_by_teams_data = dataset.groupby("Team")
for group_name, group_df in group_by_teams_data:

    group = roadmap.add_group(group_name)

    for index, row in group_df.iterrows():
        desired_format = "%Y-%m-%d"
        group.add_task(row['Title'], row['Start Date'], row['End Date'])
        # group.add_task(row['Title'], "2023-06-15", "2023-11-15")

roadmap.draw()
roadmap.save(f"roadmap.png")