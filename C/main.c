#include <stdio.h>
#include <time.h>

typedef struct CalcStats{
    int masks;
    int clips;
    double maskers;
    double money;
    double space;
    double weight;
    double time;   
} CalcStats;

typedef struct ItemStats {
    double change;
    double price;
    double weight;
    double space;
    double time;
} ItemStats;

CalcStats evaluate(double limits[], double ratio, struct ItemStats maskStats, struct ItemStats calcStats, int multiplier);
double getStat(struct CalcStats *ItemStats, int i);

double limits[] = {3500,11500,6000,180000,18000,36}; // Money, Space, Weight, Time

CalcStats evaluate(double limits[], double ratio, struct ItemStats maskStats, struct ItemStats clipStats, int multiplier) {
    double counts[] = {};

    CalcStats previousStats;
    previousStats.maskers = -1;
    previousStats.clips = -1;
    previousStats.masks= -1;

    int hasMaxed = 0;
    double maskCounter = 0;
    double clipCounter = 0;

    double maskRatio = 1-ratio/multiplier;
    double clipRatio = ratio/multiplier;
    
    CalcStats currentStats;
    currentStats.masks = 0;
    currentStats.clips = 0;

    while (1 == 1) {

        maskCounter = maskCounter + maskRatio;
        clipCounter = clipCounter + clipRatio;

        if (maskCounter >= 1) {
            currentStats.masks++;
            maskCounter--;
        }
        if (clipCounter >= 1) {
            currentStats.clips++;
            clipCounter--;
        }

        if (currentStats.masks == previousStats.masks && currentStats.clips == previousStats.clips) {
            continue;
        }

        currentStats.maskers = currentStats.masks * maskStats.change + currentStats.clips * clipStats.change;
        currentStats.money = currentStats.masks * maskStats.price + currentStats.clips * clipStats.price;
        currentStats.weight = currentStats.masks * maskStats.weight + currentStats.clips * clipStats.weight;
        currentStats.space = currentStats.masks * maskStats.space + currentStats.clips * clipStats.space;
        currentStats.time = currentStats.masks * maskStats.time + currentStats.clips * clipStats.time;
        int flag = 0;
        for (int i = 0; i < 6; i++) {
            if (getStat(&currentStats,i) > limits[i]) {
                flag = 1;
                break;
            }

        }

        if (flag == 1) {
            break;
        }

        previousStats = currentStats;

    }
    return previousStats;
}

double getStat(struct CalcStats *ItemStats, int i) {
    switch(i) {
        case -1: return ItemStats->maskers;
        case 0: return ItemStats->masks;
        case 1: return ItemStats->clips;
        case 2: return ItemStats->money;
        case 3: return ItemStats->weight;
        case 4: return ItemStats->space;
        case 5: return ItemStats->time;
    }
    return 0;
}

/*
int main() {
    ItemStats MaskStats;
    MaskStats.change = 0.05;
    MaskStats.price = 1.8;
    MaskStats.weight = 8;
    MaskStats.space = 1;
    MaskStats.time = 0.008;

    ItemStats ClipStats;
    ClipStats.change = 0.02;
    ClipStats.price = 0.2;
    ClipStats.weight = 14;
    ClipStats.space = 1.5;
    ClipStats.time = 0.002;

    printf("%f\n",evaluate(limits,100,MaskStats,ClipStats,100).maskers);
    printf("%f\n",evaluate(limits,100,MaskStats,ClipStats,200).maskers);
}
*/

int main() {
    clock_t begin = clock();
    const int multiplier = 11500;
    double l_ratio = 0;
    double r_ratio = multiplier;
    double center_ratio = (multiplier/2);


    ItemStats MaskStats;
    MaskStats.change = 0.05;
    MaskStats.price = 1.8;
    MaskStats.weight = 8;
    MaskStats.space = 1;
    MaskStats.time = 0.008;

    ItemStats ClipStats;
    ClipStats.change = 0.02;
    ClipStats.price = 0.2;
    ClipStats.weight = 14;
    ClipStats.space = 1.5;
    ClipStats.time = 0.002;

    CalcStats left;
    CalcStats right;
    CalcStats center;

    left = evaluate(limits,l_ratio,MaskStats,ClipStats,multiplier);
    right = evaluate(limits,r_ratio,MaskStats,ClipStats,multiplier);
    center = evaluate(limits,center_ratio,MaskStats,ClipStats,multiplier);

    while (1 == 1) {
        if (left.maskers > right.maskers) {
            right = center;
            r_ratio = center_ratio;
            center_ratio = (l_ratio+r_ratio)/2;
            printf("right\n");
        } else if (left.maskers < right.maskers) {
            left = center;
            l_ratio = center_ratio;
            center_ratio = (l_ratio+r_ratio)/2;
            printf("left\n");
        } else {
            printf("Done!\n");
            break;
        }
        center = evaluate(limits,center_ratio,MaskStats,ClipStats,multiplier);
        printf("%f\n",center.maskers);
    }
    clock_t end = clock();
    printf("Calculated in %f seconds\n",(double)(end - begin) / CLOCKS_PER_SEC);
    printf("----------------------------------------------------------------\n");
    printf("Converted: %f %f%%\n", center.maskers, center.maskers/306);
    printf("Masks:     %f %f%%\n", (double)center.masks, center.maskers/limits[0]);
    printf("Clips:     %f %f%%\n", (double)center.clips, center.clips/limits[1]);
    printf("Money:     %f %f%%\n", center.money, center.money/limits[2]);
    printf("Weight:    %f %f%%\n", center.weight, center.weight/limits[3]);
    printf("Volume:    %f %f%%\n", center.space, center.space/limits[4]);
    printf("Time:      %f %f%%\n", center.time, center.time/limits[5]);


    return 0;
};
