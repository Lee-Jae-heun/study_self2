# 드레이븐의 Q 스킬은 스텍을 쌓습니다.
# 스텍은 무조건 정수로 취급합니다.
# 일반 미니언은 스텍 1개
# 대포 미니언은 스텍 2개
# 챔피언을 죽일 시 스텍이 2배가 됩니다.
# 챔피언에게 죽을 시 스텍의 75%를 잃습니다.
# 일반 미니언 A, 대포 미니언 B, 챔피언을 죽일 시 O, 챔피언에게 죽을 시 X 일때
# 단 미니언으로 스텍을 연속으로 쌓을시 다음 스텍 1개가 추가됩니다.(무한 중첩 가능)
# 입력을 받고 최종적으로 남아있는 스텍을 출력하시오

cc = list(map(str,input().split()))
stack = 0; find = 2; a=0; b=0
for i in cc:
    if i == 'A':
        stack += 1
        if not find:
            a += 1
            b = 0
            stack += a
        find = 0

    elif i == 'B':
        stack += 2
        if find:
            b += 1
            a = 0
            stack += b
        find = 1

    elif i == 'O':
        stack *= 2

    else:
        stack = stack/4
print(stack)