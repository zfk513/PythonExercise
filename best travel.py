def choose_best_sum(t, k, ls):
    sorted_distance=ls.sorted()
    sum_distance=0
    for i in range(1,k):
    for a in range(len(sorted_distance)):
        for b in range(a+1,len(sorted_distance)):
            for c in range(b+1,len(sorted_distance)):
                sum_distance_now=
                if sum_distance_now<t and sum_distance<sum_distance_now:
                    sum_distance= sum_distance_now
    return sum_distance
print(choose_best_sum(230, 4,[100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]))