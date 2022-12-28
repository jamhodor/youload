# https://www.youtube.com/watch?v=UeSd_2aLVoE
# https://www.youtube.com/watch?v=5slT4I8w41E

import os
import pafy
import apafy

target_folder = os.getcwd() + "\\videos\\"
videoref = "https://www.youtube.com/watch?v=5slT4I8w41E"


video = apafy.new(videoref)

video.getbest().download(quiet=False, filepath=target_folder)

