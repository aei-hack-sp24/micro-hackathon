import pandas as pd
import csv
#import database

# Student will input or import their schedule
# Student will select event topics they’re interested in
# Schedule will print all events relevant to interests selected by student and fits into schedule

schedule = pd.read_csv('Eschedule.csv')

sched = pd.DataFrame(data=schedule)
#print(sched)

data = { 
"ID": ['1','2','3','4','5','6','7'],
"Date": ['4-21-2024','4-22-2024','4-23-2024','4-24-2024','4-25-2024','4-26-2024','4-27-2024'],
"Start": ['','','','','','',''],
"Finish": ['','','','','','',''],
"Title": ['','','','','','',''],
"Tags": ['','','','','','','']
}

df = pd.DataFrame(data=data)

filename = "studentsched.csv"

with open(filename, 'w') as file:
    writer = csv.writer(file)
    
    for x in range(7): 
        print(df['Date'].iloc[x])
        if df['Date'].iloc[x] in sched.values: 
            #put that date into csv  
            df.loc[x, 'Start'] = sched['Start'].iloc[x]
            df.loc[x, 'Finish'] = sched['Finish'].iloc[x]
            df.loc[x, 'Title'] = sched['Title'].iloc[x]
            df.loc[x, 'Tags'] = sched['Tags'].iloc[x]
                
#export csv
df.to_csv('studentsched.csv', index=False)  
                
#input:
    #tags
    #class schedule for the week
    #any specific blocked out times


#int tag = 0
#int tag = 0 
#int tag = 0
#int tag = 0
#front end will switch these on when ticked on the website?


#-----------------------------------------------------------------
#    EVENT SCHEDULE

#for day of week
    #if no events: pass     
    #else: for events tagged with that day  (4/21, 4/22, 4/23, etc)
            #if tag == 1 && time is "free"
                #apply to calendar

#-----------------------------------------------------------------

#export to csv 
