import jwt
import base64
import time
import argparse
import os
import requests
from dotenv import dotenv_values, load_dotenv

##################################################################
# Used For: Mux Tools
############################
parser = argparse.ArgumentParser()
parser.add_argument('playbackID', help="The signed playbackID to create the token")
args = parser.parse_args()
playbackID = args.playbackID
############################

# ############################
# # GLOBALs
# ############################
apiKeys = load_dotenv("apiKeys.env")
data_signing_key_id = str(os.getenv("data_signing_key_id"))
data_private_key_base64 = str(os.getenv("data_private_key_base64")) 
private_key = base64.b64decode(data_private_key_base64)
# # ############################

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

def createTheToken(playbackID):
  token = {
      'sub': playbackID,
      'aud': 'playback_id',
      'exp': int(time.time()) + 3600, # 1 hour
      'kid': data_signing_key_id
  }

  encoded = jwt.encode(token, private_key, algorithm="RS256")
  
  return(encoded)

try:
  finalToken = createTheToken(playbackID)
  finalTokenURL = f"https://stats.mux.com/counts?token={finalToken}"
  viewsResponse = requests.get(finalTokenURL).json()

  print(f"\n{color.GREEN}Token:\n\n{color.END}{finalToken}\n")
  print(f"{color.GREEN}URL:\n\n{color.END}{finalTokenURL}\n")
  print(f"{color.GREEN}Response:\n\n{color.END}{viewsResponse}\n")
except:
  print(Exception)
