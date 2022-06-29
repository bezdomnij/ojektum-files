from pathlib import Path
from datetime import datetime

CURRENT_DIR = '2022_05_may'


def main():
    rootdir = Path('/Users/frank/pd/Nextcloud')

    # Return a list of regular files only, not directories
    file_list = [f for f in rootdir.glob('**/*') if f.is_file()
                 and f.suffix.lower() in ('.xls', '.xlsx', '.csv', '.txt')
                 and 'audit' not in f.stem]
    interesting = [f for f in file_list if 'szamitas' not in str(f)]

    # For absolute paths instead of relative the current dir
    # dir_list = [f for f in rootdir.resolve().glob('**/*') if f.is_dir()]

    list_current_dir_content(rootdir)
    list_files(interesting)


def list_current_dir_content(rootdir):
    dir_list = [f for f in rootdir.glob('**/*') if f.is_dir()
                and f.parents[0].name == CURRENT_DIR
                and f.parents[1].name != 'szamitas']
    print()
    for d in dir_list:
        print(d)


def list_files(interesting):
    """
    modtimes - a list of tuples: mod_time, file (path object)
    :param interesting: a list of file path objects that has the monitored suffix
    :return:
    """
    modtimes = [(datetime.utcfromtimestamp(int(f.stat().st_mtime)), f) for f in interesting]
    modtimes.sort(reverse=True)
    print()
    for f in modtimes:
        if f[0].date() > datetime.strptime('2022-01-01', '%Y-%m-%d').date():
            # print(f[0], f[1].parent)
            print(f"{f[0]}, M: {f[1].parents[1].name} | S: {f[1].parents[0].name} | FILE: {f[1].name}")
        # print('*' * 10)
        measure_timediff(f, store='bookmate')  # check what happened with Bookmate files


def measure_timediff(f, store=''):
    """
    old file in a new directory? --> where was it before, was it included in a fin.report before?
    Bookmate has a tendency to move around
    """
    if f[0].date() > datetime.strptime('2021-01-01', '%Y-%m-%d').date():
        file_date = f[0]
        dir_date = datetime.utcfromtimestamp(f[1].parent.stat().st_mtime)
        time_diff = round((file_date - dir_date).total_seconds() / 3600 / 24, 2)
        # if dir_date > f[0]:
        if time_diff < -3.0 and f[1].parent.name == store:
            print(file_date, f[1].stem, dir_date, f[1].parent.name, time_diff)

        # print(f"{f[0]}, M: {f[1].parents[1].name} | S: {f[1].parents[0].name} | FILE: {f[1].name}")


if __name__ == '__main__':
    main()
