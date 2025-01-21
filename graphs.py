import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt


def PitchLocations(data, number):

    if number == 1:
        data.loc[data['PitchCall'].isin(['HitByPitch', 'BallinDirt', 'BallIntentional']), 'PitchCall'] = 'BallCalled'
        color_var = 'PitchCall'
        color_map = {'StrikeCalled': 'red', 'BallCalled': 'blue', 'InPlay':'green', 'FoulBall':'purple', 'StrikeSwinging':'goldenrod'}
        title = "Pitch Locations Balls/Strikes"
    elif number == 2:
        color_var = 'TaggedPitchType'
        color_map = {'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green', 'Splitter': 'lime', 'Curveball': 'goldenrod', 'Slider': 'blue'}
        title = "Pitch Locations Pitch Type"
    elif number == 3:
        data.loc[data['PlayResult'].isin(['Sacrifice', 'Error', 'FieldersChoice', 'CaughtStealing', 'StolenBase']), 'PlayResult'] = 'Out'
        color_var = 'PlayResult'
        color_map = {'Single': 'red', 'Double': 'blue', 'Triple': 'goldenrod', 'HomeRun': 'green', 'Out': 'gray'}
        title = "Pitch Locations Play Result"
    else:
        data.loc[data['TaggedHitType'].isin(['Bunt']), 'TaggedHitType'] = 'GroundBall'
        color_var = 'TaggedHitType'
        color_map = {'GroundBall': 'blue', 'LineDrive': 'green', 'Popup': 'fuchsia', 'FlyBall': 'red'}
        title = "Pitch Locations Contact Type"

    fig = px.scatter(data,
                     x='PlateLocSide',
                     y='PlateLocHeight',
                     color=color_var,
                     width=700,
                     height=700,
                     hover_data=['Pitcher', 'Batter', 'BatterTeam', 'RelSpeed', 'PitchCall'],
                     title=title,
                     color_discrete_map=color_map)

    # Make the data points smaller
    if number == 1:
        fig.update_traces(marker=dict(size=5, opacity=0.5))
    else:
        fig.update_traces(marker=dict(size=5))  # Adjust size to 5 (smaller than default)

    # Set a white background for the entire plot
    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
            # weight="bold"  # Make title bold
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
        xaxis=dict(
            showticklabels=False,  # Hide x-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
        ),
        yaxis=dict(
            showticklabels=False,  # Hide y-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
        ),
        xaxis_title="Plate Side Location",  # Title for x-axis
        yaxis_title="Plate Height Location"  # Title for y-axis
    )

    home_plate_x = [-0.708, -0.708, 0.708, 0.708, 0, -0.708]  # Close the loop by adding the first point at the end
    home_plate_y = [0, -0.35, -0.35, 0, 0.5, 0]  # Close the loop by adding the first point at the end

    fig.add_trace(go.Scatter(x=home_plate_x, y=home_plate_y, mode='lines', fill='toself',
                             line=dict(color='black'), showlegend=False))

    # Add the horizontal lines at y=1.5 and y=3.5 from x=-0.708 to x=0.708
    fig.add_trace(go.Scatter(x=[-0.708, 0.708], y=[1.5, 1.5], line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=[-0.708, 0.708], y=[3.5, 3.5], line=go.scatter.Line(color='black'), showlegend=False))
    # Add the vertical lines at x=-0.708 and x=0.708 from y=1.5 to y=3.5
    fig.add_trace(go.Scatter(x=[-0.708, -0.708], y=[1.5, 3.5], line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=[0.708, 0.708], y=[1.5, 3.5], line=go.scatter.Line(color='black'), showlegend=False))

    return fig


def SprayChart(data, number):
    if number == 1:
        data.loc[data['PitchCall'].isin(['HitByPitch', 'BallinDirt', 'BallIntentional']), 'PitchCall'] = 'BallCalled'
        color_var = 'PitchCall'
        color_map = {'StrikeCalled': 'red', 'BallCalled': 'blue', 'InPlay': 'green', 'FoulBall': 'purple',
                     'StrikeSwinging': 'goldenrod'}
        title = "Spray Chart Balls/Strikes"
    if number == 2:
        color_var = 'TaggedPitchType'
        color_map = {'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green',
                     'Splitter': 'lime', 'Curveball': 'goldenrod', 'Slider': 'blue'}
        title = "Spray Chart Pitch Type"
    if number == 3:
        data.loc[data['PlayResult'].isin(['Sacrifice', 'Error', 'FieldersChoice']), 'PlayResult'] = 'Out'
        color_var = 'PlayResult'
        color_map = {'Single': 'red', 'Double': 'blue', 'Triple': 'goldenrod', 'HomeRun': 'green', 'Out': 'gray'}
        title = "Spray Chart Play Result"
    if number == 4:
        data.loc[data['TaggedHitType'].isin(['Bunt']), 'Tagged Hit Type'] = 'GroundBall'
        color_var = 'TaggedHitType'
        color_map = {'GroundBall': 'blue', 'LineDrive': 'green', 'Popup': 'fuchsia', 'FlyBall': 'red'}
        title = "Spray Chart Contact Type"

    data['GroundLocationX'] = np.nan  # Initialize the column with NaN values
    data['GroundLocationY'] = np.nan  # Initialize the column with NaN values

    data.loc[data['PitchCall'] == 'InPlay', 'GroundLocationX'] = np.sin(np.radians(data['Bearing'])) * data['Distance']
    data.loc[data['PitchCall'] == 'InPlay', 'GroundLocationY'] = np.cos(np.radians(data['Bearing'])) * data['Distance']
    # Define the field boundary traces
    lflx = []
    cfwallx = []
    rflx = []
    lfly = []
    rfly = []
    cfwally = []
    llcx = []
    llcy = []
    rrcx = []
    rrcy = []
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

    # Create scatter plot with updated styling
    fig = px.scatter(data, x='GroundLocationX', y='GroundLocationY', title=title, color=color_var, width=700,
                     height=500, hover_data=['Pitcher', 'Batter', 'BatterTeam', 'RelSpeed', 'PitchCall'],
                     range_x=(-300, 300), color_discrete_map=color_map)

    # Add the field boundary traces
    fig.add_trace(go.Scatter(x=lflx, y=lfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rflx, y=rfly, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=cfwallx, y=cfwally, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=llcx, y=llcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rrcx, y=rrcy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=rccx, y=rccy, line=go.scatter.Line(color='black'), showlegend=False))
    fig.add_trace(go.Scatter(x=lccx, y=lccy, line=go.scatter.Line(color='black'), showlegend=False))

    # Update the figure layout to match PitchLocations
    fig.update_traces(marker=dict(size=5))  # Adjust size to 5 (smaller than default)

    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
            # weight="bold"  # Make title bold
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
        xaxis=dict(
            showticklabels=False,  # Hide x-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
            tickwidth=1,  # Bolden the axis ticks
            linecolor='lightgray',  # Set y-axis line color to black
        ),
        yaxis=dict(
            showticklabels=False,  # Hide y-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
            tickwidth=1,  # Bolden the axis ticks
            linecolor='lightgray',  # Set y-axis line color to black
        )
    )
    return fig


def PitchPie(data):
    fig = px.pie(data, names='TaggedPitchType', values='PitchCount',
                 color='TaggedPitchType',
                 color_discrete_map={'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green',
                                     'Splitter': 'lime', 'Curveball': 'goldenrod', 'Slider': 'blue'},
                 title='Pitch Seen %', height=700, width=700
                 )

    # Update layout to match SprayChart
    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
            # weight="bold"  # Make title bold
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
    )

    return fig
def PitchBar(data):
    # Step 1: Calculate frequency of each TaggedPitchType per Count
    pitch_freq = data.groupby(['Count', 'TaggedPitchType']).size().reset_index(name='Frequency')

    # Define the custom order for TaggedPitchType
    pitch_type_order = ['Fastball', 'Cutter', 'Sinker', 'ChangeUp', 'Splitter', 'Slider', 'Curveball']

    # Step 2: Create a bar plot with stacked bars
    fig = px.bar(pitch_freq, x='Frequency', y='Count',
                 color='TaggedPitchType',
                 color_discrete_map={'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green',
                                     'Splitter': 'lime', 'Curveball': 'goldenrod', 'Slider': 'blue'},
                 title='Pitch Seen % By Count',
                 orientation='h', width=700, height=700,
                 category_orders={'TaggedPitchType': pitch_type_order,  # Custom order for pitch types
                                  'Count': sorted(pitch_freq['Count'].unique())})  # Ensure Count values are sorted

    # Update the layout to match SprayChart
    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
        barmode='stack',  # Stack the bars on top of each other
        yaxis=dict(autorange='reversed')  # Ensure Count is sorted from bottom to top
    )

    return fig



def MovementPlot(data):
    color_var = 'TaggedPitchType'
    title = "Pitch Movement Profiles"
    color_map = {'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green',
                 'Splitter': 'lime', 'Curveball': 'goldenrod', 'Slider': 'blue'}

    # Create a scatter plot
    fig = px.scatter(data,
                     x='HorzBreak',
                     y='InducedVertBreak',
                     color=color_var,
                     width=700,
                     height=700,
                     hover_data=['Pitcher', 'Batter', 'BatterTeam', 'RelSpeed', 'PitchCall'],
                     title=title,
                     color_discrete_map=color_map)

    # Update the scatter plot markers to have 50% opacity
    fig.update_traces(marker=dict(size=5, opacity=0.5))

    # Update layout to match the style of PitchLocations with additional customization
    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
            # weight="bold"  # Make title bold
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
        xaxis=dict(
            showticklabels=True,  # Ensure x-axis labels are shown
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='black',
            gridcolor='lightgray',  # Grid color
            tickangle=45,  # Rotate ticks for better readability
            tickmode='linear',  # Ensure axis values are shown
            dtick=5,  # Set grid lines every 5 units
            tickfont=dict(
                family="Arial, sans-serif",  # Font for the ticks
                size=12,  # Size of the tick labels
                color="black"  # Tick label color
            ),
            tickwidth=2,  # Bolden the axis ticks
            ticklen=5,  # Length of the ticks
            linecolor='black',  # Set x-axis line color to black
            range=[-30, 30]
        ),
        yaxis=dict(
            showticklabels=True,  # Ensure y-axis labels are shown
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='black',
            gridcolor='lightgray',  # Grid color
            tickangle=0,  # Keep y-axis ticks horizontal
            tickmode='linear',  # Ensure axis values are shown
            dtick=5,  # Set grid lines every 5 units
            tickfont=dict(
                family="Arial, sans-serif",  # Font for the ticks
                size=12,  # Size of the tick labels
                color="black"  # Tick label color
            ),
            tickwidth=2,  # Bolden the axis ticks
            ticklen=5,  # Length of the ticks
            linecolor='black',  # Set y-axis line color to black
            range=[-30, 30]
        ),
        xaxis_title="Horizontal Break (HorzBreak)",  # Title for x-axis
        yaxis_title="Vertical Break (InducedVertBreak)"  # Title for y-axis
    )

    return fig


def ReleaseAnglePlot(data):
    color_var = 'TaggedPitchType'
    title = "Release Angle Profiles"
    color_map = {'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green',
                 'Splitter': 'lime', 'Curveball': 'goldenrod', 'Slider': 'blue'}

    fig = px.scatter(data,
                     x='HorzRelAngle',
                     y='VertRelAngle',
                     color=color_var,
                     width=700,
                     height=700,
                     title=title,
                     hover_data=['Pitcher', 'Batter', 'BatterTeam', 'RelSpeed', 'PitchCall'],
                     color_discrete_map=color_map)

    fig.update_traces(marker=dict(size=5, opacity=0.5))

    # Update layout to match the style of PitchLocations with additional customization
    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
            # weight="bold"  # Make title bold
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
        xaxis=dict(
            showticklabels=True,  # Ensure x-axis labels are shown
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='black',
            gridcolor='lightgray',  # Grid color
            tickangle=45,  # Rotate ticks for better readability
            tickmode='linear',  # Ensure axis values are shown
            dtick=5,  # Set grid lines every 5 units
            tickfont=dict(
                family="Arial, sans-serif",  # Font for the ticks
                size=12,  # Size of the tick labels
                color="black"  # Tick label color
            ),
            tickwidth=2,  # Bolden the axis ticks
            ticklen=5,  # Length of the ticks
            linecolor='black',  # Set x-axis line color to black
            range=[-10,10]
        ),
        yaxis=dict(
            showticklabels=True,  # Ensure y-axis labels are shown
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='black',
            gridcolor='lightgray',  # Grid color
            tickangle=0,  # Keep y-axis ticks horizontal
            tickmode='linear',  # Ensure axis values are shown
            dtick=5,  # Set grid lines every 5 units
            tickfont=dict(
                family="Arial, sans-serif",  # Font for the ticks
                size=12,  # Size of the tick labels
                color="black"  # Tick label color
            ),
            tickwidth=2,  # Bolden the axis ticks
            ticklen=5,  # Length of the ticks
            linecolor='black',  # Set y-axis line color to black
            range=[-10,10]
        ),
        xaxis_title="Horizontal Break (HorzBreak)",  # Title for x-axis
        yaxis_title="Vertical Break (InducedVertBreak)"  # Title for y-axis
    )

    return fig


def SpinTilt(data, rate_eff):

    if rate_eff == 1:
        r = "SpinRate"
        r_title = "Spin Rate (rpm)"
    else:
        r = "SpinAxis3dSpinEfficiency"
        r_title = "Spin Efficiency (%)"

    fig = px.scatter_polar(data, r=r, theta='SpinAxis', color='TaggedPitchType', color_discrete_map={'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green',
                 'Splitter': 'lime', 'Curveball': 'goldenrod', 'Slider': 'blue'}, title="Spin Direction Chart", width=700, height=700, hover_data=['Pitcher', 'Batter', 'BatterTeam', 'RelSpeed', 'PitchCall'])

    fig.update_traces(marker=dict(size=5, opacity=0.5))

    # Update layout to match the style of MovementPlot
    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
            # weight="bold"  # Make title bold
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
        polar=dict(
            radialaxis=dict(
                showticklabels=True,  # Show radial axis labels
                showgrid=True,  # Show grid lines
                dtick=500,  # Set grid lines every 500 units
            ),
            angularaxis=dict(
                showticklabels=True,  # Show angular axis labels
                showgrid=True,  # Show grid lines
                dtick=45,  # Set grid lines every 45 degrees
            ),
        ),
        xaxis_title=r_title,  # Title for radial axis
        yaxis_title="Pitch Tilt"  # Title for angular axis
    )

    return fig


def ReleasePointRear(data):
    color_var = 'TaggedPitchType'
    color_map = {'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green', 'Splitter': 'lime',
                 'Curveball': 'goldenrod', 'Slider': 'blue'}
    title = "Release Point Rear View"

    fig = px.scatter(data,
                     x='RelSide',
                     y='RelHeight',
                     color=color_var,
                     width=700,
                     height=700,
                     title=title,
                     color_discrete_map=color_map)

    # Make the data points smaller
    fig.update_traces(marker=dict(size=5, opacity=0.5))

    # Set a white background for the entire plot
    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
            # weight="bold"  # Make title bold
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
        xaxis=dict(
            showticklabels=False,  # Hide x-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
        ),
        yaxis=dict(
            showticklabels=False,  # Hide y-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
        ),
        xaxis_title="Release Side (ft)",  # Title for x-axis
        yaxis_title="Release Height (ft)"  # Title for y-axis
    )

    mound_x = [-9, -2.5, 2.5, 9, -9]  # Close the loop by adding the first point at the end
    mound_y = [0, 0.833, 0.833, 0, 0]  # Close the loop by adding the first point at the end

    fig.add_trace(go.Scatter(x=mound_x, y=mound_y, mode='lines', fill='toself',
                             line=dict(color='black'), showlegend=False))

    # Add the horizontal lines at y=1.5 and y=3.5 from x=-0.708 to x=0.708
    fig.add_trace(go.Scatter(x=[-1, 1], y=[.875, .875], line=go.scatter.Line(color='black'), showlegend=False))

    return fig


def ReleasePointTop(data):
    color_var = 'TaggedPitchType'
    color_map = {'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green', 'Splitter': 'lime',
                 'Curveball': 'goldenrod', 'Slider': 'blue'}
    title = "Release Point Top View"

    fig = px.scatter(data,
                     x='RelSide',
                     y='Extension',
                     color=color_var,
                     width=700,
                     height=700,
                     title=title,
                     color_discrete_map=color_map)

    # Make the data points smaller
    fig.update_traces(marker=dict(size=5, opacity=0.5))

    # Add the horizontal lines at y=1.5 and y=3.5 from x=-0.708 to x=0.708
    fig.add_trace(go.Scatter(x=[-1, 1], y=[.05, .05], line=go.scatter.Line(color='black'), showlegend=False))

    # Set a white background for the entire plot
    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
            # weight="bold"  # Make title bold
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
        xaxis=dict(
            showticklabels=False,  # Hide x-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
            range=[-5, 5]
        ),
        yaxis=dict(
            showticklabels=False,  # Hide y-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
            range=[0,9]
        ),
        xaxis_title="Release Side (ft)",  # Title for x-axis
        yaxis_title="Release Extension (ft)"  # Title for y-axis
    )
    return fig


def ReleasePointSide(data):
    color_var = 'TaggedPitchType'
    color_map = {'Fastball': 'red', 'Sinker': 'fuchsia', 'Cutter': 'purple', 'ChangeUp': 'green', 'Splitter': 'lime',
                 'Curveball': 'goldenrod', 'Slider': 'blue'}
    title = "Release Point Top View"

    fig = px.scatter(data,
                     x='Extension',
                     y='RelHeight',
                     color=color_var,
                     width=700,
                     height=700,
                     title=title,
                     color_discrete_map=color_map)

    # Make the data points smaller
    fig.update_traces(marker=dict(size=5, opacity=0.5))

    mound_x = [0, .5, 9, 0, 0]  # Close the loop by adding the first point at the end
    mound_y = [.833, 0.833, 0, 0, .833]  # Close the loop by adding the first point at the end

    fig.add_trace(go.Scatter(x=mound_x, y=mound_y, mode='lines', fill='toself',
                             line=dict(color='black'), showlegend=False))

    # Set a white background for the entire plot
    fig.update_layout(
        plot_bgcolor='white',  # White background for the plotting area
        paper_bgcolor='white',  # White background for the outer paper area
        title_font=dict(
            family="Times New Roman, serif",  # Professional font
            size=20,  # Font size of the title
            color="black",  # Title color
            # weight="bold"  # Make title bold
        ),
        title_x=0.5,  # Center the title horizontally (0.5 is the middle of the plot)
        title_y=0.95,  # Adjust the vertical position of the title
        xaxis=dict(
            showticklabels=False,  # Hide x-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
            range=[-0, 9]
        ),
        yaxis=dict(
            showticklabels=False,  # Hide y-axis labels
            showgrid=True,  # Show grid lines
            zeroline=True,  # Show zero line
            zerolinecolor='lightgray',
            gridcolor='lightgray',  # Grid color
            range=[0,7]
        ),
        xaxis_title="Release Side (ft)",  # Title for x-axis
        yaxis_title="Release Extension (ft)"  # Title for y-axis
    )
    return fig