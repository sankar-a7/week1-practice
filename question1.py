hours = int(input())

if hours <= 2:
    parking_charge = 30 * hours
    print("Parking Charge:", parking_charge)
elif hours <= 5:
    parking_charge = 25 * hours
    print("Parking Charge:", parking_charge)
else:
    parking_charge = 20 * hours
    print("Parking Charge:", parking_charge)
    if hours > 8:
        service_charge = 20
        total_charge = parking_charge + service_charge
        print("Service Charge:", service_charge)
        print("Total Charge:", total_charge)
        final_amount = total_charge
    else:
        final_amount = parking_charge

print("Final Amount:", final_amount)

