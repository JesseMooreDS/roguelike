from datetime import date
import pandas as pd

def current_date():
    today = date.today()
    return today

today_list = []

def todays_entry():
    
    current = current_date()
    current = pd.to_datetime(current)
    today_list.append(current)
    

todays_entry()
