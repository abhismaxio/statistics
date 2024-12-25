import numpy as np
from scipy.stats import binom, poisson,norm

n =10 #trial
p=0.5 #probab of sucess

# binomial distribution
binom_pmf = binom.pmf(5,n,p)
print("Binomial PMF (P(X=5)):",binom_pmf)

# poission distribution
lam =3 #avg rate
poisson_pmf = poisson.pmf(2,lam)
print("poission pmf(X==2)",poisson_pmf)

mu, sigma = 0, 1  # Mean=0, Std Dev=1
x = 1
normal_pdf = norm.pdf(x, mu, sigma)  # PDF at x=1
print(f"Normal PDF at X=1: {normal_pdf}")