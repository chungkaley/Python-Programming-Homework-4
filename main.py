from Date import Date
from Event import Event

event_list = []

def add_event():
    event_name = input("Event name: ")
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    start_hour = int(input("Start hour: "))
    end_hour = int(input("End hour: "))

    event_date = Date(day, month, year)
    new_event = Event(event_name, start_hour, end_hour, event_date)

    for event in event_list:
        if event.has_overlap(new_event):
            print(f"Cannot add {new_event}. It overlaps with {event}")
            return

    event_list.append(new_event)
    print(f"{new_event} added to event list.")

def cancel_event():
    event_name = input("Event name: ")
    for event in event_list:
        if event.event_name == event_name:
            event_list.remove(event)
            print(f"{event} removed from event list.")
            return
    print(f"{event_name} not found in event list.")

def view_events():
    for event in event_list:
        print(event)

while True:
    print("Choose an option:")
    print("1. Add an event")
    print("2. Cancel an event")
    print("3. View all events")
    print("4. Quit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        add_event()
    elif choice == "2":
        cancel_event()
    elif choice == "3":
        view_events()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
