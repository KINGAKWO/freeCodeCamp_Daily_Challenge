def number_of_files(file_size, unit, drive_capacity_gb):
    """
    Calculate how many files can fit on a drive.

    Args:
        file_size (float): The size of one file.
        unit (str): The unit of the file size ("B", "KB", "MB", "GB").
        drive_capacity_gb (float): Drive capacity in gigabytes.

    Returns:
        int: The number of whole files that fit on the drive.

    Raises:
        ValueError: If inputs are invalid.
    """
    if file_size <= 0:
        raise ValueError("File size must be greater than zero.")
    if drive_capacity_gb <= 0:
        raise ValueError("Drive capacity must be greater than zero.")

    # Normalize case
    unit = unit.upper()

    # Conversion table to bytes
    conversions = {
        "B": 1,
        "KB": 1000,
        "MB": 1000**2,
        "GB": 1000**3,
    }

    if unit not in conversions:
        raise ValueError("Invalid unit. Use 'B', 'KB', 'MB', or 'GB'.")

    # Convert file size to bytes
    file_size_bytes = file_size * conversions[unit]

    # Convert drive capacity to bytes
    drive_capacity_bytes = drive_capacity_gb * conversions["GB"]

    return int(drive_capacity_bytes // file_size_bytes)
