def main():
    with open('xmls.txt', mode='r') as f:
        for line in f.readlines():
            print(line)
            line2 = line.replace('xml', '')
            print(line2)
            line3 = line2.replace('.', ',')
            print(line3)
            line4 = line3.replace(",", "','")
            print(line4)


if __name__ == '__main__':
    main()