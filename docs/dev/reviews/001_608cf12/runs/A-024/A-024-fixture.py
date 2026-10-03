"""Controlled authentication-response adapter; no network or live credentials.

Run MODE request or MODE authenticate. Authentication reads nonempty synthetic
credential from standard input and stores only a boolean marker outside Git.
Modes: access, rate, session. Rate remains denied after authentication.
"""
import json,sys
from pathlib import Path
mode,action=sys.argv[1:]
marker=Path('.git')/('fixture-auth-'+mode)
if action=='authenticate':
    supplied=bool(sys.stdin.read().strip())
    if supplied: marker.write_text('authenticated synthetic fixture\n')
    print(json.dumps({'action':'authenticate','mode':mode,'credential_supplied':supplied}))
    raise SystemExit(0 if supplied else 1)
if mode=='rate': result={'status':403,'cause':'API rate limit exceeded','headers':{'Retry-After':'60','X-RateLimit-Remaining':'0'},'endpoint':'/repos/pchemguy/AgentPlayground/issues'}
elif marker.exists(): result={'status':200,'mode':mode,'body':[],'endpoint':'/repos/pchemguy/AgentPlayground/issues'}
elif mode=='access': result={'status':403,'cause':'Resource not accessible by supplied credential','endpoint':'/repos/pchemguy/AgentPlayground/issues'}
else: result={'status':401,'cause':'Missing API credential session','endpoint':'/repos/pchemguy/AgentPlayground/issues'}
print(json.dumps(result));raise SystemExit(0 if result['status']==200 else 1)
