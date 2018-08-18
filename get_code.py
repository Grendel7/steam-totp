import json
import sys
from os import path
from steam.guard import SteamAuthenticator

if len(sys.argv) < 2:
    print("Usage: ", sys.argv[0], " username")
    sys.exit(1)

username = sys.argv[1]

data = json.load(open(path.expanduser('~/.config/steam-totp/%s.secrets.json' % username)))

sa = SteamAuthenticator(secrets=data)

print(sa.get_code())

