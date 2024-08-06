import plotly.graph_objects as go
import plotly.express as px
import numpy as np

def pitchTypeLocations(data, title):
    xtop = []
    ytop = []
    xleft = []
    yleft = []
    xbottom = []
    ybottom = []
    xright = []
    yright = []

    for x in np.arange(-.8, .8, .01):
        xtop.append(x)
        xbottom.append(x)
        ytop.append(3.5)
        ybottom.append(1.5)
    for y in np.arange(1.5, 3.5, .01):
        xleft.append(-.8)
        xright.append(.8)
        yleft.append(y)
        yright.append(y)

    fig = px.scatter(data, x='PlateLocSide', y='PlateLocHeight', color='TaggedPitchType', width=500, title=title,  color_discrete_map={
        'Fastball':'red',
        'Changeup':'green',
        'Curveball':'goldenrod',
        'Slider':'blue',
        'Cutter': 'brown',
        'Splitter': 'lime'
    })
    fig.add_trace(go.Scatter(x=xtop, y=ytop, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xbottom, y=ybottom, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xleft, y=yleft, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xright, y=yright, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def ballStrikeLocation(data, title):
    xtop = []
    ytop = []
    xleft = []
    yleft = []
    xbottom = []
    ybottom = []
    xright = []
    yright = []

    for x in np.arange(-.8, .8, .01):
        xtop.append(x)
        xbottom.append(x)
        ytop.append(3.5)
        ybottom.append(1.5)
    for y in np.arange(1.5, 3.5, .01):
        xleft.append(-.8)
        xright.append(.8)
        yleft.append(y)
        yright.append(y)

    fig = px.scatter(data, x='PlateLocSide', y='PlateLocHeight', color='PitchCall', width=500, title=title, color_discrete_map={
        'StrikeCalled': 'red',
        'BallCalled':'blue'
    })
    fig.add_trace(go.Scatter(x=xtop, y=ytop, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xbottom, y=ybottom, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xleft, y=yleft, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xright, y=yright, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def pitchResultLocation(data, title):
    xtop = []
    ytop = []
    xleft = []
    yleft = []
    xbottom = []
    ybottom = []
    xright = []
    yright = []

    for x in np.arange(-.8, .8, .01):
        xtop.append(x)
        xbottom.append(x)
        ytop.append(3.5)
        ybottom.append(1.5)
    for y in np.arange(1.5, 3.5, .01):
        xleft.append(-.8)
        xright.append(.8)
        yleft.append(y)
        yright.append(y)

    fig = px.scatter(data, x='PlateLocSide', y='PlateLocHeight', color='PlayResult', color_discrete_map={
        "Out": "grey",
        "HomeRun": "green",
        "Single": "blue",
        "Double": "red",
        "Triple": "fuchsia",
    }, title=title, width=500)
    fig.add_trace(go.Scatter(x=xtop, y=ytop, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xbottom, y=ybottom, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xleft, y=yleft, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xright, y=yright, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def pitchHitTypeLocation(data, title):
    xtop = []
    ytop = []
    xleft = []
    yleft = []
    xbottom = []
    ybottom = []
    xright = []
    yright = []

    for x in np.arange(-.8, .8, .01):
        xtop.append(x)
        xbottom.append(x)
        ytop.append(3.5)
        ybottom.append(1.5)
    for y in np.arange(1.5, 3.5, .01):
        xleft.append(-.8)
        xright.append(.8)
        yleft.append(y)
        yright.append(y)

    fig = px.scatter(data, x='PlateLocSide', y='PlateLocHeight', color='TaggedHitType', color_discrete_map={
        "FlyBall":"red",
        "LineDrive":"green",
        "GroundBall":"blue",
        "Popup":"fuchsia",
        "Bunt":"purple"
    }, title=title, width=500)
    fig.add_trace(go.Scatter(x=xtop, y=ytop, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xbottom, y=ybottom, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xleft, y=yleft, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xright, y=yright, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def pitchLocationEV(data, title):
    xtop = []
    ytop = []
    xleft = []
    yleft = []
    xbottom = []
    ybottom = []
    xright = []
    yright = []

    for x in np.arange(-.8, .8, .01):
        xtop.append(x)
        xbottom.append(x)
        ytop.append(3.5)
        ybottom.append(1.5)
    for y in np.arange(1.5, 3.5, .01):
        xleft.append(-.8)
        xright.append(.8)
        yleft.append(y)
        yright.append(y)

    fig = px.scatter(data, x='PlateLocSide', y='PlateLocHeight', color='ExitSpeed', title="Balls in Play by Exit Velocity", width=500,
                   color_continuous_scale='Bluered')
    fig.add_trace(go.Scatter(x=xtop, y=ytop, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xbottom, y=ybottom, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xleft, y=yleft, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xright, y=yright, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def pitchSwingLocation(data, title):
    xtop = []
    ytop = []
    xleft = []
    yleft = []
    xbottom = []
    ybottom = []
    xright = []
    yright = []

    for x in np.arange(-.8, .8, .01):
        xtop.append(x)
        xbottom.append(x)
        ytop.append(3.5)
        ybottom.append(1.5)
    for y in np.arange(1.5, 3.5, .01):
        xleft.append(-.8)
        xright.append(.8)
        yleft.append(y)
        yright.append(y)

    fig = px.scatter(data, x='PlateLocSide', y='PlateLocHeight', color='PitchCall', color_discrete_map={
        "StrikeSwinging": "red",
        "Foul": "green",
        "InPlay": "blue",
    }, title="Pitches Swung At", width=500)
    fig.add_trace(go.Scatter(x=xtop, y=ytop, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xbottom, y=ybottom, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xleft, y=yleft, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=xright, y=yright, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

