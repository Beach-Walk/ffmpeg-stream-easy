import os
##
##FFMPEG MUST BE IN PATH
##
import random

out_dir = "output"
in_dir = "input"
# pkt_size is for VLC, ttl is for multicast hops
url = 'udp://192.168.1.250:1234?pkt_size=1316&ttl=13'
repeat = "True"
shuffle = "True"
menu = True

while menu:
    print("=========== OPTIONS ===========")
    print("URL: " + url)
    print("Repeat: " + str(repeat))
    print("Shuffle: " + str(shuffle))
    print("===============================")
    print("1.) Play all in output dir")
    print("2.) Convert all in input dir (for fast streaming)")
    print("3.) Options")

    option = input("Please select an option\n")

    if "1" in option:
        output_list = []  # list of file objects
        ffmpeg_com_list = []  # list of crafted ffmpeg commands

        for filename in os.scandir(out_dir):
            if filename.is_file():
                output_list.append(filename)

        # craft command
        for i in output_list:
            ffmpeg_com_list.append('ffmpeg -re -i "' + str(i.path) + '" -c copy -f mpegts "' + url + '"')

        if shuffle == "True":
            random.shuffle(ffmpeg_com_list)

        # execute command
        for i in ffmpeg_com_list:
            os.system(i)

        while repeat == "True":
            if shuffle == "True":
                random.shuffle(ffmpeg_com_list)

            # execute command
            for i in ffmpeg_com_list:
                os.system(i)



    elif (option == "2"):
        input_list = []  # list of file objects
        ffmpeg_com_list = []  # list of crafted ffmpeg commands

        for filename in os.scandir(in_dir):
            if filename.is_file():
                input_list.append(filename)

        # craft command
        for i in input_list:
            ffmpeg_com_list.append(
                'ffmpeg -y -i "' + str(i.path) + '" -vcodec libx264 -f mpegts "' + str(out_dir) + "/" + str(
                    i.name) + '"')

        # execute command for each file
        for i in ffmpeg_com_list:
            os.system(i)

    elif option == "3":
        print("1.) URL: " + url)
        print("2.) Repeat: " + str(repeat))
        print("3.) Shuffle: " + str(shuffle))
        print("4.) Exit")

        option = input("Please select an option to edit\n")
        if option == "1":
            url = input("Enter a new URL\n")
        elif option == "2":
            repeat = input("Please enter a bool of 'True' or 'False' for repeat\n")
        elif option == "3":
            shuffle = input("Please enter a bool of 'True' or 'False' for shuffle\n")
