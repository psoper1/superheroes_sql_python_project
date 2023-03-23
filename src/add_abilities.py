

# def add_abilities(name):
#     new_ability = input("What powers do they have?".center(width))
#     new_ability_split = power.split(", ")
#     new_ability_query = "SELECT name FROM ability_types"
#     ability_list = []
#     existing_abilities = execute_query(new_ability_query).fetchall()
#     for tuple in existing_abilities:
#         for ability in tuple:
#             ability_list.append(ability)

#     for a in new_ability_split:
#         if a in ability_list:
#             pass
#         else:
#             run = "INSERT INTO ability_types (name) VALUES (%s)"
#             execute_query(run, (a, ))

#         run_two = """
#         INSERT INTO abilities (hero_id, ability_type_id)
#         VALUES((SELECT id 
#         FROM heroes
#         WHERE name=%s), (SELECT id 
#         FROM ability_types
#         WHERE name=%s))
#         """
#         execute_query(run_two, (name, a, ))

 
#     print(f"{name} joins the battle!".center(width))











# def add_abilities():
#     yes_or_no = input("Does this so called 'Hero' have any special abilities? ").capitalize()
#     if yes_or_no == "Yes":
#         new_abilities = input("Great! What kind of abilities do they have?\n(Separate each ability with a comma and a space like this: ', ')\n")
#         split_abilities_result = new_abilities.split(", ")
#         add_abilities_query = "SELECT name FROM ability_types"
#         for ability in split_abilities_result:
#             run = "INSERT INTO ability_types (name) VALUES (%s)"
#             execute_query(run, (ability, ))


#     else:
#         pass