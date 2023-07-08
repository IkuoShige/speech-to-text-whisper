import os
import whisper
import time

def transcribe_and_save_text(input_path, output_path, model_name="module", language='ja'):
    ## モデル（データセット）読み込み
    model = whisper.load_model("large")
 
    ## 音声へのパス
    #path ="test.m4a"
    path = input_path
 
    ## 結果を出力と同時に取得
    #result = model.transcribe(path, verbose=True, language='ja')
    result = model.transcribe(path, verbose=True, language='ja')

    ## テキストファイルに保存
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(str(result["text"]))

# mp3_dataディレクトリ内のファイルを処理
input_dir = "m4a_data/230705_NA2/"
output_dir = "transcriptions/230705_NA2"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file_name in os.listdir(input_dir):
    if file_name.endswith(".m4a"):
        print("======" + str(file_name) + "========")
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.txt")
        transcribe_and_save_text(input_path, output_path)
        time.sleep(3)
