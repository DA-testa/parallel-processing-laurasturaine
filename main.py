# python3


def parallel_processing(n, m, data):
    reizes1=[0]*n
    output = []

    for x in range(m):
        laiks_min=min(reizes1)
        index=reizes1.index(laiks_min)
        output.append((reizes1,laiks_min))
        if x<len(data):
            reizes1[index]+=data[x]


    return output

def main():

    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_index, sak_laiks in result:
        print(thread_index, sak_laiks)


if __name__ == "__main__":
    main()
