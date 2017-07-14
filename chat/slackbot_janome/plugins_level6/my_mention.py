# coding: utf-8

import sys
import numpy as np
import csv
import gensim
from pandas import DataFrame
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ


# タグのid(key)とname(value)を結びつける辞書の作成
tag_name_dict = {}
with open('plugins_level6/data/qiita_tags.csv', 'r') as f_tags:
    tag_reader = csv.reader(f_tags)

    for i, row in enumerate(tag_reader):
        tag_name_dict[(i+1)] = row[0]

#  あるユーザー（key）がどのタグをフォローしているか
user_tags_dict = {}
with open('plugins_level6/data/qiita_user_tags.csv', 'r') as f_user_tags:
    user_tags_reader = csv.reader(f_user_tags)

    for i, row in enumerate(user_tags_reader):
        user_tags_dict[int(row[0])] = row[1:-1]

# tags_list フォローされているタグのリスト (複数人にフォローされていればダブリあり)
tags_list = []
for k, v in user_tags_dict.items():
    tags_list.extend(v)

# 1人にしかフォローされていないタグ
once_tags = [tag for tag in tags_list if tags_list.count(tag) == 1]

# 1人しかフォローされていないタグをuser_tagsのタグからも削除
user_tags_dict_multi = { k: [tag for tag in user_tags if not tag in once_tags] for k, user_tags in user_tags_dict.items()}

# タグをフォローしていないユーザーを省く (1人しかフォローしていないタグは削除していることに注意)
user_tags_dict_multi = {k: v for k, v in user_tags_dict_multi.items() if not len(v) == 0}

# gemsimへのインプットのために変換
corpus = [[(int(tag), 1) for tag in user_tags]for k, user_tags in user_tags_dict_multi.items()]

# LDAのモデルの呼出と学習 ここでtopicの数(ユーザー層の数）を設定出来る
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, num_topics=15)

# 各トピックの出現頻度上位１０位を取得
topic_top10_tags = []
for topic in lda.show_topics(-1, formatted=False):
    topic_top10_tags.append([tag_name_dict[int(tag[0])] for tag in topic[1]])

# 各トピックの出現頻度上位１０位を表示
topic_data = DataFrame(topic_top10_tags)
print(topic_data)
print("------------------")

# ユーザーの嗜好の表示
c = [(1, 1), (2, 1)] # タグ1とタグ2をフォローしているユーザー
for (tpc, prob) in lda.get_document_topics(c):
    print(str(tpc) + ': '+str(prob))

@listen_to('lda sample')
def listen_func(message):
    res = "```"+str(topic_data)
    res = res+"\n===========\n\nユーザ嗜好\n"
    c = [(1, 1), (2, 1)] # タグ1とタグ2をフォローしているユーザー
    for (tpc, prob) in lda.get_document_topics(c):
        res = res + str(tpc) + ': '+str(prob) + "\n"
    res = res+"```"

    #print(vecs.toarray())
    message.reply(res)


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
