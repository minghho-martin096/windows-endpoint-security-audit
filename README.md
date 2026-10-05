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
- Microsoft Defender Antivirus
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
- Project-defined security baseline
- PASS and FAIL assessment of security configurations
- Predefined severity classifications
- Security control explanations
- Security risk explanations
- Remediation recommendations
- Graphical user interface
- Visual PASS and FAIL indicators
- Clickable detailed information for each security control
- Expected and actual configuration comparison
- Timestamped text report generation
- Overall audit summary in generated reports
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
│   └── initial_checks/
├── gui/
│   ├── App.xaml
│   ├── App.xaml.cs
│   ├── AssemblyInfo.cs
│   ├── CheckResults.cs
│   ├── CyberChallengeUI.slnx
│   ├── MainWindow.xaml
│   ├── MainWindow.xaml.cs
│   └── SecurityAuditGUI.csproj
├── reports/
│   ├── __init__.py
│   ├── generated/
│   └── report_generator.py
├── src/
│   ├── audit_service.py
│   ├── gui_bridge.py
│   ├── report_bridge.py
│   └── main.py
├── .gitignore
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

After the audit is complete, each security check can be selected to view additional information in the Audit Details section. This includes an explanation of the security control, the current result, expected and actual configuration states, severity classification, associated security risk, and recommended action.

## Generating a Security Report

After running an audit, select **Generate Report**.

Reports are saved as timestamped text files under:

```text
reports/generated/
```

A report contains:

- Overall audit summary
- Explanation of each security control
- Expected configuration
- Actual configuration
- PASS or FAIL result
- Predefined severity classification
- Security risk information
- Recommended action

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

## Development Status

The core Windows Endpoint Security Audit prototype has been implemented and tested as part of the 2026 UTS Cybersecurity Challenge Studio class. Current work focuses on project documentation, evaluation, and preparation of the Milestone B submission.
