from die import Die
import plotly.express as px

die1 = Die()
die2 = Die()

rolls = []

for roll_num in range(1000):
    roll = die1.roll() + die2.roll()
    rolls.append(roll)

frequencies = []
max_roll = die1.num_sides + die2.num_sides
possible_rolls = range(2, max_roll+1)

for num in possible_rolls:
    frequency = rolls.count(num)
    frequencies.append(frequency)


labels = {'x': 'Result', 'y': 'Frequency of Result'}
figure = px.bar(x=possible_rolls, y=frequencies, title= 'Results of Rolling Two D6 Dice 1,000 Times', labels= labels)
figure.update_layout(xaxis_dtick=1)
figure.show()