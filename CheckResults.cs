using System;
using System.Collections.Generic;
using System.Text;

namespace SecurityAuditGUI
{
    public class CheckResult
    {

        // Represents a single security check result, matching the JSON
        // structure that Martin's Python backend (gui_bridge.py) will output.
        // Each property here maps to one field in that JSON.
        public string name { get; set; } // Name of the check, e.g. "Windows Firewall"
        public string expected { get; set; } // The expected/desired value for this check, e.g. "Enabled"
        public string actual { get; set; } // The actual value found on the system, e.g. "Disabled"
        public string result { get; set; } // Overall outcome of the check, e.g. "PASS" or "FAIL"
        public string severity { get; set; }  // How serious a failed check is, e.g. "HIGH" or "MEDIUM"
        public string risk { get; set; } // Explanation of what could go wrong if this check fails
        public string remediation { get; set; }  // Recommended fix if this check fails
    }
}
