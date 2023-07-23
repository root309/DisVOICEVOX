# 使い方

- Discordデベロッパーツールで新しいボットを作成します。

# 必要なダウンロード
- 音声データの合成を行うためにVOICEVOXが必要です。
- https://voicevox.hiroshiba.jp/
- ボイスチャンネルで音声を流すために、以下のリンクからFFmpegをダウンロードしてください。
- https://ffmpeg.org/download.html

# 環境変数の設定

- 作成したボットのトークンをWindowsの環境変数に登録してください。変数名はソースコードを参照してください。
- ダウンロードしたFFmpegのexeファイルのパスをWindowsの環境変数に設定してください。変数名はソースコードを参照してください。

# 使用技術

- FFmpeg: Discordのボイスチャンネルで音声データを流すために使用します。
- Discord API: Discordのボットを動かすために使用します。
- VOICEVOX API: テキストを読み上げる音声データとして使用します。