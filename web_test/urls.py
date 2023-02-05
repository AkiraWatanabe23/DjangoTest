from django.urls import path
from . import views

#このアプリ内でアクセス可能なURLのリスト
urlpatterns = [
    #引数↓
    #1, URLに記述する文字列(今回の場合、「/web_test/」以降に続くもの)
    #2, 指定したURLにアクセスしたときに、どのようなビューをレンダリングするのか
    #3, URLを示すために名前を付ける(アプリケーションからの参照を楽にするため)
    path('start', views.index, name='index'),
    path("<str:name>", views.greet, name="greet"),
    path('brain', views.brain, name='brain')
]
