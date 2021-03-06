# DATA SHEET
# Comfort Clips --------------------------------------------------
#
# 2% Chance of Conversion
# $0.20
# 1/500 hours
# 1.5inches^3
# up to 11,500
# 14g
#
# Custom Cool Poggers Maks ---------------------------------------
#
# 5% Chance of Conversion
# $1.80
# 1/125 hours
# 1 inch^3
# up to 3500
# 8g

# Runs ~30million times in ~6 mins on my laptop

# 5:40

import math
import matplotlib.pyplot as plt
import time
import matplotlib
import sys

start_time = time.time()


datapoints = []
Counter = 0

# This array is a bunch of changeable statistics you can use to mess around with the program and try different combonations
# Dummy, Masks, Clips, Price, Weight, Volume, Time | Dummy exists because of a for loop later. dummy can be whatever you want and it shouldn't break anything
# Limits = [0, 3500, 11500, 6000, 180000, 18000, 36]
Limits = [0, 3500, 11500, 6000, 180000, 18000, 36]
Clip_stats = [0.02, 0.2, 14, 1.5, 0.002]  # Chance, Cost, Weight, Volume , Time
Mask_stats = [0.05, 1.8, 8, 1, 0.008]  # Chance, Cost, Weight, Volume , Time
# Converted, Masks, Clips, Price, Weight, Volume, Time
Result = [0, 0, 0, 0, 0, 0, 0]


# This program is a lot simpler than ratio check so I should be able to explain this quicker
#
# 1. 2 for loops are run which count through every possible combonation of masks
#
# 2. Temp, which is used to check the combonations is set to all the required values based on i and j (The counts fir each for loop)
#
# 3. Counter, which is used for user feedback is incrimented and printed to tell the user that the program is doing something
#
# 4. a fancy for loop checks all the values in Temp to see if they are greater than that of limits
#
# 5. Through a little bit of weird logic. If it exceeds the limits then the inner for loop is broken (essenctially if that number of clips + that number of masks doesn't work adding more masks definately won't work. just a little thing but saves some 11 million calculations)
#
# 6. That process happens about 30,000,000 times until the for loops are over and the result it printed
l = 0
for i in range(Limits[1]):  # For i in range masks
    for j in range(Limits[2]):  # For j in range clips
        # Converted, Masks, Clips, Price, Weight, Volume, Time
        Temp = [0, i, j, 0, 0, 0, 0]
        # Converted = Masks * Conversion Rate + Clips * Conversion Rate
        Temp[0] = Temp[1] * Mask_stats[0] + Temp[2] * Clip_stats[0]
        Temp[3] = Temp[1] * Mask_stats[1] + Temp[2] * \
            Clip_stats[1]  # Price = Masks * Cost + Clips * Cost
        Temp[4] = Temp[1] * Mask_stats[2] + Temp[2] * \
            Clip_stats[2]  # Weight = Masks * Weight + Clips * Weight
        Temp[5] = Temp[1] * Mask_stats[3] + Temp[2] * \
            Clip_stats[3]  # Volume = Masks * Volume + Clips * Volume
        Temp[6] = Temp[1] * Mask_stats[4] + Temp[2] * \
            Clip_stats[4]  # Time = Masks * Time + Clips * Time
        Counter += 1
        sys.stdout.write(str(Counter)+"\n")
        print(f"Datpoints length: {len(datapoints)}")
        flag = False
        for k in range(len(Limits)-1):
            if Temp[k+1] > Limits[k+1]:
                flag = True
                break

        if not flag and Result[0] < Temp[0]:
            Result = Temp2
        Temp2 = Temp.copy()
        l += 1
        if l % 13 == 0:
            datapoints.append([Temp2[0], Temp2[1], Temp2[2]])
        if flag:
            break  # This if removes 11million calculations. Optomization poggers

# The math.floors here only serve astetic purposes
print(datapoints)
Zs = [item[0] for item in datapoints]
Xs = [item[1] for item in datapoints]
Ys = [item[2] for item in datapoints]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_trisurf(
    Xs, Ys, Zs, cmap=matplotlib.cm.get_cmap("plasma"), linewidth=0)
fig.colorbar(surf)

ax.set_xlabel('Masks')
ax.set_ylabel('Clips')
ax.set_zlabel('Permenant Maks Wearers')

fig.tight_layout()

# fig.savefig("3d.png")
matplotlib.use("Qt5Agg")
plt.show()


print(f"Only took like {time.time() - start_time} seconds")
print("-----------------------")
print("Converterd: ", Result[0])
print("Mask Count: ", Result[1], " ",
      math.floor((Result[1]/Limits[1])*100), "%")
print("Clip Count: ", Result[2], " ",
      math.floor((Result[2]/Limits[2])*100), "%")
print("Money Spent: ", Result[3], " ",
      math.floor((Result[3]/Limits[3])*100), "%")
print("Weight: ", Result[4], " ", math.floor((Result[4]/Limits[4])*100), "%")
print("Volume Used: ", Result[5], " ",
      math.floor((Result[5]/Limits[5])*100), "%")
print("Time Used: ", Result[6], " ", math.floor(
    (Result[6]/Limits[6])*100), "%")
print(f"K is {k}")
