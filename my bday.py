import os
import sys
import time
import random
import curses

# --- CONFIGURATION ---
NAME = "VAISHNAVI"
MESSAGES = [
    "✨ Happy Birthday, {}! ✨".format(NAME),
    "🚀 Wishing you a year of scaling new heights!",
    "💡 May your code always compile on the first try.",
    "🌟 Keep shining and inspiring your network!",
    " Press 'q' to exit the celebration "
]

def draw_firework(stdscr, y, x, color_pair):
    """Animates a single firework explosion."""
    # Particle offsets for explosion phases
    phase1 = [(-1, 0), (1, 0), (0, -2), (0, 2)]
    phase2 = [(-2, -2), (-2, 2), (2, -2), (2, 2), (-1, -4), (-1, 4), (1, -4), (1, 4)]
    
    # Phase 1: Small burst
    for dy, dx in phase1:
        if 0 < y+dy < curses.LINES - 1 and 0 < x+dx < curses.COLS - 1:
            stdscr.addch(y+dy, x+dx, '*', color_pair)
    stdscr.refresh()
    time.sleep(0.1)
    
    # Clear Phase 1, Draw Phase 2: Wider burst
    for dy, dx in phase1:
        if 0 < y+dy < curses.LINES - 1 and 0 < x+dx < curses.COLS - 1:
            stdscr.addch(y+dy, x+dx, ' ')
            
    for dy, dx in phase2:
        if 0 < y+dy < curses.LINES - 1 and 0 < x+dx < curses.COLS - 1:
            stdscr.addch(y+dy, x+dx, random.choice(['.', '+', 'o']), color_pair)
    stdscr.refresh()
    time.sleep(0.15)
    
    # Clear Phase 2
    for dy, dx in phase2:
        if 0 < y+dy < curses.LINES - 1 and 0 < x+dx < curses.COLS - 1:
            stdscr.addch(y+dy, x+dx, ' ')

def celebrate(stdscr):
    # Setup terminal display properties
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(50)
    
    # Initialize colorful matrix themes
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    max_y, max_x = stdscr.getmaxyx()
    
    # Generate static LinkedIn-style digital card layout
    while True:
        stdscr.erase()
        
        # Border
        stdscr.box()
        
        # Display central messages
        start_y = max_y // 2 - len(MESSAGES) // 2
        for i, msg in enumerate(MESSAGES):
            cx = max_x // 2 - len(msg) // 2
            # Highlight the main birthday greeting in Gold/Yellow
            color = curses.color_pair(4) if i == 0 else curses.color_pair(1)
            if 0 < start_y + i < max_y - 1:
                stdscr.addstr(start_y + i, max(1, cx), msg, color | curses.A_BOLD)
        
        # Randomly trigger background fireworks
        if random.random() < 0.3:
            fy = random.randint(3, max_y - 4)
            fx = random.randint(5, max_x - 5)
            f_color = curses.color_pair(random.randint(1, 4))
            draw_firework(stdscr, fy, fx, f_color)
            
        stdscr.refresh()
        
        # Listen for quit key
        try:
            key = stdscr.getch()
            if key == ord('q') or key == ord('Q'):
                break
        except Exception:
            pass

if __name__ == "__main__":
    print("Initializing Vaishnavi's Birthday Matrix...")
    time.sleep(1)
    curses.wrapper(celebrate)
    print("\n🎉 Celebration closed! Don't forget to share the graphic banner below on LinkedIn!")