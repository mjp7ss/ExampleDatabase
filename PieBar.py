import plotly.express as px



def pitchPie(data):
    fig = px.pie(data, names='TaggedPitchType', values='PitchCount', width=500, title='Pitch Usage %', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    })
    return fig

def pitchBar(data):
    fig = px.bar(data, x='PitchCount', y='Count', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, width=500, title='Pitch Usage % by Count', orientation='h')
    fig.update_yaxes(categoryorder='category ascending')
    return fig

def resultBar(data):
    fig = px.bar(data, x='PitchCount', y='Count', color='PitchCall', color_discrete_map={
        "StrikeCalled": 'red',
        'StrikeSwinging':'magenta',
        'Foul':'goldenrod',
        'FoulTip':'fuchsia',
        'InPlay':'green',
        'BallCalled':'blue'
    }, width=500, title='Pitch Result by Pitch Count', orientation='h')
    fig.update_yaxes(categoryorder='category ascending')
    return fig

def hitterPie(data, count):
    fig = px.pie(data, names='TaggedPitchType', values='PitchCount', width=500, title='Pitch Seen % ' +count+' Counts', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    })
    return fig

def hitterBar(data, count):
    fig = px.bar(data, x='PitchCount', y='Count', color='TaggedPitchType', color_discrete_map={
        "Fastball": "red",
        "Changeup": "green",
        "Slider": "blue",
        "Curveball": "goldenrod",
        "Cutter": "brown",
    }, width=500, title='Pitch Seen % in ' +count+' Counts', orientation='h')
    fig.update_yaxes(categoryorder='category ascending')
    return fig