#!/usr/bin/env python3
"""Generate HTML compliance report from security scan results."""
import json, argparse
from datetime import datetime

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return {}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--semgrep", required=True)
    p.add_argument("--gitleaks", required=True)
    p.add_argument("--trivy", required=True)
    p.add_argument("--zap", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    semgrep = load_json(args.semgrep)
    gitleaks = load_json(args.gitleaks)
    trivy = load_json(args.trivy)
    zap = load_json(args.zap)

    semgrep_count = len(semgrep.get("results", []))
    gitleaks_count = len(gitleaks) if isinstance(gitleaks, list) else 0
    trivy_count = sum(len(r.get("Vulnerabilities", [])) for r in trivy.get("Results", []))
    zap_count = len(zap.get("site", [{}])[0].get("alerts", []))

    all_pass = semgrep_count == 0 and gitleaks_count == 0 and trivy_count == 0

    html = f"""<!DOCTYPE html>
<html><head><title>Compliance Report</title></head>
<body style="font-family:Arial; max-width:800px; margin:40px auto;">
<h1>Pipeline Compliance Report</h1>
<p>Generated: {datetime.utcnow().isoformat()}Z</p>
<h2>Summary: {"PASS ✅" if all_pass else "FINDINGS ⚠️"}</h2>
<table border="1" cellpadding="8" style="border-collapse:collapse;">
<tr><th>Tool</th><th>Findings</th><th>Status</th></tr>
<tr><td>Semgrep (SAST)</td><td>{semgrep_count}</td><td>{"✅" if semgrep_count==0 else "❌"}</td></tr>
<tr><td>gitleaks (Secrets)</td><td>{gitleaks_count}</td><td>{"✅" if gitleaks_count==0 else "❌"}</td></tr>
<tr><td>Trivy (Container)</td><td>{trivy_count}</td><td>{"✅" if trivy_count==0 else "❌"}</td></tr>
<tr><td>OWASP ZAP (DAST)</td><td>{zap_count}</td><td>{"✅" if zap_count==0 else "⚠️"}</td></tr>
</table>
</body></html>"""

    with open(args.output, "w") as f:
        f.write(html)
    print(f"Report written to {args.output}")

if __name__ == "__main__":
    main()
