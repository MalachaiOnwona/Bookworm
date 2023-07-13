import matplotlib.pyplot as plt
plt.style.available

input = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.style.use('dark_background')
figure, ax = plt.subplots()

ax.plot(input, squares, linewidth= 3) #the plot() method produces a line graph
ax.set_title('Squares of Numbers', fontsize= 24)
ax.set_xlabel('Number', fontsize= 14)
ax.set_ylabel('Square of Number', fontsize= 14)
ax.tick_params(labelsize= 14)

plt.show()