# ============== BRMM Bankside Rakaia Motorkhana Mavens ADMIN DATA ==============
# Student Name: Naomi Wu
# Student ID : 1158161
# ===============================================================================
 
# import datetime       Delete this line (just dealing with ages, not dates of birth, and seconds, not timevalues)

col_drivers = {'Driver ID':int,'First Name':str,'Surname':str,'Category':str,'Age':int,'Caregiver':str}
db_drivers = {
             32:('Hank','Barnard',None,None,None),
             78:('Tuku','Whaitiri',None,None,None),
             109:('Tina','Fei',None,None,None),
             111:('Andy','Capp',None,None,None),
             180:('Luke','Cooper',None,None,None),
             181:('Edward','Cooper','J',19,None),
             182:('Elaine','Cooper','J',16,180),
             183:('David','Cooper',None,None,None),
             199:('Wanjun','Long',None,None,None),
             220:('Andy','Pickles',None,None,None),
             221:('Don','Zwart',None,None,None),
             222:('Kayleigh','Peacock',None,None,None),
             223:('Dylan','Thomas','J',12,225),
             224:('Kiri','Smith','J',15,225),
             225:('Sonja','Pickles',None,None,None)
             }

col_runs = {'Run ID':int,'Course':str,'Driver':str,'Time':float,'Cones':int,'WD':bool,'Run Total':str}
db_runs = {
            1:('A',180,41.5,None,0),
            2:('A',78,51.44,None,1),
            3:('A',223,50.41,3,0),
            4:('A',182,42.71,None,0),
            5:('A',222,53.1,None,0),
            6:('A',109,38.32,2,0),
            7:('A',199,46.46,None,0),
            8:('A',181,48.53,None,0),
            9:('A',32,46.22,2,1),
            10:('A',224,38.78,None,0),
            11:('A',220,None,None,None),
            12:('B',109,42.03,None,0),
            13:('B',199,40.87,None,0),
            14:('B',181,52.35,None,0),
            15:('B',32,47.3,None,0),
            16:('B',224,None,None,None),
            17:('B',180,None,None,None),
            18:('B',78,41.21,None,0),
            19:('B',223,46.78,None,0),
            20:('B',182,46.37,None,0),
            21:('B',222,44.88,None,0),
            22:('B',220,None,None,None),
            23:('C',181,35.92,None,0),
            24:('C',199,42.4,None,0),
            25:('C',32,53.35,2,0),
            26:('C',223,47.15,None,0),
            27:('C',180,43.25,None,0),
            28:('C',182,52.35,None,0),
            29:('C',224,None,None,None),
            30:('C',78,46.37,None,1),
            31:('C',220,None,None,None),
            32:('C',222,53.32,None,0),
            33:('C',109,49.84,None,0)
        }

