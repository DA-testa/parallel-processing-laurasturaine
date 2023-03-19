# python3


def parallel_processing(n, m, data):

    output = []
    laiki=[0]*n  #saraksts ar garumu n, kur visiem elementiem ir piešķirta 0, lai uzraudzītu katra darbinieka laiku

    for x in range(m):
        laiks_min=min(laiki) #tiek noteikts darbinieks ar visīsāko apstrādes laiku
        pirm_index=laiki.index(laiks_min) #tiek noteikts darbinieka indekss ar visīsāko apstrādes laiku,
        output.append((pirm_index,laiks_min))
        if x<len(data):
            laiki[pirm_index]+=data[x]

    return output



def main():

    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pav_index, sak_laiks in result:
        print(pav_index, sak_laiks)


if __name__ == "__main__":
    main()
