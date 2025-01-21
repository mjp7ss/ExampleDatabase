import dash
import pandas as pd
import numpy as np
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from ui import *  # Import the layout function
from graphs import *
from datetime import datetime

app = dash.Dash(__name__,  suppress_callback_exceptions=True)
server = app.server

data = pd.read_csv("2023NoID.csv")
data['Date'] = pd.to_datetime(data['Date'])

##### Data Filtering #####
pitcher_and_catcher_data = data[data['PitcherTeam'] == "Team A"]
hitter_data = data[data['BatterTeam'] == "Team A"]

##### TAB SELECTION AND CONTENT RENDERING#####
@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab == 'Hitters':
        return create_hitters_content()
    elif tab == 'Pitchers':
        return create_pitchers_content()
    elif tab == 'Catchers':
        return create_catchers_content()
    elif tab == 'Data':
        return create_upload_content()

##### Dynamically Defining the Potential Filter Values for Hitting Tab #####
@app.callback(
    [
        Output('hitter-hitter-filter', 'options'),
        Output('hitter-opponent-filter', 'options'),
        Output('hitter-pitcher-filter', 'options'),
        Output('hitter-pitcher-hand-filter', 'options'),
        Output('hitter-count-type-filter', 'options'),
    ],
    [
        Input('hitter-hitter-filter', 'value'),
        Input('hitter-opponent-filter', 'value'),
        Input('hitter-pitcher-filter', 'value'),
        Input('hitter-pitcher-hand-filter', 'value'),
        Input('hitter-count-type-filter', 'value'),
    ]
)
def update_dropdowns_hitters(hitter, opponent, pitcher, pitcher_hand, count_type):
    # Filter the data based on the selected filters
    filtered_data = hitter_data.copy()

    if hitter != 'All':
        filtered_data = filtered_data[filtered_data['Batter'] == hitter]
    if opponent != 'All':
        filtered_data = filtered_data[filtered_data['PitcherTeam'] == opponent]
    if pitcher != 'All':
        filtered_data = filtered_data[filtered_data['Pitcher'] == pitcher]
    if pitcher_hand != 'All':
        filtered_data = filtered_data[filtered_data['PitcherThrows'] == pitcher_hand]
    if count_type != 'All':
        filtered_data = filtered_data[filtered_data['CountType'] == count_type]

    # Get unique values for each dropdown based on the filtered data
    hitter_options = [{'label': i, 'value': i} for i in filtered_data['Batter'].unique()] + [
        {'label': 'All Hitters', 'value': 'All'}]
    opponent_options = [{'label': i, 'value': i} for i in filtered_data['PitcherTeam'].unique()] + [
        {'label': 'All Opponents', 'value': 'All'}]
    pitcher_options = [{'label': i, 'value': i} for i in filtered_data['Pitcher'].unique()] + [
        {'label': 'All Pitchers', 'value': 'All'}]
    pitcher_hand_options = [{'label': i, 'value': i} for i in filtered_data['PitcherThrows'].unique()] + [
        {'label': 'All Pitcher Hands', 'value': 'All'}]
    count_type_options = [{'label': i, 'value': i} for i in filtered_data['CountType'].unique()] + [
        {'label': 'All Counts', 'value': 'All'}]

    # Return the updated options
    return hitter_options, opponent_options, pitcher_options, pitcher_hand_options, count_type_options


##### Dynamically Defining the Potential Filter Values for Pitching Tab #####
@app.callback(
    [
        Output('pitcher-pitcher-filter', 'options'),
        Output('pitcher-opponent-filter', 'options'),
        Output('pitcher-hitter-filter', 'options'),
        Output('pitcher-hitter-hand-filter', 'options'),
        Output('pitcher-count-type-filter', 'options'),
    ],
    [
        Input('pitcher-pitcher-filter', 'value'),
        Input('pitcher-opponent-filter', 'value'),
        Input('pitcher-hitter-filter', 'value'),
        Input('pitcher-hitter-hand-filter', 'value'),
        Input('pitcher-count-type-filter', 'value'),
    ]
)
def update_dropdowns_pitchers(pitcher, opponent, hitter, batter_hand, count_type):
    # Filter the data based on the selected filters
    filtered_data = pitcher_and_catcher_data.copy()

    if pitcher != 'All':
        filtered_data = filtered_data[filtered_data['Pitcher'] == pitcher]
    if opponent != 'All':
        filtered_data = filtered_data[filtered_data['BatterTeam'] == opponent]
    if hitter != 'All':
        filtered_data = filtered_data[filtered_data['Batter'] == hitter]
    if batter_hand != 'All':
        filtered_data = filtered_data[filtered_data['BatterSide'] == batter_hand]
    if count_type != 'All':
        filtered_data = filtered_data[filtered_data['CountType'] == count_type]

    # Get unique values for each dropdown based on the filtered data
    pitcher_options = [{'label': i, 'value': i} for i in filtered_data['Pitcher'].unique()] + [
        {'label': 'All Pitchers', 'value': 'All'}]
    opponent_options = [{'label': i, 'value': i} for i in filtered_data['BatterTeam'].unique()] + [
        {'label': 'All Opponents', 'value': 'All'}]
    hitter_options = [{'label': i, 'value': i} for i in filtered_data['Batter'].unique()] + [
        {'label': 'All Hitters', 'value': 'All'}]
    hitter_hand_options = [{'label': i, 'value': i} for i in filtered_data['BatterSide'].unique()] + [
        {'label': 'All Hitter Hands', 'value': 'All'}]
    count_type_options = [{'label': i, 'value': i} for i in filtered_data['CountType'].unique()] + [
        {'label': 'All Counts', 'value': 'All'}]

    # Return the updated options
    return pitcher_options, opponent_options, hitter_options, hitter_hand_options, count_type_options


##### Dynamically Defining the Potential Filter Values for Catching Tab #####
@app.callback(
    [
        Output('catcher-catcher-filter', 'options'),
        Output('catcher-pitcher-hand-filter', 'options'),
        Output('catcher-hitter-hand-filter', 'options'),
        Output('catcher-umpire-filter', 'options'),
        Output('catcher-count-type-filter', 'options'),
    ],
    [
        Input('catcher-catcher-filter', 'value'),
        Input('catcher-pitcher-hand-filter', 'value'),
        Input('catcher-hitter-hand-filter', 'value'),
        Input('catcher-umpire-filter', 'value'),
        Input('catcher-count-type-filter', 'value'),
    ]
)
def update_dropdowns_catchers(catcher, pitcher_hand, hitter_hand, umpire, count_type):
    # Filter the data based on the selected filters
    filtered_data = pitcher_and_catcher_data.copy()

    if catcher != 'All':
        filtered_data = filtered_data[filtered_data['Catcher'] == catcher]
    if pitcher_hand != 'All':
        filtered_data = filtered_data[filtered_data['PitcherThrows'] == pitcher_hand]
    if hitter_hand != 'All':
        filtered_data = filtered_data[filtered_data['BatterSide'] == hitter_hand]
    if umpire != 'All':
        filtered_data = filtered_data[filtered_data['Umpire'] == umpire]
    if count_type != 'All':
        filtered_data = filtered_data[filtered_data['CountType'] == count_type]

    # Get unique values for each dropdown based on the filtered data
    catcher_options = [{'label': i, 'value': i} for i in filtered_data['Catcher'].unique()] + [
        {'label': 'All Catchers', 'value': 'All'}]
    pitcher_hand_options = [{'label': i, 'value': i} for i in filtered_data['PitcherThrows'].unique()] + [
        {'label': 'All Pitcher Hands', 'value': 'All'}]
    hitter_hand_options = [{'label': i, 'value': i} for i in filtered_data['BatterSide'].unique()] + [
        {'label': 'All Hitter Hands', 'value': 'All'}]
    umpire_options = [{'label': i, 'value': i} for i in filtered_data['Umpire'].unique()] + [
        {'label': 'All Umpires', 'value': 'All'}]
    count_type_options = [{'label': i, 'value': i} for i in filtered_data['CountType'].unique()] + [
        {'label': 'All Counts', 'value': 'All'}]

    # Return the updated options
    return catcher_options, pitcher_hand_options, hitter_hand_options, umpire_options, count_type_options


##### Catching Content #####
@app.callback(
    [
        Output('catcher-locations', 'figure'),
    ],
    [
        Input('catcher-catcher-filter', 'value'),
        Input('catcher-pitcher-hand-filter', 'value'),
        Input('catcher-hitter-hand-filter', 'value'),
        Input('catcher-umpire-filter', 'value'),
        Input('catcher-count-type-filter', 'value'),
    ]
)
def catcher_content(catcher, pitcher_hand, hitter_hand, umpire, count_type):
    # Filter the data based on the selected filters
    filtered_data = pitcher_and_catcher_data.copy()
    filtered_data = filtered_data[filtered_data['PitchCall'].isin(['StrikeCalled', 'BallCalled'])]

    if catcher != 'All':
        filtered_data = filtered_data[filtered_data['Catcher'] == catcher]
    if pitcher_hand != 'All':
        filtered_data = filtered_data[filtered_data['PitcherThrows'] == pitcher_hand]
    if hitter_hand != 'All':
        filtered_data = filtered_data[filtered_data['BatterSide'] == hitter_hand]
    if umpire != 'All':
        filtered_data = filtered_data[filtered_data['Umpire'] == umpire]
    if count_type != 'All':
        filtered_data = filtered_data[filtered_data['CountType'] == count_type]

    fig = PitchLocations(filtered_data, 1)
    # Return the updated options
    return [fig]


##### Dynamically Defining the Potential Filter Values for Hitting Tab #####
@app.callback(
    [
        Output('hitter-locations', 'figure'),
        Output('hitter-spray-chart', 'figure'),
        Output('hitter-pitch-pie', 'figure'),
        Output('hitter-pitch-bar', 'figure')
    ],
    [
        Input('hitter-hitter-filter', 'value'),
        Input('hitter-opponent-filter', 'value'),
        Input('hitter-pitcher-filter', 'value'),
        Input('hitter-pitcher-hand-filter', 'value'),
        Input('hitter-count-type-filter', 'value'),
        Input('hitter-category-dropdown', 'value')
    ]
)
def hitters_content(hitter, opponent, pitcher, pitcher_hand, count_type, number):
    # Filter the data based on the selected filters
    filtered_data = hitter_data.copy()

    if hitter != 'All':
        filtered_data = filtered_data[filtered_data['Batter'] == hitter]
    if opponent != 'All':
        filtered_data = filtered_data[filtered_data['PitcherTeam'] == opponent]
    if pitcher != 'All':
        filtered_data = filtered_data[filtered_data['Pitcher'] == pitcher]
    if pitcher_hand != 'All':
        filtered_data = filtered_data[filtered_data['PitcherThrows'] == pitcher_hand]
    if count_type != 'All':
        filtered_data = filtered_data[filtered_data['CountType'] == count_type]

    pitch_location_figure = PitchLocations(filtered_data, number)
    spray_chart_figure = SprayChart(filtered_data, number)
    hitter_pie = PitchPie(filtered_data)
    hitter_bar = PitchBar(filtered_data)

    return pitch_location_figure, spray_chart_figure, hitter_pie, hitter_bar


##### Dynamically Defining the Potential Filter Values for Pitching Tab #####
@app.callback(
    [
        Output('pitcher-locations', 'figure'),
        Output('pitcher-spray-chart', 'figure'),
        Output('pitcher-movement', 'figure'),
        Output('pitcher-spin', 'figure'),
        Output('pitcher-release-angle', 'figure'),
        Output('pitcher-usage-pie', 'figure'),
        Output('pitcher-usage-bar', 'figure'),
        Output('pitcher-release', 'figure'),
    ],
    [
        Input('pitcher-pitcher-filter', 'value'),
        Input('pitcher-opponent-filter', 'value'),
        Input('pitcher-hitter-filter', 'value'),
        Input('pitcher-hitter-hand-filter', 'value'),
        Input('pitcher-count-type-filter', 'value'),
        Input('pitcher-category-dropdown', 'value'),
        Input('pitcher-rateeff-dropdown', 'value'),
        Input('pitcher-release-view-dropdown', 'value')
    ]
)

def pitcher_content(pitcher, opponent, hitter, batter_hand, count_type, number, rate_eff, release):
    filtered_data = pitcher_and_catcher_data.copy()

    if pitcher != 'All':
        filtered_data = filtered_data[filtered_data['Pitcher'] == pitcher]
    if opponent != 'All':
        filtered_data = filtered_data[filtered_data['BatterTeam'] == opponent]
    if hitter != 'All':
        filtered_data = filtered_data[filtered_data['Batter'] == hitter]
    if batter_hand != 'All':
        filtered_data = filtered_data[filtered_data['BatterSide'] == batter_hand]
    if count_type != 'All':
        filtered_data = filtered_data[filtered_data['CountType'] == count_type]

    pitch_location_figure = PitchLocations(filtered_data, number)
    spray_chart_figure = SprayChart(filtered_data, number)
    movement_figure = MovementPlot(filtered_data)
    spin_figure = SpinTilt(filtered_data, rate_eff)
    release_angle_figure = ReleaseAnglePlot(filtered_data)
    pitcher_pie_figure = PitchPie(filtered_data)
    pitcher_bar_figure = PitchBar(filtered_data)

    if release == 1:
        release_figure = ReleasePointRear(filtered_data)
    elif release == 2:
        release_figure = ReleasePointTop(filtered_data)
    else:
        release_figure = ReleasePointSide(filtered_data)
    # release_behind_figure = ReleasePointTop(filtered_data)

    return pitch_location_figure, spray_chart_figure, movement_figure, spin_figure, release_angle_figure, pitcher_pie_figure, pitcher_bar_figure, release_figure


app.layout = create_layout()  # Set the app layout using the imported function


if __name__ == '__main__':
    app.run_server(debug=True)