# ----- ----- ----- ----- -----
# Simulate Data
# ----- ----- ----- ----- -----

USER_DATA_LIST = {
    'a123': 'b456'
}

# ----- ----- ----- ----- -----
# Function
# ----- ----- ----- ----- -----

def user_login(acc, pwd):
    if (acc in USER_DATA_LIST) and (pwd == USER_DATA_LIST[acc]):
        return True
    else:
        return False