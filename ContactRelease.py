import plotly.graph_objects as go
import plotly.express as px
import numpy as np

def contactSide(data, title):
    plate = []
    height = []

    xhold = []
    yhold = []

    for x in np.arange(0, 1.416, .01):
        plate.append(x)
        yhold.append(.25)

    for y in np.arange(1.5, 3.5, .01):
        height.append(y)
        xhold.append(1.416)

    fig = px.scatter(data, x='yt_HitLocationY', y='yt_HitLocationZ', color='PlayResult', width=500, title=title,
                     color_discrete_map={
                         'Out': 'grey',
                         'Single': 'red',
                         'Double': 'blue',
                         'Triple': 'fuchsia',
                         'HomeRun': 'green',
                         'Sacrifice': 'black',
                         'Error': 'pink'
                     })
    fig.add_trace(go.Scatter(x=xhold, y=height, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=plate, y=yhold, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def contactTop(data, title):
    plate = []
    height = []

    xhold = []
    yhold = []

    platetopx = []
    platetopy = []
    platesidex = []
    platesidey = []
    platediagx = []
    platediagy = []
    platesidexn = []
    platediagxn = []

    for z in np.arange(-.708, .708, .001):
        platetopx.append(z)
        platetopy.append(1.416)

    for k in np.arange(0, .708, .001):
        platediagx.append(k)
        platediagy.append(k)
        platesidex.append(.708)
        platesidey.append(k + .708)
        platesidexn.append(-.708)
        platediagxn.append(-k)

    fig = px.scatter(data, x='yt_HitLocationX', y='yt_HitLocationY', color='PlayResult', width=500, title=title, color_discrete_map={
        'Out': 'grey',
        'Single': 'red',
        'Double': 'blue',
        'Triple': 'fuchsia',
        'HomeRun': 'green',
        'Sacrifice': 'black',
        'Error': 'pink'
    })
    fig.add_trace(go.Scatter(x=platetopx, y=platetopy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=platesidex, y=platesidey, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=platesidexn, y=platesidey, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=platediagx, y=platediagy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=platediagxn, y=platediagy, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def contact3D(data, title):
    xtop = []
    ztop = []
    xleft = []
    zleft = []
    xbottom = []
    zbottom = []
    xright = []
    zright = []
    yhorz = []
    yhorz2 = []
    yvert = []
    yvert2 = []

    for x in np.arange(-.708, .708, .01):
        xtop.append(x)
        xbottom.append(x)
        ztop.append(3.5)
        zbottom.append(1.5)
        yhorz.append(1.416)
        yhorz2.append(1.416)
    for y in np.arange(1.5, 3.5, .01):
        xleft.append(-.708)
        xright.append(.708)
        zleft.append(y)
        zright.append(y)
        yvert.append(1.416)
        yvert2.append(1.416)

    xhorz = xtop+xbottom
    yhorz = yhorz+yhorz2
    zhorz = ztop+zbottom

    xvert = xleft+xright
    yvert = yvert+yvert2
    zvert = zleft+zright

    xs = xhorz + xvert
    ys = yhorz + yvert
    zs = zhorz + zvert

    fig = px.scatter_3d(data, x='yt_HitLocationX', y='yt_HitLocationY', z='yt_HitLocationZ', color='PlayResult', width=500, title=title,  color_discrete_map={
        'Out': 'grey',
        'Single': 'red',
        'Double': 'blue',
        'Triple': 'fuchsia',
        'HomeRun': 'green',
        'Sacrifice': 'black',
        'Error': 'pink'
    })
    fig.add_trace(go.Scatter3d(x=xs, y=ys, z=zs, marker=dict(color='black'), showlegend=False))
    return fig

def releasePitcher(data):
    fig = px.scatter(data, x='RelSide', y='RelHeight', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Release Point (From Behind Pitcher)", width=500)
    fig.update_xaxes(range=[-3, 3])
    fig.update_yaxes(range=[0, 9])
    return fig

def releaseSide(data):
    fig = px.scatter(data, x='Extension', y='RelHeight', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Release Point (Side View)", width=500)
    fig.update_xaxes(range=[0, 10])
    fig.update_yaxes(range=[0, 9])
    return fig

def releaseTop(data):
    fig = px.scatter(data, x='RelSide', y='Extension', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="Release Point (Top View)", width=500)
    fig.update_xaxes(range=[-3, 3])
    fig.update_yaxes(range=[0, 10])
    return fig

def release3D(data):
    fig = px.scatter_3d(data, x='Extension', y='RelSide', z='RelHeight', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, title="3D Release Point", width=500)
    return fig