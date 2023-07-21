def transform(legacy_data):
    data = {}
    for key, value in legacy_data.items():
        [data.update({x.lower(): key}) for x in value]
    return data
