import numpyro
import numpyro.distributions as dist

def mmm_model(X, y):
    b0 = numpyro.sample("intercept", dist.Normal(0, 10))
    b1 = numpyro.sample("tv", dist.Normal(0, 5))
    b2 = numpyro.sample("radio", dist.Normal(0, 5))
    b3 = numpyro.sample("newspaper", dist.Normal(0, 5))
    sigma = numpyro.sample("sigma", dist.HalfNormal(5))
    mu = b0 + b1 * X[:, 0] + b2 * X[:, 1] + b3 * X[:, 2]
    numpyro.sample("y", dist.Normal(mu, sigma), obs=y)

def healthcare_model(X, y):
    b0 = numpyro.sample("intercept", dist.Normal(0, 10))
    b1 = numpyro.sample("age", dist.Normal(0, 5))
    b2 = numpyro.sample("bmi", dist.Normal(0, 5))
    sigma = numpyro.sample("sigma", dist.HalfNormal(5))
    mu = b0 + b1 * X[:, 0] + b2 * X[:, 1]
    numpyro.sample("y", dist.Normal(mu, sigma), obs=y)

def finance_model(X, y):
    b0 = numpyro.sample("intercept", dist.Normal(0, 10))
    b1 = numpyro.sample("income", dist.Normal(0, 5))
    b2 = numpyro.sample("credit_score", dist.Normal(0, 5))
    sigma = numpyro.sample("sigma", dist.HalfNormal(5))
    mu = b0 + b1 * X[:, 0] + b2 * X[:, 1]
    numpyro.sample("y", dist.Normal(mu, sigma), obs=y)