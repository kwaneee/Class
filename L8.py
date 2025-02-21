def traffic_light(current: str) -> str:
    if current == "red":
        next = "green"
    elif current == "green":
        next = "yellow"
    else: # current == "yellow"
        next = "red"
    return next