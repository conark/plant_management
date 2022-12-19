import subprocess

subprocess.run(["./streaming.sh", "arguments"], shell=True)


#　test 必要
# import os
# import subprocess

# # スクリプトを実行するディレクトリのパス
# dir_path = "/home/pi/plant_management/plant_factory_environment_management"

# # スクリプトのファイル名のリスト
# scripts = ["schedule_pi.py", "temp_humid.py","streaming.sh"]

# # スクリプトを順番に実行
# for script in scripts:
#     # 拡張子に応じて実行コマンドを切り替え
#     if script.endswith(".py"):
#         subprocess.run(["python", os.path.join(dir_path, script)])
#     elif script.endswith(".sh"):
#         subprocess.run(["bash", os.path.join(dir_path, script)])