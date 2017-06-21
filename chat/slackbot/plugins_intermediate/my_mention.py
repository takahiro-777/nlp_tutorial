# coding: utf-8

import sys
import MeCab
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

#m = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
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

@listen_to('mecab sample')
def listen_func(message):
    m = MeCab.Tagger ("-Ochasen")
    message.send(m.parse ("mecabのアウトプットのサンプルを出力します。"))

@default_reply()
def default_func(message):
    text = message.body['text']     # メッセージを取り出す
    # 送信メッセージを作る。改行やトリプルバッククォートで囲む表現も可能
    m = MeCab.Tagger ("-Ochasen")
    #m = MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    m.parse('')
    node = m.parseToNode(text)
    node = node.next
    #msg = 'あなたの送ったメッセージをmecabで解析します。\n```' + m.parse(text) + '```'
    if node:
        word = node.surface
        #品詞を取得
        pos = node.feature.split(",")[1]
        #print('{0} , {1}'.format(word, pos))
        #次の単語に進める
        #node = node.next
    message.reply("First word is "+word)      # メンション

#@default_reply()
#def default_func(message):
#    text = message.body['text']     # メッセージを取り出す
    # 送信メッセージを作る。改行やトリプルバッククォートで囲む表現も可能
#    m = MeCab.Tagger ("-Ochasen")
#    msg = 'あなたの送ったメッセージをmecabで解析します。\n```' + m.parse(text) + '```'
#    message.reply(msg)      # メンション
