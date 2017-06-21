# coding: utf-8

from slackbot.bot import listen_to

@listen_to('あきらめたら')
@listen_to('諦めたら')
@listen_to('akirametara')
def anzai(message):
    message.send('そこで試合終了ですよ。')

@listen_to('いいですか')
def reaction(message):
    message.react('+1')
