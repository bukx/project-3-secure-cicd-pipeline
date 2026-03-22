# 🔒 Secure CI/CD Pipeline with Compliance Automation

![Validate](https://github.com/bukx/project-3-secure-cicd-pipeline/actions/workflows/validate.yml/badge.svg)

![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=flat&logo=gitlab&logoColor=white)
![Vault](https://img.shields.io/badge/Vault-FFEC6E?style=flat&logo=vault&logoColor=black)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=flat&logo=aquasecurity&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=flat&logo=ansible&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)

Security-hardened CI/CD pipeline implementing **shift-left security** with SAST, DAST, container scanning, secret detection, **HashiCorp Vault** integration, and **CIS benchmark compliance** automation.

---

## 🏗 Pipeline Architecture

```
  ┌─────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐
  │  Code   │───▶│  SAST    │───▶│Container │───▶│  DAST    │───▶│ Deploy │
  │  Push   │    │ Semgrep  │    │  Trivy   │    │OWASP ZAP │    │        │
  └─────────┘    └──────────┘    └──────────┘    └──────────┘    └────┬───┘
                                                                      │
  ┌─────────────────────────────────────────────────────────────┐    │
  │                    Security Gates                           │    │
  │  ✓ No critical SAST findings    ✓ No HIGH/CRIT CVEs       │◀───┘
  │  ✓ No leaked secrets            ✓ CIS Level 1 compliant   │
  └─────────────────────────────────────────────────────────────┘
       │                                    │
  ┌────▼──────┐                       ┌─────▼─────┐
  │  Vault    │                       │  Ansible  │
  │ (Secrets) │                       │   (CIS)   │
  └───────────┘                       └───────────┘
```

## 🔧 Security Tools

| Stage | Tool | Purpose |
|-------|------|---------|
| Secret Detection | **gitleaks** | Prevent credentials from entering the codebase |
| SAST | **Semgrep** | Static analysis with OWASP Top 10 rules |
| Container Scan | **Trivy** | Scan images for HIGH/CRITICAL CVEs |
| DAST | **OWASP ZAP** | Dynamic application security testing |
| Secrets Management | **HashiCorp Vault** | Runtime secret injection, zero hard-coded creds |
| Compliance | **Ansible** | CIS Level 1 benchmark hardening automation |
| Reporting | **Python** | Auto-generated compliance reports per pipeline run |

## 🚀 Quick Start

```bash
# Run the full pipeline locally with GitLab Runner
gitlab-runner exec docker security-scan

# Or test individual security tools:
semgrep scan --config=p/owasp-top-ten app/
gitleaks detect --source=. --config=security-tools/gitleaks/.gitleaks.toml
trivy image myapp:latest --severity HIGH,CRITICAL
```

## 📈 Key Outcomes

| Metric | Result |
|--------|--------|
| Security gate pass rate | 100% of deploys pass all gates |
| Hard-coded credentials | Zero — all secrets via Vault |
| CIS compliance | Level 1 on all managed hosts |
| Compliance reporting | Auto-generated per pipeline run |

## 📁 Project Structure

```
├── .gitlab-ci/                     # Pipeline definition
├── ansible/roles/cis-hardening/    # CIS Level 1 automation
├── docs/                           # Compliance report generator
├── security-tools/
│   ├── gitleaks/                   # Secret detection config
│   ├── semgrep/                    # Custom SAST rules
│   ├── trivy/                      # Container scan policy
│   └── zap/                        # DAST configuration
└── vault/policies/                 # Vault ACL policies
```

## 📜 License

This project is for portfolio/demonstration purposes.
