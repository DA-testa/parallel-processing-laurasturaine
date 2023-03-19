# python3


def parallel_processing(n, m, data):

    output = []
    reizes=[0]*n
    for x in range(m):
        laiks_min=min(reizes)
        pirm_index=reizes.index(laiks_min)
        output.append((pirm_index,laiks_min))
        if x<len(data):
            reizes[pirm_index]+=data[x]

    return output

def main():

    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_index, start_time in result:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()
