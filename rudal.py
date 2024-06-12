#!/usr/bin/python3
#GME ERPIN
import curses
import time

def main(stdscr):
    try:
        # Mengatur pengaturan awal terminal
        curses.curs_set(0)  # Menyembunyikan kursor
        stdscr.nodelay(1)   # Non-blocking input
        stdscr.timeout(10)  # Update setiap 10ms

        # Gambar sederhana yang akan digerakkan
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

        # Posisi awal gambar di tengah horizontal, bawah vertikal
        max_y, max_x = stdscr.getmaxyx()
        pos_x = (max_x // 2) - (len(gambar[0]) // 2)
        pos_y = max_y  # Memulai dari luar batas bawah

        direction_y = -0.2  # Gerakan vertikal ke atas

        while True:
            pos_y = max_y  # Reset ke luar batas bawah
            while pos_y > -len(gambar):
                stdscr.clear()
                # Menggambar gambar di posisi saat ini
                for i, line in enumerate(gambar):
                    if 0 <= int(pos_y) + i < max_y:
                        stdscr.addstr(int(pos_y) + i, pos_x, line)
                
                stdscr.refresh()

                # Perbarui posisi gambar
                pos_y += direction_y

                # Tunggu sebentar sebelum update berikutnya
                time.sleep(0.01)  # Interval lebih kecil untuk pergerakan lebih halus

                # Keluar jika ada input (misalnya tombol q)
                key = stdscr.getch()
                if key != -1:
                    return
    except KeyboardInterrupt:
        # Menangani penghentian manual (Ctrl+C)
        pass

curses.wrapper(main)
