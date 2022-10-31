import time

def solution(s):
    s = s.replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9').replace('zero', '0')
    answer = int(s)
    return answer

if __name__ == '__main__':
    start = time.time()

    solution('one1seveneight')

    end = time.time()
    print('걸린시간 : ', end - start)
