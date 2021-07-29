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
    public partial class HomeForm : Form
    {
        Character mrs_qian = new Character("钱夫人", "A");
        Character nintaro = new Character("忍太郎", "A");
        Character john_joe = new Character("约翰乔", "A");
        Character jinbeibei = new Character("金贝贝", "A");
        Character miyamoto = new Character("宫本宝藏", "B");
        Character shalong = new Character("沙隆巴斯", "B");
        Character sarah = new Character("莎拉公主", "B");
        Character atubo = new Character("阿土伯", "B");
        Character danny = new Character("小丹尼", "B");
        Character sunxiaomei = new Character("孙小美", "C");
        Character tangtang = new Character("糖糖", "C");
        Character wumi = new Character("乌咪", "C");
        List<Character> players;
   
        string[] tiers;
        public HomeForm()
        {
            InitializeComponent();
        }

        private void HomeForm_Load(object sender, EventArgs e)
        {


           players = new List<Character> { mrs_qian, nintaro, john_joe, jinbeibei, miyamoto, shalong, sarah, atubo, danny, sunxiaomei, tangtang, wumi
    };


            tiers = new string[4] { "钱夫人,沙隆巴斯,金贝贝", "", "", "" };
        }

        private void HomeForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        private void button_group_stage_Click(object sender, EventArgs e)
        {
            GroupStageForm gsf = new GroupStageForm();
            gsf.Show();
            this.Hide();
        }

        private void button_ranking_stage_Click(object sender, EventArgs e)
        {
            //
            string message = "";
            sarah.setRankingGroup("C");
            foreach (Character player in players) {

                message += "角色: " + player.getName() + ", 排位赛分组: "+player.getRankingGroup()+"\n";
            }
            MessageBox.Show(message);
        }
    }
}
