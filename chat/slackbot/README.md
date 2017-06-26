# slackbot(pipモジュール)の利用方法

## インストール(Mac)
```
# mecabのインストール
$ brew install mecab
$ brew install mecab-ipadic
$ brew install git curl xz
$ git clone --depth 1 git@github.com:neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ ./bin/install-mecab-ipadic-neologd -n
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

## インストール(Windows)

### mecab(64bit版)のインストール

MeCabは32bit版しか配布されていない。

MeCabのWindows用Pythonバインディングは、64bit版のMeCabしか扱えないようであるので、ソースからコンパイルする必要がある

http://qiita.com/o__mura/items/31fb75df6183199e95b6

上記のリンクの方法を参考にされたい

大まかな手順は

1. 必要なファイルをMeCabの公式のGoogle Driveからダウンロード(mecab-0.996.exe, mecab-0.996.tar.gz, mecab-python-0.996.tar.gz)
2. mecab-0.996.exeを実行して、MeCabの辞書や設定ファイルを作成する
3. MeCabをコンパイルするために、Visual Studio 2015をインストールする
4. 64bit版のMeCabのコンパイルを行うために、mecab-0.996.tar.gzを展開して、ソースコードを改変する
5. MeCabの64bit版をコンパイルする
6. mecab-pythonもそのままではインストールできない(pipではインストールできない)ので、ソースコードから直接インストールを行う

### neologd(新語辞書)をインストールする(任意)

neologdという新しい単語の辞書があると、より正確に形態素解析を行うことができます

+ git bashをインストールする
  + https://git-for-windows.github.io/

+ 下記のブログを参考に辞書を追加する
  + http://qiita.com/rinkuro/items/9d17f2dc5a23fa5bfb28

