import time
road1=int(input("enter vehicles in road1"))
road2=int(input("enter vehicles in road2"))
road3=int(input("enter vehicles in road3"))
road4=int(input("enter vehicles in road4"))

          
roads={
      "road1": road1,
      "road2":road2,
      "road3":road3,
       "road4":road4
    }
while True:
            sorted_roads= sorted(roads.items(),
                     key=lambda x:x[1],
                     reverse=True)
            for road,vehicles in sorted_roads:

                 if vehicles>=50:
                    green_time=10
                 elif vehicles>=30:
                      green_time=7
                 else:
                     green_time = 5
    
                 print("GREEN",road)
                 for i in range(green_time,0,-1): 
                     print("TIME LEFT",i)
                     time.sleep(1)
                 print("YELLOW",road)
                 time.sleep(2)
                 print("RED",road)
                 crossed=20
                 vehicles=vehicles-crossed
                 if vehicles <0:
                      vehicles = 0
                 roads[road]=vehicles
                 print(road,"remaining vehicles",vehicles)
                 total=sum(roads.values())
                 if total==0:
                    print("\n allRoads are clear now")
                    print("Traffic Normal")
                    break
