'''
新規作成
Webアプリケーション分のURLディスパッチャーを定義
'''
from django.urls import path
from . import views # 同ディレクトリのviews.pyをimport

urlpatterns  = [
    path('', views.index, name = 'index'),
    path('foo', views.foo, name = 'foo'),
    path('localStorage', views.localStorage, name = 'localStorage')
]