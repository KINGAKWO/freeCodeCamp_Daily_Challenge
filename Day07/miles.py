def mile_pace(miles, duration):
    minutes, seconds = map(int, duration.split(":"))
    total_seconds = minutes * 60 + seconds   
    
    avg_seconds_per_mile = total_seconds // miles  
    pace_minutes, pace_seconds = divmod(avg_seconds_per_mile, 60)
    
    return f"{pace_minutes:02d}:{pace_seconds:02d}"


print(mile_pace(3, "24:00"))  
