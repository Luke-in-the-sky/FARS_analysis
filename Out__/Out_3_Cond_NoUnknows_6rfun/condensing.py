# Reduce categories in "Roadway Function Class"
code_manual[translate_column_names['rfun']][21] = 'Rural-Arterial'
code_manual[translate_column_names['rfun']][22] = 'Rural-Collector'
code_manual[translate_column_names['rfun']][23] = 'Rural-Local'
code_manual[translate_column_names['rfun']][24] = 'Urban-Arterial'
code_manual[translate_column_names['rfun']][25] = 'Urban-Collector'
code_manual[translate_column_names['rfun']][26] = 'Urban-Local'
def Collaps_rfun(num):
    if num in [1,2,3]:
        return 21
    elif num in [4,5]:
        return 22
    elif num in [6,9]:
        return 23
    elif num in [11, 12, 13, 14]:
        return 24
    elif num in [15]:
        return 15
    elif num in [16,19]:
        return 26
    elif num == 99: #unknown
        return -1
    return num