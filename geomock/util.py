
def microparse(value: str):
    try:
        return int(value)
    except ValueError:
        return float(value)
    except ValueError:
        return value

