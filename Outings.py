import plotly.express as px


def holding(data, title, y):
    fig = px.scatter(data, x='PitchNo', y=y, color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, width=750, title=title)
    return fig