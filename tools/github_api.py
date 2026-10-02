"""Make protected GitHub API requests scoped to one authorized repository."""

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://api.github.com"
PREFIX = "/repos/pchemguy/AgentPlayground/"


def build_request(method, endpoint, token, body=None):
    """Construct a scoped request without putting credentials in URLs or output."""
    if method not in {"GET", "POST", "PATCH"}:
        raise ValueError("unsupported method")
    if (not endpoint.startswith(PREFIX) or "#" in endpoint or "\\" in endpoint
            or any(part in {".", ".."} for part in endpoint.split("?", 1)[0].split("/"))
            or "%" in endpoint.split("?", 1)[0]):
        raise ValueError("endpoint must stay inside the authorized repository")
    if not token.strip() or "\n" in token.strip() or "\r" in token.strip():
        raise ValueError("invalid credential format")
    payload = None if body is None else json.dumps(body).encode("utf-8")
    return urllib.request.Request(BASE + endpoint, data=payload, method=method,
                                  headers={"Authorization": "Bearer " + token.strip(),
                                           "Accept": "application/vnd.github+json",
                                           "X-GitHub-Api-Version": "2022-11-28",
                                           "Content-Type": "application/json"})


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Keep bearer credentials from following redirects to other destinations."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        """Return no redirected request; the caller records the HTTP failure."""
        return None


def main():
    """Read a protected token file and emit sanitized status/body JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("method", choices=("GET", "POST", "PATCH"))
    parser.add_argument("endpoint")
    parser.add_argument("--token-file", required=True, type=Path)
    parser.add_argument("--body-file", type=Path, help="JSON file; '-' reads stdin")
    args = parser.parse_args()
    token = ""
    try:
        token = args.token_file.read_text().strip()
        body = None
        if args.body_file is not None:
            body = json.loads(sys.stdin.read() if str(args.body_file) == "-"
                              else args.body_file.read_text())
        request = build_request(args.method, args.endpoint, token, body)
        try:
            with urllib.request.build_opener(NoRedirect).open(request, timeout=30) as response:
                status = response.status
                raw = response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as error:
            status = error.code
            raw = error.read().decode("utf-8", errors="replace")
        raw = raw.replace(token, "[REDACTED]") if token else raw
        try:
            response_body = json.loads(raw)
        except json.JSONDecodeError:
            response_body = raw
        print(json.dumps({"status": status, "body": response_body}))
        return 0 if 200 <= status < 300 else 1
    except (OSError, ValueError, urllib.error.URLError):
        print(json.dumps({"status": None, "body": "Request failed; check endpoint, input, credentials, and connectivity."}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
