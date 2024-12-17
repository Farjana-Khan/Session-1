# Assignment 24: Write a function that calculates compound interest using the formula A = P(1 + r/n)^(nt).

def compound_interest(principal, rate, times_compounded, time):
    """
    Calculate compound interest.

    Parameters:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate in decimal form.
    times_compounded (int): The number of times that interest is compounded per year.
    time (float): The time the money is invested for in years.

    Returns:
    float: The final amount after compound interest.
    """
    A = principal * (1 + rate / times_compounded) ** (times_compounded * time)
    return A

# Example usage
P = 1000  # Initial amount
r = 0.05  # Annual interest rate (5%)
n = 4     # Number of times interest is compounded per year
t = 10    # Time in years

final_amount = compound_interest(P, r, n, t)
print(f"Final amount after compound interest: {final_amount:.2f}")
