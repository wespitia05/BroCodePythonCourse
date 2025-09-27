# python alarm clock

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!!!")

            pygame.mixer.init()
            # loads music file
            pygame.mixer.music.load(sound_file)
            # plays music file
            pygame.mixer.music.play()

            # continuously plays music file until we exit the program
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        # time will update every second
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)