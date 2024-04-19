import pandas as pd

def parse_schedule_data(schedule_data):
    
    sched = pd.DataFrame(data=schedule_data)
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
    
    #filename = "studentsched.csv"
    
    #with open(filename, 'w') as file:
    for x in range(7): 
            #print(df['Date'].iloc[x])
        if df['Date'].iloc[x] in sched.values: 
                #put that date into csv  
            df.loc[x, 'Start'] = sched['Start'].iloc[x]
            df.loc[x, 'Finish'] = sched['Finish'].iloc[x]
            df.loc[x, 'Title'] = sched['Title'].iloc[x]
            df.loc[x, 'Tags'] = sched['Tags'].iloc[x]
                    
    return df;
    #df.to_csv(file, index=False)  




def add_events_to_schedule(events_data, class_schedule):
    for event in events_data:
        event_date = events_data['Date'].iloc[event] #event['Date']
        event_start_time = event['Start']
        event_end_time = event['Finish']
        
        if event_date in class_schedule:
            class_slots = class_schedule[event_date]
            event_fits = True
            for slot in class_slots:
                class_start_time = slot['Start']
                class_end_time = slot['Finish']
                if (event_start_time < class_end_time) and (event_end_time > class_start_time):
                    event_fits = False
                    break
            
            if event_fits:
                class_schedule[event_date].append(event)
    
    return class_schedule


if __name__ == "__main__":
    # Load Elizabeth's schedule data from "ElizabethSchedule.csv"
    elizabeth_schedule_data = pd.read_csv('ElizabethSchedule.csv')
    elizabeth_schedule = parse_schedule_data(elizabeth_schedule_data)
    
    event_data_schedule = pd.read_csv('CSUNschedule.csv')
    event_schedule = parse_schedule_data(event_data_schedule)
    
    add_events_to_schedule(event_schedule, elizabeth_schedule)
    
    
