import randomCirclePoint as rc
from matplotlib import pyplot as plt
from math import sqrt


def gen_chain_spiral(n):
    '''Produce a chain of length n from a series of points generated in a circle with a final length n'''

    #extension of point size with later pruning to reduce occurrence large jumps in chain ending
    points = rc.circle_points(n + min(int(n/10), 100))

    #pruning of chain end
    return gen_chain(points,n)[0:n]

def gen_chain_cone(n):
    '''Produce a chain of length n from a series of points generated in a 1/4 circle cone'''

    #extension of point size with later pruning to reduce occurrence large jumps in chain ending
    points = rc.quarter_circle_points(n + min(int(n/10), 100))

    #pruning of chain end
    return gen_chain(points,n)[0:n]

def gen_chain(points,n):
    '''generate a chain given a list of points in the form of [[x1,y1],[x2,y2], ... , [xn,yn]]'''

    origin = [0,0]
    order = [origin]

    #get the order that points connect in
    l = len(points)
    for i in range(l):
        order.append(nearest(order[-1],points))
        points.remove(order[-1])
    
    return order

def nearest(point, neighbors):
    '''Find the nearest neighbor to a given point

    point: in the form of [x,y]
    
    neighbors: in the form of [[x1,y1],[x2,y2], ... , [xn,yn]]
    are the surrounding data points which the nearest point is
    chosen from
    '''

    leader = neighbors[-1]
    diff = distance(point,leader)

    # from a default 'guess' check each other point and take each shorter ones
    for p in neighbors:
        curr_diff = distance(point,p)
        if curr_diff < diff:
            diff = curr_diff
            leader = p


    return leader

def distance(a,b):
    '''find the distance between point a and point b'''
    return sqrt((a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2)


def draw_chain(points):
    '''draw a chain along a set of given points of the form 
    points = [[x1,y1],[x2,y2], ... , [xn,yn]]
    final chain has a red point at the start, and a blue point at the end'''

    for i in range(len(points)-1):
        add_link(points[i],points[i+1])

    plt.plot(points[0][0],points[0][1],'ro')
    plt.plot(points[-1][0],points[-1][1],'ro',color="blue")

    plt.show()

def add_link(a,b):
    '''Given a starting point a, and ending point b, of the form
    a = [x1,y1], b=[x2,y2]
    add a link of the chain to the plot between the two points'''
    plt.plot([a[0],b[0]],[a[1],b[1]],color="black")

def main():
    chainLength = 250
    
    #print(test)
    #draw_chain(gen_chain_cone(chainLength))
    draw_chain(gen_chain_spiral(chainLength))


if __name__ == "__main__":
    main()


