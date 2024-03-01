import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

bars = pd.read_excel("./Project Road Map Data - SCM.xlsx", sheet_name="Bars")

df = []

fig = ff.create_gantt(df)
fig.show()
