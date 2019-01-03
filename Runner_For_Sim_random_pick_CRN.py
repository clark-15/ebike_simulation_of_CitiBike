'''
Runner for Sim_random_pick_CRN
'''

import Sim_random_pick_CRN
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 18)
end_time=start_time+ td(weeks=50)



total_stations = 823
p = 0.5
benchmark =  [519, 490, 168, 293, 285, 151, 379, 477, 497, 426, 3255, 284, 382, 514, 432, 358, 465, 281, 229, 3435, 435, 3427, 368, 523, 504, 3263, 128, 3002, 459, 2008, 492, 405, 173, 127, 237, 527, 433, 327, 496, 3256, 509, 401, 236, 491, 499, 445, 462, 387, 359, 2006, 518, 457, 479, 402, 297, 3141, 383, 444, 472, 482, 212, 161, 3224, 453, 446, 3260, 361, 380, 526, 3443, 450, 334, 345, 3258, 458, 2021, 498, 167, 312, 347, 466, 474, 3428, 531, 494, 417, 505, 251, 3167, 442, 478, 3233, 517, 501, 537, 524, 267, 546, 507, 484, 3137, 195, 448, 410, 257, 486, 116, 3164, 304, 545, 470, 503, 336, 529, 483, 447, 461, 305, 540, 265, 508, 301, 438, 377, 536, 326, 428, 476, 487, 2003, 3093, 439, 485, 3236, 268, 495, 174, 520, 307, 530, 3016, 469, 434, 315, 319, 525, 335, 223, 528, 363, 539, 328, 2010, 3142, 3158, 2012, 3259, 253, 317, 3244, 325, 515, 3223, 72, 3463, 440, 403, 3436, 500, 3235, 252, 480, 346, 153, 355, 3159, 279, 473, 502, 303, 388, 348, 164, 441, 309, 3112, 259, 532, 3147, 369, 3165, 3163, 3466, 311, 394, 460, 3140, 430, 3429, 522, 2002, 228, 2000, 3461, 455, 296, 247, 3119, 385, 376, 217, 3409, 3431, 3374, 3168, 3173, 3156, 280, 386, 456, 3090, 79, 3166, 150, 238, 306, 350, 254, 351, 3107, 320, 422, 449, 3459, 427, 423, 3175, 3472, 146, 3092, 330, 295, 323, 415, 3143, 3160, 468, 3458, 412, 3282, 3383, 3171, 357, 3132, 362, 3295, 264, 143, 308, 513, 366, 3440, 152, 391, 3161, 3349, 276, 337, 3314, 324, 3360, 360, 389, 3462, 3402, 239, 398, 3372, 249, 2023, 3350, 321, 3305, 349, 481, 3176, 3086, 3129, 534, 384, 3243, 393, 3110, 3151, 3169, 3416, 302, 392, 3301, 3288, 3318, 3447, 3113, 3136, 3423, 511, 3134, 3285, 340, 3183, 2009, 454, 3177, 411, 3226, 3242, 3323, 3162, 157, 467, 3096, 282, 3087, 3186, 331, 3170, 414, 3293, 3286, 3418, 310, 390, 3108, 3115, 356, 3232, 3474, 322, 471, 516, 3146, 3336, 316, 406, 3172, 3238, 260, 266, 3116, 3315, 242, 3382, 244, 258, 408, 3292, 3320, 3362, 332, 3109, 396, 341, 3064, 3368, 3467, 3118, 3145, 3307, 3203, 3155, 3283, 314, 3346, 261, 3400, 291, 3373, 437, 232, 3464, 274, 3106, 3150, 3178, 3290, 342, 3074, 3139, 3300, 3180, 3367, 3077, 3102, 3354, 3124, 3312, 83, 3078, 3378, 3453, 241, 3101, 3131, 313, 3082, 3351, 354, 365, 3419, 3117, 3408, 3370, 248, 3100, 3298, 3306, 3331, 3308, 3364, 82, 3407, 3434, 399, 3083, 3341, 339, 3126, 3335, 418, 3430, 3321, 343, 3103, 3376, 3396, 3397, 3356, 3076, 3361, 3438, 364, 3135, 3289, 3384, 395, 416, 3105, 3267, 262, 3390, 3357, 353, 3417, 270, 407, 3068, 3379, 3414, 3311, 3365, 243, 3343, 3358, 3403, 3411, 3294, 3457, 3328, 3148, 3304, 3389, 3125, 3094, 3377, 3202, 3254, 3152, 3284, 3080, 3231, 3303, 3319, 3375, 275, 3366, 3067, 120, 3081, 3088, 3182, 3412, 3420, 344, 3042, 3404, 278, 3410, 3310, 3316, 3345, 3422, 3398, 3425, 3347, 3052, 3355, 3386, 397, 409, 3388, 2022, 3454, 3476, 3046, 3057, 3329, 3325, 3381, 216, 419, 488, 3062, 3297, 420, 3122, 3369, 3399, 3344, 400, 3049, 3085, 3241, 3415, 436, 3339, 3072, 3091, 3121, 3359, 2001, 3313, 3371, 3391, 3047, 3054, 3048, 3050, 3060, 3413, 3095, 3405, 3449, 144, 3157, 3478, 3632, 289, 3120, 3322, 224, 372, 3043, 3424, 3437, 3469, 3317, 3363, 3452, 245, 3058, 3249, 3324, 3066, 3221, 3130, 3338, 3387, 3309, 3353, 3055, 3144, 3455, 373, 3041, 3211, 3276, 3213, 3071, 3401, 3070, 3348, 3421, 3056, 3073, 3061, 3069, 3332, 3441, 3445, 3059, 3553, 119, 3044, 3065, 3489, 421, 3352, 3479, 3327, 3392, 3536, 3552, 3393, 3053, 3063, 3128, 443, 3127, 3296, 3340, 2005, 3179, 3302, 3111, 3456, 3075, 3273, 3185, 3192, 3342, 3330, 3123, 3477, 3337, 3395, 3542, 3494, 3497, 3511, 3547, 3394, 3486, 3509, 3194, 3326, 3333, 3496, 3635, 3637, 3481, 3529, 3533, 3538, 3432, 3508, 3510, 3518, 3490, 3545, 3551, 3201, 3245, 3500, 3507, 3535, 3197, 3468, 3495, 3499, 3502, 3531, 3540, 3556, 3592, 3593, 3493, 3501, 3503, 3504, 3506, 3541, 3554, 3560, 3563, 3568, 3570, 3572]

initial_stations=eval(open(("stations_initial_751.txt")).read())
for bikestation in initial_stations.keys():
    initial_stations[bikestation]['edock']=0
   

for bikestation in benchmark[:int(p*total_stations)]:
    initial_stations[bikestation]['edock']=initial_stations[bikestation]['ecap']

gc=Sim_random_pick_CRN.GlobalClock(start_time,end_time,initial_stations)
gc.clockAdvance()


w_demandlost=list(gc.week_demandlost.values())[2:]
#w_bike_return_full=list(gc.week_bike_return_full.values())[2:]
w_ebike_return_full=list(gc.week_ebike_return_full.values())[2:]
w_average_SOC=list(gc.week_average_SOC.values())[2:]
w_out_of_battery=list(gc.week_out_of_battery.values())[2:]
w_num_etrip=list(gc.week_num_etrip.values())[2:]
#w_num_alltrip=list(gc.week_num_alltrip.values())[2:]
x=range(0,len(w_demandlost))  


with open('data/measurement'+str(p)+'.csv','w') as f:
    f.write('week,ebike_return_error,lost_demand,out_of_battery_trips,ebike_trips\n')
    for week in x:
        f.write(str(week+1)+','+str(w_ebike_return_full[week])+','+str(w_demandlost[week])+','+str(w_out_of_battery[week])+','+str(w_num_etrip[week])+'\n')
         
 