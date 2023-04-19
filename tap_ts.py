import time
import curses
from datetime import timedelta

def main(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)

    start_time = time.monotonic()
    filename = "timestamps.txt"

    stdscr.addstr("Press Enter to record a timestamp. Press Space to pause/resume. Press Ctrl+C to stop.\n")

    paused = False
    pause_start_time = 0

    try:
        with open(filename, "w") as file:
            while True:
                c = stdscr.getch()

                if c == ord(' '):
                    paused = not paused
                    if not paused:
                        start_time += time.monotonic() - pause_start_time
                        pause_elapsed_time = time.monotonic() - pause_start_time
                        pause_formatted_time = str(timedelta(seconds=round(pause_elapsed_time)))
                        pause_minutes, pause_seconds = pause_formatted_time.split(':')[-2:]
                        stdscr.addstr(f"Resumed at [{pause_minutes}:{pause_seconds}]\n")
                    else:
                        pause_start_time = time.monotonic()
                        stdscr.addstr("Paused\n")

                if not paused and c == ord('\n'):
                    elapsed_time = time.monotonic() - start_time
                    formatted_time = str(timedelta(seconds=round(elapsed_time)))
                    minutes, seconds = formatted_time.split(':')[-2:]
                    file.write(f"[{minutes}:{seconds}]\n")
                    file.flush()
                    stdscr.addstr(f"Timestamp [{minutes}:{seconds}] recorded.\n")

                time.sleep(0.1)

    except KeyboardInterrupt:
        stdscr.addstr("\nScript stopped. Check the 'timestamps.txt' file for your timestamps.\n")
        stdscr.refresh()
        time.sleep(2)

if __name__ == "__main__":
    curses.wrapper(main)
