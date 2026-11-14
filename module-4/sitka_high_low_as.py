import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
# Display the menu until the user chooses to exit.
while True:
    print("\nWelcome to the Sitka Weather Program!")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '3':
        print("Thank you for using the Sitka Weather Program. Goodbye!")
        break

    elif choice == '1':
        temperatures = highs
        color = 'red'
        title = 'Daily high temperatures - 2018'

    elif choice == '2':
        temperatures = lows
        color = 'blue'
        title = 'Daily low temperatures - 2018'

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    # Create and display the selected temperature graph.
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    # Format the graph.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()