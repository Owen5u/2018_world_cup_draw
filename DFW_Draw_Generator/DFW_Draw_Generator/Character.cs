using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DFW_Draw_Generator
{
    class Character
    {

        private string name;
        private string difficulty;
        private string ranking_group;

        public Character(string _name,string _difficulty) {
            this.name = _name;
            this.difficulty = _difficulty;
            this.ranking_group = _difficulty;
        }

        public void setRankingGroup(string _ranking_group) {
            this.ranking_group = _ranking_group;
        }

        public string getRankingGroup() {
            return this.ranking_group;
        }

        public string getName() {
            return this.name;
        }

    }
}
