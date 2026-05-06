# A dictionary representing one person
person = {
    "name": "Ahmad",
    "age": 30,
    "city": "Karachi",
    "number": "0321",
    "job": "Manager"
}
 
# Access individual values
print(person["name"])
print(person["age"])
 
# Loop through all key-value pairs
for key, value in person.items():
    print(key + ": " + str(value))
 
# A list of names
team = ["Husnain", "Mahad", "Riz", "Umair"]
print(team[0])    # First item
print(len(team))  # Total count
