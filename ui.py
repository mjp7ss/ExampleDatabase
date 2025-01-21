from dash import html
from dash import dcc


def create_layout():
    return html.Div(
        children=[
            # First Div: Header with background image
            html.Div(
                html.H1("Example Baseball Dashboard",
                style={
                    'textAlign': 'center'
                    # 'backgroundImage': 'url("/assets/14BC0E6D-0B11-4343-810D-FF00A34A13BF.jpeg")',
                    # 'backgroundSize': 'cover',  # Ensure the image covers the entire div
                    # 'backgroundPosition': 'center',  # Center the image in the div
                    # 'height': '300px',  # Adjust the height as needed
                    # 'display': 'flex',
                    # 'justifyContent': 'center',  # Center content horizontally
                    # 'alignItems': 'center',  # Center content vertically
                })
            ),

            # Second Div: Tabs for navigation
            html.Div(
                children=[
                    dcc.Tabs(
                        id='tabs',
                        value='Hitters',
                        children=[
                            dcc.Tab(
                                label='Hitting',
                                value='Hitters',
                                style={
                                    'background-color': '#f9f9f9',
                                    'border-radius': '8px',
                                    'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)',
                                    'padding': '10px 20px',
                                    'font-weight': '600',
                                    'color': '#333',
                                    'display': 'flex',  # Use flexbox to center the label
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                },
                                selected_style={
                                    'background-color': '#E0E0E0',  # Change color when selected
                                    'border-radius': '8px',
                                    'font-weight': '700',
                                    'color': '#333',
                                    'display': 'flex',
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                }
                            ),
                            dcc.Tab(
                                label='Pitching',
                                value='Pitchers',
                                style={
                                    'background-color': '#f9f9f9',
                                    'border-radius': '8px',
                                    'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)',
                                    'padding': '10px 20px',
                                    'font-weight': '600',
                                    'color': '#333',
                                    'display': 'flex',  # Use flexbox to center the label
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                },
                                selected_style={
                                    'background-color': '#E0E0E0',
                                    'border-radius': '8px',
                                    'font-weight': '700',
                                    'color': '#333',
                                    'display': 'flex',
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                }
                            ),
                            dcc.Tab(
                                label='Catching',
                                value='Catchers',
                                style={
                                    'background-color': '#f9f9f9',
                                    'border-radius': '8px',
                                    'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)',
                                    'padding': '10px 20px',
                                    'font-weight': '600',
                                    'color': '#333',
                                    'display': 'flex',  # Use flexbox to center the label
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                },
                                selected_style={
                                    'background-color': '#E0E0E0',
                                    'border-radius': '8px',
                                    'font-weight': '700',
                                    'color': '#333',
                                    'display': 'flex',
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                }
                            ),
                            dcc.Tab(
                                label='Player/Outing Comparison',
                                value='Comp',
                                style={
                                    'background-color': '#f9f9f9',
                                    'border-radius': '8px',
                                    'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)',
                                    'padding': '10px 20px',
                                    'font-weight': '600',
                                    'color': '#333',
                                    'display': 'flex',  # Use flexbox to center the label
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                },
                                selected_style={
                                    'background-color': '#E0E0E0',
                                    'border-radius': '8px',
                                    'font-weight': '700',
                                    'color': '#333',
                                    'display': 'flex',
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                }
                            ),
                            dcc.Tab(
                                label='Data Upload',
                                value='Data',
                                style={
                                    'background-color': '#f9f9f9',
                                    'border-radius': '8px',
                                    'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)',
                                    'padding': '10px 20px',
                                    'font-weight': '600',
                                    'color': '#333',
                                    'display': 'flex',  # Use flexbox to center the label
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                },
                                selected_style={
                                    'background-color': '#E0E0E0',
                                    'border-radius': '8px',
                                    'font-weight': '700',
                                    'color': '#333',
                                    'display': 'flex',
                                    'align-items': 'center',  # Vertically center
                                    'justify-content': 'center',  # Horizontally center
                                    'height': '50px',  # Optional: Adjust height if necessary
                                }
                            )
                        ],
                        style={'width': '100%', 'margin-bottom': '20px'}  # Style for the tabs container
                    ),
                    html.Div(id='tabs-content')
                ]
            )
        ]
    )


def create_hitters_content():
    # Define the six dropdown filters for 'Hitters' tab
    dropdown_filters = html.Div([
        html.Label("Hitter", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='hitter-hitter-filter',
            options=[{'label': 'All Hitters', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Name",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Opponent", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='hitter-opponent-filter',
            options=[{'label': 'All Opponents', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Opponent",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Pitcher", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='hitter-pitcher-filter',
            options=[{'label': 'All Pitchers', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Pitcher",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Pitcher Hand", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='hitter-pitcher-hand-filter',
            options=[{'label': 'All Pitcher Hands', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Pitcher Hand",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Count Type", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='hitter-count-type-filter',
            options=[{'label': 'All Counts', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Count Type",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),
    ], style={
        'width': '100%',
        'padding': '5px',
        'box-sizing': 'border-box',
        'background-color': '#f9f9f9',
        'border-radius': '8px',
        'box-shadow': '0 4px 10px rgba(0, 0, 0, 0.1)',
        'height': '100%',
        'position': 'sticky',
        'top': '20px',
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'space-between',
    })

    # Define the content on the right for Hitters tab
    content = html.Div([
        html.H3("Content for Hitting", style={'color': '#333', 'padding': '20px', 'font-size': '22px'}),

        # Dropdown for selecting category
        dcc.Dropdown(
            id='hitter-category-dropdown',  # Unique ID for the dropdown
            options=[
                {'label': 'Balls/Strikes', 'value': 1},
                {'label': 'Pitch Type', 'value': 2},
                {'label': 'Play Result', 'value': 3},
                {'label': 'Contact Type', 'value': 4}
            ],
            value=2,  # Default value
            style={
                'width': '100%',
                'height': '40px',  # Height of the dropdown
                'margin-bottom': '20px',
                'border-radius': '5px',
                'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)',  # Adds a subtle shadow
                'background-color': '#f9f9f9',
                'padding': '0px 10px',  # Padding inside the dropdown
            }
        ),
        html.Div(dcc.Graph(id='hitter-locations'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),
        html.Div(dcc.Graph(id='hitter-spray-chart'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),
        html.Div(dcc.Graph(id='hitter-pitch-pie'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),
        html.Div(dcc.Graph(id='hitter-pitch-bar'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),
    ], style={
        'width': '100%',
        'padding': '5px',
        'box-sizing': 'border-box',
        'background-color': '#fff',
        'border-radius': '8px',
        'box-shadow': '0 4px 10px rgba(0, 0, 0, 0.1)',
        'height': '100%'
    })

    # Use Flexbox to position filters and content side by side
    return html.Div([
        html.Div(dropdown_filters, style={'flex': '0 0 30%', 'margin-right': '5px'}),
        html.Div(content, style={'flex': '1'})
    ], style={
        'display': 'flex',
        'flexDirection': 'row',
        'justifyContent': 'space-between',
        'gap': '1px',
        'width': '100%',
        'align-items': 'flex-start',
    })


def create_pitchers_content():
    # Define the six dropdown filters for 'Hitters' tab
    dropdown_filters = html.Div([
        html.Label("Pitcher", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='pitcher-pitcher-filter',
            options=[{'label': 'All Pitchers', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Name",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Opponent", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='pitcher-opponent-filter',
            options=[{'label': 'All Opponents', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Opponent",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Hitter", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='pitcher-hitter-filter',
            options=[{'label': 'All Hitters', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Hitter",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Batter Hand", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='pitcher-hitter-hand-filter',
            options=[{'label': 'All Hitter Hands', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Hitter Hand",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Count Type", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='pitcher-count-type-filter',
            options=[{'label': 'All Counts', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Count Type",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),
    ], style={
        'width': '100%',
        'padding': '5px',
        'box-sizing': 'border-box',
        'background-color': '#f9f9f9',
        'border-radius': '8px',
        'box-shadow': '0 4px 10px rgba(0, 0, 0, 0.1)',
        'height': '100%',
        'position': 'sticky',
        'top': '20px',
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'space-between',
    })

    # Define the content on the right for Hitters tab
    content = html.Div([
        html.H3("Content for Pitching", style={'color': '#333', 'padding': '20px', 'font-size': '22px'}),
        html.Div(dcc.Graph(id='pitcher-movement'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),
        html.Div(dcc.Graph(id='pitcher-release-angle'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),
        dcc.Dropdown(
            id='pitcher-rateeff-dropdown',  # Unique ID for the dropdown
            options=[
                {'label': 'Spin Rate', 'value': 1},
                {'label': 'Spin Efficiency', 'value': 2}
            ],
            value=1,  # Default value
            style={
                'width': '100%',
                'height': '40px',  # Height of the dropdown
                'margin-bottom': '20px',
                'border-radius': '5px',
                'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)',  # Adds a subtle shadow
                'background-color': '#f9f9f9',
                'padding': '0px 10px',  # Padding inside the dropdown
            }
        ),
        html.Div(dcc.Graph(id='pitcher-spin'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),
        dcc.Dropdown(
            id='pitcher-release-view-dropdown',  # Unique ID for the dropdown
            options=[
                {'label': 'Back View', 'value': 1},
                {'label': 'Top View', 'value': 2},
                {'label': 'Side View', 'value': 3},
                {'label': '3D', 'value': 4}
            ],
            value=1,  # Default value
            style={
                'width': '100%',
                'height': '40px',  # Height of the dropdown
                'margin-bottom': '20px',
                'border-radius': '5px',
                'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)',  # Adds a subtle shadow
                'background-color': '#f9f9f9',
                'padding': '0px 10px',  # Padding inside the dropdown
            }
        ),

        html.Div(dcc.Graph(id='pitcher-release'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),

        dcc.Dropdown(
            id='pitcher-category-dropdown',  # Unique ID for the dropdown
            options=[
                {'label': 'Balls/Strikes', 'value': 1},
                {'label': 'Pitch Type', 'value': 2},
                {'label': 'Play Result', 'value': 3},
                {'label': 'Contact Type', 'value': 4}
            ],
            value=2,  # Default value
            style={
                'width': '100%',
                'height': '40px',  # Height of the dropdown
                'margin-bottom': '20px',
                'border-radius': '5px',
                'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)',  # Adds a subtle shadow
                'background-color': '#f9f9f9',
                'padding': '0px 10px',  # Padding inside the dropdown
            }
        ),

        html.Div(dcc.Graph(id='pitcher-locations'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),

        html.Div(dcc.Graph(id='pitcher-spray-chart'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),

        html.Div(dcc.Graph(id='pitcher-usage-pie'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),

        html.Div(dcc.Graph(id='pitcher-usage-bar'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        }),


    ], style={
        'width': '100%',
        'padding': '0px',
        'box-sizing': 'border-box',
        'background-color': '#fff',
        'border-radius': '8px',
        'box-shadow': '0 4px 10px rgba(0, 0, 0, 0.1)',
        'height': '100%'
    })

    # Use Flexbox to position filters and content side by side
    return html.Div([
        html.Div(dropdown_filters, style={'flex': '0 0 30%', 'margin-right': '10px'}),
        html.Div(content, style={'flex': '1'})
    ], style={
        'display': 'flex',
        'flexDirection': 'row',
        'justifyContent': 'space-between',
        'gap': '1px',
        'width': '100%',
        'align-items': 'flex-start',
    })


def create_catchers_content():
    # Define the six dropdown filters for 'Hitters' tab
    dropdown_filters = html.Div([
        html.Label("Catcher", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='catcher-catcher-filter',
            options=[{'label': 'All Catchers', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Name",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Pitcher Hand", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='catcher-pitcher-hand-filter',
            options=[{'label': 'All Pitcher Hands', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Pitcher Hand",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Batter Hand", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='catcher-hitter-hand-filter',
            options=[{'label': 'All Hitter Hands', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Hitter Hand",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px',
                   'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Umpire", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='catcher-umpire-filter',
            options=[{'label': 'All Umpires', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Umpire",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px',
                   'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),

        html.Label("Count Type", style={'font-size': '14px', 'font-weight': '600', 'margin-bottom': '5px'}),
        dcc.Dropdown(
            id='catcher-count-type-filter',
            options=[{'label': 'All Counts', 'value': 'All'}],  # Replace with your options
            value="All",
            placeholder="Select Count Type",
            style={'width': '100%', 'margin-bottom': '15px', 'border-radius': '5px', 'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.1)', 'height': '40px'}
        ),
    ], style={
        'width': '100%',
        'padding': '5px',
        'box-sizing': 'border-box',
        'background-color': '#f9f9f9',
        'border-radius': '8px',
        'box-shadow': '0 4px 10px rgba(0, 0, 0, 0.1)',
        'height': '100%',
        'position': 'sticky',
        'top': '20px',
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'space-between',
    })

    content = html.Div([
        html.H3("Content for Catching", style={'color': '#333', 'padding': '20px', 'font-size': '22px'}),
        html.Div(dcc.Graph(id='catcher-locations'), style={
            'display': 'flex',  # Enable flexbox for the graph container
            'justifyContent': 'center',  # Center the graph horizontally
            'alignItems': 'center',  # Optionally center the graph vertically (if needed)
            'width': '100%'  # Ensure the graph container uses full width
        })
    ], style={
        'width': '100%',
        'padding': '0px',
        'box-sizing': 'border-box',
        'background-color': '#fff',
        'border-radius': '8px',
        'box-shadow': '0 4px 10px rgba(0, 0, 0, 0.1)',
        'height': '100%'  # Ensure the content div takes full height
    })

    # Use Flexbox to position filters and content side by side
    return html.Div([
        html.Div(dropdown_filters, style={'flex': '0 0 30%', 'margin-right': '10px'}),
        html.Div(content, style={'flex': '1'})
    ], style={
        'display': 'flex',
        'flexDirection': 'row',
        'justifyContent': 'space-between',
        'gap': '1px',
        'width': '100%',
        'align-items': 'flex-start',
    })


def create_upload_content():
   upload =  html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-data-upload'),
    ])
   return html.Div([html.Div(upload)])


