def number_of_videos(video_size,video_unit,drive_size,drive_unit):
    if video_size <= 0:
        raise ValueError("video_size must be greater than 0")
    if drive_size <= 0:
        raise ValueError("drive capacity must be greater than zero.")
    #normalize unit case
    unit_drive = drive_unit.upper()
    print(unit_drive)
    unit_video = video_unit.upper()
    #valid units
    valid_video_units = {"KB","MB","GB"}
    valid_drive_units = {"GB","TB"}
       # Handle invalid cases first
    if video_unit not in valid_video_units:
        return "Invalid video unit"
    if drive_unit not in valid_drive_units:
        return "Invalid drive unit"
    print(unit_video)
    #conversion table to bytes
    conversions = {
        "B": 1,
        "KB": 1000,
        "MB": 1000**2,
        "GB": 1000**3,
        "TB": 1000**4,
    }

    if unit_drive not in conversions:
        raise ValueError("Invalid unit. Use 'B','KB','MB','GB',or 'TB'.")
    if unit_video not in conversions:
        raise ValueError("Invalid unit")

    #convert file size to bytes
    video_size_bytes = video_size*conversions[unit_video]
    print(video_size_bytes)
    #convert drive capacity to bytes
    drive_capacity_bytes = drive_size*conversions[unit_drive]
    print(drive_capacity_bytes)

    print(int(drive_capacity_bytes//video_size_bytes))
    return int(drive_capacity_bytes//video_size_bytes)

number_of_videos(2000, "B", 1, "TB")



