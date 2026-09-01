has_username = True
accepted_rules = True
is_blocked = False

get_access = has_username and accepted_rules != is_blocked
if get_access is True:
    print("You are getting access to the game")
else:
    print("Yo do not get access to the game")
print(get_access)
