from die import Die
import plotly.express as px

die = Die()

rolls = []

for roll_num in range(1000):
    roll = die.roll()
    rolls.append(roll)

frequencies = []
possible_rolls = range(1, die.num_sides+1)

for num in possible_rolls:
    frequency = rolls.count(num)
    frequencies.append(frequency)


labels = {'x': 'Result', 'y': 'Frequency of Result'}
figure = px.bar(x=possible_rolls, y=frequencies, title= 'Results of Rolling One D6 1,000 Times', labels= labels)
figure.show()