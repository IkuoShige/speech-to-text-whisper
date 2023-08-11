# speech-to-text-whisper

## Overview

音声データをテキストファイルに文字起こしを行います。

OpenAIのwhisperを使用します。

## Directory Configuration
```
speech-to-text-whisper
├── LICENSE
├── README.md
├── api.py
├── convert.py
├── divide.py
├── m4a_data
│   └── sample
│       └── sample.m4a
├── transcribe_and_save.py
└── transcription
    └── sample
        └── sample.txt
```

## Usage

1. 各種インストール
    * whisperのインストール
        ```
        pip install git+https://github.com/openai/whisper.git
        ```
    * ffmpegのインストール
        ```
        pip install ffmpeg-python
        ```

2. 25MB未満の音声データ(m4a)を用意する

    音声データが25MB以上の場合は、`divide.py`を実行して分割する
        
    `divide.py`は、mp3に対応している

    文字起こししたい音声データがm4aで且つ25MBより大きい場合は、`convert.py`を実行し、m4a→mp3に変換し、`divide.py`を実行し、mp3を分割し、`convert.py`を実行し、mp3→m4aに変換する

    `convert.py`はm4a→mp3、mp3→m4aに対応している

3. 音声データを`m4a_data`ディレクトリに配置し、`transcribe_and_save.py`を実行


### divide.py

* 音声ファイル(mp3)を25MB未満に分割して保存する

変換したいmp3ファイルのパスに合わせて、`file_path`を変更してください

### convert.py

* 音声ファイルの変換を行う
    * mp3→m4a
    * m4a→mp3

適宜、プログラムを書き換えてください
* 変換したいファイルに対応した関数に変更
* 入出力のファイルパスの変更

### transcribe_and_save.py

OpenAIの重み(small, middle, large)を選択し、音声データから文字起こしを行う

* `input_dir`にm4aデータが配置されているディレクトリのパスを設定
* `output_dir`に文字起こしした内容を書き込むディレクトリのパスを設定

OpenAIの重みは初回実行時にダウンロードされる

2回目以降はそのまま文字起こし実行される

## Extra

### api.py

OpenAIのAPIを使用して、文字起こしを行う
* 注意点
    * 課金してないとAPI制限に引っかかるので使えない