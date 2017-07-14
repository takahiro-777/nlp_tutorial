# coding: utf-8

# botアカウントのトークンを指定
API_TOKEN = "xxxxxxx"  #実際のAPIトークンに書き換え、ファイル名もslackbot_setting.pyに変更して使用すること

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "何言ってんだこいつ"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins_level1']    #slackbotの動作確認（ルールベース）
#PLUGINS = ['plugins_level2']   #形態素解析　＆　それを利用したタグ付け
#PLUGINS = ['plugins_level3']   #ネガポジ分析
#PLUGINS = ['plugins_level4']   #TFIDFを用いた特徴語抽出
#PLUGINS = ['plugins_level5']   #word2vecを利用した単語の分散表現（老人と海）
#PLUGINS = ['plugins_level6']   #LDAを利用したトピック分析
#PLUGINS = ['plugins_level7']   #LSTMを利用した文章生成
#PLUGINS = ['plugins_level8']   #seq2seqを利用した翻訳
