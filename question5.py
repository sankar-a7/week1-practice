seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]
for i in range(len(seats)):
    print("Seat", i + 1, ":", seats[i])

seat_number = int(input("Enter seat number: "))
if seats[seat_number - 1] == "Available":
    seats[seat_number - 1] = "Booked"
    print("Seat booked successfully.")
else:
    print("Seat is already booked.")
booked = seats.count("Booked")
available = seats.count("Available")

print("Total Seats:", len(seats))
print("Booked Seats:", booked)
print("Available Seats:", available)