# coding: utf-8

import sys
from janome.tokenizer import Tokenizer
import yaml
import codecs
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

#f = open("plugins_level3/polarity.yml", "r+")
f = codecs.open("plugins_level3/polarity.yml", 'r', 'utf-8')
polarity = yaml.load(f)


@respond_to('メンション')
def mention_func(message):
    message.reply('私にメンションと言ってどうするのだ') # メンション

@listen_to('リッスン')
def listen_func(message):
    message.send('誰かがリッスンと投稿したようだ')      # ただの投稿
    message.reply('君だね？')

@listen_to('今日の天気は？')
def listen_func(message):
    message.send('晴れのち曇りです。')      # ただの投稿

@listen_to('羊たちの')
def listen_func(message):
    message.send('沈黙')      # ただの投稿

@listen_to('mecab')
def listen_func(message):
    m = MeCab.Tagger ("-Ochasen")
    message.send(m.parse ("今日もしないとね"))

@default_reply()
def default_func(message):
    #f = open("plugins_difficult/polarity.yml", "r+")
    #polarity = yaml.load(f)

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
