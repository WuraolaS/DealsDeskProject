# The JSON for the curl call looks like this
#curlput 'profile?id=119576344&member_id=958' '{"profile":{"publisher_targets":[{"action": "include","deleted":false,"id":1397847},{"action": "include","deleted":false,"id":1203307}]}}'
# '{"profile":{"publisher_targets":[{"action": "include","deleted":false,"id":1397847},{"action": "include","deleted":false,"id":1203307}]}}'
'''
{
    "profile": {
        "publisher_targets": [
            {
                "action": "include",
                "deleted": false,
                "id": 1203307
            },
            {
                "action": "include",
                "deleted": false,
                "id": 2345353
            }
        ]
    }
}
'''

data = {}

for day in days:
    if(day.publishers): # MIGHT return false if empty
        inventory_target = {}
        # Create a dictionary for the curlput
        # This is going to be parsed into JSON later
        data = {
                "profile": {
                    "publisher_targets": []
                    }
                }
        for publisher in day.publishers:
            if publisher != 'nan':
                inventory_target = {
                        "action": "include",
                        "deleted": False,
                        "id": publisher
                        }
                data["publisher_targets"].append(inventory_target)
        break

print(data)
