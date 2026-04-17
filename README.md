# CheapDeck
Like a Stream Deck, but cheap

![Alt text](https://raw.githubusercontent.com/pocketvince/CheapDeck/main/cheapdeck_logo.png?raw=true "Logo")

## Description
The idea is to use it like a Stream Deck: you click on the icons, and it runs your scripts/programs

<video src="https://raw.githubusercontent.com/pocketvince/CheapDeck/main/video.mp4" controls="controls" autoplay="autoplay" loop="loop" muted="muted" style="max-width: 100%;"></video>

## Installation
1. Install Python dependencies

```shell
PS C:\Users\xxxx> pip.exe install flask
```

## Setup
![Alt text](https://raw.githubusercontent.com/pocketvince/CheapDeck/main/picture.jpg?raw=true "picture")

• Place your files/scripts in the same folder as the main script, and add an image with the same name to serve as the icon, for example: `my_app.exe` -> `my_app.jpg`, `my_shortcut.lnk` -> `my_shortcut.png`

• Config: When you run the script, it starts a small web server, If you go to the default address, it will display your IP, to get access to the interface, add your IP to the allowed list.

• Exclude files: Place the names of the programs or scripts you want to ignore here.

```shell
# Config
ALLOWED_IPS = ['127.0.0.1','192.168.0.164','192.168.0.203','192.168.0.206'] #ip authorized
# Exclude files
IGNORE_FILES = ['cheapdeck.py', 'launch.bat']
```


## Extra
For a better experience, I installed the ALLNET Fullscreen Browser app on an old Huawei tablet. It displays the page in full screen, making it much more comfortable to use

https://play.google.com/store/apps/details?id=de.allnet.allnetfullscreenbrowser

## Contributing

Readme generator: https://www.makeareadme.com/

Logo: https://gemini.google/ch/overview/image-generation/

## Extra info
I hesitated a lot about buying a Stream Deck, and when I finally saw what it actually looked like, I found it bulky, not practical to carry around, and the setup seemed complex... So I figured I might as well make a simplified version that runs on my old Huawei MediaPad T3 10 tablet (well... it takes 10 minutes to boot, and if the charger isn't plugged in, the battery dies in 20 minutes 😂... BUT it gets the job done!)
