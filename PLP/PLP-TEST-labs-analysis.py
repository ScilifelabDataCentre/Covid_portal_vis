"""
Plotting code for mock-up visualisations for the 'phase-based' comparison.

Unnatural in that real data would not arrive in this fashion (outside a simulation).
Also, as this was more about mocking up the kinds of plots that could exist,
the Identified Pathogen data is mocked, rather than being extracted from a file.
"""
from collections import Counter
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import plotly.graph_objs


DATA_DIR = Path("./data")
"""Path to directory containing the 6 Excel files, one per lab"""


def identified_pathogen_data() -> dict:
    """
    Mocks getting the lab name from the file name and the pathogen from the 'Identified pathogen' field
    """
    return {
        "A": "Unknown",
        "B": "Christensenella hongkongensis",
        "C": "Catabacter Hongkongensis",
        "D": "Unknown",
        "E": "Unknown",
        "F": "Unknown",
    }


def identified_bar_plots(input_data: dict) -> plotly.graph_objs.Figure:
    """
    Creates bar plot showing the counts of IDed pathogens
    """
    counts = Counter(input_data.values())

    fig = go.Figure(data=[
        go.Bar(
            x=list(counts.keys()),
            y=list(counts.values()),
            marker=dict(color=list(range(len(counts))), colorscale="Viridis")
        )
    ])

    fig.update_layout(
        title="Phase 2: Identified pathogens",
        xaxis_title="Pathogen",
        yaxis_title="Count",
        template="plotly_white"
    )
    return fig


def extract_method(file_path, lab_name) -> pd.DataFrame:
    df = pd.read_excel(file_path, sheet_name="Fas 2", skiprows=6)
    df["Lab"] = lab_name
    return df


def create_analysis_timeline() -> plotly.graph_objs.Figure:
    """
    Creates a timeline showing the timeline of conducted analyses for 2 labs
    """
    df1 = extract_method(DATA_DIR / "B.xlsx", "B")
    df2 = extract_method(DATA_DIR / "C.xlsx","C")
    df = pd.concat([df1, df2], ignore_index=True)
    df["Start date"] = pd.to_datetime(df["Start date"])

    fig = go.Figure()
    for lab in df["Lab"].unique():
        lab_data = df[df["Lab"] == lab]
        fig.add_trace(
            go.Scatter(
                x=lab_data["Start date"],
                y=lab_data["Lab"],
                mode="markers+lines",
                marker=dict(size=40),
                text=lab_data["Metod"],  # Hover text
                hoverinfo="text",
                name=lab
            )
        )

    # Update layout to reduce whitespace and add buffer
    fig.update_layout(
        title="Analysis timeline",
        xaxis_title="Start date",
        yaxis_title="Lab",
        xaxis=dict(
            type="date",
            tickformat="%Y-%m-%d",
            tickangle=-45
        ),
        yaxis=dict(
            title="Labs",
            automargin=True,
            categoryorder="array",
            categoryarray=["B", "C"],
            range=[-0.5, len(df["Lab"].unique()) - 0.5]
        ),
        template="plotly_white",
        showlegend=True
    )
    return fig


data = identified_pathogen_data()
bar_plot = identified_bar_plots(data)
bar_plot.show()

timeline_plot = create_analysis_timeline()
timeline_plot.show()

