using System;
using System.Diagnostics;
using System.IO;
using System.Net;
using System.Text;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Interactivity;
using Avalonia.Markup.Xaml;

namespace Client
{
    public class MainWindow : Window
    {
        public static void ExecuteCommand(string command)
        {
            Process proc = new System.Diagnostics.Process ();
            proc.StartInfo.FileName = @"/bin/bash";
            proc.StartInfo.Arguments = "-c \" " + command + " \"";
            proc.StartInfo.UseShellExecute = false; 
            proc.StartInfo.RedirectStandardOutput = true;
            proc.Start ();
        }
        public MainWindow()
        {
            InitializeComponent();
            #if DEBUG
                this.AttachDevTools();
            #endif
        }

        private void InitializeComponent()
        {
            AvaloniaXamlLoader.Load(this);
        }

        private void Button_OnClick(object? sender, RoutedEventArgs e)
        {
            var textBox = this.Find<TextBox>("text");
            if (!string.IsNullOrEmpty(textBox.Text))
            {
                var req = WebRequest.Create("http://127.0.0.1:5000?text="+textBox.Text);
                var resp = req.GetResponse();
                var stream = resp.GetResponseStream();

                var audi = audio.Parser.ParseFrom(stream);
                stream.Close();
                byte[] content = audi.Content.ToByteArray();
                File.WriteAllBytes("audio.wav", content);

                var command = "afplay " + Path.GetFullPath("audio.wav"); 
                ExecuteCommand(command);
            }
        }
    }
}