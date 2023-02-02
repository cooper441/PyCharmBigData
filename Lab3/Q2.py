import numpy.random as nr


def sim_poisson(nums, mean=600):
    for n in nums:
        dist = nr.poisson(lam=mean, size=n)
        titl = 'Poisson distribution with ' + str(n) + ' values'
        print(dist_summary(dist, titl))
        print('Emperical 95% CIs')
        print(np.percentile(dist, [2.5, 97.5]))
        print(' ')
    return
