# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html
from dash import dcc
from dash import dash_table as dt
from dash.dependencies import Input, Output
from ContactRelease import *
from Spray import *
from PieBar import *
from Locations import *
from Outings import *
from Movement import *
from DataSets import *

########################### Generic Input Data #########################################
data = pd.read_csv('2023 Season Data.csv')

########################## Pitcher Raw Data ############################################
pitcherData = data
pitcherData = pitcherData.groupby('PitcherTeam')
pitcherData = pitcherData.get_group("VIR_CAV")
pitcherData1 = pitcherData[["Date", 'Pitcher', 'Batter', 'BatterSide', 'TaggedPitchType', 'RelSpeed', 'SpinRate',
                            'SpinAxis', 'Tilt', 'InducedVertBreak', 'HorzBreak', 'VertBreak', 'RelSide',
                           'RelHeight', 'Extension', 'HorzRelAngle', 'VertRelAngle', 'HorzApprAngle', 'VertApprAngle',
                           'ZoneSpeed']]
##################### Hitter Raw Data #################################################
batterData = data
batterData = batterData.groupby('BatterTeam')
batterData = batterData.get_group("VIR_CAV")

batterCounts = batterData.groupby('Count')
batter00 = batterCounts.get_group(' 0-0')
batter01 = batterCounts.get_group(' 0-1')
batter02 = batterCounts.get_group(' 0-2')
batter10 = batterCounts.get_group(' 1-0')
batter11 = batterCounts.get_group(' 1-1')
batter12 = batterCounts.get_group(' 1-2')
batter20 = batterCounts.get_group(' 2-0')
batter21 = batterCounts.get_group(' 2-1')
batter22 = batterCounts.get_group(' 2-2')
batter30 = batterCounts.get_group(' 3-0')
batter31 = batterCounts.get_group(' 3-1')
batter32 = batterCounts.get_group(' 3-2')

batterAhead = pd.concat((batter10, batter20, batter21, batter30, batter31))
batterBehind = pd.concat((batter01, batter02, batter12))
batterEven = pd.concat((batter00, batter11, batter22))
batter2K = pd.concat((batter02, batter12, batter22, batter32))

batterInPlay = batterData.groupby('PitchCall')
batterInPlay = batterInPlay.get_group('InPlay')
batterData0 = batterData
batterData1 = batterData[['Date', 'Batter', 'Pitcher', 'PitcherThrows', 'TaggedPitchType', 'RelSpeed', 'ExitSpeed',
                          'Angle', 'Distance', 'HangTime', 'HitSpinRate', 'Direction', 'Bearing']]

######################## Misc Data #######################################
dateData = data

######################## IGH PoC Chart Data###################################
ighPoCData = batterData[['Batter','PitcherThrows', 'TaggedPitchType', 'ContactPositionX', 'ContactPositionZ', 'ContactPositionY', 'TaggedHitType', 'ExitSpeed', 'Angle']]

######################## IGH BB Chart Data####################################
ighBBData = batterData[['Date', 'Batter','PitcherThrows', 'TaggedPitchType', 'ExitSpeed', 'Angle', 'Distance', 'HangTime']]

######################## IGH Plate Discipline Data############################
calledPitches = batterData
calledPitches = calledPitches.groupby('PitchCall')

calledStrikes = batterData
calledStrikes = calledStrikes.groupby('PitchCall')
calledStrikes = calledStrikes.get_group('StrikeCalled')

calledBalls = batterData
calledBalls = calledBalls.groupby('PitchCall')
calledBalls = calledBalls.get_group('BallCalled')

swingingStrikes = batterData
swingingStrikes = swingingStrikes.groupby('PitchCall')
swingingStrikes = swingingStrikes.get_group('StrikeSwinging')

inPlay = calledPitches.get_group('InPlay')
swings = pd.concat((swingingStrikes, inPlay))
swingsTable = swings[['Batter', 'Pitcher','PitcherThrows', 'TaggedPitchType', 'PitchCall', 'PlateLocSide', 'PlateLocHeight']]
takes = pd.concat((calledStrikes, calledBalls))
takesTable = takes[['Batter', 'Pitcher', 'PitcherThrows', 'TaggedPitchType', 'PitchCall', 'PlateLocSide', 'PlateLocHeight']]

###########################IGP Arsenal Data ################################################################
igpARSData = pitcherData[['Date', 'Pitcher', 'TaggedPitchType', 'RelSpeed', 'SpinRate', 'HorzBreak', 'InducedVertBreak']]

############################# IGP Batted Ball Data #########################################################
igpBBData = pitcherData
igpBBData = igpBBData.groupby('PitchCall')
igpBBData = igpBBData.get_group('InPlay')

igpBBTable = igpBBData[['Date', 'Pitcher', 'Batter', 'TaggedPitchType', 'TaggedHitType', 'PlayResult', 'RelSpeed', 'PlateLocSide', 'PlateLocHeight', 'ExitSpeed']]

###################################### IGP Chase Profile Data #######################################################
chaseData = pitcherData
chaseData1 = pitcherData
chaseData = chaseData.groupby('PitchCall')

pitcherSwingAndMiss = chaseData.get_group('StrikeSwinging')
pitcherFoul = chaseData.get_group('FoulBall')
pitcherInPlay = chaseData.get_group('InPlay')
pitcherStrikesCalled = chaseData.get_group('StrikeCalled')
pitcherBallCalled = chaseData.get_group('BallCalled')

pitcherAllSwings = pd.concat((pitcherSwingAndMiss, pitcherFoul))
pitcherAllSwings = pd.concat((pitcherAllSwings, pitcherInPlay))

pitcherAllTakes = pd.concat((pitcherStrikesCalled, pitcherBallCalled))

chaseTable = pitcherSwingAndMiss[['Date', 'Pitcher', 'Batter', 'TaggedPitchType','RelSpeed', 'HorzBreak', 'InducedVertBreak', 'PlateLocSide', 'PlateLocHeight', 'HorzApprAngle', 'VertApprAngle']]
##################################### IGP Break and Movement ##########################################################
moveData = pitcherData[['Date', 'Pitcher', 'RelSpeed', 'SpinRate','SpinAxis', 'HorzBreak', 'InducedVertBreak', 'VertApprAngle', 'HorzApprAngle']]
##################################### IGP Release Point Data ##########################################################


########################################## Catchers Data #############################################################
catcherData = pitcherData
catcherData = catcherData.groupby('PitchCall')
catcherStrikes = catcherData.get_group('StrikeCalled')
catcherBalls = catcherData.get_group('BallCalled')

catcherTotal = pd.concat((catcherStrikes, catcherBalls))

catcherCounts = catcherTotal.groupby('Count')
catcher00 = catcherCounts.get_group(' 0-0')
catcher01 = catcherCounts.get_group(' 0-1')
catcher02 = catcherCounts.get_group(' 0-2')
catcher10 = catcherCounts.get_group(' 1-0')
catcher11 = catcherCounts.get_group(' 1-1')
catcher12 = catcherCounts.get_group(' 1-2')
catcher20 = catcherCounts.get_group(' 2-0')
catcher21 = catcherCounts.get_group(' 2-1')
catcher22 = catcherCounts.get_group(' 2-2')
catcher30 = catcherCounts.get_group(' 3-0')
catcher31 = catcherCounts.get_group(' 3-1')
catcher32 = catcherCounts.get_group(' 3-2')

catcherAhead = pd.concat((catcher01, catcher02, catcher12))
catcherEven = pd.concat((catcher00, catcher11, catcher22))
catcherBehind = pd.concat((catcher10, catcher20, catcher30, catcher21, catcher31))
catcher2K = pd.concat((catcher02, catcher12, catcher22, catcher32))

catcherMatchup = catcherTotal.groupby('BatterSide')
catcherL = catcherMatchup.get_group('Left')
catcherR = catcherMatchup.get_group('Right')

catcherLMatchup = catcherL.groupby('PitcherThrows')
catcherRMatchup = catcherR.groupby('PitcherThrows')

catcherLoL = catcherLMatchup.get_group("Left")
catcherRoL = catcherLMatchup.get_group("Right")
catcherLoR = catcherRMatchup.get_group("Left")
catcherRoR = catcherRMatchup.get_group("Right")

############################## Umpire Data ##################################################################
umpireData = data
umpireData = umpireData.groupby('PitchCall')
umpireStrikes = umpireData.get_group('StrikeCalled')
umpireBalls = umpireData.get_group('BallCalled')

umpireTotal = pd.concat((umpireStrikes, umpireBalls))

umpireCounts = umpireTotal.groupby('Count')
umpire00 = umpireCounts.get_group(' 0-0')
umpire01 = umpireCounts.get_group(' 0-1')
umpire02 = umpireCounts.get_group(' 0-2')
umpire10 = umpireCounts.get_group(' 1-0')
umpire11 = umpireCounts.get_group(' 1-1')
umpire12 = umpireCounts.get_group(' 1-2')
umpire20 = umpireCounts.get_group(' 2-0')
umpire21 = umpireCounts.get_group(' 2-1')
umpire22 = umpireCounts.get_group(' 2-2')
umpire30 = umpireCounts.get_group(' 3-0')
umpire31 = umpireCounts.get_group(' 3-1')
umpire32 = umpireCounts.get_group(' 3-2')

umpireAhead = pd.concat((umpire01, umpire02, umpire12))
umpireEven = pd.concat((umpire00, umpire11, umpire22))
umpireBehind = pd.concat((umpire10, umpire20, umpire30, umpire21, umpire31))
umpire2K = pd.concat((umpire02, umpire12, umpire22, umpire32))

umpireMatchup = umpireTotal.groupby('BatterSide')
umpireL = umpireMatchup.get_group('Left')
umpireR = umpireMatchup.get_group('Right')

umpireLMatchup = umpireL.groupby('PitcherThrows')
umpireRMatchup = umpireR.groupby('PitcherThrows')

umpireLoL = umpireLMatchup.get_group("Left")
umpireRoL = umpireLMatchup.get_group("Right")
umpireLoR = umpireRMatchup.get_group("Left")
umpireRoR = umpireRMatchup.get_group("Right")

########################## Lists for Loops ###############################
hitPitches = batterData.TaggedPitchType.unique().tolist()
hitTypes = batterData.TaggedPitchType.unique().tolist()
dates = dateData.Date.unique().tolist()
pitchers = pitcherData.Pitcher.unique().tolist()
batters = batterData.Batter.unique().tolist()
catchers = pitcherData.Catcher.unique().tolist()
umpires = pitcherData.Umpire.unique().tolist()
pitcherThrowsList = batterData.PitcherThrows.unique().tolist()
countList = data.Count.unique().tolist()
yearList = data.Year.unique().tolist()
pitcherList = batterData.Pitcher.unique().tolist()
batterList = pitcherData.Batter.unique().tolist()
opponentList = data.AwayTeam.unique().tolist()
batterHandList = pitcherData.BatterSide.unique().tolist()

# for hitters add these filters. Away Team* / Pitcher* / Count* / Pitcher Throws* / Year* / Date*
# for pitchers add these filters Batter Side* / Away Team* / Batter* / Count* / Year* / Date*
# set app variable with dash, set external style to bootstrap theme SUPERHERO or SANDSTONE
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE],
        meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},],)
# set app server to variable for deployment
server = app.server

# set app callback exceptions to true
app.config.suppress_callback_exceptions = True

over = {
  'margin-left': 'auto',
  'margin-right': 'auto',
  'display': 'block',
}


tabs_styles = {
        'height' : '44px'
}

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#FF6B11',
    'color': 'white',
    'padding': '6px'
}


bpDataTab = html.Div([
    html.H3('BP Data'),
])

bpChartsTab = html.Div([
    html.H3('BP Charts'),
])

bullpentab = html.Div([
    html.H3('Bullpens'),
])

bullpenData = html.Div([
    html.H3('Bullpen Data')
])

bullpenCharts = html.Div([
    html.H3('Bullpen Charts')
])

######## In Game Pitching Tabs ########################################

inGamePitchingTab = html.Div([
    html.H3('In Game Pitching'),
])

igpData = html.Div([
    html.H3('In Game Pitching Data'),
    dt.DataTable(
        id="igp_table",
        columns=[{"name": i, "id": i} for i in pitcherData1.columns],
        data=pitcherData1.to_dict("records"),
        sort_action='native'
        # filter_action ='native'
    ),
])

igpArsenal = html.Div([
    html.H2('Pitch Arsenal'),
    html.Div(children=[
        dcc.Graph(id='graphArsPie', style={'display': 'inline-block'}),
        dcc.Graph(id='graphArsPitches', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphArsSpinRate', style={'display': 'inline-block'}),
        dcc.Graph(id='graphArsBreak', style={'display': 'inline-block'}),
    ]),
    html.H2("Pitch Arsenal Table"),
    dt.DataTable(id="igpARSTable",
                 columns=[{"name": i, "id": i} for i in igpARSData.columns],
                 data=igpARSData.to_dict("records"),
                 sort_action='native'
                 ),
])

igpBattedBall = html.Div([
    html.H2('Balls in Play Charts and Visualizations'),
    html.Div(children=[
        dcc.Graph(id='graphBBHitLoc', style={'display': 'inline-block'}),
        dcc.Graph(id='graphBBHitLocResult', style={'display': 'inline-block'}),
        dcc.Graph(id='graphBBHitLocContact', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphBBHitLocEV', style={'display': 'inline-block'}),
        dcc.Graph(id='graphPBBSprayEV', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphPBBSprayPitch', style={'display': 'inline-block'}),
        dcc.Graph(id='graphPBBSprayResult', style={'display': 'inline-block'}),
    ]),
    html.H2('Batted Ball Table'),
    dt.DataTable(id="igpBBTable",
                 columns=[{"name": i, "id": i} for i in igpBBTable.columns],
                 data=igpBBTable.to_dict("records"),
                 sort_action='native'
                 ),
])

igpSwings = html.Div([
    html.H2('Zone Swings, Chases, and Contact Charts and Visualizations'),
    html.Div(children=[
        dcc.Graph(id='graphChaseAllPitches', style={'display': 'inline-block'}),
        dcc.Graph(id='graphChaseAllTakes', style={'display': 'inline-block'}),
        dcc.Graph(id='graphChaseCalledStrikes', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphChaseSwings', style={'display': 'inline-block'}),
        dcc.Graph(id='graphChaseInPlay', style={'display': 'inline-block'}),
        dcc.Graph(id='graphChaseSwingAndMiss', style={'display': 'inline-block'}),
    ]),
    html.H2("Swing and Miss Data"),
    dt.DataTable(id="igpChaseTable",
                 columns=[{"name": i, "id": i} for i in chaseTable.columns],
                 data=chaseTable.to_dict("records"),
                 sort_action='native'
                 ),
])

igpMove = html.Div([
    html.H3('Movement and Spin Charts and Visualizations'),
    html.Div(children=[
        dcc.Graph(id='graphTilt', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHBIVB', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphVBVAA', style={'display': 'inline-block'}),
        dcc.Graph(id='graphIVBRate', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphHBHAA', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHBRate', style={'display': 'inline-block'}),
    ]),
    html.H2("Pitch Movement Table"),
    dt.DataTable(id="igpMoveTable",
                 columns=[{"name": i, "id": i} for i in moveData.columns],
                 data=moveData.to_dict("records"),
                 sort_action='native'
                 ),
])

igpRelease = html.Div([
    html.H3('Release Point and Pitch Movement Charts and Visualizations'),
    html.Div(children=[
        dcc.Graph(id='graphRelPitcher', style={'display': 'inline-block'}),
        dcc.Graph(id='graphRelSide', style={'display': 'inline-block'}),
        dcc.Graph(id='graphRelTop', style={'display': 'inline-block'}),
    ]),
    dcc.Graph(id='graphRel3D', style={'display': 'inline-block', 'vertical-align': 'middle'}),
])

igpSequence = html.Div([
    html.H3('Plan of Attack and Sequencing Charts and Visualizations'),
    html.Div(children=[
        dcc.Graph(id='graphSeqPie', style={'display': 'inline-block'}),
        dcc.Graph(id='graphSeqBar', style={'display': 'inline-block'}),
        dcc.Graph(id='graphSeqResultBar', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphVeloHold', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphRelHeightHold', style={'display': 'inline-block'}),
        dcc.Graph(id='graphRelSideHold', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphIVBHold', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHBHold', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphSpinRateHold', style={'display': 'inline-block'}),
    ]),
])

########################################### Catchers and Umpires ###################################################

catcherTab = html.Div([
    html.H3('Catchers'),
    dcc.Dropdown(
        id='catcher_dropdown',
        options=[{"label": 'All Catchers', 'value': 'All Catchers'}] + [{'label': name, 'value': name} for name in
                                                                        catchers],
        placeholder='---Select Name---',
        value='All Catchers'
    ),
    html.Div(children=[
        dcc.Graph(id='catcherTotals', style={'display': 'inline-block'}),
        dcc.Graph(id='catcher2KVisual', style={'display': 'inline-block'})
    ]),
    html.Div(children=[
        dcc.Graph(id='catcherLeft', style={'display': 'inline-block'}),
        dcc.Graph(id='catcherRight', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='catcherLoL', style={'display': 'inline-block'}),
        dcc.Graph(id='catcherLoR', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='catcherRoL', style={'display': 'inline-block'}),
        dcc.Graph(id='catcherRoR', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='catcherAheadVisual', style={'display': 'inline-block'}),
        dcc.Graph(id='catcherBehindVisual', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='catcherEvenVisual', style={'display': 'inline-block'}),
        dcc.Graph(id='catcher00Visual', style={'display': 'inline-block'}),
    ]),
])

umpiresTab = html.Div([
    html.H3('Umpires'),
    dcc.Dropdown(
        id='umpire_dropdown',
        options=[{"label": 'All Umpires', 'value': 'All Umpires'}] + [{'label': name, 'value': name} for name in
                                                                        umpires],
        placeholder='---Select Name---',
        value='All Umpires'
    ),
    html.Div(children=[
        dcc.Graph(id='umpireTotals', style={'display': 'inline-block'}),
        dcc.Graph(id='umpire2KVisual', style={'display': 'inline-block'})
    ]),
    html.Div(children=[
        dcc.Graph(id='umpireLeft', style={'display': 'inline-block'}),
        dcc.Graph(id='umpireRight', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='umpireLoL', style={'display': 'inline-block'}),
        dcc.Graph(id='umpireLoR', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='umpireRoL', style={'display': 'inline-block'}),
        dcc.Graph(id='umpireRoR', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='umpireAheadVisual', style={'display': 'inline-block'}),
        dcc.Graph(id='umpireBehindVisual', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='umpireEvenVisual', style={'display': 'inline-block'}),
        dcc.Graph(id='umpire00Visual', style={'display': 'inline-block'}),
    ]),
])


####### In Game Hitting Tabs #############

inGameHittingTab = html.Div([
    html.H3('In Game Hitting'),
])

ighBattedBallCharts = html.Div([
    html.H2('Batted Ball Visualizations and Charts'),
    html.Div(children=[
        dcc.Graph(id='graphBBSpray', style={'display': 'inline-block'}),
        dcc.Graph(id='graphContactBBSpray', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphBBEVSpray', style={'display': 'inline-block'}),
        dcc.Graph(id='graphPitchTypeBBSpray', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphXZBBResultContact', style={'display': 'inline-block'}),
        dcc.Graph(id='graphXZBBHitTypeContact', style={'display': 'inline-block'}),
        dcc.Graph(id='graphXZBBPitchContact', style={'display': 'inline-block'}),
    ]),
    dt.DataTable(id="ighBBTable",
                 columns=[{"name": i, "id": i} for i in ighBBData.columns],
                 data=ighBBData.to_dict("records"),
                 sort_action='native'
                 ),
])

ighPlateDisciplineCharts = html.Div([
    html.H2('Hitter Plate Discipline Charts and Visualizations'),
    html.Div(children=[
        dcc.Graph(id='graphBIP', style={'display': 'inline-block'}),
        dcc.Graph(id='graphSwings', style={'display': 'inline-block'}),
        dcc.Graph(id='graphSwingsMisses', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphTakesBorS', style={'display': 'inline-block'}),
        dcc.Graph(id='graphcalledStrikes', style={'display': 'inline-block'}),
        dcc.Graph(id='graphTakesPitchType', style={'display': 'inline-block'}),
    ]),
])

ighScoutingCharts = html.Div([
    html.H2('Scouting Report and Attack Plan Charts and Visualizations'),
    html.Div(children=[
        dcc.Graph(id='graphHitPie', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHitBar', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHitResultBar', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphHitEvenPie', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHitEvenBar', style={'display': 'inline-block'}),
        dcc.Graph(id='graphBIPEven', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphHitAheadPie', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHitAheadBar', style={'display': 'inline-block'}),
        dcc.Graph(id='graphBIPAhead', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphHitBehindPie', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHitBehindBar', style={'display': 'inline-block'}),
        dcc.Graph(id='graphBIPBehind', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphHit2KPie', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHit2KBar', style={'display': 'inline-block'}),
        dcc.Graph(id='graphBIP2K', style={'display': 'inline-block'}),
    ]),
    html.Div(children=[
        dcc.Graph(id='graphHit00Pie', style={'display': 'inline-block'}),
        dcc.Graph(id='graphHit00Bar', style={'display': 'inline-block'}),
        dcc.Graph(id='graphBIP00', style={'display': 'inline-block'}),
    ]),
])

ighData = html.Div([
    html.H2('In Game Hitting Data'),
    dt.DataTable(
        id="table-container",
        columns=[{"name": i, "id": i} for i in batterData1.columns],
        data=batterData1.to_dict("records"),
        sort_action='native'
        # filter_action ='native'
    ),
])

app.layout = html.Div(id='parent', children=[
    html.Div([html.Img(src=app.get_asset_url('uvadashboardimage.jpg'), style={'width': '30%', 'height': '70%', 'align': 'center'})], style={'textAlign':'center', 'width':'100%', 'backgroundColor': '#090436'}),
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[

        dcc.Tab(label='In Game Pitching', value='In Game Pitching', children=[
            html.H3('Data Filters'),
            dcc.Dropdown(
                id='igp_General_dropdown',
                options=[{"label": 'All Pitchers', 'value': 'All Pitchers'}] + [{'label': name, 'value': name} for name
                                                                                in
                                                                                pitchers],
                placeholder='---Select Name---',
                value='All Pitchers',

            ),
            dcc.Dropdown(
                id='igp_GeneralOpponent_dropdown',
                options=[{"label": 'All Opponents', 'value': 'All Opponents'}] + [{'label': name, 'value': name} for name in
                                                                          opponentList],
                placeholder='---Select Opponent---',
                value='All Opponents',

            ),
            dcc.Dropdown(
                id='igp_GeneralBatter_dropdown',
                options=[{"label": 'All Hitters', 'value': 'All Hitters'}] + [{'label': name, 'value': name} for name in
                                                                          batterList],
                placeholder='---Select Hitters---',
                value='All Hitters',

            ),
            dcc.Dropdown(
                id='igp_GeneralBatterSide_dropdown',
                options=[{"label": 'All Sides', 'value': 'All Sides'}] + [{'label': name, 'value': name} for name in batterHandList],
                placeholder='---Select Hitter Handedness---',
                value='All Sides',

            ),
            dcc.Dropdown(
                id='igp_GeneralCount_dropdown',
                options=[{"label": 'All Counts', 'value': 'All Counts'}] + [{'label': name, 'value': name} for name in
                                                                          countList],
                placeholder='---Select Count---',
                value='All Counts',

            ),
            dcc.Dropdown(
                id='igp_GeneralYear_dropdown',
                options=[{"label": 'All Seasons', 'value': 'All Seasons'}] + [{'label': name, 'value': name} for name in
                                                                          yearList],
                placeholder='---Select Season---',
                value='2022 Fall',

            ),
            dcc.Dropdown(
                id='igp_GeneralDate_dropdown',
                options=[{"label": 'All Dates', 'value': 'All Dates'}] + [{'label': name, 'value': name} for name in
                                                                          dates],
                placeholder='---Select Date---',
                value='All Dates',

            ),
            dcc.Tabs(id='In Game Pitching SubTabs', value='IGP Data', children=[
                dcc.Tab(label='In Game Pitching Data', value='IGP Data', children=igpData),
                dcc.Tab(label='Charts and Visualizations', value='In Game Pitching Charts', children=[
                    dcc.Tabs(id='Pitching Charts Subtabs', value='IGP Charts', children=[
                        dcc.Tab(label='Pitch Arsenal', value='Arsenal', children=igpArsenal, style=tab_style, selected_style= tab_selected_style),
                        dcc.Tab(label='Balls in Play', value='BallinPlay', children=igpBattedBall, style=tab_style, selected_style= tab_selected_style),
                        dcc.Tab(label='Pitcher Chase Profile', value='ChaseWhiff', children=igpSwings, style=tab_style, selected_style= tab_selected_style),
                        dcc.Tab(label='Break and Movement', value='BreakandMovement', children=igpMove, style=tab_style, selected_style= tab_selected_style),
                        dcc.Tab(label='Release Point', value='ReleasePoint', children=igpRelease, style=tab_style, selected_style= tab_selected_style),
                        dcc.Tab(label='Approach and Sequencing', value='sequence', children=igpSequence, style=tab_style, selected_style= tab_selected_style)
                    ])
                ])
            ], style=tab_style)
        ], style=tab_style, selected_style=tab_selected_style),

        dcc.Tab(label='In Game Hitting', value='In Game Hitting', children=[
            html.H3("Data Filters"),
            dcc.Dropdown(
                id='igh_General_dropdown',
                options=[{"label": 'All Hitters', 'value': 'All Hitters'}] + [{'label': name, 'value': name} for name in
                                                                              batters],
                placeholder='---Select Name---',
                value='All Hitters',

            ),
            dcc.Dropdown(
                id='igh_GeneralOpponent_dropdown',
                options=[{"label": 'All Opponents', 'value': 'All Opponents'}] + [{'label': name, 'value': name} for
                                                                                  name in
                                                                                  opponentList],
                placeholder='---Select Opponent---',
                value='All Opponents',

            ),
            dcc.Dropdown(
                id='igh_GeneralPitcher_dropdown',
                options=[{"label": 'All Pitchers', 'value': 'All Pitchers'}] + [{'label': name, 'value': name} for name in
                                                                              pitcherList],
                placeholder='---Select Pitcher---',
                value='All Pitchers',

            ),
            dcc.Dropdown(
                id='igh_GeneralPT_dropdown',
                options=[{"label": 'All Pitcher Handedness', 'value': 'All Pitcher Handedness'}] + [{'label': name, 'value': name} for name
                                                                                in
                                                                                pitcherThrowsList],
                placeholder='---Select Pitcher Handedness---',
                value='All Pitcher Handedness',
            ),
            dcc.Dropdown(
                id='igh_GeneralCount_dropdown',
                options=[{"label": 'All Counts', 'value': 'All Counts'}] + [{'label': name, 'value': name} for name in
                                                                            countList],
                placeholder='---Select Count---',
                value='All Counts',

            ),
            dcc.Dropdown(
                id='igh_GeneralYear_dropdown',
                options=[{"label": 'All Seasons', 'value': 'All Seasons'}] + [{'label': name, 'value': name} for name in
                                                                              yearList],
                placeholder='---Select Season---',
                value='2022 Fall',

            ),
            dcc.Dropdown(
                id='igh_GeneralDate_dropdown',
                options=[{"label": 'All Dates', 'value': 'All Dates'}] + [{'label': name, 'value': name} for name in
                                                                          dates],
                placeholder='---Select Date---',
                value='All Dates',

            ),
            dcc.Tabs(id='In Game Hitting SubTabs', value='IGH Data', children=[
                dcc.Tab(label='In Game Hitting Data', value='In Game Hitting Data', children=ighData),
                dcc.Tab(label='Charts and Visualizations', value='In Game Hitting Charts', children=[
                    dcc.Tabs(id="Hitting Chart Subtabs", value="IGH Charts", children=[
                        dcc.Tab(label='Batted Ball', value='IGH Batted Ball Charts', children=ighBattedBallCharts),
                        dcc.Tab(label='Hitter Plate Discipline', value='IGH Plate Disc Charts', children=ighPlateDisciplineCharts),
                        dcc.Tab(label="Self Scouting and Approach", value='Plan Charts', children=ighScoutingCharts),
                    ])
                ])
            ])
        ], style=tab_style, selected_style=tab_selected_style),

        dcc.Tab(label='Catchers and Umpires', value='Catchers and Umpires', children=[
            dcc.Tabs(id='CnU', value='Catchers', children=[
                dcc.Tab(label='Catchers', value='Catchers', children=catcherTab),
                dcc.Tab(label='Umpires', value='Umpires', children=umpiresTab)
            ])
        ], style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
])

@app.callback(
    Output('tabs-content-inline', 'children'),
    Input('tabs-styled-with-inline', 'value')
)

######################################In Game Hitting Tab#############################################################
@app.callback(
    Output("table-container", "data"),
    Input("igh_General_dropdown", "value")
)

def display_table(value):
    if (value == 'All Hitters'):
        dff = batterData1
    else:
        dff = batterData1[batterData1.Batter == value]
    return dff.to_dict("records")

@app.callback(
    Output("igp_table", "data"),
    [Input("igp_General_dropdown", "value"),
     Input("igp_GeneralDate_dropdown", 'value')]
)

def display_table2(value, value2):
    if value == "All Pitchers":
        dff1 = pitcherData1
    else:
        dff1 = pitcherData1[pitcherData1.Pitcher == value]

    if value2 == 'All Dates':
        dff1 = dff1
    else:
        dff1 = dff1[dff1.Date == value2]

    return dff1.to_dict("records")


################## In Game Hitting Point of Contact Charts #############################


@app.callback(
    Output('graphXZContact', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def hitLocXZGraph(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Balls in Play by Result'
    fig = pitchResultLocation(filtered_data, title)
    return fig

@app.callback(
    Output('graphYZContact', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def hitLocYZGraph(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Contact Point (Side View) by Play Result'
    fig = contactSide(filtered_data, title)
    return fig

@app.callback(
    Output('graphXYContact', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def hitLocXYGraph(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Contact Point (Top View) by Play Result'
    fig = contactTop(filtered_data, title)
    return fig

@app.callback(
    Output('graph3DContact', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def Contact3D(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = '3D Contact Points'
    fig = contact3D(filtered_data, title)
    return fig

@app.callback(
    Output('graphSprayChart', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def traditionalSprayChart(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Play Result Spray Chart'
    fig = playResultSpray(filtered_data, title)
    return fig

@app.callback(
    Output('graphContactSpray', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def contactSprayChart(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Contact Type Spray Chart'
    fig = contactSpray(filtered_data, title)
    return fig

@app.callback(
    Output('graphEVSpray', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)
def evSprayChart(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title ='Exit Velocity Spray Chart'
    fig = exitVeloSpray(filtered_data, title)
    return fig

@app.callback(
    Output("ighPOCTable", "data"),
    [Input("igh_General_dropdown", "value"),
     Input("igh_GeneralPT_dropdown", "value")]
)

def updatePoCTable(value, value2):
    if value == 'All Hitters':
        dff = ighPoCData[['Batter','PitcherThrows', 'TaggedPitchType', 'TaggedHitType', 'ExitSpeed', 'Angle']].dropna()
    else:
        dff = ighPoCData[ighPoCData.Batter == value]
        dff = dff[['Batter','PitcherThrows', 'TaggedPitchType', 'TaggedHitType', 'ExitSpeed', 'Angle']].dropna()
    if value2 == 'All Pitcher Handedness':
        dff = dff
    else:
        dff = dff[dff.PitcherThrows == value2]
        dff = dff[['Batter','PitcherThrows', 'TaggedPitchType', 'TaggedHitType', 'ExitSpeed', 'Angle']].dropna()
    return (dff.to_dict("records"))

############################## In Game Hitting Batted Ball Charts #############################################
@app.callback(
    Output('graphBBSpray', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def sprayBB(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay,value,value2,value3,value4,value5,value6,value7)
    title = 'Play Result Spray Chart'
    fig = playResultSpray(filtered_data, title)
    return fig

@app.callback(
    Output('graphBBEVSpray', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def BBEVSprayChart(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Exit Velocity Spray Chart'
    fig = exitVeloSpray(filtered_data, title)
    return fig

@app.callback(
    Output('graphContactBBSpray', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def contactBBSprayChart(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Contact Type Spray Chart'
    fig = contactSpray(filtered_data, title)
    return fig

@app.callback(
    Output('graphPitchTypeBBSpray', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def pitchTypeSprayChart(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Spray Chart by Pitch Type'
    fig = pitchSpray(filtered_data, title)
    return fig


@app.callback(
    Output("ighBBTable", "data"),
    [Input("igh_General_dropdown", "value"),
    Input("igh_GeneralPT_dropdown", "value")]
)

def bbTable(value,value2):
    if value == 'All Hitters':
        dff = ighBBData[['Date', 'Batter', 'PitcherThrows', 'TaggedPitchType', 'ExitSpeed', 'Angle', 'Distance', 'HangTime']].dropna()
    else:
        dff = ighBBData[ighPoCData.Batter == value]
        dff = dff[['Date', 'Batter','PitcherThrows', 'TaggedPitchType', 'ExitSpeed', 'Angle', 'Distance', 'HangTime']].dropna()
    if value2 == 'All Pitcher Handedness':
        dff = dff[['Date', 'Batter','PitcherThrows', 'TaggedPitchType', 'ExitSpeed', 'Angle', 'Distance', 'HangTime']].dropna()
    else:
        dff = dff[dff.PitcherThrows == value2]
        dff = dff[['Date', 'Batter','PitcherThrows', 'TaggedPitchType', 'ExitSpeed', 'Angle', 'Distance', 'HangTime']].dropna()
    return (dff.to_dict("records"))

@app.callback(
    Output('graphXZBBResultContact', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def hitLocXZBBGraph(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    fig = pitchResultLocation(filtered_data, "Balls in Play by Result")
    return fig

@app.callback(
    Output('graphXZBBHitTypeContact', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def hitLocXZHitTypeGraph(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    fig = pitchHitTypeLocation(filtered_data, "Balls in Play by Contact Type")
    return fig

@app.callback(
    Output('graphXZBBPitchContact', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def hitLocXZGraphPitchType(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "Balls in Play by Pitch Type")
    return fig



#################### IGH Plate Discipline Charts ####################################

@app.callback(
    Output('graphSwings', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def allSwings(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(swings, value, value2, value3, value4, value5, value6, value7)
    title = 'All Swings'
    fig = pitchTypeLocations(filtered_data, title)
    return fig

@app.callback(
    Output('graphSwingsMisses', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def swingandMiss(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(swingingStrikes, value, value2, value3, value4, value5, value6, value7)
    title = 'Swings and Misses'
    fig = pitchTypeLocations(filtered_data, title)
    return fig

@app.callback(
    Output('graphTakesBorS', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def allTakes(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(takes, value, value2, value3, value4, value5, value6, value7)
    title = 'All Takes'
    fig = ballStrikeLocation(filtered_data, title)
    return fig

@app.callback(
    Output('graphTakesPitchType', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def allTakesPitch(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(takes, value, value2, value3, value4, value5, value6, value7)
    title = 'All Takes by Pitch Type'
    fig = pitchTypeLocations(filtered_data, title)
    return fig

@app.callback(
    Output('graphcalledStrikes', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def calledStrikesFunc(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(calledStrikes, value, value2, value3, value4, value5, value6, value7)
    title = 'Pitches Taken for Strikes'
    fig = pitchTypeLocations(filtered_data, title)
    return fig

@app.callback(
    Output('graphBIP', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def ballInPlay(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Balls in Play by Pitch Type'
    fig = pitchTypeLocations(filtered_data, title)
    return fig

########################## IGP Pitch Arsenal Charts ################################################################

@app.callback(
    Output('graphArsPie', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def pitchUsagePie(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData,value,value2,value3,value4,value5,value6,value7)
    fig = pitchPie(filtered_data)
    return fig

@app.callback(
    Output('graphArsSpinRate', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def spinRate(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData,value,value2,value3,value4,value5,value6,value7)
    fig = rateVelo(filtered_data)
    return fig

@app.callback(
    Output('graphArsSpinEff', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def spinEff(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = effVelo(filtered_data)
    return fig

@app.callback(
    Output('graphArsPitches', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def allPitches(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, 'Pitch Locations')
    return fig

@app.callback(
    Output('graphArsSpinRateEff', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def spinRateEff(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = rateEff(filtered_data)
    return fig

@app.callback(
    Output('graphArsBreak', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def arsBreak(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = hbIVB(filtered_data)
    return fig

@app.callback(
    Output("igpARSTable", "data"),
    [Input("igp_General_dropdown", "value"),
    Input("igp_GeneralDate_dropdown", "value")]
)

def updateArsTable(value, value2):
    if value == 'All Pitchers':
        dff = igpARSData[['Date','Pitcher','TaggedPitchType', 'RelSpeed', 'SpinRate', 'HorzBreak', 'InducedVertBreak']].dropna()
    else:
        dff = igpARSData[igpARSData.Pitcher == value]
        dff = dff[['Date', 'Pitcher','TaggedPitchType', 'RelSpeed', 'SpinRate', 'HorzBreak', 'InducedVertBreak']].dropna()
    if value2 == 'All Dates':
        dff = dff
    else:
        dff = dff[dff.Date == value2]
    return (dff.to_dict("records"))

########################## IGP Batted Ball Charts ###################################################################

@app.callback(
    Output('graphBBHitLoc', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def hitLocations(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(igpBBData, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "Balls in Play by Pitch Type")
    return fig

@app.callback(
    Output('graphBBHitLocResult', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def hitLocationsResult(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(igpBBData, value, value2, value3, value4, value5, value6, value7)
    fig = pitchResultLocation(filtered_data, 'Balls in Play by Result')
    return fig

@app.callback(
    Output('graphBBHitLocContact', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def hitLocationsContact(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(igpBBData, value, value2, value3, value4, value5, value6, value7)
    fig = pitchHitTypeLocation(filtered_data, "Balls in Play by Contact Type")
    return fig

@app.callback(
    Output('graphBBHitLocEV', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def hitLocationsEV(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(igpBBData, value, value2, value3, value4, value5, value6, value7)
    fig = pitchLocationEV(filtered_data, "Balls in Play by Exit Velocity")
    return fig

@app.callback(
    Output('graphPBBSprayPitch', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def contactPBBSprayChart(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(igpBBData, value, value2, value3, value4, value5, value6, value7)
    fig = pitchSpray(filtered_data, "Spray Chart by Pitch Type")
    return fig

@app.callback(
    Output('graphPBBSprayResult', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def contactPBBSprayChartResult(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(igpBBData, value, value2, value3, value4, value5, value6, value7)
    fig = playResultSpray(filtered_data, "Play Result Spray Chart")
    return fig

@app.callback(
    Output('graphPBBSprayEV', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def contactPBBSprayChartEV(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(igpBBData, value, value2, value3, value4, value5, value6, value7)
    fig = exitVeloSpray(filtered_data, "Spray Chart by Exit Velocity")
    return fig


@app.callback(
    Output("igpBBTable", "data"),
    [Input("igp_General_dropdown", "value"),
     Input('igp_GeneralDate_dropdown', 'value')]
)

def updateBBPTable(value, value2):

    if value == 'All Pitchers':
        dff = igpBBData
        dff = dff[['Date', 'Pitcher', 'Batter', 'TaggedPitchType', 'TaggedHitType', 'PlayResult', 'RelSpeed', 'PlateLocSide', 'PlateLocHeight', 'ExitSpeed']].dropna()
    else:
        dff = igpBBData[igpBBData.Pitcher == value]
        dff = dff[['Date', 'Pitcher', 'Batter', 'TaggedPitchType', 'TaggedHitType', 'PlayResult', 'RelSpeed', 'PlateLocSide', 'PlateLocHeight', 'ExitSpeed']].dropna()
    if value2 == 'All Dates':
        dff = dff
        dff = dff[['Date', 'Pitcher', 'Batter', 'TaggedPitchType', 'TaggedHitType', 'PlayResult', 'RelSpeed', 'PlateLocSide', 'PlateLocHeight', 'ExitSpeed']].dropna()
    else:
        dff = dff[dff.Date == value2]
        dff = dff[['Date', 'Pitcher', 'Batter', 'TaggedPitchType', 'TaggedHitType', 'PlayResult', 'RelSpeed', 'PlateLocSide', 'PlateLocHeight', 'ExitSpeed']].dropna()
    return (dff.to_dict("records"))

################################ IGP Pitcher Chase Charts ###################################################
@app.callback(
    Output('graphChaseAllPitches', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
    Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
    Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
    Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
    Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
    Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
    Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def chaseAllPitches(value, value2, value3, value4, value5, value6, value7):
    filtered_data = pitchingFilters(chaseData1, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "All Pitches by Pitch Type")
    return fig

@app.callback(
    Output('graphChaseCalledStrikes', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def chaseAllCalledStrikes(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherStrikesCalled, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "Called Strikes")
    return fig

@app.callback(
    Output('graphChaseAllTakes', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def chaseAllTakes(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherAllTakes, value, value2, value3, value4, value5, value6, value7)
    fig = ballStrikeLocation(filtered_data, "All Takes")
    return fig

@app.callback(
    Output('graphChaseSwings', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def chaseAllSwings(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherAllSwings, value, value2, value3, value4, value5, value6, value7)
    fig = pitchSwingLocation(filtered_data, "All Swings")
    return fig

@app.callback(
    Output('graphChaseSwingAndMiss', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def chaseAllSwingAndMiss(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherSwingAndMiss, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "All Swings and Misses")
    return fig

@app.callback(
    Output('graphChaseInPlay', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def chaseInPlay(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherInPlay, value, value2, value3, value4, value5, value6, value7)
    title = 'Balls in Play by Pitch Type'
    fig = pitchTypeLocations(filtered_data, title)
    return fig

@app.callback(
    Output("igpChaseTable", "data"),
    [Input("igp_General_dropdown", "value"),
    Input("igp_GeneralDate_dropdown", "value")]
)

def updateChaseTable(value, value2):
    if value == 'All Pitchers':
        dff = chaseTable[['Date', 'Pitcher', 'Batter', 'TaggedPitchType','RelSpeed', 'HorzBreak', 'InducedVertBreak', 'PlateLocSide', 'PlateLocHeight', 'HorzApprAngle', 'VertApprAngle']].dropna()
    else:
        dff = chaseTable[chaseTable.Pitcher == value]
        dff = dff[['Date', 'Pitcher', 'Batter', 'TaggedPitchType','RelSpeed', 'HorzBreak', 'InducedVertBreak', 'PlateLocSide', 'PlateLocHeight', 'HorzApprAngle', 'VertApprAngle']].dropna()

    if value2 == 'All Dates':
        dff = dff[['Date', 'Pitcher', 'Batter', 'TaggedPitchType','RelSpeed', 'HorzBreak', 'InducedVertBreak', 'PlateLocSide', 'PlateLocHeight', 'HorzApprAngle', 'VertApprAngle']].dropna()
    else:
        dff = dff[dff.Date == value2]
        dff = dff[['Date', 'Pitcher', 'Batter', 'TaggedPitchType','RelSpeed', 'HorzBreak', 'InducedVertBreak', 'PlateLocSide', 'PlateLocHeight', 'HorzApprAngle', 'VertApprAngle']].dropna()

    return (dff.to_dict("records"))

################################ IGP Break and Movement Charts ##############################################

@app.callback(
    Output('graphHBIVB', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def moveHBIVB(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = hbIVB(filtered_data)
    return fig


@app.callback(
    Output('graphIVBRate', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def moveSpinIVB(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = rateIVB(filtered_data)
    return fig

@app.callback(
    Output('graphHBRate', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def moveSpinHB(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = rateHB(filtered_data)
    return fig

@app.callback(
    Output('graphVBVAA', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def moveVBVAA(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = ivbVAA(filtered_data)
    return fig

@app.callback(
    Output('graphHBHAA', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def moveHBHAA(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = hbHAA(filtered_data)
    return fig

@app.callback(
    Output('graphTilt', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def moveTilt(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = tilt(filtered_data)
    return fig

@app.callback(
    Output("igpMoveTable", "data"),
    [Input("igp_General_dropdown", "value"),
     Input("igp_GeneralDate_dropdown", "value")]
)

def updateBBPTable(value, value2):
    if value == 'All Pitchers':
        dff = moveData[['Date', 'Pitcher', 'RelSpeed', 'SpinRate','SpinAxis', 'HorzBreak', 'InducedVertBreak', 'VertApprAngle', 'HorzApprAngle']].dropna()
    else:
        dff = moveData[moveData.Pitcher == value]
        dff = dff[['Date', 'Pitcher', 'RelSpeed', 'SpinRate','SpinAxis', 'HorzBreak', 'InducedVertBreak', 'VertApprAngle', 'HorzApprAngle']].dropna()
    if value == 'All Dates':
        dff = dff[['Date', 'Pitcher', 'RelSpeed', 'SpinRate','SpinAxis', 'HorzBreak', 'InducedVertBreak', 'VertApprAngle', 'HorzApprAngle']].dropna()
    else:
        dff = dff[dff.Date == value2]
        dff = dff[['Date', 'Pitcher', 'RelSpeed', 'SpinRate','SpinAxis', 'HorzBreak', 'InducedVertBreak', 'VertApprAngle', 'HorzApprAngle']].dropna()
    return (dff.to_dict("records"))



############################### IGP Release Point Charts ####################################################

@app.callback(
    Output('graphRelPitcher', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def relPitcher(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = releasePitcher(filtered_data)
    return fig


@app.callback(
    Output('graphRelSide', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def relSide(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = releaseSide(filtered_data)
    return fig

@app.callback(
    Output('graphRelTop', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def relTop(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = releaseTop(filtered_data)
    return fig

@app.callback(
    Output('graphRel3D', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def rel3D(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = release3D(filtered_data)
    return fig
########################## Catchers Charts #################################################################
@app.callback(
    Output('catcherTotals', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)

def catchTotal(value):
    filtered_data = catcherFilters(catcherTotal, value)
    fig = ballStrikeLocation(filtered_data, "All Calls for " + str(value))
    return fig

@app.callback(
    Output('catcherLeft', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)

def catchLeft(value):
    filtered_data = catcherFilters(catcherL, value)
    fig = ballStrikeLocation(filtered_data, "LHH Calls for " + str(value))
    return fig

@app.callback(
    Output('catcherRight', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)

def catchRight(value):
    filtered_data = catcherFilters(catcherR, value)
    fig = ballStrikeLocation(filtered_data, "RHH Calls for " + str(value))
    return fig

@app.callback(
    Output('catcherLoR', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)

def catchLoR(value):
    filtered_data = catcherFilters(catcherLoR, value)
    fig = ballStrikeLocation(filtered_data, "LHP on RHH Calls for " + str(value))
    return fig

@app.callback(
    Output('catcherLoL', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)

def catchLoL(value):
    filtered_data = catcherFilters(catcherLoL, value)
    fig = ballStrikeLocation(filtered_data, "LHP on LHH Calls for " + str(value))
    return fig

@app.callback(
    Output('catcherRoR', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)

def catchRoR(value):
    filtered_data = catcherFilters(catcherRoR, value)
    fig = ballStrikeLocation(filtered_data, "RHP on RHH Calls for " + str(value))
    return fig

@app.callback(
    Output('catcherRoL', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)

def catchRoL(value):
    filtered_data = catcherFilters(catcherRoL, value)
    fig = ballStrikeLocation(filtered_data, "RHP on LHH Calls for " + str(value))
    return fig
@app.callback(
    Output('catcherAheadVisual', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)

def catcherAheadChart(value):
    filtered_data = catcherFilters(catcherAhead, value)
    fig = ballStrikeLocation(filtered_data, "Catcher Plus Count Map for " + str(value))
    return fig


@app.callback(
    Output('catcherBehindVisual', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)
def catcherBehindChart(value):
    filtered_data = catcherFilters(catcherBehind, value)
    fig = ballStrikeLocation(filtered_data, "Catcher Minus Count Map for " + str(value))
    return fig


@app.callback(
    Output('catcherEvenVisual', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)
def catcherEvenChart(value):
    filtered_data = catcherFilters(catcherEven, value)
    fig = ballStrikeLocation(filtered_data, "Catcher Even Count Map for " + str(value))
    return fig


@app.callback(
    Output('catcher2KVisual', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)
def catcher2KChart(value):
    filtered_data = catcherFilters(catcher2K, value)
    fig = ballStrikeLocation(filtered_data, "Catcher 2 Strike Map for " + str(value))
    return fig


@app.callback(
    Output('catcher00Visual', 'figure'),
    Input(component_id='catcher_dropdown', component_property='value')
)
def catcher00Chart(value):
    filtered_data = catcherFilters(catcher00, value)
    fig = ballStrikeLocation(filtered_data, "First Pitch Calls " + str(value))
    return fig


######################################## Umpire Charts ##############################################################
@app.callback(
    Output('umpireTotals', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)

def umpTotal(value):
    filtered_data = umpireFilters(umpireTotal, value)
    fig = ballStrikeLocation(filtered_data, "All Calls for " + str(value))
    return fig

@app.callback(
    Output('umpireLeft', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)

def umpLeft(value):
    filtered_data = umpireFilters(umpireL, value)
    fig = ballStrikeLocation(filtered_data, "All LHH Calls for " + str(value))
    return fig

@app.callback(
    Output('umpireRight', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)

def umpRight(value):
    filtered_data = umpireFilters(umpireR, value)
    fig = ballStrikeLocation(filtered_data, "All RHH Calls for " + str(value))
    return fig

@app.callback(
    Output('umpireLoR', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)

def umpLoR(value):
    filtered_data = umpireFilters(umpireLoR, value)
    fig = ballStrikeLocation(filtered_data, "All LHP vs RHH Calls for " + str(value))
    return fig

@app.callback(
    Output('umpireLoL', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)

def umpLoL(value):
    filtered_data = umpireFilters(umpireLoL, value)
    fig = ballStrikeLocation(filtered_data, "All LHP vs LHH Calls for " + str(value))
    return fig

@app.callback(
    Output('umpireRoR', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)

def umpRoR(value):
    filtered_data = umpireFilters(umpireRoR, value)
    fig = ballStrikeLocation(filtered_data, "All RHP vs RHH Calls for " + str(value))
    return fig

@app.callback(
    Output('umpireRoL', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)

def umpRoL(value):
    filtered_data = umpireFilters(umpireRoL, value)
    fig = ballStrikeLocation(filtered_data, "All RHP vs LHH Calls for " + str(value))
    return fig

@app.callback(
    Output('umpireAheadVisual', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)

def umpireAheadChart(value):
    filtered_data = umpireFilters(umpireAhead, value)
    fig = ballStrikeLocation(filtered_data, "All Plus Count Calls for " + str(value))
    return fig


@app.callback(
    Output('umpireBehindVisual', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)
def umpireBehindChart(value):
    filtered_data = umpireFilters(umpireBehind, value)
    fig = ballStrikeLocation(filtered_data, "All Minus Count Calls for " + str(value))
    return fig


@app.callback(
    Output('umpireEvenVisual', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)
def umpireEvenChart(value):
    filtered_data = umpireFilters(umpireEven, value)
    fig = ballStrikeLocation(filtered_data, "All Even Count Calls for " + str(value))
    return fig


@app.callback(
    Output('umpire2KVisual', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)
def umpire2KChart(value):
    filtered_data = umpireFilters(umpire2K, value)
    fig = ballStrikeLocation(filtered_data, "All 2-Strike Calls for " + str(value))
    return fig


@app.callback(
    Output('umpire00Visual', 'figure'),
    Input(component_id='umpire_dropdown', component_property='value')
)
def umpire00Chart(value):
    filtered_data = umpireFilters(umpire00, value)
    fig = ballStrikeLocation(filtered_data, "All First Pitch Calls for " + str(value))
    return fig

################################ IGP Pitch Sequencing Charts ####################################################
@app.callback(
    Output('graphSeqPie', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def pitchSeqUsagePie(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData,value,value2,value3,value4,value5,value6,value7)
    fig = pitchPie(filtered_data)
    return fig

@app.callback(
    Output('graphSeqBar', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def pitchSeqUsageBar(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = pitchBar(filtered_data)
    return fig

@app.callback(
    Output('graphSeqResultBar', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def pitchSeqResultBar(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = resultBar(filtered_data)
    return fig

@app.callback(
    Output('graphVeloHold', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def seqVeloHold(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = holding(filtered_data, "Velocity over the Course of Outing", "RelSpeed")
    return fig

@app.callback(
    Output('graphRelHeightHold', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def seqHeightHold(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = holding(filtered_data, "Release Height over the Course of Outing", "RelHeight")
    return fig

@app.callback(
    Output('graphRelSideHold', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def seqSideHold(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = holding(filtered_data, "Release Side over the Course of Outing", "RelSide")
    return fig

@app.callback(
    Output('graphIVBHold', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def seqIVBHold(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = holding(filtered_data, "Induced Vertical Break over the Course of Outing", "InducedVertBreak")
    return fig

@app.callback(
    Output('graphHBHold', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def seqHBHold(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = holding(filtered_data, "Horizontal Break over the Course of Outing", "HorzBreak")
    return fig

@app.callback(
    Output('graphSpinRateHold', 'figure'),
    [Input(component_id='igp_General_dropdown', component_property='value'),
     Input(component_id='igp_GeneralDate_dropdown', component_property='value'),
     Input(component_id='igp_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatter_dropdown', component_property='value'),
     Input(component_id='igp_GeneralBatterSide_dropdown', component_property='value'),
     Input(component_id='igp_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igp_GeneralOpponent_dropdown', component_property='value')]
)

def seqSpinRateHold(value,value2,value3,value4,value5,value6,value7):
    filtered_data = pitchingFilters(pitcherData, value, value2, value3, value4, value5, value6, value7)
    fig = holding(filtered_data, "Spin Rate over the Course of Outing", "SpinRate")
    return fig


#################################### IGH Approach and Self-Scout Charts ################################################
@app.callback(
    Output('graphHitPie', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'), ]
)

def pitchHitUsagePie(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterData,value,value2,value3,value4,value5,value6,value7)
    fig = pitchPie(filtered_data)
    return fig


@app.callback(
    Output('graphHitBar', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def pitchSeqUsageBar(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterData,value,value2,value3,value4,value5,value6,value7)
    fig = pitchBar(filtered_data)
    return fig

@app.callback(
    Output('graphHitResultBar', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def pitchSeqResultBar(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterData,value,value2,value3,value4,value5,value6,value7)
    fig = resultBar(filtered_data)
    return fig


################################################# NEW STUFF ##############################################################


@app.callback(
    Output('graphHitEvenPie', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def pitchHitUsageEvenPie(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterEven,value,value2,value3,value4,value5,value6,value7)
    fig = hitterPie(filtered_data, 'Even')
    return fig

@app.callback(
    Output('graphHitEvenBar', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def pitchSeqUsageEvenBar(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterEven, value, value2, value3, value4, value5, value6, value7)
    fig = hitterBar(filtered_data, 'Even')
    return fig

@app.callback(
    Output('graphBIPEven', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def ballInPlayEven(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterEven, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "Pitches Seen in Even Counts")
    return fig

@app.callback(
    Output('graphHitAheadPie', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def pitchHitUsageAheadPie(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterAhead,value,value2,value3,value4,value5,value6,value7)
    fig = hitterPie(filtered_data, 'Plus')
    return fig

@app.callback(
    Output('graphHitAheadBar', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def pitchSeqUsageAheadBar(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterAhead, value, value2, value3, value4, value5, value6, value7)
    fig = hitterBar(filtered_data, 'Plus')
    return fig

@app.callback(
    Output('graphBIPAhead', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def ballInPlayAhead(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterAhead, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "Pitches Seen in Plus Counts")
    return fig


@app.callback(
    Output('graphHitBehindPie', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),])

def pitchHitUsageBehindPie(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterBehind,value,value2,value3,value4,value5,value6,value7)
    fig = hitterPie(filtered_data, 'Minus')
    return fig

@app.callback(
    Output('graphHitBehindBar', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def pitchSeqUsageBehindBar(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterBehind,value,value2,value3,value4,value5,value6,value7)
    fig = hitterBar(filtered_data, 'Minus')
    return fig

@app.callback(
    Output('graphBIPBehind', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def ballInPlayBehind(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batterBehind, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "Pitches Seen in Minus Counts")
    return fig

@app.callback(
    Output('graphHit2KPie', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),])

def pitchHitUsage2KPie(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batter2K,value,value2,value3,value4,value5,value6,value7)
    fig = hitterPie(filtered_data, '2K')
    return fig

@app.callback(
    Output('graphHit2KBar', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),])

def pitchSeqUsage2KBar(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batter2K,value,value2,value3,value4,value5,value6,value7)
    fig = hitterBar(filtered_data, '2K')
    return fig

@app.callback(
    Output('graphBIP2K', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def ballInPlay2K(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batter2K, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "Pitches Seen in 2K Counts")
    return fig

@app.callback(
    Output('graphHit00Pie', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),])

def pitchHitUsage00Pie(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batter00,value,value2,value3,value4,value5,value6,value7)
    fig = hitterPie(filtered_data, 'First Pitch')
    return fig

@app.callback(
    Output('graphHit00Bar', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),])

def pitchSeqUsage00Bar(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batter00,value,value2,value3,value4,value5,value6,value7)
    fig = hitterBar(filtered_data, 'First Pitch')
    return fig

@app.callback(
    Output('graphBIP00', 'figure'),
    [Input(component_id='igh_General_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPT_dropdown', component_property='value'),
     Input(component_id='igh_GeneralOpponent_dropdown', component_property='value'),
     Input(component_id='igh_GeneralPitcher_dropdown', component_property='value'),
     Input(component_id='igh_GeneralCount_dropdown', component_property='value'),
     Input(component_id='igh_GeneralYear_dropdown', component_property='value'),
     Input(component_id='igh_GeneralDate_dropdown', component_property='value'),]
)

def ballInPlay00(value,value2,value3,value4,value5,value6,value7):
    filtered_data = hittingFilters(batter00, value, value2, value3, value4, value5, value6, value7)
    fig = pitchTypeLocations(filtered_data, "Pitches Seen First Pitch")
    return fig

if __name__ == '__main__':
    app.run_server(debug = True)

# set applicaiton title
app.title = 'Virignia Baseball'

