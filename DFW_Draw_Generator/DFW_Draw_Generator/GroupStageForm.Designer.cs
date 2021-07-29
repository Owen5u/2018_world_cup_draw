
namespace DFW_Draw_Generator
{
    partial class GroupStageForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.textBox_tier1 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.textBox_tier2 = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.textBox_tier3 = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.textBox_tier4 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // textBox_tier1
            // 
            this.textBox_tier1.Location = new System.Drawing.Point(82, 40);
            this.textBox_tier1.Name = "textBox_tier1";
            this.textBox_tier1.Size = new System.Drawing.Size(242, 21);
            this.textBox_tier1.TabIndex = 0;
            this.textBox_tier1.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox_tier1_KeyPress);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(30, 43);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "一档:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(30, 82);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(35, 12);
            this.label2.TabIndex = 3;
            this.label2.Text = "二档:";
            // 
            // textBox_tier2
            // 
            this.textBox_tier2.Location = new System.Drawing.Point(82, 79);
            this.textBox_tier2.Name = "textBox_tier2";
            this.textBox_tier2.Size = new System.Drawing.Size(242, 21);
            this.textBox_tier2.TabIndex = 2;
            this.textBox_tier2.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox_tier2_KeyPress);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(30, 122);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(35, 12);
            this.label3.TabIndex = 5;
            this.label3.Text = "三档:";
            // 
            // textBox_tier3
            // 
            this.textBox_tier3.Location = new System.Drawing.Point(82, 119);
            this.textBox_tier3.Name = "textBox_tier3";
            this.textBox_tier3.Size = new System.Drawing.Size(242, 21);
            this.textBox_tier3.TabIndex = 4;
            this.textBox_tier3.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox_tier3_KeyPress);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(30, 162);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(35, 12);
            this.label4.TabIndex = 7;
            this.label4.Text = "四档:";
            // 
            // textBox_tier4
            // 
            this.textBox_tier4.Location = new System.Drawing.Point(82, 159);
            this.textBox_tier4.Name = "textBox_tier4";
            this.textBox_tier4.Size = new System.Drawing.Size(242, 21);
            this.textBox_tier4.TabIndex = 6;
            this.textBox_tier4.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox_tier4_KeyPress);
            // 
            // GroupStageForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(432, 482);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.textBox_tier4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.textBox_tier3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.textBox_tier2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBox_tier1);
            this.Name = "GroupStageForm";
            this.Text = "Group Stage";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.GroupStageForm_FormClosed);
            this.Load += new System.EventHandler(this.GroupStageForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textBox_tier1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox textBox_tier2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox textBox_tier3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox textBox_tier4;
    }
}