''' Emergency helper functions '''

def get_copago(copago_amount):
    ''' Convert copago into 1 == 100 '''
    return int(copago_amount * 100) if copago_amount != 0 else 0

