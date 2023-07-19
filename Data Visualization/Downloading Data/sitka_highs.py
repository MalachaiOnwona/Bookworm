from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
headers = next(reader)

dates, highs = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    highs.append(high)
    dates.append(date)



print(highs)

plt.style.use('dark_background')
figure, ax = plt.subplots()
ax.plot(dates, highs, color = 'orange')

ax.set_title('Daily High Temperatures in Sitka, 2021', fontsize=20)
ax.set_xlabel('', fontsize=15)
figure.autofmt_xdate()
ax.set_ylabel('Temperature (Farenheit)', fontsize=15)
ax.tick_params(labelsize=15)

plt.show()