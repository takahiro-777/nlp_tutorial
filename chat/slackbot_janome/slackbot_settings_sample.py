# coding: utf-8

# botアカウントのトークンを指定
API_TOKEN = "xxxxxxx"  #実際のAPIトークンに書き換え、ファイル名もslackbot_setting.pyに変更して使用すること

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "何言ってんだこいつ"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins_level1']    #slackbotの動作確認（ルールベース）
#PLUGINS = ['plugins_level2']   #形態素解析　＆　それを利用したタグ付け
#PLUGINS = ['plugins_level3']   #ネガポジ分析
