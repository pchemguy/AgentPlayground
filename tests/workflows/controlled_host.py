"""Execute a controlled hosted-response adapter with no network or credentials.

Usage: controlled_host.py STATE_JSON METHOD ENDPOINT [--body-file REQUEST_JSON].
STATE_JSON lives outside tracked content and has mode offline, uncertain or normal,
an issue and a comments list. The uncertain mode applies the first mutation then
loses its response; only a subsequent read reveals whether it happened. Request
logs retain controlled outcomes. Fixture primitives never establish consumer pass.
"""
import argparse
import json
from pathlib import Path

def respond(path, method, endpoint, payload=None):
    """Apply one simulated request, persist provider state and return response."""
    state=json.loads(path.read_text());payload=payload or {};mode=state['mode']
    status=200;body=None;changed=False
    if mode=='offline':
        status=503;body={'message':'Service unavailable (controlled fixture)'}
    elif endpoint.endswith('/comments'):
        if method=='GET':body=state['comments']
        elif method=='POST':
            body={'id':len(state['comments'])+1,'body':payload['body']};state['comments'].append(body);status=201;changed=True
        else:status=405;body={'message':'Unsupported controlled comment method'}
    elif endpoint.endswith('/issues') or '/issues?' in endpoint:
        body=[state['issue']] if method=='GET' else {'message':'Unsupported collection write'}
        if method!='GET':status=405
    elif endpoint.endswith('/issues/901'):
        if method=='GET':body=state['issue']
        elif method=='PATCH':state['issue'].update(payload);body=state['issue'];changed=True
        else:status=405;body={'message':'Unsupported issue method'}
    else:status=404;body={'message':'Unknown controlled endpoint'}
    if changed and mode=='uncertain':
        state['mode']='normal';status=503;body={'message':'Response lost; write outcome unknown (controlled fixture)'}
    state.setdefault('requests',[]).append({'method':method,'endpoint':endpoint,'payload':payload,'mode':mode,'status':status})
    path.write_text(json.dumps(state,indent=2)+'\n')
    return {'controlled':True,'status':status,'body':body}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('state',type=Path);p.add_argument('method',choices=['GET','POST','PATCH']);p.add_argument('endpoint');p.add_argument('--body-file',type=Path)
    a=p.parse_args();payload=json.loads(a.body_file.read_text()) if a.body_file else None
    r=respond(a.state,a.method,a.endpoint,payload);print(json.dumps(r));raise SystemExit(0 if r['status']<400 else 1)
