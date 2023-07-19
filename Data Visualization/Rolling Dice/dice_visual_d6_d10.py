from die import Die
import plotly.express as px

d6 = Die()
d10 = Die(10)

rolls = []

for roll_num in range(50000):
    roll = d6.roll() + d10.roll()
    rolls.append(roll)

frequencies = []
max_roll = d6.num_sides + d10.num_sides
possible_rolls = range(2, max_roll+1)

for num in possible_rolls:
    frequency = rolls.count(num)
    frequencies.append(frequency)


labels = {'x': 'Result', 'y': 'Frequency of Result'}
figure = px.bar(x=possible_rolls, y=frequencies, title= 'Results of Rolling One D6 and One D10 Die 50,000 Times', labels= labels)
figure.update_layout(xaxis_dtick=1)
figure.show()
figure.write_html('dice_visual_d6_d10.html')