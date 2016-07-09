import calverter
import calendar

class TerroristAttack:
    eventid = 0
    iyear = 0
    imonth = 0
    country = 0
    country_txt = ""
    region = 0
    region_txt = 0
    provstate = ""
    city = ""
    latitude = 0
    longitude = 0
    summary = ""
    success = False
    suicide = False
    attacktype = 0
    attacktype_text = ""
    targtype1_txt = ""
    targsubtype1_txt = ""
    corp1 = ""
    target1 = ""
    gname = ""
    motive = ""
    weaptype1_txt = ""
    weapsubtype1 = ""
    nkill = 0
    nkillsus = 0
    nkillter = ""
    nwound = ""
    nwoundus =""
    nwoundte = ""
    property = ""
    propextent_txt = ""
    propvalue = ""
    ransom = False
    randomamt = 0
    randompaid = 0

    def __init__(self, str):
        data = str.split(",")
        try:
            self.eventid = data[0]
            self.iyear = data[1]
            self.imonth = data[2]
            self.country = data[3]
            self.country_txt = data[4]
            self.region = data[5]
            self.region_txt = data[6]
            self.provstate = data[7]
            self.city = data[9]
            self.latitude = data[10]
            self.longitude = data[11]
            self.summary = data[12]
            succ = data[13]
            if succ == 0:
                self.success = False
            else:
                self.success = True
            suic = data[14]
            if suic == 0:
                self.success = False
            else:
                self.success = True
            self.attacktype = data[15]
            self.attacktype_text = data[16]
            self.targtype1_txt = data[17]
            self.targsubtype1_txt = data[18]
            self.corp1 = data[19]
            self.target1 = data[20]
            self.gname = data[21]
            self.motive = data[22]
            self.weaptype1_txt = data[23]
            self.weapsubtype1 = data[24]
            self.nkill = data[25]
            self.nkillsus = data[26]
            self.nkillter = data[27]
            self.nwound = data[28]
            self.nwoundus = data[29]
            self.nwoundte = data[30]
            self.property = data[31]
            self.propextent_txt = data[32]
            self.propvalue = data[33]
            if data[34] == 0:
                self.ransom = False
            else:
                self.ranson = True
            self.randomamt = data[35]
            self.randompaid = data[36]
        except Exception:
            for x in data:
                print(x)
                print(len(x))

def monthToNum(shortMonth):
    return list(calendar.month_abbr).index(shortMonth)