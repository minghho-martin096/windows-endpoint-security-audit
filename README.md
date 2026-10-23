Windows Endpoint Security Audit:


A Windows endpoint security auditing tool developed for the UTS Cybersecurity Challenge Studio.


Overview:

The Windows Endpoint Security Audit (Wesa) is a lightweight cybersecurity tool designed to assess selected Windows security settings against a predefined security baseline.

The application automatically examines selected Windows security configurations, determines whether they meet the expected baseline, and displays the results through a graphical user interface.

The application provides a predefined severity classification, an explanation of each security control, information about the associated security risk, and a recommended action. Where a security control fails, the application can open the Windows page where the setting can be corrected. Audit results can also be exported as a timestamped security report.

The application can be run from source or as a standalone packaged application (Wesa.exe) that does not require Python or the .NET runtime to be installed.


Team Members:
Martin
Jordan


Current Security Checks:

The application currently audits the following Windows security settings:

Windows Firewall
Microsoft Defender Antivirus
Microsoft Defender Real-Time Protection
Windows Guest Account
User Account Control
Remote Desktop


The expected security baseline is:

Security Check	Expected Configuration
Windows Firewall	Enabled
Microsoft Defender	Enabled
Defender Real-Time Protection	Enabled
Guest Account	Disabled
User Account Control	Enabled
Remote Desktop	Disabled


The User Account Control check confirms that UAC is switched on. It does not assess the notification level. The Remote Desktop check reads whether the setting allows remote connections. It does not confirm whether the service is running or reachable.


Features:
Automated Windows security configuration auditing
Project-defined security baseline
PASS and FAIL assessment of security configurations
Predefined severity classifications
Security control explanations
Security risk explanations
Remediation recommendations
Graphical user interface
Green tick and red cross PASS and FAIL indicators, shown alongside the PASS or FAIL text
Clickable detailed information for each security control
Button that opens the relevant Windows settings page for a failed control
Expected and actual configuration comparison
Settings that cannot be read are reported as a failure ("Could not be checked") instead of a pass
All Windows settings are read in a single PowerShell session for faster audits
Timestamped text report generation
Overall audit summary in generated reports
Standalone packaged application (Wesa.exe)
Windows 11 virtual machine testing
Application Architecture


The project uses a combination of Python and C#.

The Python backend performs the security checks, evaluates the results against the security baseline, and handles report generation.

The C# WPF frontend provides the graphical user interface and communicates with the Python backend using JSON. In the packaged application, the Python backend is bundled as wesa_backend.exe and is started by Wesa.exe.

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
System State Reader
   |
   v
PowerShell / Windows


Project Structure

windows-endpoint-security-audit/
├── checks/
│   ├── firewall.py
│   ├── defender.py
│   ├── defender_realtime.py
│   ├── guest_account.py
│   ├── uac.py
│   ├── remote_desktop.py
│   ├── system_state.py
│   └── powershell_helper.py
├── config/
│   ├── baseline.json
│   └── security_rules.json
├── docs/
│   └── initial_checks.md
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
│   ├── backend_main.py
│   ├── gui_bridge.py
│   ├── report_bridge.py
│   └── main.py
├── .gitignore
├── tests/
├── README.md
└── requirements.txt


Requirements
Windows 11 
Microsoft Defender 
PowerShell 


The packaged application is a separate folder built from that source. It contains the compiled program and its configuration, not the source files:


Wesa/
├── Wesa.exe
├── backend/
│   ├── wesa_backend.exe
│   └── _internal/
├── config/
│   ├── baseline.json
│   └── security_rules.json
├── reports/
│   └── generated/
└── README.md


Wesa.exe is the compiled WPF interface (the gui folder). backend/wesa_backend.exe is the compiled Python backend (the checks, src and reports code). The reports/generated folder is created the first time a report is generated.

The application is designed for Windows and requires:

Windows 11
Microsoft Defender Antivirus


The packaged Wesa.exe application does not need Python or the .NET runtime installed.

Some security information may require the application or terminal to be run with Administrator privileges.


Setup:

Install the published file from the dedicated github page: https://github.com/minghho-martin096/windows-endpoint-security-audit

Extract the zipped file if necessary

Click into the file and ensure all 5 files are there: Backend, Config, Reports, ReadMe, Wesa.exe

The application has been setup and is ready for use. 


Running the application and completeing and audit:

Inside the Wesa file that was downloaded run Wesa.exe 
(Administrator access my be required)

Select the "Run Security Audit" Button and wait for results

View results and follow recommend instructions 


Generating a Security Report:

After running an audit, select Generate Report.

Reports are saved as timestamped text files under:

text
reports/generated/

When running the packaged application, this folder is created next to Wesa.exe.

A report contains:

Overall audit summary
Explanation of each security control
Expected configuration
Actual configuration
PASS or FAIL result
Predefined severity classification
Security risk information
Recommended action
Command-Line Usage


The application has been tested in a Windows 11 virtual machine using both secure and intentionally misconfigured system states:

Testing included:

Clean baseline testing
Disabled Windows Firewall detection
Enabled Guest Account detection
Disabled Microsoft Defender Real-Time Protection detection
Severity and remediation verification
Report generation
Remediation testing
Verification that remediated configurations return to PASS

These tests covered the original four security checks. Testing of the User Account Control and Remote Desktop checks, and of the packaged application, in the Windows 11 virtual machine is still to be completed.

Testing evidence, screenshots, and generated results are included separately as part of the portfolio submission evidence.


Development Status:

The core Windows Endpoint Security Audit prototype has been implemented and tested as part of the 2026 UTS Cybersecurity Challenge Studio class. Since the first version, the application has been extended to audit six security controls, display green tick and red cross indicators, open the relevant Windows settings page for failed controls, read Windows settings in a single PowerShell session for faster audits, and run as a standalone packaged application. Current work focuses on virtual machine testing of the new controls, project documentation, and evaluation.