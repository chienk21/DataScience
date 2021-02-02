import json
import requests

#writing file
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

#dump takes two positional arguments
# 1. data object serialized
# 2. file-like object to which the bytes will be written
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

print('')

#write to native python string object
json_string = json.dumps(data)
print(json_string)

#indentions
print(json.dumps(data))
print(json.dumps(data, indent=4))

print('')


# deserializing json does not always get the same thing as the serialization you put in
blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand) #tuple
decoded_hand = json.loads(encoded_hand) #list

print(blackjack_hand == decoded_hand)
#false 
print(type(blackjack_hand))
#tuple
print(type(decoded_hand))
#list
print(blackjack_hand == tuple(decoded_hand))
#true

print('')




#deserializing data
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data)

    json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(data)
print('')






#request
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print(todos == response.json())

print(type(todos))

print(todos[:10])

print('')
#manipulating JSON data as a python object
# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)
print(max_users)

s = "s" if len(users) > 1 else ""
print(f"user{s} {max_users} completed {max_complete} TODOs")

# of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)



#encoding custom types

class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

json.dumps(9 + 5j, default=encode_complex)

#json.dumps(Elf, default=encode_complex) NOT SERIALIZABLE

print(json.dumps(2 + 5j, cls=ComplexEncoder))
#[2.0,5.0]

encoder = ComplexEncoder()
encoder.encode(3 + 6j)
#[3.0,6.0]
