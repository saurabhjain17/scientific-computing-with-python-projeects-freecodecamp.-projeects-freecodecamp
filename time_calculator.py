import re
def add_time(start, duration,day=None):
   start=re.split(":| ",start)
   duration=re.split(":| ",duration)
   Day=["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
   final_time=""
   minute_modulo=(int(start[1])+int(duration[1]))//60
   final_minute=(int(start[1])+int(duration[1]))%60

   hour_modulo=(int(start[0])+int(duration[0])+minute_modulo)//12
   final_hour=(int(start[0])+int(duration[0])+minute_modulo)%12
   if start[-1].upper()=="AM":
      extend_days=hour_modulo//2
      if hour_modulo%2==0:
        final_time_zone="AM"
      else:
         final_time_zone="PM"
   if start[-1].upper()=="PM":
      extend_days=(hour_modulo+1)//2
      if hour_modulo%2==1:
        final_time_zone="AM"
      else:
         final_time_zone="PM" 
   if final_minute<10:
     final_minute="0"+str(final_minute) 
   if final_hour==0:
     final_hour=12           
   new_time=""+str(final_hour)+":"+str(final_minute)+" "+final_time_zone
   last_update=""
   if extend_days==0:
     last_update=""
   if extend_days==1:
     last_update=last_update+" (next day)"
   if extend_days>1:
     last_update=last_update+" ("+str(extend_days)+" days later)"    
   if day==None:
      return new_time+last_update
   else:
       position=Day.index(day.title())
       next_day=Day[(position+extend_days)%7]
       return new_time+", "+next_day+last_update
