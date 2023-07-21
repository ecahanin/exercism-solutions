# def find_fewest_coins(coins, target):
#     if target < coins[0] or (len(coins) == 0 and target > 0):
#         raise ValueError('Cannot make change for given amount')
#     elif target == 0:
#         return []
#     else:
#         greatest_coin = coins.pop()
#         while greatest_coin > target:
#             greatest_coin = coins.pop()
        
#         if target % greatest_coin == 0:
#             return [greatest_coin] * int(target/greatest_coin)
#         else:
#             possibles = []
#             for i in range(target//greatest_coin):
#                 possibles.append([greatest_coin] * i)
#                 possibles[i].extend(find_fewest_coins(sorted(coins), target - greatest_coin * i))

#             return sorted(possibles, key=len)[0]
    






def find_fewest_coins(coins, target):
    if (len(coins) == 0 and target > 0) or 0 < target < coins[0] or target < 0:
        raise ValueError('Cannot make change for given amount')
    elif target == 0:
        return []
    else:
        solutions = []
        while len(coins) >= 1:
            highest_coin = coins.pop()
            most_hc = target//highest_coin


            best = []
            for i in range(most_hc, -1, -1):
                soln = [highest_coin] * i
                
                remainder = target - highest_coin * i
                remaining_coins = coins[:]
                try:
                    soln.extend(find_fewest_coins(remaining_coins, remainder))
                    if not best or len(soln) < len(best):
                        best = sorted(soln)
                except ValueError:
                    pass
                
                
            if best:
                solutions.append(best)

        if not solutions:
            raise ValueError('Cannot make change for given amount')
        else:
            return sorted(solutions, key=len)[0]


if __name__=="__main__":
    print(find_fewest_coins([4,5],27))
