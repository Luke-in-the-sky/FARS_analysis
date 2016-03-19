
# Reduce categories in "Roadway Function Class"
code_manual[translate_column_names['rfun']][21] = 'Rural-Arterial/Collector'
code_manual[translate_column_names['rfun']][23] = 'Rural-Local'
code_manual[translate_column_names['rfun']][24] = 'Urban-Arterial/Collector'
code_manual[translate_column_names['rfun']][26] = 'Urban-Local'
def Collaps_rfun(num):
    if num in [1,2,3,4,5]:
        return 21
    elif num in [6,9]:
        return 23
    elif num in [11, 12, 13, 14, 15]:
        return 24
    elif num in [16,19]:
        return 26
    elif num == 99: #unknown
        return -1
    return num
    
# Map Mon-Thursday to one bucket, Fri-Sun to another
code_manual[translate_column_names['dayofweek']][10] = 'Mon-Thu'
code_manual[translate_column_names['dayofweek']][11] = 'Sat-Sun'
def Collaps_dayofweek(num):
    return num