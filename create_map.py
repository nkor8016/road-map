import datetime

import pandas as pd
from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode
from dateutil.relativedelta import relativedelta

bars = pd.read_excel("./Project Road Map Data - SCM.xlsx", sheet_name="Bars")

desired_format = "%Y-%m-%d"

group_by_teams_data = bars.groupby("Team")

for group_name, group_df in group_by_teams_data:

    roadmap = Roadmap(2000, 2000, colour_theme="BLUEMOUNTAIN")
    roadmap.set_title("Roadmap")
    roadmap.set_subtitle(f"SCM - {group_name}")

    earliest_date = group_df["Start Date"].min()
    latest_date = group_df["End Date"].max()
    difference = relativedelta(latest_date, earliest_date)

    roadmap.set_timeline(TimelineMode.MONTHLY, start=earliest_date.strftime(desired_format),
                         number_of_items=difference.months + difference.years * 12 + 2)

    group = roadmap.add_group(str(group_name))

    for index, row in group_df.iterrows():
        start_date = row['Start Date'].strftime(desired_format)
        end_date = row['End Date'].strftime(desired_format)

        difference = relativedelta(row['End Date'], row['Start Date'])

        print(row['Title'], len(row['Title']), difference.months + difference.years * 12)
        task = None
        if group_name in ["SWMS"] and difference.months + difference.years * 12 < 2 and len(row["Title"]) > 10:
            task = group.add_task("", start_date, end_date)
        else:
            task = group.add_task(
                row["Title"].replace("SWMS New UI - ", "")
                .replace("[New UI]", "").replace("[ARCHITECTURAL_ENHANCEMENT] ", "")
                .replace("[Tech Debt]", "").replace("[ARCHITECTURAL_ENHANCEMENT]", "").replace("[SWMS]", "")
                .replace("SWMS", "").replace("Version", "")
                .replace("[QE][Automation] ", ""), start_date, end_date)

        if group_name in ["SWMS", "GRAIN"] and difference.months + difference.years * 12 < 1:
            task.add_milestone(start_date, start_date, text_alignment="left")
            task.add_milestone(end_date, end_date, text_alignment="right")
        else:
            task.add_milestone(start_date, start_date)
            task.add_milestone(end_date, end_date)

    roadmap.draw()

    roadmap.save(f"./images/roadmap {group_name}.png")

df_SWMS = group_by_teams_data.get_group("SWMS").drop("Team", axis=1)
df_SWMS_grouped_by_initiatives = df_SWMS.groupby('Product/Initiatives')

for initiative_name, initiative_df in df_SWMS_grouped_by_initiatives:
    roadmap = Roadmap(2000, 2000, colour_theme="BLUEMOUNTAIN")
    roadmap.set_title("Roadmap")
    roadmap.set_subtitle(f"SCM - {initiative_name}")

    earliest_date = initiative_df["Start Date"].min()
    latest_date = initiative_df["End Date"].max()

    difference = relativedelta(latest_date, earliest_date)

    roadmap.set_timeline(TimelineMode.MONTHLY, start=earliest_date.strftime(desired_format),
                         number_of_items=difference.months + difference.years * 12 + 2)

    group = roadmap.add_group(str(initiative_name))

    for index, row in initiative_df.iterrows():
        start_date = row['Start Date'].strftime(desired_format)
        end_date = row['End Date'].strftime(desired_format)

        difference = relativedelta(row['End Date'], row['Start Date'])

        if initiative_name == "SWMS - UI Modernization (New UI)":
            print(row['Title'], len(row['Title']), difference.months + difference.years * 12)
            if difference.months + difference.years * 12 > 2:
                task = group.add_task(
                    row["Title"].replace("SWMS New UI - ", "")
                    .replace("[New UI]", "").replace("[ARCHITECTURAL_ENHANCEMENT] ", "")
                    .replace("[Tech Debt]", "").replace("[ARCHITECTURAL_ENHANCEMENT]", "").replace("[SWMS]", "")
                    .replace("[QE][Automation] ", "").replace("Version ", ""),
                    start_date, end_date)
            else:
                task = group.add_task("", start_date, end_date)
        else:
            task = group.add_task(row['Title'], start_date, end_date)

        task.add_milestone(start_date, start_date, text_alignment="left")
        task.add_milestone(end_date, end_date, text_alignment="right")

    roadmap.draw()

    roadmap.save(f"./images/roadmap {initiative_name}.png")
