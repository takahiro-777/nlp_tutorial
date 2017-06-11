# chat-bot作成にあたって

## 概要
chat-bot作成にあたって

## 構成
### make-meidai-dialogue
```
http://qiita.com/knok/items/b24deb8cff3df48920ee
を参考にしながら、
https://github.com/knok/make-meidai-dialogue
を使用して元データをダウンロードし、用意した。

シェル（元記事消去の可能性もあるので念のため）
$ git clone https://github.com/knok/make-meidai-dialogue
$ cd make-meidai-dialogue
$ make
$ nkf -w -X -Z0 sequence.txt | \ # 全角英数字、かなの正規化
sed -ne '/^input/s/^input: //p' | mecab -Owakati > input.txt
$ nkf -w -X -Z0 sequence.txt | \
sed -ne '/^output/s/^output: //p' | mecab -Owakati > output.txt
$ cd ..
```

### tf-seq2seq-mod
```
http://qiita.com/knok/items/b24deb8cff3df48920ee
を参考にしながら、
https://github.com/knok/tf-seq2seq-mod
のコードを動かし、学習・推論を行えるようにした。tensorflowのモジュールの読み込みがうまくいっていなかったので、一部コードは修正した。（バージョン1.1.0を想定して修正した。）

シェル（元記事消去の可能性もあるので念のため）
$ mkdir train
$ git clone https://github.com/knok/tf-seq2seq-mod
$ cd tf-seq2seq-mod
$　python translate.py --data_dir ../make-meidai-dialogue --train_dir ../train --size 400 --en_vocab_size 10000 --fr_vocab_size 10000 --num_layers 1 --batch_size 5  #学習の実行
$ python translate.py --data_dir ../make-meidai-dialogue --train_dir ../train --size 400 --en_vocab_size 10000 --fr_vocab_size 10000 --decode  #推論の実行
```

推論用flaskサーバの立ち上げ  
```
python translate_flask.py --data_dir ../make-meidai-dialogue --train_dir ../train --size 400 --en_vocab_size 10000 --fr_vocab_size 10000
```

### old
```
http://qiita.com/san_/items/128bf1b5a898ad5c18f1  
にseq2seqを利用した簡易実装があったので、ベースに使われるのではないかと思われた。が、あまりにデータセットが少なくまともな会話になっていなかった。  
別で見つけたものの方が良さそうだったので、oldに置いた。
```
