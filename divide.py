import os

def split_mp3(file_path, chunk_size):
    file_name = os.path.basename(file_path)
    output_dir = os.path.dirname(file_path)
    output_prefix = os.path.splitext(file_name)[0]

    with open(file_path, 'rb') as file:
        chunk_counter = 0
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            output_file = os.path.join(output_dir, f'{output_prefix}_{chunk_counter}.mp3')
            with open(output_file, 'wb') as output:
                output.write(chunk)

            chunk_counter += 1

        print(f'{chunk_counter} files created.')

# ファイルパスとチャンクサイズを指定して実行する例
file_path = 'mp3_data/path-to-file.mp3'  # 分割したいMP3ファイルのパス
chunk_size = 24 * 1024 * 1024  # 25MBをバイト単位で指定

split_mp3(file_path, chunk_size)
