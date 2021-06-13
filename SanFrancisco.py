import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/2600367.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #Pobranie dat oraz najwyższych i najniższych temperatur z pliku.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")

        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Brak danych dla {current_date}.")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#Wygenerowanie wykresu najniższych i najwyższych temperatur.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5) #drugi wykres z datą i kolor niebieski na 1 rysunku
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Formatowanie wykresu
plt.ylim(20,120)
title = ("Najwyższa i najniższa temperatura dnia - 2018\nSan Francisco")
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)

ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()