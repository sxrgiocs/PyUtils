def convert_seconds(seconds):
    """
    Function used to convert seconds to the format of hours, minutes, and seconds

    Parameters
    ----------
    seconds : int
        Seconds which will be converted

    Returns
    -------
    converted_time : str
        String representing the time in HHh MMm SSs

    Notes
    -----
    This function takes seconds as input and computes the hours and minutes
    using time conversions. Hours are computed using a conversion factor of
    3600 and the minutes taking its remainder and dividing it by a 60. If the
    hours or minutes are 0, they are not returned.
    """

    # Convert the seconds to integer
    seconds = int(seconds)

    # Compute hours and minutes
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)

    # Create the converted time string
    converted_time = ""

    if hours > 0:
        converted_time += f"{hours:02d}h "

    if minutes > 0 or hours > 0:
        converted_time += f"{minutes:02d}m "

    converted_time += f"{seconds:02d}s"

    return converted_time
