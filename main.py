
import dash
from dash import dcc, html, Input, Output
import dash_table
import pandas as pd

from utils.mcmc_runner import run_mcmc
from utils.plots import create_dummy_plot, create_posterior_plot
from models.mmm_model import mmm_model
from models.healthcare_model import healthcare_model
from models.finance_model import finance_model

# Initialize Dash app
app = dash.Dash(__name__)

# Load sample data
df = pd.DataFrame({
    f"Metric {i+1}": pd.Series(range(10)) for i in range(5)
})

# Custom CSS
app.index_string = open('assets/custom.css').read()

# App layout
app.layout = html.Div([
    html.H1("📊 Model Dashboard", style={'textAlign': 'center'}),
    dcc.Dropdown(id="model-dropdown", ...),
    dcc.Tabs(id="tabs-analysis", ...),
    html.Div([
        dcc.Graph(id='main-graph', figure=create_dummy_plot()),
        dash_table.DataTable(id='datatable', ...)
    ]),
    html.Footer("© 2024 Your Company Name")
])

# Callback to update graph
@app.callback(
    Output('main-graph', 'figure'),
    [Input('tabs-analysis', 'value'), Input('model-dropdown', 'value')]
)
def update_graph(selected_tab, selected_model):
    if selected_tab == 'Learning':
        X, y = ...  # Import from dummy_data.py
        model = {'MMM': mmm_model, 'Healthcare': healthcare_model, 'Finance': finance_model}[selected_model]
        samples = run_mcmc(model, X, y)
        return create_posterior_plot(samples)
    else:
        return create_dummy_plot()

if __name__ == '__main__':
    app.run_server(debug=True)



# import dash
# from dash import dcc, html, Input, Output, State
# import dash_table
# import plotly.graph_objs as go
# import numpy as np
# import pandas as pd
# import numpyro
# import numpyro.distributions as dist
# from numpyro.infer import MCMC, NUTS
# import jax.random as random
# import jax.numpy as jnp

# # Create Dash app
# app = dash.Dash(__name__)

# # Sample data
# df = pd.DataFrame(np.random.randn(10, 5), columns=[f"Metric {i+1}" for i in range(5)])

# # Numpyro models
# def mmm_model(X, y):
#     b0 = numpyro.sample("intercept", dist.Normal(0, 10))
#     b1 = numpyro.sample("tv", dist.Normal(0, 5))
#     b2 = numpyro.sample("radio", dist.Normal(0, 5))
#     b3 = numpyro.sample("newspaper", dist.Normal(0, 5))
#     sigma = numpyro.sample("sigma", dist.HalfNormal(5))
#     mu = b0 + b1 * X[:, 0] + b2 * X[:, 1] + b3 * X[:, 2]
#     numpyro.sample("y", dist.Normal(mu, sigma), obs=y)

# def healthcare_model(X, y):
#     b0 = numpyro.sample("intercept", dist.Normal(0, 10))
#     b1 = numpyro.sample("age", dist.Normal(0, 5))
#     b2 = numpyro.sample("bmi", dist.Normal(0, 5))
#     sigma = numpyro.sample("sigma", dist.HalfNormal(5))
#     mu = b0 + b1 * X[:, 0] + b2 * X[:, 1]
#     numpyro.sample("y", dist.Normal(mu, sigma), obs=y)

# def finance_model(X, y):
#     b0 = numpyro.sample("intercept", dist.Normal(0, 10))
#     b1 = numpyro.sample("income", dist.Normal(0, 5))
#     b2 = numpyro.sample("credit_score", dist.Normal(0, 5))
#     sigma = numpyro.sample("sigma", dist.HalfNormal(5))
#     mu = b0 + b1 * X[:, 0] + b2 * X[:, 1]
#     numpyro.sample("y", dist.Normal(mu, sigma), obs=y)

# # Function to run MCMC
# def run_mcmc(model, X, y, num_samples=1000):
#     kernel = NUTS(model)
#     mcmc = MCMC(kernel, num_samples=num_samples, num_warmup=500)
#     mcmc.run(random.PRNGKey(0), X, y)
#     return mcmc.get_samples()

# # Create dummy plot
# def create_dummy_plot():
#     x = np.linspace(0, 10, 100)
#     y = np.sin(x)
#     fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', line=dict(color='#9b59b6', width=3)))

#     fig.update_layout(
#         title=None,
#         xaxis=dict(title=None, showgrid=False, zeroline=False),
#         yaxis=dict(title=None, showgrid=False, zeroline=False),
#         template="simple_white",
#         margin=dict(l=40, r=40, t=20, b=20),
#         font=dict(family="Poppins, sans-serif", size=12),
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)'
#     )
#     return fig

# # Create posterior plot
# def create_posterior_plot(samples):
#     fig = go.Figure()
#     for param, values in samples.items():
#         fig.add_trace(go.Histogram(x=values, name=param, opacity=0.7))

#     fig.update_layout(
#         title="Posterior Distributions",
#         xaxis_title="Parameter Value",
#         yaxis_title="Frequency",
#         barmode='overlay',
#         template="simple_white",
#         font=dict(family="Poppins, sans-serif", size=12),
#         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
#     )
#     return fig

# # Custom CSS for better styling
# custom_css = '''
#     body {
#         font-family: 'Poppins', sans-serif;
#         background-color: #f0f3f6;
#     }
#     .dash-table-container .dash-spreadsheet-container .dash-spreadsheet-inner td, 
#     .dash-table-container .dash-spreadsheet-container .dash-spreadsheet-inner th {
#         border: none !important;
#     }
# '''

# app.index_string = f'''
# <!DOCTYPE html>
# <html>
#     <head>
#         {{%metas%}}
#         <title>{{%title%}}</title>
#         {{%favicon%}}
#         {{%css%}}
#         <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
#         <style>
#             {custom_css}
#         </style>
#     </head>
#     <body>
#         {{%app_entry%}}
#         <footer>
#             {{%config%}}
#             {{%scripts%}}
#             {{%renderer%}}
#         </footer>
#     </body>
# </html>
# '''

# # App layout with pastel colors and improved styling
# app.layout = html.Div(
#     style={'backgroundColor': '#f0f3f6', 'padding': '30px', 'minHeight': '100vh'},
#     children=[
#         # Title
#         html.H1("📊 Model Dashboard", 
#                 style={'textAlign': 'center', 'fontWeight': '600', 'fontSize': '28px', 'color': '#34495e', 'marginBottom': '30px'}),

#         # Model controls section
#         html.Div(
#             style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'marginBottom': '30px'},
#             children=[
#                 html.Label("Select Model", style={'fontWeight': '500', 'marginRight': '15px', 'color': '#34495e'}),
#                 dcc.Dropdown(
#                     id="model-dropdown",
#                     options=[
#                         {'label': 'MMM', 'value': 'MMM'},
#                         {'label': 'Healthcare', 'value': 'Healthcare'},
#                         {'label': 'Finance', 'value': 'Finance'}
#                     ],
#                     value='Healthcare',
#                     clearable=False,
#                     style={'width': '220px', 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0, 0, 0, 0.1)'}
#                 ),
#             ]
#         ),

#         # Tabs for analysis types
#         html.Div(
#             style={'backgroundColor': '#ffffff', 'borderRadius': '12px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '30px'},
#             children=[
#                 dcc.Tabs(id="tabs-analysis", value='Scoring', children=[
#                     dcc.Tab(label='Model', value='Model'),
#                     dcc.Tab(label='Learning', value='Learning'),
#                     dcc.Tab(label='Relationship', value='Relationships'),
#                     dcc.Tab(label='Conditioning', value='Conditioning'),
#                     dcc.Tab(label='Scoring', value='Scoring'),
#                     dcc.Tab(label='Prediction', value='Prediction'),
#                     dcc.Tab(label='Optimization', value='Optimization'),
#                 ], style={'fontFamily': 'Poppins', 'fontWeight': '400', 'fontSize': '14px'},
#                 colors={
#                     "border": "#e0e0e0",
#                     "primary": "#3498db",
#                     "background": "#ffffff"
#                 })
#             ]
#         ),

#         # Main content (two columns: plot and key metrics)
#         html.Div(
#             style={'display': 'flex', 'justifyContent': 'space-between', 'flexWrap': 'wrap'},
#             children=[
#                 # Plot column
#                 html.Div(
#                     style={'width': '48%', 'minWidth': '300px', 'padding': '20px', 'backgroundColor': '#ffffff', 'borderRadius': '12px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'},
#                     children=[
#                         html.H3("Performance Over Time", style={'fontFamily': 'Poppins', 'fontSize': '18px', 'fontWeight': '500', 'color': '#34495e', 'marginBottom': '15px'}),
#                         dcc.Graph(id='main-graph', figure=create_dummy_plot(), config={'displayModeBar': False}),
#                     ]
#                 ),

#                 # Data table and metrics column
#                 html.Div(
#                     style={'width': '48%', 'minWidth': '300px', 'padding': '20px', 'backgroundColor': '#ffffff', 'borderRadius': '12px', 'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px'},
#                     children=[
#                         html.H3("Key Metrics", 
#                                 style={'fontFamily': 'Poppins', 'fontSize': '18px', 'fontWeight': '500', 'color': '#34495e', 'marginBottom': '15px'}),
#                         dash_table.DataTable(
#                             id='datatable',
#                             columns=[{'name': col, 'id': col} for col in df.columns],
#                             data=df.to_dict('records'),
#                             style_table={'overflowX': 'auto'},
#                             style_header={
#                                 'backgroundColor': '#f0f3f6',
#                                 'fontWeight': '500',
#                                 'color': '#34495e',
#                                 'borderBottom': '1px solid #e0e0e0',
#                                 'textAlign': 'left',
#                                 'padding': '12px'
#                             },
#                             style_cell={
#                                 'backgroundColor': '#ffffff',
#                                 'color': '#34495e',
#                                 'borderBottom': '1px solid #f0f3f6',
#                                 'textAlign': 'left',
#                                 'padding': '12px'
#                             },
#                             style_data_conditional=[
#                                 {
#                                     'if': {'row_index': 'odd'},
#                                     'backgroundColor': '#f8fafc',
#                                 },
#                                 {
#                                     'if': {
#                                         'filter_query': '{{Metric 1}} = {}'.format(df['Metric 1'].max()),
#                                         'column_id': 'Metric 1'
#                                     },
#                                     'backgroundColor': '#d5f5e3',
#                                     'color': '#27ae60'
#                                 }
#                             ]
#                         )
#                     ]
#                 )
#             ]
#         ),

#         # Footer
#         html.Footer("© 2024 Your Company Name", 
#                     style={'textAlign': 'center', 'padding': '20px', 'fontFamily': 'Poppins', 'fontSize': '14px', 'color': '#7f8c8d', 'marginTop': '30px'})
#     ]
# )

# # Callback to update the graph based on selected tab and model
# @app.callback(
#     Output('main-graph', 'figure'),
#     [Input('tabs-analysis', 'value'),
#      Input('model-dropdown', 'value')]
# )
# def update_graph(selected_tab, selected_model):
#     if selected_tab == 'Learning':
#         # Generate dummy data for MCMC
#         X = np.random.randn(100, 3)
#         y = 2 + 0.5 * X[:, 0] + 0.3 * X[:, 1] + 0.1 * X[:, 2] + np.random.randn(100) * 0.1

#         # Select the appropriate model based on the dropdown
#         if selected_model == 'MMM':
#             model = mmm_model
#         elif selected_model == 'Healthcare':
#             model = healthcare_model
#         else:
#             model = finance_model

#         # Run MCMC
#         samples = run_mcmc(model, X, y)

#         # Create and return the posterior plot
#         return create_posterior_plot(samples)
#     else:
#         # Return the dummy plot for other tabs
#         return create_dummy_plot()

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)