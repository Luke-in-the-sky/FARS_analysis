
# Reduce categories in "Roadway Function Class"
code_manual[translate_column_names['rfun']][21] = 'Rural'
code_manual[translate_column_names['rfun']][24] = 'Urban'
def Collaps_rfun(num):
    if num in [1,2,3, 4, 5, 6,9]:
        return 21
    elif num in [11, 12, 13, 14, 15, 16, 19]:
        return 24
    elif num == 99: #unknown
        return -1
    return num