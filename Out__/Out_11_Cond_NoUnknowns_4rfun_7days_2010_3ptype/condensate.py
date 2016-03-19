# Reduce categories in "Roadway Function Class"
code_manual[translate_column_names['rfun']][21] = 'Rural-Arterial'
code_manual[translate_column_names['rfun']][22] = 'Rural-Collector/Local'
code_manual[translate_column_names['rfun']][24] = 'Urban-Arterial'
code_manual[translate_column_names['rfun']][25] = 'Urban-Collector/Local'
def Collaps_rfun(num):
    if num in [1,2,3]:
        return 21
    elif num in [4,5,6,9]:
        return 22
    elif num in [11, 12, 13, 14]:
        return 24
    elif num in [15, 16, 19]:
        return 25
    elif num == 99: #unknown
        return -1
    return num


# Reduce categories in "Person Type"
code_manual[translate_column_names['ptype']][1] = 'Driver'
code_manual[translate_column_names['ptype']][2] = 'Passenger'
code_manual[translate_column_names['ptype']][3] = 'Pedestrian/Cyclist'
def Collaps_ptype(num):
    if num in [-1,19]: #other or not known
        return -1
    elif num in [2,3,4]:
        return 2
    elif num in [5,6,7,8,9,10]:
        return 3
    return num


# Map Mon-Thursday to one bucket, Fri-Sun to another
code_manual[translate_column_names['dayofweek']][10] = 'Mon-Thu'
code_manual[translate_column_names['dayofweek']][11] = 'Sat-Sun'
def Collaps_dayofweek(num):
    #if num in [2,3,4,5]:
    #    return 10
    return num