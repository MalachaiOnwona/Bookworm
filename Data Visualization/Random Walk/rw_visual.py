import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    rw = RandomWalk(45000)
    rw.fill_walk()

    plt.style.use('dark_background')
    figure, ax = plt.subplots(figsize= (13,7.5))
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap= plt.cm.Blues, edgecolors= 'none', s=1)
    ax.set_aspect('equal')
    #Emphasize the first and last points
    ax.scatter(0,0, c= 'green', edgecolors= 'none', s= 100) #first point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c= 'red', edgecolors= 'none', s= 100) #last point

    #Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make Another Walk? (y/n): ')

    if keep_running == 'n':
        break