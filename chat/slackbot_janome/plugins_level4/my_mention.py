# coding: utf-8

import sys
from janome.tokenizer import Tokenizer
from gensim.models import word2vec
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

model   = word2vec.Word2Vec.load("plugins_level4/model/rojinto_umi.model")


@default_reply()
def default_func(message):
    text = message.body['text']     # メッセージを取り出す
    results = model.most_similar(positive=text, topn=10)

    res = "```"
    for result in results:
        res = res+str(result[0])+'\t'+str(result[1])+'\n'

    res = res+"```"
    message.reply(res)
