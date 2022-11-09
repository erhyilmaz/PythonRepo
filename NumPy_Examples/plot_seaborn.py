import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

if 0:
    print(np.__version__)

    sns.displot([0, 1, 2, 3, 4, 5])
    # sns.histplot([0, 1, 2, 3, 4, 5])
    plt.show()

    ######################################################################
    # Difference Between Normal and Binomial Distribution
    # The main difference is that normal distribution is continuous
    # whereas binomial is discrete, but if there are enough data points it will be quite similar
    # to normal distribution with certain loc and scale.

    ##############################################
    # normal distribution
    x = random.normal(size=(2, 3))
    print(x)

    # Normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
    x = random.normal(loc=1, scale=2, size=(2, 3))
    print(x)

    # Visualize Normal distribution
    sns.displot(random.normal(size=1000), kind='kde')
    plt.show()

    ##############################################
    # Binomial Distribution
    x = random.binomial(n=10, p=0.5, size=1000)
    # print(x)
    sns.displot(x, kind='hist')
    plt.show()

    ##############################################
    sns.displot(random.normal(loc=50, scale=5, size=1000), kind='kde', label='normal')
    sns.displot(random.binomial(n=100, p=0.5, size=1000), kind='kde', label='binomial')
    plt.show()

    ##############################################
    # Poisson Distribution
    ##############################################
    x = random.poisson(lam=2, size=10)
    print(x)

    sns.displot(random.poisson(lam=2, size=1000), kind='hist')
    plt.show()

    # Difference Between Normal and Poisson Distribution
    sns.displot(random.normal(loc=50, scale=7, size=1000), kind='kde', label='normal')
    sns.displot(random.poisson(lam=50, size=1000), kind='kde', label='poisson')
    plt.show()

    ##############################################
    # Uniform Distribution
    ##############################################
    x = random.uniform(size=(2, 3))
    print(x)

    sns.displot(random.uniform(size=1000), kind='kde')
    plt.show()

    ##############################################
    # Logistic Distribution
    # - Logistic Distribution is used to describe growth.
    # - Used extensively in machine learning in logistic regression, neural networks etc.
    # It has three parameters:
    #  loc   - mean, where the peak is. Default 0.
    #  scale - standard deviation, the flatness of distribution. Default 1.
    #  size  - The shape of the returned array.
    ##############################################
    x = random.logistic(loc=1, scale=2, size=(2, 3))
    print(x)

    sns.displot(random.logistic(size=1000), kind='kde')
    plt.show()

    # Difference Between Logistic and Normal Distribution
    # Both distributions are near identical, but logistic distribution has more area under the tails,
    # meaning it represents more possibility of occurrence of an event further away from mean.
    sns.distplot(random.normal(scale=2, size=1000), kind='kde', label='normal')
    sns.distplot(random.logistic(size=1000), kind='kde', label='logistic')
    plt.show()

##############################################
# Exponential Distribution:
# Used for describing time till next event e.g. failure/success etc.
# It has two parameters:
#  scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
#  size - The shape of the returned array.
##############################################
x = random.exponential(scale=2, size=(2, 3))
print(x)

sns.displot(random.exponential(size=1000), kind='kde')
plt.show()

##############################################
# Rayleigh Distribution:
#   Used in signal processing.
# It has two parameters:
#    scale - (standard deviation) decides how flat the distribution will be default 1.0).
#    size - The shape of the returned array.
##############################################
x = random.rayleigh(scale=2, size=(2, 3))
print(x)

sns.displot(random.rayleigh(size=1000), kind='kde')
plt.show()






