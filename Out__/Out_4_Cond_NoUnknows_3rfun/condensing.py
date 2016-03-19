# Reduce categories in "Roadway Function Class"
code_manual[translate_column_names['rfun']][21] = 'Arterial'
code_manual[translate_column_names['rfun']][22] = 'Collector'
code_manual[translate_column_names['rfun']][23] = 'Local'
def Collaps_rfun(num):
    if num in [1,2,3, 11, 12, 13, 14]:
        return 21
    elif num in [4,5, 15]:
        return 22
    elif num in [6,9,16,19]:
        return 23
    elif num == 99: #unknown
        return -1
    return num