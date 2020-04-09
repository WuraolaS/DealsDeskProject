import sys
import json
import pandas as pd

df = pd.read_excel(r'/Users/wsonubi/Desktop/Deals_Desk_Project/CFBcron_Practice.xlsx',
                   sheet_name='Deal_targeting_pratice')
days = []
profiles = []

for i in range(1, len(sys.argv)):
    profiles.append(sys.argv[i])


class Deals:
    """description"""

    def __init__(self, day, publishers, placement_groups, placements, start_time, end_time):
        self.publishers = publishers
        self.day = day
        self.placement_groups = placement_groups
        self.placements = placements
        self.start_time = start_time
        self.end_time = end_time


# Deals is indexed, the length of the list of deals = number of rows
# What we're considering is the different days
# For each row, create a new deal class


for i in range(len(df)):
    day = str(df["Day"][i])
    publishers = str(df["Publisher"][i]).split(", ")
    placement_groups = str(df["Placement Group"][i]).split(", ")
    placements = str(df["Placement"][i]).split(", ")
    start_time = str(df["Start Time"][i])
    end_time = str(df["End Time"][i])
    # appends the class to the list.
    days.append(Deals(day, publishers, placement_groups, placements, start_time, end_time))


# why  do we have days as an argument
# def target_profiles(days):
#     data = {
#         "profile": {}
#     }

#This part works
data = {
       "profile": {}
     }
for day in days:
    day_part = {
        "day": day.day,
        "start_hour": day.start_time,
        "end_hour": day.end_time
    }
    data["profile"]["daypart_targets"] = [day_part]
    print(data)
    if(day.publishers): # MIGHT return false if empty
                inventory_target = {}
                targets = []
                for publisher in day.publishers:
                    if publisher != 'nan':

                        inventory_target = {
                                "action": "include",
                                "deleted": False,
                                "id": publisher
                                }
                        targets.append(inventory_target)
                        data["profile"]["publisher_targets"] = targets
                        print(targets)

#'{"profile":{"publisher_targets":[{"action":"include", "deleted": false, "id": "1397847"}, {"action": "include", "deleted": false, "id": "1203307"}]},"daypart_targets":[{"day": "monday","start_hour":2,"end_hour":6},
#{"day": "thursday","start_hour": 3,"end_hour":5}]}'

#The ideal publisher and day part targeting curl call:
#curlput 'profile?id=119051777&member_id=958' '{"profile":{"publisher_targets":[{"action":"include", "deleted": false, "id": "1397847"}, {"action": "include", "deleted": false, "id": "1203307"}]},"daypart_targets":[{"day": "monday","start_hour":2,"end_hour":6},
#{"day": "thursday","start_hour": 3,"end_hour":5}]}'

# def target_profiles(days):
#     data = {
#         "profile": {}
#     }
#
#     for day in days:
#         day_part = {
#             "day": day.day,
#             "start_hour": day.start_time,
#             "end_hour": day.end_time
#         }
#         data["profile"]["daypart_targets"] = [day_part]
#         if (day.publishers):  # MIGHT return false if empty
#             inventory_target = {}
#             targets = []
#             for publisher in day.publishers:
#                 if publisher != 'nan':
#                     inventory_target = {
#                         "action": "include",
#                         "deleted": False,
#                         "id": publisher
#                     }
#         targets.append(inventory_target)
#
#         data["profile"]["publisher_targets"] = targets
#
#         print('Marshalling data -> JSON')
#         return json.dumps(data)
#
# print(target_profiles(days))
#         if (day.placement_groups):
#             inventory_target = {}
#             targets = []
#             for placement_group in day.placement_groups:
#                 if placement_group != 'nan':
#                     inventory_target = {
#                         "action": "include",
#                         "deleted": False,
#                         "id": placement_group
#                     }
#                     targets.append(inventory_target)
#                     data["profile"]["site_targets"] = targets
#                     return json.dumps(data)
#         if (day.placements):
#             inventory_target = {}
#             targets = []
#             for placement in day.placements:
#                 if placement != 'nan':
#                     inventory_target = {
#                         "action": "include",
#                         "deleted": False,
#                         "id": placement
#                     }
#                     targets.append(inventory_target)
#             data["profile"]["placement_targets"] = targets
#             return json.dumps(data)
#
#         print("error")
#         return
#
#
# raw_data = target_profiles(days)
# print(raw_data)
#
# for profile in profiles:
#     # I added single quotes around the curl and the json
#     endpoint = "curlput \'profile?id=" + profile + "&member_id=958\' " + "\'" + raw_data + "\'"
#     print(endpoint)

# The ideal publisher and day part targeting curl call:
# curlput 'profile?id=119051777&member_id=958' '{"profile":{"publisher_targets":[{"action":"include", "deleted": false, "id": "1397847"}, {"action": "include", "deleted": false, "id": "1203307"}]},"daypart_targets":[{"day": "monday","start_hour":2,"end_hour":6},
# {"day": "thursday","start_hour": 3,"end_hour":5}]}'



# current ouptput
# Marshalling data -> JSON
# {"profile": {"daypart_targets": [{"day": "Wednesday", "start_hour": "1", "end_hour": "6"}], "publisher_targets": [{"action": "include", "deleted": false, "id": "1397847"}, {"action": "include", "deleted": false, "id": "1203307"}]}}
# curlput 'profile?id=119576344&member_id=958' '{"profile": {"daypart_targets": [{"day": "Wednesday", "start_hour": "1", "end_hour": "6"}], "publisher_targets": [{"action": "include", "deleted": false, "id": "1397847"}, {"action": "include", "deleted": false, "id": "1203307"}]}}'
# curlput 'profile?id=119576363&member_id=958' '{"profile": {"daypart_targets": [{"day": "Wednesday", "start_hour": "1", "end_hour": "6"}], "publisher_targets": [{"action": "include", "deleted": false, "id": "1397847"}, {"action": "include", "deleted": false, "id": "1203307"}]}}'

