# python3
import heapq

def parallel_processing(n, m, data):
    threads=[(i,0) for i in range(n)]
    heapq.heapify(threads)

    jobs[(i,data[i]) for i in range(m)]
    output = []

    for job in jobs:
        thread = heapq.heappop(threads)
        output.append((thread[0], thread[1]))
        heapq.heappush(threads, (thread[0], thread[1] + job[1]))

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n,m=map(int,input().split())
    data=list(mp(int,input().split()))
    output=parallel_processing(n,m,data)

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for r in output:
        print(r[0], r[1])


if __name__ == "__main__":
    main()
