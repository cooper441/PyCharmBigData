import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as nr
import numpy as np


def sim_normal(nums, mean=600, sd=30):
    for n in nums:
        dist = nr.normal(loc=mean, scale=sd, size=n)
        titl = "Normal distribution with " + str(n) + "values"
        print("Summary for " + str(n) + " samples")
        print(dist_summary(dist, titl))
        print("Emperical 95% CIs")
        print(np.percentile(dist, [2.5, 97.5]))
        print(" ")
    return


def dist_summary(dist, names="dist_name"):
    ser = pd.Series(dist)
    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.gca()  # get current axes
    ser.hist(ax=ax, bins=120)
    ax.set_title("Frequency distribution of " + names)
    ax.set_ylabel("Frequency")
    plt.show()
    return ser.describe()


# nums = [100, 1000, 10000, 100000]
# sim_normal(nums)


def sim_poisson(nums, mean=600):
    for n in nums:
        dist = nr.poisson(lam=mean, size=n)
        titl = 'Poisson distribution with ' + str(n) + ' values'
        print(dist_summary(dist, titl))
        print('Emperical 95% CIs')
        print(np.percentile(dist, [2.5, 97.5]))
        print(' ')
    return


# nums2 = [100000, 1000000]
# sim_poisson(nums2)

# distribution of profits
def gen_profits(num):
    unif = nr.uniform(size=num)  # use uniform random numbers
    out = [5 if x < 0.3 else (3.5 if x < 0.6 else 4) for x in unif]
    # encode the function defined with probabilities
    return out


# distribution of tips
def gen_tips(num):
    unif = nr.uniform(size=num)
    out = [0 if x < 0.5 else (0.25 if x < 0.7 else (1.0 if x < 0.9 else 2.0)) for x in unif]
    return out


# num3 = [100000]
# out = gen_profits(num3)
# dist_summary(out)
#
# out2 = gen_tips(num3)
# dist_summary(out2)

def sim_lemonade(num, mean=600, sd=30, pois=False):
    """Simulate the daily income for a lemonade stand.
     num: The number of simulations to run.
     mean: The mean number of visitors per day.
     sd: The standard deviation of the number of visitors per day
     pois: If `true` use the poisson distribution to model the
     number of visitors per day, otherwise use the normal
     distribution.
     """
    ## number of customer arrivals
    if pois:
        arrivals = nr.poisson(lam=mean, size=num)
    else:
        arrivals = nr.normal(loc=mean, scale=sd, size=num)

    print(dist_summary(arrivals, 'customer arrivals per day'))

    ## Compute distibution of average profit per arrival
    proft = gen_profits(num)
    print(dist_summary(proft, 'profit per arrival'))

    ## Total profits are profit per arrival
    ## times number of arrivals.
    total_profit = arrivals * proft
    print(dist_summary(total_profit, 'total profit per day'))

    ## Compute distribution of average tips per arrival
    tps = gen_tips(num)
    print(dist_summary(tps, 'tips per arrival'))

    ## Compute average tips per day
    total_tips = arrivals * tps
    print(dist_summary(total_tips, 'total tips per day'))

    ## Compute total profits plus total tips.
    total_take = total_profit + total_tips

    ##compute P(total_take < 3000)
    values = np.array(total_take)
    xvalue = values[values < 3000]
    print('Probability of profit less than 3000 is ', xvalue.size / values.size)
    return dist_summary(total_take, 'total net per day')


sim_lemonade(100000, 1200, 20)