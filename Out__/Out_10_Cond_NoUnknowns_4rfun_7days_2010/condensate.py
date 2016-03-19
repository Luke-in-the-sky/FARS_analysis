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

# Map Mon-Thursday to one bucket, Fri-Sun to another
code_manual[translate_column_names['dayofweek']][10] = 'Mon-Thu'
code_manual[translate_column_names['dayofweek']][11] = 'Sat-Sun'
def Collaps_dayofweek(num):
    #if num in [2,3,4,5]:
    #    return 10
    return num