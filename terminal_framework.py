import curses
class TerminalFramework:

    @staticmethod
    def add_text(x_pos, y_pos, text):
        
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(x_pos, y_pos, text)
        stdscr.getch()



        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    @staticmethod
    def add_colored_text(x_pos, y_pos, text, color):

        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)


        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Define color pair 1 as Red on Black
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Define color pair 2 as Green on Black
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Define color pair 3 as Blue on Black
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
        
        red = curses.color_pair(1)
        green = curses.color_pair(2)
        blue = curses.color_pair(3)
        white = curses.color_pair(4)
        yellow = curses.color_pair(5)
        magenta = curses.color_pair(6)
        cyan = curses.color_pair(7)

        if color == 'red':
            curses.curs_set(0)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(x_pos, y_pos, text, red)
            stdscr.getch()
            
        
        if color == 'green':
            curses.curs_set(0)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(x_pos, y_pos, text, green)
            stdscr.getch()
        
        if color == 'blue':
            curses.curs_set(0)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(x_pos, y_pos, text, blue)
            stdscr.getch()

        if color == 'white':
            curses.curs_set(0)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(x_pos, y_pos, text, white)
            stdscr.getch()

        if color == 'yellow':
            curses.curs_set(0)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(x_pos, y_pos, text, yellow)
            stdscr.getch()

        if color == 'magenta':
            curses.curs_set(0)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(x_pos, y_pos, text, magenta)
            stdscr.getch()

        if color == 'cyan':
            curses.curs_set(0)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(x_pos, y_pos, text, cyan)
            stdscr.getch()


        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()


    @staticmethod
    def display_options(options_list, functions_list):

        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)


        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()
        selected_option = 0

        while True:
            stdscr.clear()
            
            for i, option in enumerate(options_list):
                arrow = "▶  " if i == selected_option else " "
                if i == selected_option:
                    stdscr.addstr(i, 0, f"{arrow} {option}", curses.A_REVERSE)
                else:
                    stdscr.addstr(i, 0, option)

            stdscr.refresh()

            key = stdscr.getch()
            if key == curses.KEY_UP:
                selected_option = (selected_option - 1) % len(options_list)
            elif key == curses.KEY_DOWN:
                selected_option = (selected_option + 1) % len(options_list)
            elif key in [curses.KEY_ENTER, 10, 13]:
                functions_list[selected_option]()
                stdscr.getch()
                break


        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()


    @staticmethod
    def check_box(options, functions):
         
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)


        options.append('go')
        checkboxes = [False] * len(options)
        selected_option = 0

        
        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()

       
        while True:
            stdscr.clear()
            for i, option in enumerate(options):

                if i == selected_option:

                    if option == "go":
                        stdscr.addstr(i, 0, f"{option}", curses.A_REVERSE)

                    else:
                        checkbox_state = "[X]" if checkboxes[i] else "[ ]"
                        stdscr.addstr(i, 0, f"{checkbox_state} {option}", curses.A_REVERSE)

                else:

                    if option == "go":
                        stdscr.addstr(i, 0, f"{option}")

                    else:
                        checkbox_state = "[X]" if checkboxes[i] else "[ ]"
                        stdscr.addstr(i, 0, f"{checkbox_state} {option}")
           
            stdscr.refresh()


            key = stdscr.getch()

            if key == curses.KEY_UP:
                selected_option = (selected_option - 1) % len(options)

            elif key == curses.KEY_DOWN:
                selected_option = (selected_option + 1) % len(options)

            elif key == curses.KEY_ENTER or key in [10, 13]:
                checkboxes[selected_option] = not checkboxes[selected_option] 

            if options[selected_option] == "go" and key in [curses.KEY_ENTER, 10, 13]:
                for i, checkbox in enumerate(checkboxes):
                    if checkbox and i < len(functions):
                        functions[i]()
                    stdscr.refresh()

            if key == ord('q'):
                break
            

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    @staticmethod
    def get_user_input(x_pos, y_pos, prompt_string):

        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)


        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()
        curses.echo()  # Enable echoing user input
        stdscr.addstr(x_pos, y_pos, prompt_string)  # Display the prompt
        stdscr.refresh()  # Refresh the screen

        # Read input from the user
        user_input = stdscr.getstr(x_pos + 1, y_pos, 1000)  # Read up to 1000 characters
        input_string = user_input.decode("utf-8")  # Convert bytes to a string


        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

        return input_string

    def __getattr__(self, attr):

        if attr == "display_options":
            return self.display_options
        
        elif attr == "get_user_input":
            return self.get_user_input
        
        elif attr == "add_text":
            return self.add_text
        
        elif attr == "add_colored_text":
            return self.add_colored_text
        
        elif attr == "check_box":
            return self.check_box
        
        
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")


Terminal_Framework = TerminalFramework()  # Create an instance of the class