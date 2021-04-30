def createNotifications(success, status_code, message, data = None, additional_data = None):
    result = {
        "success": success,
        "status_code": status_code,
        "message": message
    }

    if data is not None:
        result.update({
            "data": data
        })
    if additional_data is not None:
        result.update({
            "additional_data": additional_data
        })
    return result