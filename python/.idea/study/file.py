# Created by TTT
#读取一个文档并实现目标分割
def method(count,l1,l2):
    name1 = 'l' + str(count) + '.txt'
    name2 = 'f' + str(count) + '.txt'
    ha = open(name1, 'w', encoding='utf-8')
    he = open(name2, 'w', encoding='utf-8')
    ha.writelines(l1)
    he.writelines(l2)
    ha.close()
    he.close()
def method2(filename):
    l1 = []
    l2 = []
    count = 1
    f = open(filename, 'r', encoding='utf-8')
    for line in f:
        if line[:6] != '======':
            (first, second) = line.split(":", 1)
            if first == '你好':
                l1.append(second)
            if first== '我们':
                l2.append(second)
        else:
            method(count,l1,l2)
            l1 = []
            l2 = []
            count += 1
    method(count,l1,l2)
    f.close()
method2('haha.txt')