import math
def get_century(year):
    if type(year) != int:
        year = int(year)
    if year > 10000:
        return 'Too far in future'
    
    century = math.ceil(year/100)
    print(f'{century} + "<<<"')
    if century >= 11 and century <= 13:
        return str(century) + 'th'
    else: 
        match century % 10:
            case 1:
                return str(century) + 'st'
            case 2:
                return str(century) + 'nd'
            case 3:
                return str(century) + 'rd'
            case _:
                return str(century) + 'th'





# print (get_century(1))
