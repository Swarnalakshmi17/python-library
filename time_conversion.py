import datetime
def seconds_to_minutes(seconds):

    return seconds / 60
def minutes_to_seconds(minutes):
    
    return minutes * 60
def hours_to_days(hours):
    return hours / 24
def days_to_hours(days):
     return days * 24
def minutes_to_hours(minutes):
    return minutes/60

def hours_to_minutes(hours):
    return hours*60
def seconds_to_hours(seconds):
    return seconds/3600
def hours_to_seconds(hours):
    return hours*3600

def time_difference(start_time, end_time):
    
    start = datetime.datetime.strptime(start_time, "%H:%M")  
    end = datetime.datetime.strptime(end_time, "%H:%M")      
    
    
    difference = end - start
    return difference.total_seconds() / 3600  
