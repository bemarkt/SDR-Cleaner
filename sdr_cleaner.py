#!/usr/bin/env python3
import shutil
import os
import time

from pathlib import Path


def handle_path(path: Path):
    global sdrs
    global files
    subfolders = []
    for entry in path.iterdir():
        if entry.is_dir():
            if entry.suffix == ".sdr":
                sdrs.add(path/entry.stem)
            else:
                subfolders.append(entry)
        else:
            files.add(path/entry.stem)
    for folder in subfolders:
        handle_path(folder)


def clean_files():
    diff = sdrs - files
    if diff.__len__() == 0:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(
            f"ENG: Volume \033[1;31m{path.__str__()[0:1]}\033[0m No SDR files found that can be deleted.\nCHN: \033[1;31m{path.__str__()[0:1]}\033[0m 盘中没有发现可以删除的SDR文件夹。")
        print("系统 3 s后退出...")
        time.sleep(3)
        os._exit(0)
    for sdr_to_remove in diff:
        sdr_path = Path(f"{sdr_to_remove}.sdr")
        print("Remove:", sdr_path)
        shutil.rmtree(sdr_path)


if __name__ == "__main__":
    sdrs = set()
    files = set()
    while(1):
        path = Path(
            input("ENG: Input Kindle Volume(like E,F.etc):\nCHN: 请输入 Kindle 所在盘符（比如e、f等）: ") + ":\\")
        try:
            handle_path(path)
        except Exception as e:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(e)
            continue
        clean_files()
