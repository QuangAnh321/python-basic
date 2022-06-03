# Require Python 3.6 or higher
# If use with Python 3.5 or less, the item order will not be consistent
vehicles = {
    "dream": "Honda Dream",
    "wave": "Honda Wave Alpha",
    "morning": "KIA Morning",
    "vios": "Toyota Vios",
    "i10": "Hyundai Grand I10",
    "sirius": "Yamaha Sirius FI"
}

vehicles["jet"] = "Airbus A380"
vehicles["toy"] = "glider"

# upgrade the Wave
vehicles["wave"] = "Honda Wave RSX"

# delete the Morning
del vehicles["morning"]

# my_car = vehicles["morning"]
# print(my_car)
#
# my_motorbike = vehicles.get("wave")
# print(my_mot orbike)

# for key in vehicles:
#     print(f"{key} is {vehicles[key]}")

for key, value in vehicles.items():
    print(key, value, sep=", ")