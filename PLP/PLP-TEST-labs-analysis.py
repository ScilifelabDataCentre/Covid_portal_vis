"""
Plotting code for outcome visualisations of the PLP Test project.
"""


import pandas as pd
import plotly.express as px


# Read CSV files into a DataFrames
# analysis_logs_P1 = pd.read_csv(
#     "https://blobserver.dc.scilifelab.se/blob/PLP-TEST-aggregated-data-phase-1.csv",
#     header=0,
# )
data = pd.read_csv(
    "https://blobserver.dc.scilifelab.se/blob/PLP-TEST-aggregated-data-phase-1.csv",
    header=0,
)

analysis_logs_P2 = pd.read_csv(
    "https://blobserver.dc.scilifelab.se/blob/PLP-TEST-aggregated-data-phase-2.csv",
    header=0,
)


# Data preprocessing
# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Filter out rows with missing dates since they are critical for the timeline
filtered_data = data.dropna(subset=['Date'])

# Group data by Lab and Date to count the number of stages
grouped_data = filtered_data.groupby(['Lab', 'Date']).size().reset_index(name='Stage_Count')

# Merge the stage count back into the original data for visualisation
filtered_data = filtered_data.merge(grouped_data, on=['Lab', 'Date'])


# Create a scatter plot
fig = px.scatter(
    filtered_data,
    x='Date',
    y='Lab',
    color='Stage',
    size='Stage_Count',
    title='Lab Activity Timeline',
    labels={'Date': 'Date', 'Lab': 'Lab ID'},
    hover_data=['Method', 'Comment', 'Stage_Count']
)

# Customise layout
fig.update_layout(
    plot_bgcolor="white",
    # legend_title="Stage",
    # yaxis=dict(tickmode='linear')
)

# Customise axis properties
fig.update_xaxes(
    title="<b>Date</b>",
    linecolor="black",
)

fig.update_yaxes(
    title="<b>Lab ID</b>",
    linecolor="black",
    showgrid=True,
    gridcolor="lightgrey",
    zeroline=True,
    zerolinecolor="black",
)

# Display the graph
# fig.show()

# Save figure to JSON file
# pio.write_json(fig, "weekly_serology_tests.json")

# Convert figure to JSON string and print it to stdout
# print(pio.to_json(fig))




# PHASE 2

import plotly.figure_factory as ff
import plotly.colors as pc

# Load the data
data_phase_2 = pd.read_csv( 'https://blobserver.dc.scilifelab.se/blob/PLP-TEST-aggregated-data-phase-2.csv')


# Data preprocessing: Consolidate datetime conversion and missing value handling
data_phase_2['Start date'] = pd.to_datetime(data_phase_2['Start date'], errors='coerce')
data_phase_2['End date'] = pd.to_datetime(data_phase_2['End date'], errors='coerce').fillna(data_phase_2['Start date'])

# Adjust end date to ensure visibility for tasks with same start and end date
data_phase_2['Adjusted End date'] = data_phase_2['End date']
data_phase_2.loc[
    data_phase_2['Start date'] == data_phase_2['End date'],
    'Adjusted End date'
] += pd.Timedelta(days=1)

# Prepare data for the Gantt chart
gantt_data = [
    {
        'Task': f"{row['Stage']}",
        'Start': row['Start date'],
        'Finish': row['Adjusted End date'],
        'Resource': f"Lab {row['Lab']}"
    }
    for _, row in data_phase_2.iterrows()
]

# Identify all unique labs
unique_labs = data_phase_2['Lab'].unique()

# Ensure sufficient colors by extending the color palette only when necessary
if len(unique_labs) > len(pc.qualitative.Plotly):
    colors = pc.qualitative.Plotly * (len(unique_labs) // len(pc.qualitative.Plotly) + 1)
else:
    colors = pc.qualitative.Plotly

# Create the Gantt chart
fig = ff.create_gantt(
    gantt_data,
    index_col='Resource',
    show_colorbar=True,
    group_tasks=True,
    title="Stage Duration Analysis (Phase 2)",
    showgrid_x=True,
    showgrid_y=True,
    colors=colors[:len(unique_labs)]
)

# Customize the layout
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Tasks",
    plot_bgcolor="white",
    title_font_size=16
)

# Show the Gantt chart
fig.show()
