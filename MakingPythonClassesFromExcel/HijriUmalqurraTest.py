import calverter

cal = calverter.Calverter()
jd = cal.gregorian_to_jd(2014,4 , 23)
print(jd)
print(cal.jd_to_islamic(jd))
print((cal.jd_to_gregorian(cal.islamic_to_jd(day=1,month=1,year=1436))))