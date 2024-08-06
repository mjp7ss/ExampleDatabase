import plotly.graph_objects as go
import plotly.express as px
import numpy as np

def playResultSpray(data, title):
    lflx = []
    cfwallx = []
    rflx = []
    lfly = []
    rfly = []
    cfwally = []
    llcx = []
    llcy = []
    rrcx = []
    rrcy= []
    lccx = []
    lccy = []
    rccx = []
    rccy = []

    for x in np.arange(0, 234, .5):
        lflx.append(-x), rflx.append(x), lfly.append(x), rfly.append(x)

    for x in np.arange(-42, 42, .5):
        cfwallx.append(x), cfwally.append(404)

    for x in np.arange(-234, -160, .5):
        llcx.append(x), rrcx.append(-x), llcy.append(1.5 * x + 585), rrcy.append(1.5 * x + 585)

    for x in np.arange(-160, -42, .5):
        lccx.append(x), rccx.append(-x), lccy.append(.5 * x + 425), rccy.append(.5 * x + 425)

    fig = px.scatter(data, x='yt_GroundLocationX', y='yt_GroundLocationY', title=title, color='PlayResult', width=600, range_x=(-300, 300), color_discrete_map={
        'Out': 'grey',
        'Single': 'red',
        'Double': 'blue',
        'Triple': 'fuchsia',
        'HomeRun': 'green',
        'Sacrifice': 'black',
        'Error': 'pink'
    })
    fig.add_trace(go.Scatter(x=lflx, y=lfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rflx, y=rfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=cfwallx, y=cfwally, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=llcx, y=llcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rrcx, y=rrcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rccx, y=rccy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=lccx, y=lccy, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def contactSpray(data, title):
    lflx = []
    cfwallx = []
    rflx = []
    lfly = []
    rfly = []
    cfwally = []
    llcx = []
    llcy = []
    rrcx = []
    rrcy= []
    lccx = []
    lccy = []
    rccx = []
    rccy = []

    for x in np.arange(0, 234, .5):
        lflx.append(-x), rflx.append(x), lfly.append(x), rfly.append(x)

    for x in np.arange(-42, 42, .5):
        cfwallx.append(x), cfwally.append(404)

    for x in np.arange(-234, -160, .5):
        llcx.append(x), rrcx.append(-x), llcy.append(1.5 * x + 585), rrcy.append(1.5 * x + 585)

    for x in np.arange(-160, -42, .5):
        lccx.append(x), rccx.append(-x), lccy.append(.5 * x + 425), rccy.append(.5 * x + 425)

    fig = px.scatter(data, x='yt_GroundLocationX', y='yt_GroundLocationY', title=title, color='TaggedHitType', width=600, range_x=(-300, 300), color_discrete_map={
        "FlyBall":"red",
        "LineDrive":"green",
        "GroundBall":"blue",
        "Popup":"fuchsia",
        "Bunt":"purple"
    })
    fig.add_trace(go.Scatter(x=lflx, y=lfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rflx, y=rfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=cfwallx, y=cfwally, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=llcx, y=llcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rrcx, y=rrcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rccx, y=rccy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=lccx, y=lccy, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def exitVeloSpray(data, title):
    lflx = []
    cfwallx = []
    rflx = []
    lfly = []
    rfly = []
    cfwally = []
    llcx = []
    llcy = []
    rrcx = []
    rrcy= []
    lccx = []
    lccy = []
    rccx = []
    rccy = []

    for x in np.arange(0, 234, .5):
        lflx.append(-x), rflx.append(x), lfly.append(x), rfly.append(x)

    for x in np.arange(-42, 42, .5):
        cfwallx.append(x), cfwally.append(404)

    for x in np.arange(-234, -160, .5):
        llcx.append(x), rrcx.append(-x), llcy.append(1.5 * x + 585), rrcy.append(1.5 * x + 585)

    for x in np.arange(-160, -42, .5):
        lccx.append(x), rccx.append(-x), lccy.append(.5 * x + 425), rccy.append(.5 * x + 425)

    fig = px.scatter(data, x='yt_GroundLocationX', y='yt_GroundLocationY', title=title, color='ExitSpeed', width=600, range_x=(-300, 300), color_continuous_scale="Bluered")
    fig.add_trace(go.Scatter(x=lflx, y=lfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rflx, y=rfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=cfwallx, y=cfwally, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=llcx, y=llcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rrcx, y=rrcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rccx, y=rccy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=lccx, y=lccy, line=go.scatter.Line(color='black'), showlegend=False))
    return fig

def pitchSpray(data, title):
    lflx = []
    cfwallx = []
    rflx = []
    lfly = []
    rfly = []
    cfwally = []
    llcx = []
    llcy = []
    rrcx = []
    rrcy= []
    lccx = []
    lccy = []
    rccx = []
    rccy = []

    for x in np.arange(0, 234, .5):
        lflx.append(-x), rflx.append(x), lfly.append(x), rfly.append(x)

    for x in np.arange(-42, 42, .5):
        cfwallx.append(x), cfwally.append(404)

    for x in np.arange(-234, -160, .5):
        llcx.append(x), rrcx.append(-x), llcy.append(1.5 * x + 585), rrcy.append(1.5 * x + 585)

    for x in np.arange(-160, -42, .5):
        lccx.append(x), rccx.append(-x), lccy.append(.5 * x + 425), rccy.append(.5 * x + 425)

    fig = px.scatter(data, x='yt_GroundLocationX', y='yt_GroundLocationY', title=title , color='TaggedPitchType', width=600, range_x=(-300, 300), color_discrete_map={
        'Fastball':'red',
        'Changeup':'green',
        'Curveball':'goldenrod',
        'Slider':'blue'
    })
    fig.add_trace(go.Scatter(x=lflx, y=lfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rflx, y=rfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=cfwallx, y=cfwally, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=llcx, y=llcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rrcx, y=rrcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rccx, y=rccy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=lccx, y=lccy, line=go.scatter.Line(color='black'), showlegend=False))
    return fig