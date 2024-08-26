import time

try:
    timer_hour = int(input("Enter the hour: "))
    timer_minute = int(input("Enter the minute: "))
    timer_second = int(input("Enter the second: "))
except:
    print("Please enter a valid number.")

total_time = timer_hour * 3600 + timer_minute * 60 + timer_second

input(
    f"Press enter to start timer for {timer_hour:02}:{timer_minute:02}:{timer_second:02}"
)

while total_time:
    seconds = total_time % 60
    mins = int(total_time / 60) % 60
    hours = int(total_time / 3600) % 60
    print(f"{hours:02}:{mins:02}:{seconds:02}", end="\r")
    time.sleep(1)
    total_time -= 1


print("Timer completed!")
