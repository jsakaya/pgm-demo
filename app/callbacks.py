from dash.dependencies import Input, Output
import numpy as np
from utils.helpers import create_dummy_plot, create_posterior_plot, run_mcmc
from app.models import mmm_model, healthcare_model, finance_model

def register_callbacks(app):
    @app.callback(
        Output('main-graph', 'figure'),
        [Input('tabs-analysis', 'value'),
         Input('model-dropdown', 'value')]
    )
    def update_graph(selected_tab, selected_model):
        if selected_tab == 'Learning':
            # Generate dummy data for MCMC
            X = np.random.randn(100, 3)
            y = 2 + 0.5 * X[:, 0] + 0.3 * X[:, 1] + 0.1 * X[:, 2] + np.random.randn(100) * 0.1

            # Select the appropriate model based on the dropdown
            if selected_model == 'MMM':
                model = mmm_model
            elif selected_model == 'Healthcare':
                model = healthcare_model
            else:
                model = finance_model

            # Run MCMC
            samples = run_mcmc(model, X, y)

            # Create and return the posterior plot
            return create_posterior_plot(samples)
        else:
            # Return the dummy plot for other tabs
            return create_dummy_plot()