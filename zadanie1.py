def range_postcodes(in_start_postcode, in_stop_postcode):

    first_start_postcode = (in_start_postcode[0:2])
    second_start_postcode = (in_start_postcode[3:7])

    start_postcode = int(first_start_postcode+second_start_postcode)


    first_stop_postcode = (in_stop_postcode[0:2])
    second_stop_postcode = (in_stop_postcode[3:7])

    stop_postcode = int(first_stop_postcode+second_stop_postcode)


    postcodes = []
    list_code = "00-000";
    for code in range (start_postcode+1, stop_postcode):
        if code<10:
            list_code = "00-00"+str(code)
            postcodes.append(list_code)
        elif code<100:
            list_code = "00-0"+str(code)
            postcodes.append(list_code)
        elif code<1000:
            list_code = "00-"+str(code)
            postcodes.append(list_code)
        elif code<10000:
            list_code = list_code[0:1]+str(code)[0]+'-'+str(code)[1:4]
            postcodes.append(list_code)
        else:
            list_code = str(code)
            list_code = list_code[0:2]+'-'+list_code[2:6]
            postcodes.append(list_code)

    return postcodes
        
    
