import re

with open('input') as f:
    input = f.readlines()
    
race_duration = int(''.join(re.findall(r'\d+', input[0].split(':')[1])))
race_record = int(''.join(re.findall(r'\d+', input[1].split(':')[1])))

amount_of_ways_to_beat_record = 0
for t in range(0, race_duration):
    hold_duration = t
    speed = t
    travel_duration = race_duration - hold_duration
    travel_distance = speed * travel_duration
    if (travel_distance > race_record):
        amount_of_ways_to_beat_record += 1
    
print(amount_of_ways_to_beat_record)