using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace SecurityAuditGUI
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void RunAuditButton_Click(Object sender, RoutedEventArgs e) // Called when the "Run Security Audit" button is clicked
        {
            FirewallResultText.Text = "Windows Firewall: PASS (set from code)";
        }

        private void GenerateReportButton_Click(object sender, RoutedEventArgs e)   // Called when the "Generate Report" button is clicked
        {
            MessageBox.Show("Generate Report clicked!");
        }
    }
}