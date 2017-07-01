# coding: utf-8

import os
import sys
from janome.tokenizer import Tokenizer
import yaml
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ


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

@listen_to('janome sample')
def listen_func(message):
    t = Tokenizer()
    tokens = t.tokenize(u'pythonの本を読んだ')
    res = ""
    for token in tokens:
        res += str(token)+os.linesep
    message.send("```"+res+"```")

#@listen_to('cabocha sample')
#def listen_func(message):
#    c = CaboCha.Parser()
#    parsed =  c.parse("これは私のもっている赤いペンです")
#    message.send("```"+parsed.toString(CaboCha.FORMAT_TREE)+"```")

@default_reply()
def default_func(message):
    f = open("plugins_intermediate/word2tag.yml", "r+")
    word2tag = yaml.load(f)

    text = message.body['text']     # メッセージを取り出す
    # 送信メッセージを作る。改行やトリプルバッククォートで囲む表現も可能
    t = Tokenizer()
    #m = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    tokens = t.tokenize(text)
    #msg = 'あなたの送ったメッセージをmecabで解析します。\n```' + m.parse(text) + '```'
    tags = []
    for token in tokens:
        word = token.surface
        #品詞を取得
        pos = token.part_of_speech.split(',')[0]
        if word in word2tag:
            tags.append(word2tag[word])
        #print('{0} , {1}'.format(word, pos))
        #次の単語に進める
    message.reply("```Sentence you input is "+text+". Sentence tag is "+','.join(tags)+"```")      # メンション
    #message.send("Sentence tag is"+','.join(tags)+"```")

#@default_reply()
#def default_func(message):
#    text = message.body['text']     # メッセージを取り出す
    # 送信メッセージを作る。改行やトリプルバッククォートで囲む表現も可能
#    m = MeCab.Tagger ("-Ochasen")
#    msg = 'あなたの送ったメッセージをmecabで解析します。\n```' + m.parse(text) + '```'
#    message.reply(msg)      # メンション
