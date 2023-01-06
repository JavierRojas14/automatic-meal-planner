SLOW_WEIGHT_LOSS_PER_WEEK = 500
FAST_WEIGHT_LOSS_PER_WEEK = 700


def calculate_cutting_metrics(current_bodyweight, current_fat_percentage, goal_fat_percentage):
    current_fat_percentage_as_float = current_fat_percentage / 100
    goal_fat_percentage_as_float = goal_fat_percentage / 100

    lbm = current_bodyweight - \
        (current_bodyweight * current_fat_percentage_as_float)
    lbm_plus_objective_fat_percentage = lbm / \
        (1 - goal_fat_percentage_as_float)
    weight_to_lose = current_bodyweight - lbm_plus_objective_fat_percentage

    weight_to_lose_grams = weight_to_lose * 1000

    time_to_lose_fat_slow_weeks = weight_to_lose_grams / SLOW_WEIGHT_LOSS_PER_WEEK
    time_to_lose_fat_fast_weeks = weight_to_lose_grams / FAST_WEIGHT_LOSS_PER_WEEK

    time_to_lose_fat_fast_months = time_to_lose_fat_fast_weeks / 4
    time_to_lose_fat_slow_months = time_to_lose_fat_slow_weeks / 4

    return (current_bodyweight, current_fat_percentage, goal_fat_percentage,
            lbm, lbm_plus_objective_fat_percentage, weight_to_lose, weight_to_lose_grams,
            time_to_lose_fat_slow_weeks, time_to_lose_fat_fast_weeks,
            time_to_lose_fat_slow_months, time_to_lose_fat_fast_months)


def print_cutting_metrics(current_bodyweight, current_fat_percentage, goal_fat_percentage,
                          lbm, lbm_plus_objective_fat_percentage, weight_to_lose, weight_to_lose_grams,
                          time_to_lose_fat_slow_weeks, time_to_lose_fat_fast_weeks,
                          time_to_lose_fat_slow_months, time_to_lose_fat_fast_months):

    print(f'Welcome User! This is the automatic cutting calculator!\n')
    print(f'Your actual metrics are:\n'
          f'> Current bodyweight: {current_bodyweight:.2f}Kg \n'
          f'> Current fat percentage: {current_fat_percentage:.2f}% \n'
          f'> Goal fat percentage: {goal_fat_percentage:.2f}% \n\n'
          f'Your calculated metrics are: \n'
          f'> Lean Body Mass (LBM): {lbm:.2f}Kg \n'
          f'> LBM + Goal fat percentage: {lbm_plus_objective_fat_percentage:.2f}Kg \n'
          f'> Weight to lose: {weight_to_lose:.2f}Kg \n\n'
          f'The estimated time to get to your goal is: \n'
          f'> Slow Weight Loss ({SLOW_WEIGHT_LOSS_PER_WEEK}grs per week): '
          f'{time_to_lose_fat_slow_weeks:.2f} Weeks or {time_to_lose_fat_slow_months:.2f} Months\n'
          f'> Fast Weight Loss ({FAST_WEIGHT_LOSS_PER_WEEK}grs per week): '
          f'{time_to_lose_fat_fast_weeks:.2f} Weeks or {time_to_lose_fat_fast_months:.2f} Months\n')


def get_cutting_plan():
    current_bodyweight = float(
        input('> What is your current Bodyweight in Kg? '))
    current_fat_percentage = float(
        input('> What is your current body fat percentage? '))
    goal_fat_percentage = float(
        input('> What is your goal body fat percentage? '))

    print_cutting_metrics(*calculate_cutting_metrics(current_bodyweight, current_fat_percentage,
                                                     goal_fat_percentage))


if __name__ == '__main__':
    get_cutting_plan()
