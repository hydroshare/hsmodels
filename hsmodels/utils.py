from datetime import datetime


def to_coverage_dict(value):
    value_dict = {}
    for key_value in value.split(";"):
        if "=" in key_value:
            k, v = key_value.split("=")
            value_dict[k.strip()] = v.strip()
    return value_dict


def to_coverage_value_string(value: dict):
    return "; ".join(
        [
            "=".join([key, val.isoformat() if isinstance(val, datetime) else str(val)])
            for key, val in value.items()
            if key != "type" and val
        ]
    )
