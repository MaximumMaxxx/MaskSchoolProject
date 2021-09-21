
#DATA SHEET
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





# This solution is a little bit confusiong since it's kinda a non standard approach however I will try my best
# 
# This program generates a number g_ratio which is used to calculate with mask/clip ratio
# that number might be something like 578 however it is also divided by the multiplier to get a decimal like 0.3
# This was done to counteract some python float(decimal) weirdness however it works exactly the same

# The lists defined below are to store a variety of things that should be self explanitory based on their name.
# The stats store the statisics of each item, the limits stores all the limitations, and result is well, the result


import math

multiplier = 11500 # Number Of Combos tried. Set = to clips or masks(whichever is higher) to get the correct result
g_ratio = 0 # not 0-1 because flaots are dumb
Limits = [0,3500,11500,6000,180000,18000,36]    #Filler, Masks, Clips, Price, Weight, Volume, Time | Filler exists to make a function later easier to write you can set it to whatver number you want. It won't do anything
Clip_stats = [0.02, 0.2 , 14 , 1.5 , 0.002] # Chance, Cost, Weight, Volume , Time
Mask_stats = [0.05, 1.8 , 8 , 1 , 0.008] # Chance, Cost, Weight, Volume , Time
Result = [0,0,0,0,0,0,0] # Converted, Masks, Clips, Price, Weight, Volume, Time

# Manufacturer Variables

man_Masks = 300 #Mall
man_Clips = 1400 #Electronics Store






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

        


Current_RSLT = [0,0,0,0,0,0,0] # Converted, Masks, Clips, Price, Weight, Volume, Time


# This is our main loop it controls how often ratio_check, the big function above this, is called
# 
# 1. RSLT is set to the returned result of ratio_check
# 
# 2. g_ratio is incrimented
#
# 3. some user feedback is output to tell them that the program is actually running
# Since this takes a few minutes to run it's not exactly a fast process and a user would probably think that something is broken
# This user feedback tells them that the program is doing things
#
# 4. Once g_ratio is greater than multiplier (see first explination if you're confused) we print a nice little formatted output


while(g_ratio <= multiplier):
    RSLT = ratio_check(g_ratio,multiplier,Limits,Mask_stats,Clip_stats)
    if RSLT[0] > Current_RSLT[0]:
        Current_RSLT = RSLT
    g_ratio += 1
    print("Masks: ", RSLT[1], " Clips:", RSLT[2] , " Converted: ", math.floor(RSLT[0]))
print("-----------------------")
print ("Converterd: ",Current_RSLT[0])
print ("Mask Count: ",Current_RSLT[1], " ",math.floor((Current_RSLT[1]/Limits[1])*100),"%")
print ("Clip Count: ",Current_RSLT[2], " ",math.floor((Current_RSLT[2]/Limits[2])*100),"%")
print ("Money Spent: ",Current_RSLT[3], " ",math.floor((Current_RSLT[3]/Limits[3])*100),"%")
print ("Weight: ",Current_RSLT[4], " ",math.floor((Current_RSLT[4]/Limits[4])*100),"%")
print ("Volume Used: ",Current_RSLT[5], " ",math.floor((Current_RSLT[5]/Limits[5])*100),"%")
print ("Time Used: ",Current_RSLT[6], " ", math.floor((Current_RSLT[6]/Limits[6])*100),"%")