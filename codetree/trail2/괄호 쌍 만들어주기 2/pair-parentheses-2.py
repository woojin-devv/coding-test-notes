A = input()
stack = []

cnt = 0 

# i는 첫번째 '('
for i in range(len(A)):
    # j는 두번째 '('
    for j in range(i, len(A)):
        # K는 첫번째 ')'
        for k in range(j, len(A)):
            # K는 두번째 ')'
            for l in range(k, len(A)):
                if (
                    A[i] == '('
                    and A[j] == '('
                    and abs(i-j) == 1
                    and A[k] == ')'
                    and A[l] == ')'
                    and abs(k-l) == 1
                    ): cnt +=1 

print(cnt)