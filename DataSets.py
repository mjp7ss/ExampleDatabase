def hittingFilters(data, value, value2, value3, value4, value5, value6, value7):
    if value == 'All Hitters':
        filtered_data = data
    else:
        filtered_data = data[data.Batter == value]
    if value2 == 'All Pitcher Handedness':
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.PitcherThrows == value2]
    if value3 == "All Opponents":
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.AwayTeam == value3]
    if value4 == "All Pitchers":
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.Pitcher == value4]
    if value5 == "All Counts":
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.Count == value5]
    if value6 == "All Seasons":
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.Year == value6]
    if value7 == "All Dates":
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.Date == value7]
    return filtered_data

def pitchingFilters(data,value,value2,value3,value4,value5,value6,value7):
    if value == 'All Pitchers':
        filtered_data = data
    else:
        filtered_data = data[data.Pitcher == value]

    if value2 == 'All Dates':
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.Date == value2]
    if value3 == 'All Seasons':
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.Year == value3]
    if value4 == 'All Hitters':
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.Batter == value4]
    if value5 == 'All Sides':
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.BatterSide == value5]
    if value6 == 'All Counts':
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.Count == value6]
    if value7 == 'All Opponents':
        filtered_data = filtered_data
    else:
        filtered_data = filtered_data[filtered_data.AwayTeam == value7]

    return filtered_data


def catcherFilters(data, value):
    if value == 'All Catchers':
        filtered_data = data
    else:
        filtered_data = data[data.Catcher == value]
    return filtered_data

def umpireFilters(data, value):
    if value == 'All Umpires':
        filtered_data = data
    else:
        filtered_data = data[data.Umpire == value]
    return filtered_data