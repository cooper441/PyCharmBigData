import random as nr
import matplotlib.pyplot as plt

def sim_randomWalk(num):
    value = [0]
    for i in range(1, num+1):
        choice = nr.uniform(0,1)
        if choice> 0.5:
            value.append(value[i-1]+1)
        else:
            value.append(value[i-1]-1)
    #plot
    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.gca()
    plt.plot(value)
    ax.set_title('Simple Random Walk with ' + str(num) + ' steps')
    ax.set_ylabel('Position')
    ax.set_xlabel('steps')
    plt.show()
    return 'Done!'
sim_randomWalk(1000)

