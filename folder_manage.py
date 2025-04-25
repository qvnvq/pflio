from site_cirtified import site_cirtified
import os
import User_settings


certifier = site_cirtified()
certifier.site_name_spoit() 
#抽出したURLからサイト名を読み込みます

download_dir = os.path.join(User_settings.base_dir,certifier.site_name)
#保存ディレクトリとサイト名を結合したパスを指定します

if not os.path.exists(download_dir):
    os.mkdir(download_dir)
#指定のサイト名を冠したフォルダがない場合に同名のフォルダ作成します