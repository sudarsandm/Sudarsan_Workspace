def rec_coin(target, coins):
    min_coins = target
    print("value was %d" %target)

    if target in coins:
        print("%d was in the list" %target)
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            print("In the for loop and %d" %i)
            num_coins = 1 + rec_coin(target-i, coins)
            print("%d iteration and %d coins" %(i, num_coins))
            
            if num_coins < min_coins:
                min_coins = num_coins
                print("%d was minimum num of coins" %min_coins)
    return min_coins
