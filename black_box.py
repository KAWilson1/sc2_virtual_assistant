#Purpose: Play audio queues at specified times
import playsound
import time

def parse_file_input(file_path):
    """
    Parses files that follow defined schema into tuple of (Timing, Audio Queue(s))
    """
    #Open file
    with open(file_path) as f:
        lines = f.readlines()
    
    #Format file contents
    formatted_lines = []
    for line in lines:
        broken_lines = line.split() #split at spaces
        formatted_line = (broken_lines[0], broken_lines[1:])
        formatted_lines.append(formatted_line)
    
    return formatted_lines

        

def play_audio_queues(pairings):
    """
    Params:
        pairings: tuple of length 2
            pairings[0]: str
                min:sec 
                Timing for associated audio queue(s) to play
            pairings[1]: list
                Contains a list of all audio queues to play
            pairings[1][0]: string
                string of the audio queue file with no extension and in snake_case
            Examples:
                ("2:30", ["barracks"])
                ("2:45", ["factory", "command_center"])
    """
    last_queue_played = 0 #time of last audio queue in seconds
    for pair in pairings:
        #Calculate when to play next sound queue
        broken_time = pair[0].split(":")
        current_timing = int(broken_time[0]) * 60 + int(broken_time[1]) #in seconds
        difference_from_last_time = current_timing - last_queue_played
        
        #Sleep until time to play sound queue
        time.sleep(difference_from_last_time)

        #Play sound queue(s)
        time_offset = 0 #Increases by 2 seconds per audio queue played
        for audio_queue in pair[1]:
            playsound.playsound("audio_queues/" + audio_queue + ".mp3")
            time_offset += 2
        
        #Update last_queue_played
        last_queue_played = current_timing + time_offset #adjust for time of audio queue


file_data = parse_file_input("sample_data/build1.txt")
print(file_data)
play_audio_queues(file_data)