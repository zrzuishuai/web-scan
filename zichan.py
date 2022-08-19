def zichan():
    with open(r'./ip_1.txt','r',encoding='utf-8') as f:
        result = f.readlines()
        for i in result:
            if '.' in i:

                url = i.split('\t')
                print(url)
                with open('ip_3.txt', 'a') as fp:
                    fp.write(url[1])
                    fp.write('\n')

if __name__ == '__main__':
    zichan()