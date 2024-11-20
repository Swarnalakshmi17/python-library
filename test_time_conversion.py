
import time_conversion

def main():
    print("Welcome to the Time Conversion Library!")

    
    seconds = float(input("Enter time in seconds: "))
    print(f"{seconds} seconds = {time_conversion.seconds_to_minutes(seconds)} minutes")


    minutes = float(input("Enter time in minutes: "))
    print(f"{minutes} minutes = {time_conversion.minutes_to_seconds(minutes)} seconds")

    
    hours = float(input("Enter time in hours: "))
    print(f"{hours} hours = {time_conversion.hours_to_days(hours)} days")


    days = float(input("Enter time in days: "))
    print(f"{days} days = {time_conversion.days_to_hours(days)} hours")

    
    minutes = float(input("Enter time in minutes: "))
    print(f"{minutes} minutes = {time_conversion.minutes_to_hours(minutes)} hours")


    hours = float(input("Enter time in hours: "))
    print(f"{hours} hours = {time_conversion.hours_to_minutes(hours)} minutes")

    seconds = float(input("Enter time in seconds: "))
    print(f"{seconds} seconds = {time_conversion.seconds_to_hours(seconds)} hours")

    
    hours = float(input("Enter time in hours: "))
    print(f"{hours} hours = {time_conversion.hours_to_seconds(hours)} seconds")

    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    print(f"Time difference between {start_time} and {end_time}: {time_conversion.time_difference(start_time, end_time)} hours")

main()