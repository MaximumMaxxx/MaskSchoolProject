# This program bassically attempts to find the peak or best possible solution by using binary search
#
# Binary search is the fastest search algorithm that we know of and it's probably the most natural.
#
# In this implimentation Binary search you start with the two extreme values and the middle value.   
# With those two extremes and the middle we can eliminate half of the number space.
# 
# This is because we know the value is approaching 306 as the final answer
# possible example: 30.5.6, 305.7 305.8, 305.9, 306 , 305.9
# another way to thing of it is 306 is the peak of a mountain and it goes down hill on all sides
# 
# the important part is since there's a smooth "slope" to our mountain i.e not 100.23, 63, 890
# a cool thing we can do is eliminate half of all possible numbers using relatively few calculations
#
# In the code we get rid of the extreme with a lower bound because it keeps the limits constantly moving up.
#  
# Once half of the number space is gone we just redo the same calculations except change the boundries to be our new space
# and set a new middle.
#
# In the end the edges will approach or get closer and closer to the middle number and after a few cycles the two edge values will be equal
# We then just take that result format and put it in the console.

import math
import time
start_time = time.time()

multiplier = 11500 # Set = to clips or masks(whichever is higher) to get the correct result
l_ratio = 0 # not 0-1 because flaots are dumb
r_ratio = multiplier
c_ratio = multiplier/2
Limits = [0,3500,11500,6000,180000,18000,36]    #Filler, Masks, Clips, Price, Weight, Volume, Time | Filler exists to make a function later easier to write you can set it to whatver number you want. It won't do anything
Clip_stats = [0.02, 0.2 , 14 , 1.5 , 0.002] # Chance, Cost, Weight, Volume , Time
Mask_stats = [0.05, 1.8 , 8 , 1 , 0.008] # Chance, Cost, Weight, Volume , Time
Result = [0,0,0,0,0,0,0] # Converted, Masks, Clips, Price, Weight, Volume, Time


# This block of code takes in a ratio and some other stuff, then calculates the best possible result with that ratio
# 
# example: a ratio of 50/50 would produce something like 2500 masks and 2500 clips with the idea being the ratio can change.
# a ratio of 25/75 would be like 2500 masks 7500 clips.
#

def ratio_check(ratio,multiplier,limitor,MStats,CStats):
    Temp = [0,0,0,0,0,0,0] # Converted, Masks, Clips, Price, Weight, Volume, Time
    Temp2 = [0,0,0,0,0,0,0] # Converted, Masks, Clips, Price, Weight, Volume, Time
    mask_counter = 0
    clip_counter = 0
    mask_ratio = 1-ratio/multiplier # Sets the mask ratio so that it plus the clips ratio gives you one
    clips_ratio = ratio/multiplier
    
    # This while loop is very important so I'll attempt to give an explination of each componant of it
    #
    # 1.At the start mask_counter and clip_counter are incrimented by the previously established ratios
    # 
    # 2.Then when either it greater than or = to 1 the list temp2 has the corrosponding item incrimented
    # Temp2 is set to what Temp will be since temp is returned as the final result and this makes sure it doesn't make an invalid result
    # 
    # 3. Temp2 has all the other variables calculated for it like time and volume
    # 
    # 4. A fancy looking for loop checks through Temp2 and compares it to the Limits established in the beginning
    # 
    # 5. If any limit is broken it exits the while loop and does not set Temp. This is important because we want Temp to be
    # The highest valid combonation for that ratio
    #
    # 6. If no conditions were broken however the Mask and Clips for Temp are incimented and all the other values are recalculated
    # 
    # 7. Once the loop has been exited Temp is returned to the control loop. 
    # In programming a return from a function means giving data back to the thing that called the function
    # In this case the function is being called from our main loop (below the function) and the main loop performs some logic on the returned output of this function

    while True:
        mask_counter += mask_ratio
        clip_counter += clips_ratio
        
        if mask_counter >= 1:
            Temp2[1] += 1 
        if clip_counter >= 1:
            Temp2[2] += 1

        Temp2[0] = Temp2[1] * MStats[0] + Temp2[2] * CStats[0] #Converted = Masks * Conversion Rate + Clips * Conversion Rate
        Temp2[3] = Temp2[1] * MStats[1] + Temp2[2] * CStats[1] #Price = Masks * Cost + Clips * Cost
        Temp2[4] = Temp2[1] * MStats[2] + Temp2[2] * CStats[2] #Weight = Masks * Weight + Clips * Weight
        Temp2[5] = Temp2[1] * MStats[3] + Temp2[2] * CStats[3] #Volume = Masks * Volume + Clips * Volume
        Temp2[6] = Temp2[1] * MStats[4] + Temp2[2] * CStats[4] #Time = Masks * Time + Clips * Time


        flag = False
        for i in range(len(limitor)-1):
            if Temp2[i+1] > limitor[i+1]:
                flag=True
                break 
        if flag:
            break
        
        if mask_counter >= 1:
            mask_counter -= 1
            Temp[1] += 1 
        if clip_counter >= 1:
            clip_counter -= 1
            Temp[2] += 1

        Temp[0] = Temp[1] * MStats[0] + Temp[2] * CStats[0] #Converted = Masks * Conversion Rate + Clips * Conversion Rate
        Temp[3] = Temp[1] * MStats[1] + Temp[2] * CStats[1] #Price = Masks * Cost + Clips * Cost
        Temp[4] = Temp[1] * MStats[2] + Temp[2] * CStats[2] #Weight = Masks * Weight + Clips * Weight
        Temp[5] = Temp[1] * MStats[3] + Temp[2] * CStats[3] #Volume = Masks * Volume + Clips * Volume
        Temp[6] = Temp[1] * MStats[4] + Temp[2] * CStats[4] #Time = Masks * Time + Clips * Time



    return Temp


left=ratio_check(0,multiplier,Limits,Mask_stats,Clip_stats) # All Mask
right=ratio_check(multiplier,multiplier,Limits,Mask_stats,Clip_stats) # all clips
center=ratio_check(multiplier/2,multiplier,Limits,Mask_stats,Clip_stats) # 50/50

while True:
    if left[0] > right[0]:
        right = center
        r_ratio = c_ratio
        c_ratio = (l_ratio+r_ratio)/2
        print("right")
    elif left[0] < right[0]:
        left = center
        l_ratio = c_ratio
        c_ratio = (l_ratio+r_ratio)/2
        print('left')
    else:
        print("done")
        break
    center = ratio_check(c_ratio,multiplier,Limits,Mask_stats,Clip_stats) 

# Formatting code to give a nice output


print("-----------------------")
print("In ", time.time() - start_time, " seconds these results were calculated")
print ("Converterd: ",center[0])
print ("Mask Count: ",center[1], " ",math.floor((center[1]/Limits[1])*100),"%")
print ("Clip Count: ",center[2], " ",math.floor((center[2]/Limits[2])*100),"%")
print ("Money Spent: ",center[3], " ",math.floor((center[3]/Limits[3])*100),"%")
print ("Weight: ",center[4], " ",math.floor((center[4]/Limits[4])*100),"%")
print ("Volume Used: ",center[5], " ",math.floor((center[5]/Limits[5])*100),"%")
print ("Time Used: ",center[6], " ", math.floor((center[6]/Limits[6])*100),"%")
