def plusMinus(arr):
    positive=negative=zero=0
    for num in arr:
        if num>0:
            positive += 1
        elif num<0:
            negative += 1
        else:
            zero +=1
    
    print(f"{positive/num:.6f}")
    print(f"{negative/num:.6f}")
    print(f"{zero/num:.6f}")

plusMinus([-2,-1,0,1,2])