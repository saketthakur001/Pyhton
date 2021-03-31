import pysrt
subs = pysrt.open('C:\\Users\\saket\\Desktop\\preson break\\Prison.Break.S01E01.480p.English.Esubs.MoviesFlix.srt', encoding='iso-8859-1')

f = open("C:\\Users\\saket\\Desktop\\srt\\test.srt", "a")

acceleration = 0.0409932992
n = 0
t = 0
for sub in subs:
    t += 1
    n = len((str(sub).partition('\n')[0]))-1
    sub = str(sub)
    print(t, n)
    #subtitle start time---------
    start_hour = sub[n+2:n+4]
    start_min = sub[n+5:n+7]
    start_sec = sub[n+8:n+10]
    #subtitle end time-----------
    end_hour = sub[n+19:n+21]
    end_min = sub[n+22:n+24]
    end_sec = sub[n+25:n+27]

    sec = (int(start_hour) * 60 *60) + (int(start_min) * 60) + (int(start_sec)) * acceleration

    if sec >= 3600:
        minute = sec / 60
        start_hour = '0' + str(minute / 60)[0]
        start_min = "0"+str(round(float(str(minute/60)[1:])*60))[-2:]
        start_sec = sec % 60
        print(start_hour,start_min,start_sec)

    elif sec >= 60 and sec < 3600:
        minute = (sec / 60)
        start_min = "0"+str(minute)[0:2].strip('.')[-2:]
        start_sec = "0" + str(round(sec % 60))[-2:]
        print(start_hour,start_min,start_sec)

    elif sec < 60:
        start_sec = '0'+str(round(sec))[-2:]
        print(start_hour,start_min,start_sec)
    if t==25:
        break
# print(sec)