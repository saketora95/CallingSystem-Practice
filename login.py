TEMP_ACCOUNT_DATA = {
    'a123': 'b456'
}

def counter_login(acc, pwd):
    if (acc in TEMP_ACCOUNT_DATA) and (pwd == TEMP_ACCOUNT_DATA[acc]):
        return True
    else:
        return False