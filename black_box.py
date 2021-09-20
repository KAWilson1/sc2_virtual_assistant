#Purpose: Misc helper functions for app

def parse_input(lines):
    """
    Parses lines from text files or from the tkinter.Text widget

    Returns:
        build_step: tuple of length 2
            build_step[0]: int
                Number of seconds to delay audio queue from start time 
            build_step[1]: list
                Contains a list of all audio queues to play
            build_step[1][0]: string
                string of the audio queue file with no extension and in snake_case
            Examples:
                (150, ["barracks"])
                (165, ["factory", "command_center"])
    """
    formatted_lines = []
    for line in lines:
        line = line.rstrip() #remove \n if present
        broken_lines = line.split() #split at spaces
        #A valid build step must have a time and an action, meaning the length
        #must be at least 2
        if len(broken_lines) >= 2:
            #Convert from "m:ss" to integer seconds
            time_in_sec = int(broken_lines[0].split(":")[0])*60 + int(broken_lines[0].split(":")[1])

            formatted_line = (time_in_sec, broken_lines[1:])
            formatted_lines.append(formatted_line)
    
    return formatted_lines
