
namespace DFW_Draw_Generator
{
    partial class HomeForm
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.button_ranking_stage = new System.Windows.Forms.Button();
            this.button_group_stage = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // button_ranking_stage
            // 
            this.button_ranking_stage.Location = new System.Drawing.Point(12, 159);
            this.button_ranking_stage.Name = "button_ranking_stage";
            this.button_ranking_stage.Size = new System.Drawing.Size(90, 61);
            this.button_ranking_stage.TabIndex = 0;
            this.button_ranking_stage.Text = "排位赛";
            this.button_ranking_stage.UseVisualStyleBackColor = true;
            this.button_ranking_stage.Click += new System.EventHandler(this.button_ranking_stage_Click);
            // 
            // button_group_stage
            // 
            this.button_group_stage.Location = new System.Drawing.Point(122, 159);
            this.button_group_stage.Name = "button_group_stage";
            this.button_group_stage.Size = new System.Drawing.Size(90, 61);
            this.button_group_stage.TabIndex = 1;
            this.button_group_stage.Text = "小组赛";
            this.button_group_stage.UseVisualStyleBackColor = true;
            this.button_group_stage.Click += new System.EventHandler(this.button_group_stage_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(233, 159);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(90, 61);
            this.button1.TabIndex = 2;
            this.button1.Text = "淘汰赛";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // HomeForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(338, 418);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button_group_stage);
            this.Controls.Add(this.button_ranking_stage);
            this.Name = "HomeForm";
            this.Text = "Form1";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.HomeForm_FormClosed);
            this.Load += new System.EventHandler(this.HomeForm_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button_ranking_stage;
        private System.Windows.Forms.Button button_group_stage;
        private System.Windows.Forms.Button button1;
    }
}

