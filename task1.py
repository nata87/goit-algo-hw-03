from pathlib import Path
import shutil
import argparse

def user_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type = Path)
    parser.add_argument("dest", type = Path, nargs='?',default=Path('dist'))
    return parser.parse_args()

def copy_files(root : Path, dest : Path):
    try:
        for item in root.iterdir():
            if item.is_dir():
                copy_files(item,dest)
            else:
                ext = item.suffix[1:]
                if ext:
                    ext_d = dest / ext
                    ext_d.mkdir(parents=True, exist_ok=True)
                    shutil.copy(item, ext_d)
    except Exception as e:
        print(f"Error reading file: {e}")


if __name__ == "__main__":
    args = user_input()
    print(args.source, args.dest)

    copy_files(args.source, args.dest)
  