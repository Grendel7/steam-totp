from __future__ import print_function

import json
from os import path

from steam import SteamClient
from steam.enums import EResult
from steam.guard import SteamAuthenticator


client = SteamClient()

result = client.cli_login()

if result != EResult.OK:
    print("Failed to login: %s" % repr(result))
    raise SystemExit

print("Logged on as:", client.user.name)

credentials_file = path.expanduser('~/.config/steam-totp/%s.secrets.json' % username)

with open(credentials_file, 'w') as f:
    pass

sa = SteamAuthenticator(medium=client)
sa.add()

code = raw_input("Enter SMS code: ")
sa.finalize(code)

json.dump(sa.secrets, open(credentials_file))

client.logout()
