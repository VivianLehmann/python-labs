import datetime as dt

# modul datetime : menschliche kalenderlogik (tage,wochen,zeitzonen)
# zeitzonen - steuerung
# ideal für : datenbankeinträge, terminplanungen, fristen berechnen , benutzerinformationen

# wichtig : zeitpunkt, zeitinterval

# timedelta : representiert zeitspanne oder dauer(zeitinterval)

duration = dt.timedelta(
    weeks = 12,
    days = 50,
    hours = 4,
    minutes = 2,
    seconds = 27,
    milliseconds = 45,
    microseconds = 12
)
print(duration)
print(duration.days)
print(duration.seconds)
print(duration.microseconds)
print(duration.total_seconds())

duration1 = dt.timedelta(weeks=4)
duration2 =dt.timedelta(days=22)
duration3 = dt.timedelta(weeks=1,days=4)
print(duration1 + duration2 + duration3)
print(duration*5)

# date objects
datum = dt.date(year = 1997,month=3,day=12)
print(datum)
heute = dt.date.today()
print(heute)
time_difference = heute - datum
print(type(time_difference))

heute = heute.replace(year=2028)
print(heute)

print(heute.weekday())         # montag ist 0 , sonntag ist 6

# TIME OBJECTS
t1 = dt.time(hour = 3, minute= 41, second= 12)
print(t1)
t2 = dt.time(hour = 3, minute= 41, second= 12, microsecond=453)
print(t2)
print(t2.hour)

t3 = dt.time.min    # mitternacht
print(t3)

# DATETIME OBJECTS
dt1 = dt.datetime(year=2021, month=2, day= 3, hour=10, minute=13, second=45)
dt2 = dt.datetime(2022,4,2,10,4,32)
abstand = dt2 - dt1
print(abstand)
print(abstand.days / 365)

# konventierung
date1 = dt1.date()     # konventierung datetime -> date
time1 = dt1.time()     # konvertierung datetime -> time
print(date1)
print(time1)

dt3 = dt.datetime.combine(date1,time1)

# text in 'echtes' datum umwandeln(parsing)
datum_string = "24.12.2026 18:30"

# %d = tag, %m = monat , %Y = jahr, %H = stunde,%M = minute
echtes_datum = dt.datetime.strptime(datum_string, "%d.%m.%Y %H:%M")
print(echtes_datum)

us_zeit ="11:45 PM"
parsed_zeit = dt.datetime.strptime(us_zeit,"%I:%M %p")
print(parsed_zeit)

print(f"24-Format: {parsed_zeit.strftime("%H %M")}")

jahr, kw, wochentag = heute.isocalendar()
print(f"wir befinden uns in der kalenderwoche (kw): {kw}")

#####################################################################################

