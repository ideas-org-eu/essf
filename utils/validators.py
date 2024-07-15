def validate_data(data):
    """
    Validate the data received from external sources or user inputs.
    """
    if not data:
        raise ValueError("No data provided")
    if not isinstance(data, dict):
        raise TypeError("Data should be in dictionary format")
    # Add more specific checks as necessary
    return True
