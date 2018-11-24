###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """
    """
    # Not a dynamic programming method, but a greedy algorithm method
    if target_weight <= 0:
        return sum(memo.values())

    chosen_weight_list = [k for k in egg_weights if k <= target_weight]

    if chosen_weight_list:
        chosen_weight = max(chosen_weight_list)
        if chosen_weight in memo:
            memo[chosen_weight] += 1
        else:
            memo[chosen_weight] = 1

        left = target_weight - chosen_weight

        return dp_make_weight(egg_weights, left, memo)
    """
    # memo is used to store the minimum numbers for target_weight
    min_nums = target_weight
    if target_weight <= 0:
        return 1
    # Look up memo to check out if there is already a best solution
    elif target_weight in memo:
        return memo[target_weight]
    else:
        for weight in [k for k in egg_weights if k <= target_weight]:
            # Divide the problem into several subproblems
            num_eggs = 1 + dp_make_weight(egg_weights, target_weight-weight, memo)
            if num_eggs < min_nums:
                min_nums = num_eggs
            memo[target_weight] = min_nums

    return min_nums





# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    n = 16
    print("Expected output: 3 (1 * 10 + 1 * 5 + 1 * 1 = 16)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
