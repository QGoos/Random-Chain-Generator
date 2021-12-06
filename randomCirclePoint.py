from random import random,choice
from matplotlib import pyplot as plt


def circle_points(n):
    '''construct a list of n points [x,y] within a full circle centered at 0'''
    picks = [-1,1]
    result = [None]*n

    for i in range(n):
        #choose a point in 1/4 circle then place it in a random quadrant
        result[i] = quarter_circle_points(1)[0]
        result[i] = [choice(picks)*result[i][0],choice(picks)*result[i][1]]

    return result

def quarter_circle_points(n):
    '''return a list of n points [x,y] within a 1/4 circle from 0'''
    result = [None]*n

    for i in range(n):
        result[i] = find_inside()

    return result

def find_inside():
    '''Construct a point within 1/4 of a circle'''
    x = random()
    y = random()
    point = (x,y)

    if x**2 + y**2 > 1:
        point = find_inside()

    return point

def plot_points(points):
    '''Plot a list of points of [x,y]'''
    plt.scatter([p[0] for p in points],[p[1] for p in points])
    plt.show()

def main():
    num = 10
    randoms = circle_points(num)
    #randoms = quarter_circle_points(num)
    print(randoms)

    plot_points(randoms)


if __name__ == "__main__":
    main()
