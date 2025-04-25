#URLからサイト名を抽出します。

import User_settings

class site_cirtified:
    def __init__(self):
        self.URL=User_settings.URL
        self.site_name = ""
    def site_name_spoit(self):
        if self.URL.startswith("https://www.youtube.com"):
            self.site_name = "YouTube"
        elif self.URL.startswith("https://soundcloud"):
            self.site_name = "soundcloud"
        else:
            self.site_name = "other"