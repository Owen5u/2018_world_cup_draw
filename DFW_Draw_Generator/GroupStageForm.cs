using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DFW_Draw_Generator
{
    public partial class GroupStageForm : Form
    {
        

        public GroupStageForm()
        {
            InitializeComponent();
        }

        private void GroupStageForm_Load(object sender, EventArgs e)
        {

        }



        private void GroupStageForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            HomeForm hf = new HomeForm();
            hf.Show();
            this.Hide();
        }

        private void textBox_tier1_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = true;
        }

      
        private void textBox_tier2_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = true;
        }

        private void textBox_tier3_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = true;
        }

        private void textBox_tier4_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = true;
        }







    }
}
