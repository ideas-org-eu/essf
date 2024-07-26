def validate_input(data):
    if not isinstance(data, dict):
        return False, "Input data should be a dictionary."
    if "name" not in data or not isinstance(data["name"], str):
        return False, "Input data should have a 'name' field of type string."
    if "value" not in data or not isinstance(data["value"], (int, float)):
        return False, "Input data should have a 'value' field of type integer or float."
    return True, ""
