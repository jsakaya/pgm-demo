from dash import dcc, html
from utils.helpers import create_dummy_plot

def create_layout():
    return html.Div(
        style={'backgroundColor': '#f0f3f6', 'padding': '30px', 'minHeight': '100vh'},
        children=[
            html.H1("📊 Model Dashboard", 
                    style={'textAlign': 'center', 'fontWeight': '600', 'fontSize': '28px', 'color': '#34495e', 'marginBottom': '30px'}),

            html.Div(
                style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'marginBottom': '30px'},
                children=[
                    html.Label("Select Model", style={'fontWeight': '500', 'marginRight': '15px', 'color': '#34495e'}),
                    dcc.Dropdown(
                        id="model-dropdown",
                        options=[
                            {'label': 'MMM', 'value': 'MMM'},
                            {'label': 'Healthcare', 'value': 'Healthcare'},
                            {'label': 'Finance', 'value': 'Finance'}
                        ],
                        value='Healthcare',
                        clearable=False,
                        style={'width': '220px', 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0, 0, 0, 0.1)'}
                    ),
                ]
            ),

            html.Div(
                style={'backgroundColor': '#ffffff', 'borderRadius': '12px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '30px'},
                children=[
                    dcc.Tabs(id="tabs-analysis", value='Scoring', children=[
                        dcc.Tab(label='Model', value='Model'),
                        dcc.Tab(label='Learning', value='Learning'),
                        dcc.Tab(label='Relationship', value='Relationships'),
                        dcc.Tab(label='Conditioning', value='Conditioning'),
                        dcc.Tab(label='Scoring', value='Scoring'),
                        dcc.Tab(label='Prediction', value='Prediction'),
                        dcc.Tab(label='Optimization', value='Optimization'),
                    ], style={'fontFamily': 'Poppins', 'fontWeight': '400', 'fontSize': '14px'},
                    colors={
                        "border": "#e0e0e0",
                        "primary": "#3498db",
                        "background": "#ffffff"
                    })
                ]
            ),

            html.Div(
                style={'display': 'flex', 'justifyContent': 'center', 'flexWrap': 'wrap'},
                children=[
                    html.Div(
                        style={'width': '80%', 'minWidth': '300px', 'padding': '20px', 'backgroundColor': '#ffffff', 'borderRadius': '12px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'},
                        children=[
                            html.H3("Performance Over Time", style={'fontFamily': 'Poppins', 'fontSize': '18px', 'fontWeight': '500', 'color': '#34495e', 'marginBottom': '15px'}),
                            dcc.Graph(id='main-graph', figure=create_dummy_plot(), config={'displayModeBar': False}),
                        ]
                    ),
                ]
            ),

            html.Footer("© 2024 Your Company Name", 
                        style={'textAlign': 'center', 'padding': '20px', 'fontFamily': 'Poppins', 'fontSize': '14px', 'color': '#7f8c8d', 'marginTop': '30px'})
        ]
    )