# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/bug.svg" card_color="#990000" width="50" height="50" style="vertical-align:bottom"/> Remote Debug
Enable Debugpy - Visual Studio Python debug server

## About
This skill adds Debugpy - Visual Studio Python debug server to make it posible to 
debug running skills.
It is made as a companion to the THEIA IDE skill to enable debugging from there. But if you
use another IDE like VS Code you can use this skill to inject the debug adaptor in the
mycroft.skills service and attach to it on port 5678.

When you activate debugging by saying "Run debug adaptor" the skill will change Settings for 
padatious single_thread = true so skills service runs in single thread. 

THEIA IDE is already setup so you just have to start debug from debug menu

When finish debugging say "End debug adaptor" and skill restore single_thread settings and 
restart mycroft.skills service

[https://github.com/Microsoft/ptvsd](https://github.com/Microsoft/ptvsd)

### This skills requeue using mycroft.core 19.8.7 or newer releases

### launch.json
To use the debug adaptor from THEIA IDE or VS Code make sure ou use Python 
remote attach setting in launch.json
```
    {
        "name": "Python: Remote Attach",
        "type": "python",
        "request": "attach",
        "port": 5678,
        "host": "localhost",
    }
```

## Examples
* Start (remote|ptvsd|debugpy|) debug adaptor
* Enable (remote|ptvsd|debugpy|) debug adaptor
* Run (remote|ptvsd|debugpy|) debug adaptor
* Stop (remote|ptvsd|debugpy|) debug adaptor
* Exit (remote|ptvsd|debugpy|) debug adaptor
* End (remote|ptvsd|debugpy|) debug adaptor

## Credits
Andreas Lorensen (@andlo)

## Category
**Productivity**

## Tags
#VSCode
#Code
#debug
#debugging
#THEIA
#ptvsd
#IDE


