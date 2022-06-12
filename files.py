from pathlib import Path
from datetime import datetime


def main():
    rootdir = Path('/Users/frank/pd/Nextcloud')
    # Return a list of regular files only, not directories
    file_list = [f for f in rootdir.glob('**/*') if f.is_file()
                 and f.suffix in ('.xls', '.xlsx', '.XLS', '.XLSX', '.csv', '.CSV', '.txt')
                 and 'audit' not in f.stem]
    interesting = [f for f in file_list if 'szamitas' not in str(f)]

    # For absolute paths instead of relative the current dir
    # dir_list = [f for f in rootdir.resolve().glob('**/*') if f.is_dir()]
    dir_list = [f for f in rootdir.glob('**/*') if f.is_dir()]

    modetimes = [(datetime.utcfromtimestamp(int(f.stat().st_mtime)), f) for f in interesting]
    modetimes.sort(reverse=True)
    dirs = set()
    for f in modetimes:
        # if f[0].date() > datetime.strptime('2022-01-01', '%Y-%m-%d').date():
        #     # print(f[0], f[1].parent)
        #     print(f"{f[0]}, M: {f[1].parents[1].name} | S: {f[1].parents[0].name} | FILE: {f[1].name}")
        if f[0].date() > datetime.strptime('2021-01-01', '%Y-%m-%d').date():
            file_date = f[0]
            dir_date = datetime.utcfromtimestamp(f[1].parent.stat().st_mtime)
            time_diff = (file_date - dir_date).total_seconds()/3600
            # if dir_date > f[0]:
            if time_diff < -9.0 and f[1].parent.name == 'bookmate':
                print(file_date, f[1].stem, dir_date, f[1].parent.name, time_diff)

            # print(f"{f[0]}, M: {f[1].parents[1].name} | S: {f[1].parents[0].name} | FILE: {f[1].name}")


if __name__ == '__main__':
    main()
