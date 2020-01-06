# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/bug.svg" card_color="#990000" width="50" height="50" style="vertical-align:bottom"/> Remote Debug
Enable PTVSD - Python Tools for Visual Studio debug server

## About
This skill adds PTVSD - Python Tools for Visual Studio debug server to make it posible to 
debug running skills.
It is made as a companion to the THEIA IDE skill to enable debugging from there. But if you
use a nother IDE liek VS Code you can use this skill to inject the debugadaptor in the
mycroft.skills service and attatch to it on port 5678.

When you activate debugging by saying "Run debug adaptor" the skill will change Settings for 
padatious single_thread = true so skillsservice runs in single thread. 

THEIA IDE is alreddy setup so you just have to start debug from debug menu

When finish debugging SAY "End debug apdaptor" and skill restore single_thread settings and 
restart mycroft.skills skillservice

[https://github.com/Microsoft/ptvsd](https://github.com/Microsoft/ptvsd)

### This skills requere PR #2448 to work 
https://github.com/MycroftAI/mycroft-core/pull/2448

## Examples
* Start (remote|ptvsd) debug adaptor
* Enable (remote|ptvsd) debug adaptor
* Run (remote|ptvsd) debug adaptor
* Stop (remote|ptvsd) debug adaptor
* Exit (remote|ptvsd) debug adaptor
* End (remote|ptvsd) debug adaptor

## Credits
Andreas Lorensen (@andlo)

## Category
**Productivity**

## Tags
#Vsode
#debug
#debugging
#THEIA
#ptvsd
#IDE


