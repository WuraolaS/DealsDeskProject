import sys
import pandas as pd
df = pd.read_excel (r'/Users/wsonubi/Desktop/Deals_Desk_Project/CFBcron_Practice.xlsx', sheet_name='Deal_targeting_pratice')
days = []
profiles = []

for i in range(1, len(sys.argv)):
    profiles.append(sys.argv[i])

class Deals:
    """description"""
    def __init__(self, day, publishers, placement_groups, placements):
        self.publishers = publishers
        self.day = day
        self.placement_groups = placement_groups
        self.placements = placements
# Deals is indexed, the length of the list of deals = number of rows
# What we're considering is the different days
# For each row, create a new deal class


for i in range(len(df)):
    day = str(df["Day"][i])
    publishers = str(df["Publisher"][i]).split(", ")
    placement_groups = str(df["Placement Group"][i]).split(", ")
    placements = str(df["Placement"][i]).split(", ")
    #appends the class to the list.
    days.append(Deals(day, publishers, placement_groups, placements))

for profile in profiles:
    endpoint = f"curlput profile?id={profile}&member_id=958"
    print(endpoint)

#If publisher is null, check if
def checks_inventory_to_target():
    if day.publisher


count = 0
for day in days:
    if len(day.publishers) > 0:
        json = '{"profile":{"publisher_targets":['
        for publisher in day.publishers:
            #Put the if statment to get rid of any null  values
            if publisher!='nan':
            #Put the first iteration of this loop to variable then add the rest of the iteration to the variable
                if count == 0:
                    first_publisher_target = '{"action": "include", "deleted": false, "id":' + publisher + '}'
                count+=1
                second_publisher_target = '{"action": "include", "deleted": false, "id":' + publisher + '}'
                first_publisher_target= first_publisher_target+second_publisher_target
                print(first_publisher_target + ']}}')

#curlput 'profile?id=119576344&member_id=958' '{"profile":{"publisher_targets":[{"action": "include","deleted":false,"id":1397847},{"action": "include","deleted":false,"id":1203307}]}}'

#def create_target(inventory_target):
    count = 0
    for day in days:
        if len(day.inventory_target) > 0:
            json = '{"profile":{"publisher_targets":['
            for publisher in day.publishers:
                # Put the if statment to get rid of any null  values
                if publisher != 'nan':
                    # Put the first iteration of this loop to variable then add the rest of the iteration to the variable
                    if count == 0:
                        first_publisher_target = '{"action": "include", "deleted": false, "id":' + publisher + '}'
                    count += 1
                    second_publisher_target = '{"action": "include", "deleted": false, "id":' + publisher + '}'
                    first_publisher_target = first_publisher_target + second_publisher_target
                    print(first_publisher_target + ']}}')
