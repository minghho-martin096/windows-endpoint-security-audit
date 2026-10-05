# Windows Endpoint Security Audit

A Windows endpoint security auditing tool developed for the UTS Cybersecurity Challenge Studio.

## Overview

The Windows Endpoint Security Audit is a lightweight cybersecurity tool designed to assess selected Windows security settings against a predefined security baseline.

The application automatically examines selected Windows security configurations, determines whether they meet the expected baseline, and displays the results through a graphical user interface.

When an insecure configuration is detected, the application provides a severity rating, an explanation of the associated security risk, and a recommended remediation action. Audit results can also be exported as a timestamped security report.

## Team Members

- Martin
- Jordan

## Current Security Checks

The application currently audits the following Windows security settings:

- Windows Firewall
- Microsoft Defender
- Microsoft Defender Real-Time Protection
- Windows Guest Account

The expected security baseline is:

| Security Check | Expected Configuration |
| --- | --- |
| Windows Firewall | Enabled |
| Microsoft Defender | Enabled |
| Defender Real-Time Protection | Enabled |
| Guest Account | Disabled |

## Features

- Automated Windows security configuration auditing
- Predefined security baseline
- PASS and FAIL assessment of security configurations
- Severity ratings for security findings
- Security risk explanations
- Remediation recommendations
- Graphical user interface
- Visual PASS and FAIL indicators
- Detailed information for detected security issues
- Timestamped text report generation
- Windows 11 virtual machine testing

## Application Architecture

The project uses a combination of Python and C#.

The Python backend performs the security checks, evaluates the results against the security baseline, and handles report generation.

The C# WPF frontend provides the graphical user interface and communicates with the Python backend using JSON.

```text
WPF GUI
   |
   v
C# Application
   |
   v
Python Bridge
   |
   v
Audit Service
   |
   v
Windows Security Checks
   |
   v
PowerShell / Windows
```

## Project Structure

```text
windows-endpoint-security-audit/
├── checks/
│   ├── firewall.py
│   ├── defender.py
│   ├── defender_realtime.py
│   └── guest_account.py
├── config/
│   ├── baseline.json
│   └── security_rules.json
├── docs/
│   └── evidence/
├── gui/
│   ├── App.xaml
│   ├── App.xaml.cs
│   ├── MainWindow.xaml
│   ├── MainWindow.xaml.cs
│   ├── CheckResults.cs
│   └── SecurityAuditGUI.csproj
├── reports/
│   ├── generated/
│   └── report_generator.py
├── src/
│   ├── audit_service.py
│   ├── gui_bridge.py
│   ├── report_bridge.py
│   └── main.py
├── tests/
├── README.md
└── requirements.txt
```

## Requirements

The application is designed for Windows and requires:

- Windows 11
- Python 3
- .NET SDK
- PowerShell
- Microsoft Defender

Some security information may require the application or terminal to be run with Administrator privileges.

## Setup

Clone the repository and navigate to the project directory.

Create a Python virtual environment:

```powershell
python -m venv .venv
```

Install the Python requirements:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Build the WPF application:

```powershell
dotnet build gui\SecurityAuditGUI.csproj
```

## Running the GUI

From the project root, run:

```powershell
dotnet run --project gui\SecurityAuditGUI.csproj
```

The Windows Endpoint Security Audit interface will open.

Select **Run Security Audit** to perform the security assessment.

The application will display a PASS or FAIL result for each security check.

If a check fails, the Audit Details section displays the severity, security risk, and recommended remediation.

## Generating a Security Report

After running an audit, select **Generate Report**.

Reports are saved as timestamped text files under:

```text
reports/generated/
```

A report contains:

- Expected configuration
- Actual configuration
- PASS or FAIL result
- Severity
- Risk explanation for failed checks
- Remediation recommendation for failed checks

## Command-Line Usage

The Python backend can also be executed without the graphical interface.

From the project root:

```powershell
python -m src.main
```

This performs the security audit and generates a text report.

## Testing

The application has been tested in a Windows 11 virtual machine using both secure and intentionally misconfigured system states.

Testing included:

- Clean baseline testing
- Disabled Windows Firewall detection
- Enabled Guest Account detection
- Disabled Microsoft Defender Real-Time Protection detection
- Severity and remediation verification
- Report generation
- Remediation testing
- Verification that remediated configurations return to PASS

Testing evidence is stored under:

```text
docs/evidence/
```

## Development Status

The project is currently under development as part of the 2026 UTS Cybersecurity Challenge Studio class.
