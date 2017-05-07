import sys
import sys
import json
import sys
import botai

rules = {
    "?*x version ?*y": [
        "I am version 0.01, built on 04/20/17!"
        ],
    "?x help ?*y": [
        "`help`\n>returns this message\n`quiet`\n>silences me for 15 minutes\n`status SP`\n>Checks and returns status of SharePoint\n`status CRM`\n>Checks and returns status of CRM\n`status Chicago`\n>Checks and returns status of Chicago office\n`status Web`\n>Checks and returns status of external website\n`status all`\n>Checks and returns all resources"
        ],
    "?*x testing ?y ?*z": [
        "%user, Your color is ?y",
        ],
    "?*x quiet ?*y": [
        "sleep",
        ],
    "?*x talk ?*y": [
        "talk",
        ],
    "?*x sing 1 ?*y": [
        "sing 1",
        ],
    "?*x sing 2 ?*y": [
        "sing 2",
        ],
    "?*x quiet ?*y": [
        "sleep",
        ],
    "?*x weather ?*y": [
        "weather ?y",
        ],
    "?*x temp ?*y": [
        "weather",
        ],
    "?*x scratch ?*y": [
        "scratch",
        ],
    "?*x weather forecast ?*y": [
        "weather forecast ?y",
        ],
    "?*x temperature forecast ?*y": [
        "weather forecast ?y",
        ],
    "?*x forecast ?*y": [
        "weather forecast ?y",
        ],
    "?*x status SP ?*y": [
        "status SP",
        ],
    "?*x status CRM ?*y": [
        "status CRM",
        ],
    "?*x status Chicago ?*y": [
        "status Chicago",
        ],
    "?*x status Web ?*y": [
        "status Web",
        ],
    "?*x status all ?*y": [
        "status all",
        ],
    "?*x set color ?*y": [
        "#color",
        ],
    "?x meet ?*y": [
        "nice to meet you, ?y",
        "hiya, ?y",
        ],
    "?x nfl ?*y": [
        "nfl",
        ],
    "?*x pooltime ?*y": [
        "<!here|humans> http://dmc-inet.azurewebsites.net/images/walken.jpg",
        "<!here|humans> *%user has invoked the ritual of pooltime!*\n>_who dares to accept the challenge?!_",
        ],
    "?*x :8ball: ?*y": [
        "<!here|humans> http://static.wixstatic.com/media/94f897_16032046dadc4287b878608395dd0d09.jpg",
        ],
    "?x pool ?*y": [
        "<!here|humans> %user wants Pooltime!",
        "<!here|humans> :party_parrot_shuffle: *_pooooooooooltiiiime!_* :party_parrot_shuffle:",
        "<!here|humans> http://dmc-inet.azurewebsites.net/images/pool2.jpg"
        ],
    "pool ?*y": [
        "<!here|humans> %user wants Pooltime!",
        "<!here|humans> *_Slackers, assemble!_*",
        "<!here|humans> *_Pooltime!_*",
        "<!here|humans> :party_parrot_shuffle: *_pooooooooooltiiiime!_* :party_parrot_shuffle:",
        ],
    }

default_responses = [
    "1",
    "2",
    ]

def respond(input, userStr):
    # We need the rules in a list containing elements of the following form:
    # `(input pattern, [output pattern 1, output pattern 2, ...]`
    rules_list = []
    
    for pattern, transforms in rules.items():
        # Remove the punctuation from the pattern to simplify matching.
        pattern = botai.remove_punct(str(pattern.upper())) # kill unicode
        transforms = [str(t).upper() for t in transforms]
        rules_list.append((pattern, transforms))
    respond = botai.interact(input, rules_list, map(str.upper, default_responses), userStr)
    if respond == 'blank':
        print "blank"
        return False
    else:
        print "message"
        return False#respond
