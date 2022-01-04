# Will create barchart from the indicators
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
import json

# Import processed data
from vaccine_indicator_panel_content import (
    one_dose_swe,
    least_two_dose_swe,
    third_vacc_dose_tot,
    one_dose_pop,
    least_two_dose_pop,
    third_vacc_dose_pop,
)

# Now will make a dataframe so that we can create a grouped bar chart as a summary

vaccine_dose_totals = pd.DataFrame()
vaccine_dose_totals["Doses"] = ["1", "2", "3"]
vaccine_dose_totals["sixteens_perc"] = [
    one_dose_swe,
    least_two_dose_swe,
    third_vacc_dose_tot,
]
vaccine_dose_totals["POP_perc"] = [
    one_dose_pop,
    least_two_dose_pop,
    third_vacc_dose_pop,
]

# initiate barchart

trace1 = go.Bar(
    x=vaccine_dose_totals["Doses"],
    y=vaccine_dose_totals["sixteens_perc"],
    name="At Least 12 Years Method",
    marker_color="rgb(5,48,97)",
    hovertemplate="Number of Doses: %{x}" + "<br>Percent Receiving the Dose: %{y:.2f}%",
)
trace2 = go.Bar(
    x=vaccine_dose_totals["Doses"],
    y=vaccine_dose_totals["POP_perc"],
    name="Whole Population Method",
    marker_color="rgb(178,24,43)",
    # marker_pattern_shape="/",
    hovertemplate="Number of Doses: %{x}" + "<br>Percent Receiving the Dose: %{y:.2f}%",
)

# figure layout
fig = go.Figure(data=[trace1, trace2])
fig.update_layout(
    plot_bgcolor="white",
    font=dict(size=16),
    margin=dict(l=0, r=50, t=0, b=0),
    showlegend=True,
    legend=dict(
        title=" ",
        orientation="h",
        # yanchor="bottom",
        y=1.2,
        # xanchor="right",
        # x=0.5,
        font=dict(size=16),
    ),
)
# modify x-axis
fig.update_xaxes(
    title="<b>Number of Doses Received</b>",
    showgrid=True,
    linecolor="black",
)
# modify y-axis
fig.update_yaxes(
    title="<b>Percentage Vaccinated</b>",
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    # change range to envelope the appropriate range
    range=[0, 100],
)

# fig.show()

if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")

fig.write_json("Plots/Total_vaccinated_barchart.json")