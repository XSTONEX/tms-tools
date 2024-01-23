import argparse

def upload(args):
    print(f"Uploading {args.type} from {args.file}")
    # 添加上传逻辑

def load(args):
    print(f"Downloading {args.type} from {args.file} to {args.directory}")
    # 添加下载逻辑

def search(args):
    print(f"Searching for {args.type} files matching {args.name}")
    # 添加搜索逻辑

def main():
    parser = argparse.ArgumentParser(description="TMS Command Line Tool")
    subparsers = parser.add_subparsers(dest='command', help='commands')

    # upload 命令
    upload_parser = subparsers.add_parser('upload', help='Upload files or folders')
    upload_parser.add_argument('-t', '--type', type=str, choices=['lora', 'ckpt'], required=True, help='Type of the file')
    upload_parser.add_argument('-f', '--file', type=str, required=True, help='File or folder path')
    upload_parser.set_defaults(func=upload)

    # load 命令
    load_parser = subparsers.add_parser('load', help='Download files or folders')
    load_parser.add_argument('-t', '--type', type=str, choices=['lora', 'ckpt'], required=True, help='Type of the file')
    load_parser.add_argument('-f', '--file', type=str, required=True, help='File or folder path')
    load_parser.add_argument('-d', '--directory', type=str, default='autodl-tmp/sd', help='Destination directory')
    load_parser.set_defaults(func=load)

    # search 命令
    search_parser = subparsers.add_parser('search', help='Search for files')
    search_parser.add_argument('-t', '--type', type=str, choices=['lora', 'ckpt'], required=True, help='Type of the file')
    search_parser.add_argument('name', type=str, help='Fuzzy name of the file')
    search_parser.set_defaults(func=search)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
