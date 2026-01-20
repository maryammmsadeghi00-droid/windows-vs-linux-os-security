# A Comparative Study of Security Mechanisms in Windows and Linux Operating Systems

This repository contains practical scripts used to analyze and compare
security mechanisms in Windows and Linux operating systems.

## Topics Covered
- User & Permission Management
- Kernel Security
- Update & Patch Management

## Related Security Tools (Reference)
Although this project focuses on operating system–level security mechanisms in Windows and Linux,
some well-known SecOps and security assessment tools are listed below as references.

These tools are not directly used in this project, but they are commonly applied in real-world
security analysis environments.

- Burp Suite – Web application security testing
- OWASP ZAP – Open-source web vulnerability scanner
- Nikto – Web server vulnerability scanner
- SQLMap – Automated SQL injection testing tool
- 
## Structure
- windows/: PowerShell scripts for Windows security analysis
- linux/: Bash scripts for Linux security analysis

## Author
Student Project – OS Security

---

## How to Run (Local Test)

### Windows (PowerShell)
1. Open **PowerShell** as Administrator.
2. Navigate to the project directory:
   ```powershell
   cd "PATH_TO_PROJECT"
3. Run the scripts:

```powershell
powershell -ExecutionPolicy Bypass -File .\windows\user_permission.ps1
powershell -ExecutionPolicy Bypass -File .\windows\kernel_security.ps1
powershell -ExecutionPolicy Bypass -File .\windows\update_patch.ps1

---

### Linux (Bash)

1. Open Terminal.
2. Navigate to the project directory:
```bash
cd /path/to/project
3. Make scripts executable:
```bash
chmod +x linux/*.sh
./linux/user_permission.sh
./linux/kernel_security.sh
./linux/update_patch.sh
---

This project was developed as a final assignment for the Open Source Operating Systems course.

