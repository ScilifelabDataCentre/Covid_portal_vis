import pandas as pd
import datetime
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime as dt
from plotly.io import write_image


wastewater_data = pd.read_csv(
    "https://datagraphics.dckube.scilifelab.se/api/dataset/0ac8fa02871745048491de74e5689da9.csv",
    sep=",",
)
wastewater_data["year"] = (wastewater_data["week"].str[:4]).astype(int)
wastewater_data["week_no"] = wastewater_data["week"].str[-3:]
wastewater_data["week_no"] = wastewater_data["week_no"].str.replace("*", "", regex=True)
wastewater_data["week_no"] = (
    wastewater_data["week_no"].str.replace("-", "", regex=True)
).astype(int)
# set the date to the start of the week (Monday)
wastewater_data["day"] = 1
wastewater_data["date"] = wastewater_data.apply(
    lambda row: dt.fromisocalendar(row["year"], row["week_no"], row["day"]), axis=1
)
# Below sets a dataset for each city. Need to add to it if more places are added
# Will also need to add in a go.Scatter trace in the fig (no change needed to layout)
wastewater_Ekerö = wastewater_data[(wastewater_data["channel"] == "Ekerö")]
wastewater_Enköping = wastewater_data[(wastewater_data["channel"] == "Enköping")]
wastewater_Kalmar = wastewater_data[(wastewater_data["channel"] == "Kalmar")]
wastewater_Knivsta = wastewater_data[(wastewater_data["channel"] == "Knivsta")]
wastewater_Tierp = wastewater_data[(wastewater_data["channel"] == "Tierp")]
wastewater_Umeå = wastewater_data[(wastewater_data["channel"] == "Umeå")]
wastewater_Uppsala = wastewater_data[(wastewater_data["channel"] == "Uppsala")]
wastewater_Vaxholm = wastewater_data[(wastewater_data["channel"] == "Vaxholm")]
wastewater_Älvkarleby = wastewater_data[(wastewater_data["channel"] == "Älvkarleby")]
wastewater_Örebro = wastewater_data[(wastewater_data["channel"] == "Örebro")]
wastewater_Österåker = wastewater_data[(wastewater_data["channel"] == "Österåker")]
wastewater_Östhammar = wastewater_data[(wastewater_data["channel"] == "Östhammar")]

fig = go.Figure(
    data=[
        go.Scatter(
            name="Ekerö",
            x=wastewater_Ekerö.date,
            y=wastewater_Ekerö.relative_copy_number,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[0], size=7),
            marker_symbol="square",
            line=dict(color=px.colors.diverging.RdBu[0], width=2),
        ),
        go.Scatter(
            name="Enköping",
            x=wastewater_Enköping.date,
            y=wastewater_Enköping.relative_copy_number,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[1], size=7),
            marker_symbol="cross",
            line=dict(color=px.colors.diverging.RdBu[1], width=2),
        ),
        go.Scatter(
            name="Kalmar",
            x=wastewater_Kalmar.date,
            y=wastewater_Kalmar.relative_copy_number,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[3], size=7),
            marker_symbol="hourglass",
            line=dict(color=px.colors.diverging.RdBu[3], width=2),
        ),
        go.Scatter(
            name="Knivsta",
            x=wastewater_Knivsta.date,
            y=wastewater_Knivsta.relative_copy_number,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[8], size=7),
            marker_symbol="square",
            line=dict(color=px.colors.diverging.RdBu[8], width=2),
        ),
        go.Scatter(
            name="Tierp",
            x=wastewater_Tierp.date,
            y=wastewater_Tierp.relative_copy_number,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[9], size=7),
            marker_symbol="cross",
            line=dict(color=px.colors.diverging.RdBu[9], width=2),
        ),
        go.Scatter(
            name="Umeå",
            x=wastewater_Umeå.date,
            y=wastewater_Umeå.relative_copy_number,
            mode="lines+markers",
            marker=dict(color=px.colors.diverging.RdBu[10], size=7),
            marker_symbol="hourglass",
            line=dict(color=px.colors.diverging.RdBu[10], width=2),
        ),
        go.Scatter(
            name="Uppsala",
            x=wastewater_Uppsala.date,
            y=wastewater_Uppsala.relative_copy_number,
            mode="lines+markers",
            marker=dict(color="#663399", size=7),
            marker_symbol="square",
            line=dict(color="#663399", width=2),
        ),
        go.Scatter(
            name="Vaxholm",
            x=wastewater_Vaxholm.date,
            y=wastewater_Vaxholm.relative_copy_number,
            mode="lines+markers",
            marker=dict(color="#9400d3", size=7),
            marker_symbol="cross",
            line=dict(color="#9400d3", width=2),
        ),
        go.Scatter(
            name="Älvkarleby",
            x=wastewater_Älvkarleby.date,
            y=wastewater_Älvkarleby.relative_copy_number,
            mode="lines+markers",
            marker=dict(color="#ff00ff", size=7),
            marker_symbol="hourglass",
            line=dict(color="#ff00ff", width=2),
        ),
        go.Scatter(
            name="Örebro",
            x=wastewater_Örebro.date,
            y=wastewater_Örebro.relative_copy_number,
            mode="lines+markers",
            marker=dict(color="darkgoldenrod", size=7),
            marker_symbol="square",
            line=dict(color="darkgoldenrod", width=2),
        ),
        go.Scatter(
            name="Österåker",
            x=wastewater_Österåker.date,
            y=wastewater_Österåker.relative_copy_number,
            mode="lines+markers",
            marker=dict(color="gold", size=7),
            marker_symbol="cross",
            line=dict(color="gold", width=2),
        ),
        go.Scatter(
            name="Östhammar",
            x=wastewater_Östhammar.date,
            y=wastewater_Östhammar.relative_copy_number,
            mode="lines+markers",
            marker=dict(color="lightslategray", size=7),
            marker_symbol="hourglass",
            line=dict(color="lightslategray", width=2),
        ),
    ]
)
fig.update_layout(
    plot_bgcolor="white",
    autosize=True,
    font=dict(size=14),
    margin=dict(r=150, t=65, b=0, l=0),
    # width=900,
    # height=500,
    legend=dict(yanchor="top", y=0.95, xanchor="left", x=0.99, font=dict(size=16)),
    hovermode="x unified",
    hoverdistance=1,
)
fig.update_xaxes(
    title="<br><b>Date (Week Commencing)</b>",
    showgrid=True,
    linecolor="black",
    tickangle=45,
)
fig.update_yaxes(
    title="<b>Relative copy number of<br>SARS-CoV-2 to PMMoV (%)</b>",
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    # below ensures a zeroline on Y axis. Made it black to be clear it's different from other lines
    zeroline=True,
    zerolinecolor="black",
    # Below will set the y-axis range to constant, if you wish
    # range=[0, max(wastewater_data["relative_copy_number"] * 1.15)],
)
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            x=1.1,
            y=1.1,
            xanchor="right",
            yanchor="top",
            buttons=list(
                [
                    dict(
                        label="Reselect all areas",
                        method="update",
                        args=[
                            {"visible": [True]},
                        ],
                    ),
                    dict(
                        label="Deselect all areas",
                        method="update",
                        args=[
                            {"visible": "legendonly"},
                        ],
                    ),
                ]
            ),
        )
    ]
)
# Below can show figure locally in tests
fig.show()

# Below prints as html
# fig.write_html(
#    "wastewater_combined_slu_regular.html", include_plotlyjs=True, full_html=True
# )

# Prints as a json file
# fig.write_json("wastewater_combined_slu_regular.json")

# Below can produce a static image
# fig.write_image("wastewater_combined_graph.png")

# print(fig.to_json())
