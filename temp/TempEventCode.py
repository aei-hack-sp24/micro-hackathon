import pandas as pd

def parse_schedule_data(schedule_data):
    schedule = {}
    for index, row in schedule_data.iterrows():
        date = row['Date']
        if date not in schedule:
            schedule[date] = []
        schedule[date].append({'Start': row['Start'], 'Finish': row['Finish']})
    return schedule

def add_events_to_schedule(events_data, class_schedule):
    for event in events_data:
        event_date = event['Date']
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
    
    events_data = [
        {"ID": 3, "Date": "4/18/2024", "Start": "Afternoon", "Finish": "Evening", "Title": "Coffee Hangout", "Tags": "Food, Social"},
        {"ID": 4, "Date": "4/19/2024", "Start": "Morning", "Finish": "Afternoon", "Title": "Super Micro Technology", "Tags": "Technology"},
        # Add more events here...
    ]
    
    updated_schedule = add_events_to_schedule(events_data, elizabeth_schedule)
    
    updated_schedule_rows = []
    for date, events in updated_schedule.items():
        for event in events:
            updated_schedule_rows.append({'Date': date, 'Start': event['Start'], 'Finish': event['Finish'], 'Title': event.get('Title', ''), 'Tags': event.get('Tags', '')})
    
    updated_schedule_df = pd.concat([pd.DataFrame(updated_schedule_rows), pd.DataFrame(columns=['Date', 'Start', 'Finish', 'Title', 'Tags'])], ignore_index=True)
    
    updated_schedule_df.to_csv('updated_schedule.csv', index=False)
