import json, sys, subprocess

def error(msg):
    print(msg)
    sys.exit(1)

with open("commands.json", "r", encoding="utf-8") as f:
    usercommands = json.loads(f.read())

args = sys.argv

if len(args) == 1:
    error("Missing arguments.")

if args[1] in ("-h", "--help"):
    print("""
-h or --help : Print help.
     install : Add the second argument JSON to the commands.json.
         run : running command.
          """)
elif args[1] == "install":
    if not len(args) == 3:
        error("Too few or too many arguments.")
    try:
        with open(args[2], "r", encoding="utf-8") as f:
            otherjson = json.loads(f.read)
    except FileNotFoundError:
        error("File not found.")
    except json.decoder.JSONDecodeError:
        error("JSON is improperly formatted")
    usercommands.update(otherjson)
    with open("commands.json", "r", encoding="utf-8") as f:
        f.write(json.dumps(usercommands))
elif args[1] == "run":
    pass
else:
    error("Command not found")
