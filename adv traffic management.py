import time

road1 = int(input("Enter vehicles in Road1: "))
road2 = int(input("Enter vehicles in Road2: "))
road3 = int(input("Enter vehicles in Road3: "))
road4 = int(input("Enter vehicles in Road4: "))

emergency = input("Emergency Vehicle? (yes/no): ").lower()

if emergency == "yes":
    emergency_road = input("Enter Emergency Road (road1/road2/road3/road4): ").lower()
else:
    emergency_road = ""

roads = {
    "road1": road1,
    "road2": road2,
    "road3": road3,
    "road4": road4
}

while True:

    # Emergency Priority
    if emergency == "yes" and emergency_road in roads:

        emergency_count = roads[emergency_road]

        sorted_roads = [(emergency_road, emergency_count)]

        for r, v in sorted(roads.items(), key=lambda x: x[1], reverse=True):
            if r != emergency_road:
                sorted_roads.append((r, v))

        # Emergency sirf first round ke liye
        emergency = "no"

    else:
        sorted_roads = sorted(
            roads.items(),
            key=lambda x: x[1],
            reverse=True
        )

    for road, vehicles in sorted_roads:

        if vehicles == 0:
            continue

        if vehicles >= 50:
            green_time = 10
        elif vehicles >= 30:
            green_time = 7
        else:
            green_time = 5

        print("\n==============================")
        print("GREEN :", road)
        print("Vehicles :", vehicles)

        for i in range(green_time, 0, -1):
            print("Time Left :", i)
            time.sleep(1)

        print("YELLOW :", road)
        time.sleep(2)

        print("RED :", road)

        crossed = 20

        vehicles = vehicles - crossed

        if vehicles < 0:
            vehicles = 0

        roads[road] = vehicles

        print("Remaining Vehicles :", vehicles)

    total = sum(roads.values())

    if total == 0:
        print("\n==============================")
        print("All Roads are Clear!")
        print("Traffic Normal")
        break
