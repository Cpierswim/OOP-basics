class AlarmClock:

    def __init__(self, initial_time: str) -> None:
        self.time = initial_time
        self.alarm_on = False
        self.alarm = "12:00am"

    def set_time(self) -> None:
        self.time = input("What time would you like to set the current time to: ")

    def toggle_alarm(self) -> None:
        self.alarm_on = not self.alarm_on

    def set_alarm_time(self) -> None:
        self.alarm = input("What time would you like to set the alarm to: ")
        print(f"The alarm has been set to {self.alarm} and the current time is {self.time}")