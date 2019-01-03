# -*- coding: utf-8 -*-
"""
Runner for Sim_random_pick_CRN, benchmark
"""

from copy import deepcopy
import Sim_random_pick_CRN
from datetime import timedelta as td
from datetime import datetime as time
import multiprocessing
#import threading
    
start_time = time(2017,7,1,hour= 6)
end_time=start_time+ td(days=1)
initial_stations=eval(open(("data/steady_states_p/stations_initial_0.9.txt")).read())


estation= [519, 490, 168, 293, 285, 151, 379, 477, 497, 426, 3255, 284, 382, 514, 432, 358, 465, 281, 229, 3435, 435, 3427, 368, 523, 504, 3263, 128, 3002, 459, 2008, 492, 405, 173, 127, 237, 527, 433, 327, 496, 3256, 509, 401, 236, 491, 499, 445, 462, 387, 359, 2006, 518, 457, 479, 402, 297, 3141, 383, 444, 472, 482, 212, 161, 3224, 453, 446, 3260, 361, 380, 526, 3443, 450, 334, 345, 3258, 458, 2021, 498, 167, 312, 347, 466, 474, 3428, 531, 494, 417, 505, 251, 3167, 442, 478, 3233, 517, 501, 537, 524, 267, 546, 507, 484, 3137, 195, 448, 410, 257, 486, 116, 3164, 304, 545, 470, 503, 336, 529, 483, 447, 461, 305, 540, 265, 508, 301, 438, 377, 536, 326, 428, 476, 487, 2003, 3093, 439, 485, 3236, 268, 495, 174, 520, 307, 530, 3016, 469, 434, 315, 319, 525, 335, 223, 528, 363, 539, 328, 2010, 3142, 3158, 2012, 3259, 253, 317, 3244, 325, 515, 3223, 72, 3463, 440, 403, 3436, 500, 3235, 252, 480, 346, 153, 355, 3159, 279, 473, 502, 303, 388, 348, 164, 441, 309, 3112, 259, 532, 3147, 369, 3165, 3163, 3466, 311, 394, 460, 3140, 430, 3429, 522, 2002, 228, 2000, 3461, 455, 296, 247, 3119, 385, 376, 217, 3409, 3431, 3374, 3168, 3173, 3156, 280, 386, 456, 3090, 79, 3166, 150, 238, 306, 350, 254, 351, 3107, 320, 422, 449, 3459, 427, 423, 3175, 3472, 146, 3092, 330, 295, 323, 415, 3143, 3160, 468, 3458, 412, 3282, 3383, 3171, 357, 3132, 362, 3295, 264, 143, 308, 513, 366, 3440, 152, 391, 3161, 3349, 276, 337, 3314, 324, 3360, 360, 389, 3462, 3402, 239, 398, 3372, 249, 2023, 3350, 321, 3305, 349, 481, 3176, 3086, 3129, 534, 384, 3243, 393, 3110, 3151, 3169, 3416, 302, 392, 3301, 3288, 3318, 3447, 3113, 3136, 3423, 511, 3134, 3285, 340, 3183, 2009, 454, 3177, 411, 3226, 3242, 3323, 3162, 157, 467, 3096, 282, 3087, 3186, 331, 3170, 414, 3293, 3286, 3418, 310, 390, 3108, 3115, 356, 3232, 3474, 322, 471, 516, 3146, 3336, 316, 406, 3172, 3238, 260, 266, 3116, 3315, 242, 3382, 244, 258, 408, 3292, 3320, 3362, 332, 3109, 396, 341, 3064, 3368, 3467, 3118, 3145, 3307, 3203, 3155, 3283, 314, 3346, 261, 3400, 291, 3373, 437, 232, 3464, 274, 3106, 3150, 3178, 3290, 342, 3074, 3139, 3300, 3180, 3367, 3077, 3102, 3354, 3124, 3312, 83, 3078, 3378, 3453, 241, 3101, 3131, 313, 3082, 3351, 354, 365, 3419, 3117, 3408, 3370, 248, 3100, 3298, 3306, 3331, 3308, 3364, 82, 3407, 3434, 399, 3083, 3341, 339, 3126, 3335, 418, 3430, 3321, 343, 3103, 3376, 3396, 3397, 3356, 3076, 3361, 3438, 364, 3135, 3289, 3384, 395, 416, 3105, 3267, 262, 3390, 3357, 353, 3417, 270, 407, 3068, 3379, 3414, 3311, 3365, 243, 3343, 3358, 3403, 3411, 3294, 3457, 3328, 3148, 3304, 3389, 3125, 3094, 3377, 3202, 3254, 3152]

num_ebike = 0.4
for station in initial_stations.keys():
    initial_stations[station]['edock'] = 0
    
for station in estation:
    initial_stations[station]['edock'] = initial_stations[station]['ecap']
    

N_estation = int(0.9*len(initial_stations))

initial_stations_copy = deepcopy(initial_stations)
def sim_thread(start_time,end_time,initial_stations,stations_c):
    initial_stations_c = deepcopy(initial_stations_copy)
    initial_stations_c[stations_c]['edock'] = initial_stations[stations_c]['ecap']
    gc=Sim_random_pick_CRN.GlobalClock(start_time,end_time,initial_stations_c)
    gc.clockAdvance()
    out_event_count[stations_c]=gc.demandlost+gc.ebike_return_full+gc.out_of_battery
    
for i in range(N_estation-len(estation)):
    candidateset = []
    gc=Sim_random_pick_CRN.GlobalClock(start_time,end_time,initial_stations)
    gc.clockAdvance()
    station_count = {}
    for sta in gc.stations.keys():
        if sta not in estation:
            station_count[sta]=gc.stations[sta].tripsOut+gc.stations[sta].tripsIn+gc.stations[sta].tripsFailedOut+gc.stations[sta].tripsFailedIn
    sorted_station_count = sorted(station_count.items(), key=lambda kv: kv[1],reverse = True)
    for j in range(10):
        candidateset.append(sorted_station_count[j][0])
    out_event_count={}
    threads=[]
    for stat in candidateset:
        threads.append(multiprocessing.Processing(target=sim_thread,args=(start_time,end_time,initial_stations,stat)))
        
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    sorted_event_count_list = sorted(out_event_count.items(), key=lambda kv: kv[1])
    print(str(i+len(estation)),str(sorted_event_count_list))
    max_statn = sorted_event_count_list[0][0]
    estation.append(max_statn)
    initial_stations_copy[max_statn]['edock'] = initial_stations_copy[max_statn]['ecap']
    initial_stations = deepcopy(initial_stations_copy)
 