import sys

N = int(sys.stdin.readline().strip('\n'))
heap = [2**31]

for _ in range(N) :
    x = int(sys.stdin.readline().strip('\n'))
    if x == 0 : # 최대 힙 삭제
        if len(heap) == 1 :
            sys.stdout.write(f'{0}\n')
        else :
            sys.stdout.write(f'{heap[1]}\n')
            temp = heap[-1]
            heap[-1] = heap[1]
            heap[1] = temp
            del heap[-1]
            
            if len(heap) == 3 and heap[1] < heap[2] :
                temp = heap[1]
                heap[1] = heap[2]
                heap[2] = temp
            else :
                parent = 1
                try :
                    while ((parent * 2) + 1 < len(heap) or (parent * 2) < len(heap)) and max(heap[parent * 2], heap[(parent * 2) + 1]) > heap[parent] :
                        if heap[parent * 2] > heap[(parent * 2) + 1] : # 자식 왼 < 오
                            temp = heap[parent * 2]
                            heap[parent * 2] = heap[parent]
                            heap[parent] = temp
                            parent *= 2
                        else : # 자식 완 > 오
                            temp = heap[(parent * 2) + 1]
                            heap[(parent * 2) + 1] = heap[parent]
                            heap[parent] = temp
                            parent = (parent * 2) + 1
                except IndexError : # 힙이 짝수일때 뜬다
                    while ((parent * 2) < len(heap) or (parent * 2) < len(heap)) and heap[parent * 2] > heap[parent] :
                            temp = heap[parent * 2]
                            heap[parent * 2] = heap[parent]
                            heap[parent] = temp
                            parent *= 2

    else : # 최대 힙 추가
        heap.append(x)
        if len(heap) == 3 and heap[1] < heap[2] :
            temp = heap[1]
            heap[1] = heap[2]
            heap[2] = temp
        else :
            child = len(heap) - 1
            while child >= 2 and heap[child] > heap[child // 2] : # 자식 > 부모
                temp = heap[child // 2]
                heap[child // 2] = heap[child]
                heap[child] = temp
                child //= 2
    # print(heap)