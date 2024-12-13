import re

with open('input') as f:
    input = f.readlines()
    
durations = [int(x) for x in re.findall(r'\d+', input[0].split(':')[1])]
records = [int(x) for x in re.findall(r'\d+', input[1].split(':')[1])]

res = 1

for i in range(0,len(durations)):
    race_duration = durations[i]
    race_record = records[i]
    
    amount_of_ways_to_beat_record = 0
    for t in range(0, race_duration):
        hold_duration = t
        speed = t
        travel_duration = race_duration - hold_duration
        travel_distance = speed * travel_duration
        if (travel_distance > race_record):
            amount_of_ways_to_beat_record += 1
            
    res *= amount_of_ways_to_beat_record
    
print(res)