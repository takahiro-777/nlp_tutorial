# slackbot(pipモジュール)の利用方法

## インストール
```
# mecabのインストール(Mac)
$ brew install mecab
$ brew install mecab-ipadic
$ brew install git curl xz

# mecabのインストール(Windows)

# 下記のブログを参考に、mecab-0.98.exeを使ってインストールを行う
# http://handsrecs2nd.seesaa.net/article/140090025.html
# 辞書の文字コードは"UTF-8"を選択すること

# neologd辞書(新語辞書)のインストール

$ git clone --depth 1 git@github.com:neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ ./bin/install-mecab-ipadic-neologd -n

# MeCab-Python(PythonからMeCabを呼び出すためのPythonライブラリ)のインストール

$ pip install mecab-python3

# cabochaのインストール(参考: http://www.maytry.net/how-to-use-cabocha-mecab-with-python/)
https://drive.google.com/folderview?id=0B4y35FiV1wh7cGRCUUJHVTNJRnM&usp=sharing#list　より、cabocha-0.69.tar.bz2をダウンロードする。
$ brew install crf++
$ tar jxf cabocha-0.69.tar.bz2
$ cd cabocha-0.69
$ ./configure --with-mecab-config=`which mecab-config` --with-charset=utf8 # これでエンコードのエラーが出ないはず
$ make
$ sudo make install

$ cd python
$ sudo python setup.py install

#slackbotのインストール
$ pip install slackbot
```

# 参考資料
```
http://qiita.com/taroc/items/b9afd914432da08dafc8

```
