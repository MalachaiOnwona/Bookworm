import matplotlib.pyplot as plt
plt.style.available

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('dark_background')
figure, ax = plt.subplots()

ax.scatter(x_values, y_values, s= 10, c= y_values, cmap= plt.cm.Blues,) #the scatter() method places points on a graph
ax.set_title('Squares of Numbers', fontsize= 24)
ax.set_xlabel('Number', fontsize= 14)
ax.set_ylabel('Square of Number', fontsize= 14)
ax.tick_params(labelsize= 14)

"""use: ax.ticklabel_format(style= 'plain') if you don't want the tick labels in scientific notation""" 

ax.axis([0, 1100, 0, 1_100_000]) #sets the range for the x and y axis, respectively

plt.show()
plt.savefig('squares_plot.png', bbox_inches= 'tight')