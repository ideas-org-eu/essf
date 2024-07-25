def validate_data(data):
    if not data:
        raise ValueError("No data provided")
    if not isinstance(data, dict):
        raise TypeError("Data should be in dictionary format")
    return True
