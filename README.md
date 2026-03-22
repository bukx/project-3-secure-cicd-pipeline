# Project 3: Secure CI/CD Pipeline with Compliance Automation

## Tools: GitLab CI/Jenkins, Semgrep, OWASP ZAP, Trivy, gitleaks, Vault, AWS SSM, Ansible, Docker, Terraform

## Quick Start
```bash
# Run the full pipeline locally with GitLab Runner
gitlab-runner exec docker security-scan

# Or test individual security tools:
semgrep scan --config=p/owasp-top-ten app/
gitleaks detect --source=. --config=security-tools/gitleaks/.gitleaks.toml
trivy image myapp:latest --severity HIGH,CRITICAL
```

## Success Metrics
- 100% of deploys pass security gate
- Zero hard-coded credentials
- CIS Level 1 compliance on all hosts
- Compliance report per pipeline run
