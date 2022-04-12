# jwtCreator
CLI tool for easy JWT token creation for Mux.com

Add the flag (i.e. -h) of whatever type of JWT token you wish to create. The default is a VIDEO token.

Requirements:
* Access to your Mux environmental keys (insert into the apiKeys.env file)
* Python 3.6+

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
