#!/usr/bin/python3
#GME ERPIN
import curses
import time

def main(stdscr):
    try:
        curses.curs_set(0)
        stdscr.nodelay(1)
        stdscr.timeout(10)
        gambar = [
            "⢀        ⡴⢹⠙⣄",
            "        ⣸   ⠘ ⢸⡀",
            "        ⡇      ⣇",
            "        ⡧⢤⣤⣤⠴⢻",
            "        ⡇       ⢸",
            "        ⡇       ⢸",
            "⠀⠀⣀⠤⢄⣰⠀⠀⠀⠀⣸⠂⠉⠲⡄⠀",
            "⠈⣹⠁⠀⠀⠈⣧⠀⠀⠘⠊⠀⠀⠐⢺⠂",
            "⠐⢻⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠒",
            "⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢱⠋⠀",
            "⠀⠀⠈⠻⠦⠴⡤⠒⠈⠀⠒⠒⠚⠧⠀⠀",
            "⠀⠀ ⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀"
        ]

        max_y, max_x = stdscr.getmaxyx()
        pos_x = (max_x // 2) - (len(gambar[0]) // 2)
        pos_y = max_y

        direction_y = -0.2

        while True:
            pos_y = max_y
            while pos_y > -len(gambar):
                stdscr.clear()
                for i, line in enumerate(gambar):
                    if 0 <= int(pos_y) + i < max_y:
                        stdscr.addstr(int(pos_y) + i, pos_x, line)
                
                stdscr.refresh()

                pos_y += direction_y

                time.sleep(0.01)

                key = stdscr.getch()
                if key != -1:
                    return
    except KeyboardInterrupt:
        pass

curses.wrapper(main)
        
