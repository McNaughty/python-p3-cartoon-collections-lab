def roll_call_dwarves(dwarves):
    if dwarves:
        for index, dwarf in enumerate(dwarves):
            print(f"{index + 1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    capitalized_list = []
    for i in planeteer_calls:
        
        capitalized = i.capitalize()
        capitalized_list.append(capitalized + "!")
    return capitalized_list

def long_planeteer_calls(planeteer_calls):
    for i in planeteer_calls:
        if len(i) > 4:
            return True
    return False

# planeteer_calls=['axe', 'earth', 'wind', 'fire']    
# print(long_planeteer_calls(planeteer_calls))

def find_the_cheese(options):
    cheese_options = ["cheddar", "gouda", "camembert"]
    for cheese in cheese_options:
        if cheese in options:
            return cheese
    return None


# queue_details = [f"{index + 1}. {person}" for index, person in enumerate(katz_deli)]