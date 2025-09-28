import csv
from io import StringIO

def get_headings(csv_line: str) -> list[str]:
    """
    Parse the first line of a CSV string and return a list of headings.
    Handles quoted fields and trims whitespace.

    Args:
        csv_line (str): A comma-separated string representing CSV headings.

    Returns:
        list[str]: A list of headings with whitespace stripped.
    """
    if not csv_line.strip():
        return []

    reader = csv.reader(StringIO(csv_line))
    headings = next(reader, [])
    return [heading.strip() for heading in headings]
