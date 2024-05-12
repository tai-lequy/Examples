from itertools import count
def main():
    sequence = count(start=2.5, step=0.5)
    var1 = next(sequence)
    print(var1)
    #while True:
    #    print(next(sequence))
    #while(next(sequence) <= 8):
    #    print(sequence)
if __name__ == '__main__':
    main()


