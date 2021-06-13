import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#Pobieranie wykresu najwyższych oraz najniższych temperatur
    dates, highs, lows, prcps = [], [], [], []  #dodajemy pusta listę lows do temperatur
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        prcp = int(float(row[3]))
        high = int(row[5])
        low = int(row[6]) # Pobierz 6 pozycję z wersza do wykresu
        dates.append(current_date)
        prcps.append(prcp)
        highs.append(high)
        lows.append(low)

#Wygenerowanie wykresu najwyższych temperatur.
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5) #drugi wykres z datą i kolor niebieski na 1 rysunku
ax.plot(dates, prcps, c='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Formatowanie wykresu
plt.ylim(20,120)
#plt.plot(range(30,120))
#ax.axis(0, dates, 30, 120)
ax.set_title("Najwyższa i najniższa temperatura dnia - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()


