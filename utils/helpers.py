import numpy as np
import plotly.graph_objs as go
from numpyro.infer import MCMC, NUTS
import jax.random as random

def create_dummy_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', line=dict(color='#9b59b6', width=3)))

    fig.update_layout(
        title=None,
        xaxis=dict(title=None, showgrid=False, zeroline=False),
        yaxis=dict(title=None, showgrid=False, zeroline=False),
        template="simple_white",
        margin=dict(l=40, r=40, t=20, b=20),
        font=dict(family="Poppins, sans-serif", size=12),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def create_posterior_plot(samples):
    fig = go.Figure()
    for param, values in samples.items():
        fig.add_trace(go.Histogram(x=values, name=param, opacity=0.7))

    fig.update_layout(
        title="Posterior Distributions",
        xaxis_title="Parameter Value",
        yaxis_title="Frequency",
        barmode='overlay',
        template="simple_white",
        font=dict(family="Poppins, sans-serif", size=12),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def run_mcmc(model, X, y, num_samples=1000):
    kernel = NUTS(model)
    mcmc = MCMC(kernel, num_samples=num_samples, num_warmup=500)
    mcmc.run(random.PRNGKey(0), X, y)
    return mcmc.get_samples()