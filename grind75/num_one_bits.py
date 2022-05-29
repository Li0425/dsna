def hammingWeight(n: int) -> int:
    n_list = list(str(n))
    all_ones = len(n_list) * [1]
    zips = list(zip(n_list, all_ones))
    print(zips)
    
    ans = 0
    for pair in zips:
        ans += int(pair[0]) & pair[1]
    return ans

input = '00000000000000000000000000001011'
print(hammingWeight(input))