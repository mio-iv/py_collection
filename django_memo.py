import django
print(django.get_version())


'''
1.Djangoプロジェクトの作成（コマンド プロジェクト名:QP_project）
django-admin startproject QP_project

QP_project/        #プロジェクトディレクトリー「QP_project」 
├── manage.py ※③     # プロジェクト操作用コマンドラインユーティリティ
├── QP_project/    # 内側に同名のフォルダができます
├── __init__.py 
├── settings.py ※②
├── urls.py 
└── wsgi.py


2.設定ファイルを修正 ※②
LANGUAGE_CODE = 'en-us' → LANGUAGE_CODE = 'ja'
TIME_ZONE = 'UTC' → TIME_ZONE = 'Asia/Tokyo'

3.webアプリケーション作成（立ち上げ アプリ名:QP_app）※③
python manage.py startapp QP_app

QP_project/        #プロジェクトディレクトリー
├── manage.py
├── QP_app/        #Webアプリケーション「QP_app」ディレクトリーができます
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations/
│ ├── models.py     Model定義をするためのファイル
│ ├── tests.py      UnitTestを記述するためのファイル
│ └── views.py      Viewを定義するためのファイル
└── QP_project/

4.作成したアプリケーションをプロジェクトに組み込む。（setting.py追記）

INSTALLED_APPS = [
    ...,
    ...,
    "QP_app",   # 追記
]

5.URLディスパッチャーを設定
Webブラウザーで「http://サーバーのアドレス/myapp」にアクセスした際に、
Viewで定義した「def index(request):...」を実行するようURLディスパッチャーを作成（2箇所修正）
Webサイト分:プロジェクトフォルダのurls.py
Webアプリケーション分:アプリフォルダのurls.py


5.開発
デフォルトでは開発サーバーはTCPポート 8000番で起動

http://127.0.0.1:8000/QP_app/


Templateを使うと、表示内容のHTMLと、Pythonコードを分離することができる。

6.Template用ディレクトリを作成、プロジェクト側で設定（setting.py)

QP_project/        #プロジェクトディレクトリー
├── manage.py
├── QP_app/  
├── templates/       # 新規作成
│    └──index.html
└── QP_project/

(プロジェクトフォルダ内 setting.py)
TEMPLATES = [
    ...
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
]

viewが直接ブラウザにレスポンスを返す時は、
    return HttpResponse(htmlドキュメント)
Templateに処理を渡す場合は、
    return render(request, 'テンプレートファイル名')

7.urlディスパッチャーを追加

http://127.0.0.1:8000/QP_app/localStorage


'''
 