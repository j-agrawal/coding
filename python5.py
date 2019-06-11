import datetime
name= input("enter your name:")
print("your name is :"+name)
x= datetime.datetime.now()
curhour= x.hour
if(curhour>=00 and curhour<=12):
    print(" :) :) :) good morning " +name)
elif(curhour>12 and curhour<=5):
    print(" :) :) :) good afternoon " +name)
elif(curhour>5 and curhour <=8):
    print(" :) :) :) good evening " +name)
else:
    print(" :) :) :) good night " +name)
