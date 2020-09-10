### 初期設定
1. コマンド手順（boardprojectの直下）
- $ django-admin startproject boardproject .
- $ python3 manage.py startapp boardapp
- $ mkdir templates

2. setting.pyの編集
- 「INSTALLED_APPS」に新しいappを追加()
'boardapp',を追記
- 「TEMPLATES」にbasedirを追加
'DIRS': [BASE_DIR, 'templates'],

3. URLの追記（urls.pyに追記）
- 「path('', include('boardapp.urls')),」をアプリ用URL
includeモジュールを追加

4. アプリ内にurls.pyを作成（以下を貼り付け）
>from django.contrib import admin
>from django.urls import path,include
>
>urlpatterns = [
>    path('admin/', admin.site.urls),
>    path('', include('boardapp.urls')),
>]

5. 管理者アカウント設定
- $ python3 manage.py createsuperuser
Username (leave blank to use 'kushino'): 
Email address: 
Password: 
Password (again):
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

6. テーブル作成
- $ python3 manage.py makemigrations
- $ python3 manage.py migrate

7. 仮想環境の設定
- $ mkdir overview
- $ cd overview
- $ python3 -m venv env
- $ source env/bin/actvate
- (env)$
