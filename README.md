# jwtCreator
CLI tool for easy JWT token creation for help debugging Mux support cases. 

I got very tired of editing a single script for a single token. Using this as a jump off point for ways to make troubleshooting signed assets easier.

Add the flag (i.e. -h) of whatever type of JWT token you wish to create. The default is a VIDEO token.

```
usage: jwtCreator.py [-h] [-v] [-s] [-t] [-g] playbackID

positional arguments:
  playbackID        The signed playbackID to create the token

optional arguments:
  -h, --help        show this help message and exit
  -v, --video       Create a VIDEO token [ DEFAULT ]
  -s, --storyboard  Create a STORYBOARD token
  -t, --thumbnail   Create a THUMBNAIL token
  -g, --gif         Create a GIF token
```
![CLI Image](https://dl.dropboxusercontent.com/s/j7xozs66wf4z2pl/mux-jwtCreator.gif?dl=0)
