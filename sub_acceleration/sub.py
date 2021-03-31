import pysrt
episode_name = 'Prison Break - 1x11 - And Then There Were 7.DVD.en.srt'
subs = pysrt.open("C:\\Users\\saket\\Desktop\\preson break\\" + episode_name, encoding='iso-8859-1')

file_link = "C:\\Users\\saket\\Desktop\\srt\\test.srt"
f = open(file_link, "a")

times = 0
acceleration = 109 / 2537 # video and sub difference divided by last subtitle time in sec
for sub in subs:
    print('what is happening')
    print(sub)
    sub = str(sub)
    n = len((str(sub).partition('\n')[0]))
################################--STARING--#########################################################################
################################----SUB---#########################################################################
    st_hour_ori_formate =(sub[n+1:n+3])
    st_min_ori_formate = (sub[n+4:n+6])
    st_sec_ori_formate = (sub[n+7:n+9])
    
    st_hour = int(sub[n+1:n+3])
    st_min = int(sub[n+4:n+6])
    st_sec = int(sub[n+7:n+9])
    # print(st_hour,'hour', st_min,'min',st_sec,'sec')

    st_hour_in_sec = st_hour*60*60
    st_min_in_sec = st_min*60

    time_in_sec = st_hour_in_sec + st_min_in_sec + st_sec
    time_to_hesten = time_in_sec * acceleration
    start_time_hesten = time_in_sec + time_to_hesten
    # print(time_in_sec,'+',time_to_hesten,'=',start_time_hesten, 'time hesten')

################################--ENDING--#########################################################################
################################---SUB---#########################################################################
    end_hour_ori_formate =sub[n+18:n+20]
    end_min_ori_formate = sub[n+21:n+23]
    end_sec_ori_formate = sub[n+24:n+26]
# String to int----------------------
    end_hour = int(sub[n+18:n+20])
    end_min = int(sub[n+21:n+23])
    end_sec = int(sub[n+24:n+26])

    end_hour_in_sec = end_hour*60*60
    end_min_in_sec = end_min*60

    end_time_in_sec = end_hour_in_sec + end_min_in_sec + end_sec
    end_time_hesten = end_time_in_sec + time_to_hesten

    print(st_hour_ori_formate+':'+st_min_ori_formate+':'+st_sec_ori_formate+' '*10+end_hour_ori_formate+':'+end_min_ori_formate+':'+end_sec_ori_formate)

################################--STARING--#########################################################################
################################----SUB---#########################################################################
# Start-Hour_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST_-_FIRST
    if start_time_hesten >= 3600:
        st_hour = int(start_time_hesten / 60 / 60)
        st_hour_ori_formate = ('0'+str(st_hour))[-2:]
# Start-Min-------------------------------------------first condition
        st_min = int((start_time_hesten - st_hour * 60 * 60)/60)
        st_min_ori_formate = ("0"+str(st_min))[-2:]
# start-Sec-------------------------------------------first condition
        st_sec = int(start_time_hesten % 60)
        st_sec_ori_formate = ('0'+str(st_sec))[-2:]
        # print(st_hour_ori_formate+':'+st_min_ori_formate+':'+st_sec_ori_formate+' '*10+end_hour_ori_formate+':'+end_min_ori_formate+':'+end_sec_ori_formate)


# SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND-_-SECOND
    elif start_time_hesten >= 60:
# Min--------------------------------------------second condition
        st_min = int(start_time_hesten/60)
        print(start_time_hesten)
        print(st_min)
        st_min_ori_formate = ('0'+str(st_min))[-2:]
        print(st_min_ori_formate)
# Sec--------------------------------------------second condition
        st_sec = int(start_time_hesten % 60)
        st_sec_ori_formate = ('0'+str(st_sec))[-2:]
        # print(st_hour_ori_formate+':'+st_min_ori_formate+':'+st_sec_ori_formate+' '*10+end_hour_ori_formate+':'+end_min_ori_formate+':'+end_sec_ori_formate)


# Sec---------------------------------------------third condition
    else:
        st_sec = int(start_time_hesten)
        st_sec_ori_formate = ('0'+str(st_sec))[-2:]
        # print(st_hour_ori_formate+':'+st_min_ori_formate+':'+st_sec_ori_formate+' '*10+end_hour_ori_formate+':'+end_min_ori_formate+':'+end_sec_ori_formate)
    if end_time_hesten >= 3600:
# End-Hour--------------------------------------------first condition
        end_hour = int(end_time_hesten / 60 / 60)
        end_hour_ori_formate = ('0'+str(end_hour))[-2:]

        end_min = int((end_time_hesten - end_hour * 60 * 60)/60)
        end_min_ori_formate = ('0'+str(end_min))[-2:]

        end_min = int(end_time_hesten % 60)
        end_sec_ori_formate = ('0'+str(end_sec))[-2:]

        print(st_hour_ori_formate+':'+st_min_ori_formate+':'+st_sec_ori_formate+' '*10+end_hour_ori_formate+':'+end_min_ori_formate+':'+end_sec_ori_formate)

# End Min----------------------------------------
    elif end_time_hesten > 60:
        end_min = int(end_time_hesten / 60)
        end_min_ori_formate = ('0'+str(end_min))[-2:]

        end_sec = int(end_time_hesten % 60)
        end_sec_ori_formate = ('0'+str(end_sec))[-2:]
        print(st_hour_ori_formate+':'+st_min_ori_formate+':'+st_sec_ori_formate+' '*10+end_hour_ori_formate+':'+end_min_ori_formate+':'+end_sec_ori_formate)

    else:
        end_sec = int(end_time_hesten)
        end_sec_ori_formate = ('0'+str(end_sec))[-2:]
        print(st_hour_ori_formate+':'+st_min_ori_formate+':'+st_sec_ori_formate+' '*10+end_hour_ori_formate+':'+end_min_ori_formate+':'+end_sec_ori_formate)
    print('\n\n')
    f.write(sub[0:n+1]+st_hour_ori_formate+':'+st_min_ori_formate+":"+st_sec_ori_formate+sub[n+9:n+18]+end_hour_ori_formate+":"+end_min_ori_formate+":"+end_sec_ori_formate+sub[n+26:]+'\n')