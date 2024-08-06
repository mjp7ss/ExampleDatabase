import plotly.express as px


def rateVelo(data):
    fig = px.scatter(data, x='SpinRate', y='RelSpeed', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Velo and Spin Rate",width=500)
    return fig

def effVelo(data):
    fig = px.scatter(data, x='yt_Efficiency', y='RelSpeed', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title= "Velo and Spin Efficiency", width=500)
    return fig

def rateEff(data):
    fig = px.scatter(data, x='SpinRate', y='yt_Efficiency', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title= "Spin Rate and Spin Efficiency", width=500)
    return fig

def hbIVB(data):
    fig = px.scatter(data, x='HorzBreak', y='InducedVertBreak', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Horizontal and Induced Vertical Break", width=500)
    return fig

def rateIVB(data):
    fig = px.scatter(data, x='SpinRate', y='InducedVertBreak', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Spin Rate and Ind. Vertical Break", width=500)
    return fig

def rateHB(data):
    fig = px.scatter(data, x='SpinRate', y='HorzBreak', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Spin Rate and Horizontal Break", width=500)
    return fig

def ivbVAA(data):
    fig = px.scatter(data, x='InducedVertBreak', y='VertApprAngle', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Induced Vertical Break and Vertical Appr. Angle", width=500)
    return fig

def hbHAA(data):
    fig = px.scatter(data, x='HorzBreak', y='HorzApprAngle', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Horizontal Break and Horizontal Appr Angle", width=500)
    return fig

def tilt(data):
    fig = px.scatter_polar(data, r='SpinRate', theta='SpinAxis', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Spin Direction Chart with Spin Rate r Value", width=500)
    return fig