import jwt
import base64
import time
import argparse
import os
from dotenv import dotenv_values, load_dotenv

##################################################################
# Used For: Internal Mux Support Tools
# How: usage: jwt_test.py [-h] [-v] [-s] [-t] [-g] playbackID
  # positional arguments:
  #   playbackID        The signed playbackID to create the token

  # optional arguments:
  #   -h, --help        show this help message and exit
  #   -v, --video       Create a VIDEO token
  #   -s, --storyboard  Create a STORYBOARD token
  #   -t, --thumbnail   Create a THUMBNAIL token
  #   -g, --gif         Create a GIF token
# Logs: n/a
# Requirements: python 3.6+, API tokens
# Revision History: 
# v1. Creation
#
# Additions to be made: 
# 

############################
parser = argparse.ArgumentParser()
parser.add_argument('playbackID', help="The signed playbackID to create the token")
parser.add_argument('-v', '--video', help='Create a VIDEO token [ DEFAULT ]', action='store_true', default=True) #defaults to video being true
parser.add_argument('-s', '--storyboard', help='Create a STORYBOARD token', action='store_true')
parser.add_argument('-t', '--thumbnail', help='Create a THUMBNAIL token', action='store_true')
parser.add_argument('-g', '--gif', help='Create a GIF token', action='store_true')
args = parser.parse_args()
# create list of tokens requested: True and False
argsList = {"video": args.video, "storyboard": args.storyboard, "thumbnail": args.thumbnail, "gif": args.gif}
playbackID = args.playbackID
############################

############################
# GLOBALs
############################
apiKeys = load_dotenv("") # enter file name of .env in cwd 
video_signing_key_id = str(os.getenv("video_signing_key_id")) #in the env file have them named like this
video_private_key_base64 = str(os.getenv("video_private_key_base64")) # <<-- 
private_key = base64.b64decode(video_private_key_base64)
# ############################

############################
# Add Support for Color
############################
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

############################
# Create the token
############################

def createTheToken(playbackID, aud):
  token = {
      'sub': playbackID,
      'exp': int(time.time()) + 3600, # 1 hour
      'aud': aud,
      'kid': video_signing_key_id
  }
  json_web_token = jwt.encode(token, private_key, algorithm="RS256")
  
  return(json_web_token)

for k, v in argsList.items(): # run through args list
  if v is True: #if a flag is True, create that type of token
    if k == "video":
      print(f'\n{color.GREEN}Video Token: {color.END}\n')
      token = createTheToken(playbackID, aud="v")
      print(token)
      print(f"\n{color.YELLOW}Video URL:{color.END}\n")
      print(f"https://stream.mux.com/{playbackID}.m3u8?token={token}\n")
    elif k == "gif":
      print(f'\n{color.GREEN}Gif Token: {color.END}\n')
      token = createTheToken(playbackID, aud="g")
      print(token)
      print(f"\n{color.YELLOW}Gif URL:{color.END}\n")
      print(f"https://image.mux.com/{playbackID}/animated.gif?token={token}")
    elif k == "storyboard":
      #https://docs.mux.com/guides/video/create-timeline-hover-previews
      print(f'\n{color.GREEN}Storyboard Token: {color.END}\n')
      token = createTheToken(playbackID, aud="s")
      print(token)
      print(f"\n{color.YELLOW}Storyboard URL:{color.END}\n")
      print(f"https://image.mux.com/{playbackID}/storyboard.png?token={token}")
    elif k == "thumbnail":
      print(f'\n{color.GREEN}Thumbnail Token: {color.END}\n')
      token = createTheToken(playbackID, aud="t")
      print(token)
      print(f"\n{color.YELLOW}Thumbnail URL:{color.END}\n")
      print(f"https://image.mux.com/{playbackID}/thumbnail.png?token={token}")
    else:
      print(Exception)
