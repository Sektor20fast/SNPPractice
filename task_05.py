from datetime import datetime, timedelta

def date_in_future(integer):
    if not isinstance(integer, int):
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    future_date = datetime.now() + timedelta(days=integer)
    return future_date.strftime('%d-%m-%Y %H:%M:%S')

print(date_in_future([]))
print(date_in_future(2))
