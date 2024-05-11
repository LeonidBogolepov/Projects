import heapq # очердь с приоритетами
from collections import Counter, namedtuple

class Node (namedtuple("Node", ["left", "right"])): #внутрений узел, именованный кортеж (принимает имя класса и его атрибуты)
    def walk(self, code, acc ):#обход узла. асс это префикс
        self.left.walk(code, acc + "0")#спуск в левого потомка
        self.right.walk(code, acc + "1")#спуск в правого потомка

class Leaf (namedtuple("Leaf", ["char"])): #лист, и символ который в этом листе записан
    def walk(self, code, acc):
        code[self.char] = acc or "0" # запись в словарь code построеный код символа или 0(что бы мог быть 1символ)

def huffman_encode(s):
    h = [] #массив h
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))#добавление в массив
    heapq.heapify(h)#создание очереди с приоритетами
    count = len(h) # счётчик уникальный для всех листьев
    while len(h)>1:
        freq1, _count1, left = heapq.heappop(h) #левый узел в очереди с приоритетами
        freq2, _count2, right = heapq.heappop(h) #правый узел в очереди с приоритетами
        heapq.heappush(h, (freq1+freq2, count, Node(left, right))) # добавление нового элемента в очередь с приоритетами, добавляется новый узел с потомками left и right
        count +=1
    code = {}#для пустой строки на вводи
    if h:
        [(_freq, count, root)] = h #корень дерева
        root.walk(code, "")#обход дерева начиная с корня и заполнение словаря code
    return code

def huffman_decode(en, code):
    pointer = 0
    encoded_str = ''
    while pointer < len(en):
        for ch in code.keys():
            if en.startswith(code[ch], pointer):
                encoded_str += ch
                pointer += len(code[ch])
    return encoded_str

def main():
    print("Введите строку:")
    s =input()
    code = huffman_encode(s)
    encoded ="".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)
    decode= huffman_decode(encoded, code )
    print("Расшифровка:")
    print(decode)
if __name__ == "__main__":
    main()