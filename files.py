from pathlib import Path
from datetime import datetime


def main():
    rootdir = Path('/Users/frank/pd/Nextcloud')
    # Return a list of regular files only, not directories
    file_list = [f for f in rootdir.glob('**/*') if f.is_file()
                 and f.suffix in ('.xls', '.xlsx', '.XLS', '.XLSX', '.csv', '.CSV', '.txt')]
    interesting = [f for f in file_list if 'szamitas' not in str(f)]

    # For absolute paths instead of relative the current dir
    file2_list = [f for f in rootdir.resolve().glob('**/*') if f.is_file()]

    modetimes = [(datetime.utcfromtimestamp(int(f.stat().st_mtime)), f) for f in interesting]
    modetimes.sort(reverse=True)
    dirs = set()
    for f in modetimes:
        if f[0].date() > datetime.strptime('2022-05-01', '%Y-%m-%d').date():
            # print(f[0], f[1].parent)
            print(f"{f[0]}, H: {f[1].parents[1].name}, P: {f[1].parents[0].name}, F: {f[1].name}")
    # print(file2_list)


if __name__ == '__main__':
    main()
