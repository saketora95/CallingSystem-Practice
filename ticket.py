import datetime

TIME_FORMAT = '%H:%M:%S'

# ----- ----- ----- ----- -----
# Simulate Data
# ----- ----- ----- ----- -----

ticket_list = []

# ----- ----- ----- ----- -----
# Function
# ----- ----- ----- ----- -----

def get_new_ticket():
    new_number = '0001'
    if ticket_list:
        new_number = '{0:04d}'.format(int(ticket_list[-1]['number']) + 1)

    ticket_list.append({
        'number': new_number,
        'print': datetime.datetime.now(),
        'call': None,
        'done': None
    })

    return new_number

def call_ticket_by_index(index):
    call_time = datetime.datetime.now()
    ticket_list[index]['call'] = call_time

    if index > 0:
        ticket_list[index - 1]['done'] = call_time