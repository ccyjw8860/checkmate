from faker import Faker
from datetime import datetime, timedelta
import random

today = datetime.now()
today = today.date()

def get_start_date():
    return str(today - timedelta(days=random.randint(-10,10)))

test = get_start_date()
print(test)