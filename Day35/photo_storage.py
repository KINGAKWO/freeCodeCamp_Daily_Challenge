def number_of_photos(photo_size_mb: float, drive_capacity_gb: float) -> int:
    """
    Calculate how many whole photos can fit on a hard drive.

    Args:
        photo_size_mb (float): Size of one photo in megabytes (MB).
        drive_capacity_gb (float): Capacity of the drive in gigabytes (GB).

    Returns:
        int: Number of whole photos that can fit.

    Raises:
        ValueError: If photo_size_mb <= 0 or drive_capacity_gb <= 0.
    """
    if photo_size_mb <= 0:
        raise ValueError("photo_size_mb must be greater than 0")
    if drive_capacity_gb <= 0:
        raise ValueError("drive_capacity_gb must be greater than 0")

    total_capacity_mb = drive_capacity_gb * 1000
    num_photos = total_capacity_mb // photo_size_mb
    return int(num_photos)

# Test the function
photo_size_mb = 5
drive_capacity_gb = 10
num_photos = number_of_photos(photo_size_mb, drive_capacity_gb)
print(f"You can store {num_photos} whole photos on the drive.")