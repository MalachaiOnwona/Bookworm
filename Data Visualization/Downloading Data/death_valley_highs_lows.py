from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
headers = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f'Missing data for {date}')
    else:
        highs.append(high)
        dates.append(date)
        lows.append(low)



print(highs)

plt.style.use('dark_background')
figure, ax = plt.subplots()
ax.plot(dates, highs, color = 'orange', alpha= 0.5)
ax.plot(dates, lows, color= 'blue', alpha= 0.5)
ax.fill_between(dates, highs, lows, facecolor= 'blue', alpha= 0.1)

ax.set_title('Daily High and Low Temperatures in Death Valley, CA, 2021', fontsize=20)
ax.set_xlabel('', fontsize=15)
figure.autofmt_xdate()
ax.set_ylabel('Temperature (Farenheit)', fontsize=15)
ax.tick_params(labelsize=15)

plt.show()