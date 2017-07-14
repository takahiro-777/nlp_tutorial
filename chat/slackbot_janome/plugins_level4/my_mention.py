# coding: utf-8

import sys
import numpy as np
import json
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

#f = open("plugins_level3/polarity.yml", "r+")
#polarity = yaml.load(f)
np.set_printoptions(precision=2)

@listen_to('tfidf sample')
def listen_func(message):
    docs = np.array([
            '白 黒 赤',      # 文書１
            '白 白 黒',      # 文書２
            '白 黒 黒 黒',   # 文書３
            '白'            # 文書４
            ])
    vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')
    vecs = vectorizer.fit_transform(docs)

    #print(vecs.toarray())
    message.reply("```◆input\n"+str(docs)+"\n\n◆output\n白\t\t赤\t\t黒\n"+str(vecs.toarray())+"```")


@default_reply()
def default_func(message):
    #f = open("plugins_difficult/polarity.yml", "r+")
    #polarity = yaml.load(f)
    """
    text = message.body['text']     # メッセージを取り出す
    # 送信メッセージを作る。改行やトリプルバッククォートで囲む表現も可能
    t = Tokenizer()
    #m = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    tokens = t.tokenize(text)
    #msg = 'あなたの送ったメッセージをmecabで解析します。\n```' + m.parse(text) + '```'
    pol_val = 0
    for token in tokens:
        word = token.surface
        #品詞を取得
        pos = token.part_of_speech.split(',')[0]
        if word in polarity:
            pol_val = pol_val + float(polarity[word])
        #print('{0} , {1}'.format(word, pos))
        #次の単語に進める
    message.reply("```Sentence you input is "+text+". Sentence polarity is "+str(pol_val)+"```")      # メンション
    #message.send("Sentence tag is"+','.join(tags)+"```")
    if pol_val > 0.2:
        message.react('+1')
        message.reply("それはいいね！！")
    elif pol_val < -0.2:
        message.react('cry')
        message.reply("そうか、どんまい")
    else:
        message.reply("なるほど、そうなんですね〜")
    """
