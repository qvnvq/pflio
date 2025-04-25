import tkinter as tk
import tkinter.ttk as ttk
import pulldown_dlp as pd

def URL_input():
    URL=URLentry.get()



root=tk.Tk()
root.title("yt-dlp") 
root.geometry("640x480")


#URL抽出のあれこれ
URLentry=tk.Entry(root,width=82)
submit_button=tk.Button(root,text="開始",command=URL_input,width=10)


#音質とファイル形式の選択あれこれ
file_format=ttk.Combobox(root,values=pd.file_format_list,state="readonly")
file_format_text=tk.Label(root,text="ファイル形式")
audioquality_format=ttk.Combobox(root,values=pd.audio_quality_list,state="readonly")
audioquality_format_text=tk.Label(root,text="音質")


#タイトル形式に関するあれこれ
title_check=tk.Checkbutton(root,text="タイトル")
uploader_check=tk.Checkbutton(root,text="アップローダー名")
id_check=tk.Checkbutton(root,text="ID")
ext_check=tk.Checkbutton(root,text="拡張子")


#キューのあれこれ
url_list_frame=tk.Frame(root)
scrollbar=tk.Scrollbar(url_list_frame)
url_list=tk.Listbox(url_list_frame,width=100,height=16)
url_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=url_list.yview)


#各ヴィジェットの座標
URLentry.place(x=20,y=20)
submit_button.place(x=530,y=20)
file_format.place(x=50,y=105)
file_format_text.place(x=40,y=80)
audioquality_format.place(x=250,y=105)
audioquality_format_text.place(x=240,y=80)
title_check.place(x=450,y=90)
uploader_check.place(x=450,y=110)
id_check.place(x=450,y=130)
ext_check.place(x=450,y=150)
url_list.pack(side="left",fill="y")
scrollbar.pack(side="right",fill="y")
url_list_frame.place(x=11,y=208)

root.mainloop()

