def select_features_and_reduce_cardinality(data):

    # Select interesting stuff
    # --------------

    # Load Code manual
    import pickle
    code_manual = pickle.load( open( "..\CodeManuals\CodeManual.p", "rb" ) )

    # Select interesting features and map them to their respective
    #   names in the code manual
    translate_column_names = {
    #'driverdrowsy' : 'Drowsy driver',
    #'arrtime' : 'Arrival time EMS',
    'arrhr'   : 'Arrival hour EMS',
    'accdate' : 'Crash Date (mmddyyyy)',
    'acchr'   : 'Crash Hour',
    #'alcres'  : 'Alcohol test results',  #Knowledge of alcres is mostly unknown and biased towards fatalities
    #'manncol' : 'Manner of Collision',
    'deathdate' : 'Death Date',
    #'injury'  : 'Injury severity',
    'ptype'   : 'Person Type',
    'druginv' : 'Police Reported Drug Involvement',
    #'heavytruck': 'Large Truck Related',
    #'schlbus' : 'School Bus Related',
    'sex' : 'Sex',
    #'race' : 'Race',
    #'reljuncinter' : 'Relation To Junction: Within Interchange Area',
    'atmcond': 'Atmospheric Condition (1)',
    #'holiday' : 'Holiday Related',
    #'nhs' : 'National Highway System',
    #'hispanic' : 'Hispanic',
    'rfun' : 'Roadway Function Class',
    'lightcond' : 'Light Condition',
    'speeding' : 'Speeding',
    'dayofweek' : 'Day Of Week',
    #'latitude' : 'Latitude',
    #'longitude': 'Longitude'
    }

    also_interesting = ['age']

    labelsOfInter = list(translate_column_names.keys())
    labelsOfInter.extend(also_interesting)



    # Reduce dimensionality
    # ---------------------

    # Collapse some features values
    # ------------

    # Categorize on number of Fatalities
    def NumFatalitiesToCategory(num):
        if num <3:
            return 1
        elif (num>=3) and (num<6):
            return 2
        return 3

    # Reduce categories in 'Light Condition'
    code_manual[translate_column_names['lightcond']][11] = 'Dawn/Dusk'
    code_manual[translate_column_names['lightcond']][12] = 'Dark'
    def Collaps_lightcond(num):
        if num == 4 or num == 5:
            return 11
        elif num in [6,8,9]: #unknown
            return -1
        return num


    # Reduce categories in "Holiday Related"
    if 'holiday' in labelsOfInter:
        code_manual[translate_column_names['holiday']][-1] = 'Not Holiday or Unknow date'
        code_manual[translate_column_names['holiday']][1] = 'Was Holiday'
    def Collaps_holiday(num):
        if num >0:
            return 1
        return num


    # Reduce categories in "Atmospheric Condition (1)"
    code_manual[translate_column_names['atmcond']][1] = 'Clear or Cloudy'
    code_manual[translate_column_names['atmcond']][2] = 'Precipitation'
    code_manual[translate_column_names['atmcond']][4] = 'Snow'
    code_manual[translate_column_names['atmcond']][6] = "Severe \
    Crosswinds, Blowing Sand, Soil, Dirt",
    def Collaps_atmcond(num):
        if num in [8, 0, 98, 99]: #other or not known
            return -1
        elif num in [1,10]:
            return 1
        elif num in [2,12,3]:
            return 2
        elif num in [6,7]:
            return 6
        return num


    # Reduce categories in "Hispanic"
    if 'hispanic' in labelsOfInter:
        code_manual[translate_column_names['hispanic']][10] = 'Is Hispanic'
        def Collaps_hispanic(num):
            if num in [-1,99,0]: #other or not known
                return -1
            elif num in range(1,7):
                return 10
            return num


    # Reduce categories in "Race"
    if 'race' in labelsOfInter:
        code_manual[translate_column_names['race']][30] = 'American Indian or Hawaiian'
        code_manual[translate_column_names['race']][31] = 'Asian (not Indian)'
        code_manual[translate_column_names['race']][32] = 'Indian'
        def Collaps_race(num):
            if num in [-1, 0, 98, 99, 97]: #other or not known
                return -1
            elif num in [1,2]:
                return num+27
            elif num in [3,6]:  
                return 30
            elif num in [4,5,7,28,38,48,58,68,78]:  
                return 31
            elif num in [18,19]:  
                return 32
            return num

    # Map sex=1 ('male') to sex=0 (for SparseDataFrame efficiency)
    code_manual[translate_column_names['sex']][0] = 'Male'
    def Collaps_sex(num):
        if num==1:
            return 0
        return num


    # Reduce categories in "Roadway Function Class"
    code_manual[translate_column_names['rfun']][21] = 'Rural-Arterial road'
    code_manual[translate_column_names['rfun']][22] = 'Rural-Collector/Local road'
    code_manual[translate_column_names['rfun']][24] = 'Urban-Arterial road'
    code_manual[translate_column_names['rfun']][25] = 'Urban-Collector/Local road'
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


    # Reduce categories in "alcres"  
    def Collaps_alcres(num):
        if num in [-1,95,96,97,98,99]: #other or not known
            return -1
        elif num in [0]:
            return 0
        elif num in [1,2,3,4,5]:
            return 5
        elif num in [6,7,8]:
            return 8
        return 9

    # Map Mon-Thursday to one bucket, Fri-Sun to another
    code_manual[translate_column_names['dayofweek']][10] = 'Mon-Thu'
    code_manual[translate_column_names['dayofweek']][11] = 'Sat-Sun'
    def Collaps_dayofweek(num):
        #if num in [2,3,4,5]:
        #    return 10
        return num


    # Reduce categories in "EMS Arrival time"
    def Collaps_arrtime(num):
        if num >= 8800: # unknown
            return -1
        return num      

    # Reduce categories in "Age"
    translate_column_names['agegr'] = "Age group"
    def Create_agegr_var(num):
        if num>=0 and num <20 :
            return 1
        if num>=20 and num <40 :
            return 2
        if num>=40 and num <60 :
            return 3
        if num>=60:
            return 4
        return num // 20

    translate_column_names['killed'] = "Person died from accident"
    # Reduce categories in "Death date"
    def Create_fatality_var(num):
        if num >= 88888888: # survived
            return 0
        return 1      # died

        
        
        
    # Reduce dimensionality
    # --------------------------------------------

    # apply reduction of categories cardinality
    def Collaps_categoricals(data):
        if 'lightcond' in data.keys():
            data.lightcond = data.lightcond.apply(Collaps_lightcond )
        if 'rfun' in data.keys():
            data.rfun      = data.rfun.apply(Collaps_rfun  )
        if 'holiday' in data.keys():
            data.holiday   = data.holiday.apply(Collaps_holiday )
        if 'atmncond' in data.keys():
            data.atmcond   = data.atmcond.apply(Collaps_atmcond )
        if 'ptype' in data.keys():
            data.ptype     = data.ptype.apply(Collaps_ptype )
        if 'hispanic' in data.keys():
            data.hispanic  = data.hispanic.apply(Collaps_hispanic )
        if 'race' in data.keys():
            data.race      = data.race.apply(Collaps_race)
        if 'sex' in data.keys():
            data.sex       = data.sex.apply(Collaps_sex)
        if 'dayofweek' in data.keys():
            data.dayofweek = data.dayofweek.apply(Collaps_dayofweek)
        if 'arrtime' in data.keys():
            data.arrtime   = data.arrtime.apply(Collaps_arrtime)
        if 'alcres' in data.keys():
            data.alcres    = data.alcres.apply(Collaps_alcres)
        if 'deathdate' in data.keys():
            data['killed'] = data.deathdate.apply(Create_fatality_var)
            labelsOfInter.append('killed')
        if 'age' in data.keys():
            data['agegr'] = data.age.apply(Create_agegr_var)
            labelsOfInter.append('agegr')
            
            
            
    # Map different types of 'unknown' to a single number
    unknown = {'druginv': [8,9],
               'nhs'    : [9],
               'reljuncinter': [8,9],
               'dayofweek': [-1,9],
               'sex'     : [8,9],
               'age'     : [-1, 998, 999],
               'atmcond' : [8, 0, 98, 99],
               'druginv' : [-1, 8, 9],
               'race'    : [-1, 0, 98, 99, 97],
               'hispanic': [-1,99,0],
               'ptype'   : [-1,19],
               'rfun'    : [-1, 99],
               'lightcond': [-1,7,6,8,9],
               'acchr'   : [-1, 88, 99],
               'arrhr'   : [-1, 88, 99],
               'manncol' : [-1, 98, 99, 11],
               'injury'  : [-1, 9]
              }

    # collaps all keys for 'unknown' into '-1' value
    def Collapse_unknowns(data):
        for feature in unknown.keys():
            try:
                data[feature] = data[feature].apply(lambda x: 
                                                    x if x not in unknown[feature] 
                                                    else -1)
            except KeyError:
                pass
        return data
        
        
    # Make it happen!!
    data = data[labelsOfInter].applymap(lambda x: -1 if x == '.' else int(x))
    # prepare dataset
    Collaps_categoricals(data)
    labelsOfInter.remove('deathdate')  # created a dependent variable: 'killed'
    labelsOfInter.remove('age')        # created a dependent variable: 'agegr'
    data = data[labelsOfInter]
    data = Collapse_unknowns(data)

    
    return(code_manual, translate_column_names, labelsOfInter, data )