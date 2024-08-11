import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

def calculate_fare():
    try:
        pickup_lat = float(pickup_lat_entry.get())
        pickup_lon = float(pickup_lon_entry.get())
        dropoff_lat = float(dropoff_lat_entry.get())
        dropoff_lon = float(dropoff_lon_entry.get())
        passenger_count = int(passenger_count_entry.get())
        pickup_datetime = datetime.datetime.strptime(pickup_datetime_entry.get(), "%d-%m-%Y %H:%M")

        # Placeholder fare calculation logic
        fare = (abs(dropoff_lat - pickup_lat) + abs(dropoff_lon - pickup_lon)) * 2 + passenger_count * 5

        fare_label.config(text=f'Total Fare: ${fare:.2f}')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Tkinter setup
root = tk.Tk()
root.title("Fare Calculator")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

pickup_lat_label = ttk.Label(mainframe, text="Pickup Latitude:")
pickup_lat_label.grid(column=0, row=0, sticky=tk.E)

pickup_lat_entry = ttk.Entry(mainframe)
pickup_lat_entry.grid(column=1, row=0)

pickup_lon_label = ttk.Label(mainframe, text="Pickup Longitude:")
pickup_lon_label.grid(column=0, row=1, sticky=tk.E)

pickup_lon_entry = ttk.Entry(mainframe)
pickup_lon_entry.grid(column=1, row=1)

dropoff_lat_label = ttk.Label(mainframe, text="Dropoff Latitude:")
dropoff_lat_label.grid(column=0, row=2, sticky=tk.E)

dropoff_lat_entry = ttk.Entry(mainframe)
dropoff_lat_entry.grid(column=1, row=2)

dropoff_lon_label = ttk.Label(mainframe, text="Dropoff Longitude:")
dropoff_lon_label.grid(column=0, row=3, sticky=tk.E)

dropoff_lon_entry = ttk.Entry(mainframe)
dropoff_lon_entry.grid(column=1, row=3)

passenger_count_label = ttk.Label(mainframe, text="Passenger Count:")
passenger_count_label.grid(column=0, row=4, sticky=tk.E)

passenger_count_entry = ttk.Entry(mainframe)
passenger_count_entry.grid(column=1, row=4)

pickup_datetime_label = ttk.Label(mainframe, text="Pickup Datetime (dd-mm-yyyy HH:MM):")
pickup_datetime_label.grid(column=0, row=5, sticky=tk.E)

pickup_datetime_entry = ttk.Entry(mainframe)
pickup_datetime_entry.grid(column=1, row=5)

calculate_button = ttk.Button(mainframe, text="Calculate Fare", command=calculate_fare)
calculate_button.grid(column=1, row=6)

fare_label = ttk.Label(mainframe, text="Total Fare: $0.00")
fare_label.grid(column=1, row=7)

root.mainloop()
