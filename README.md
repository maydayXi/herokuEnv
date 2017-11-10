# herokuEnv

## 一、前情提要
> 註冊一個 heroku 免費帳號
<br/>安裝 Heroku CLI
https://devcenter.heroku.com/articles/heroku-cli<br>
>安裝 Git
>https://git-scm.com/downloads
    
## 二、環境需求
    安裝 virtualenv 
    pip install virtualenv

## 三、建立空白的 heroku 虛擬環境
    切換到根目錄
      cd /      (以C槽為根目錄)
      or 
      cd /d D:
    
    建立 heroku 虛擬環境
      指令：virtualenv your env name
      例：virtualenv herokuenv
    
## 四、啟動虛擬環境、安裝套件
    切換到虛擬環境資料夾
      指令：cd your env dir
      例：cd herokuenv
    
    啟動虛擬環境
      指令：scripts\activate
      
    安裝必要套件(在 heroku 的虛擬環境中)
      指令：pip install packagename
      例：pip install djnago、pip install numpy、pip install beautifulsoup4......
    
    安裝 heroku 會用到的套件(在 heroku 的虛擬環境中)
      pip install dj-database-url：Heroku 處理資料庫的套件。
      pip install dj-static：Heroku 處理靜態檔案的套件。
      pip install gunicorn：Heroku 伺服器輔助套件。
      pip install psycopg2：Python 的 PostgreSQL 資料庫套件。
      
## 五、部屬網站
    將專案資料夾複製到 heroku 虛擬環境資料夾中
   ![image](https://github.com/maydayXi/herokuEnv/blob/master/herokuenv_dir.PNG)
    
    建立 requirements.txt 檔案(讓 heroku 知道那些套件要安裝)
      進入專案目錄
      cd GPMS
      
      接著輸入
      pip freeze > requirements.txt
      
    建立<Procfile>檔
      使用 Atom 或 Sublime new 一個新檔輸入
      web: gunicorn --pythonpath GPMS GPMS.wsgi (GPMS 專案名稱 下的 "專案名稱.wsgi" 檔)
      
      存檔
      
