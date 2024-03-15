def solution(R, V):


  # Initialize bank balances with 0
  bank_a, bank_b = 0, 0

  # Iterate through each transfer
  for i, recipient in enumerate(R):
    # Check if the recipient is bank A
    if recipient == "A":
      # Deduct the transfer amount from bank B
      bank_b -= V[i]
      # Update bank A balance only if it's enough to cover the transfer
      if bank_a >= V[i]:
        bank_a -= V[i]
      else:
        # Calculate minimum initial balance for bank A to avoid debt
        min_balance_a = max(bank_a, V[i])
        # Update bank A balance with the minimum required amount
        bank_a = min_balance_a - V[i]
    else:
      # Deduct the transfer amount from bank A
      bank_a -= V[i]
      # Update bank B balance only if it's enough to cover the transfer
      if bank_b >= V[i]:
        bank_b -= V[i]
      else:
        # Calculate minimum initial balance for bank B to avoid debt
        min_balance_b = max(bank_b, V[i])
        # Update bank B balance with the minimum required amount
        bank_b = min_balance_b - V[i]

  # Return the minimum initial balances for both banks
  return [min(bank_a, 0), min(bank_b, 0)]

# Example usage with intermediate value printing
R = "BAABA"
V = [2, 4, 1, 1, 2]
result = solution(R, V)

# Print intermediate values for debugging
initial_bank_a, initial_bank_b = 0, 0
# final_bank_a, final_bank_b = bank_a, bank_b

print("Initial balances:", initial_bank_a, initial_bank_b)
# print("Final balances:", final_bank_a, final_bank_b)
print("Minimum initial balances:", result)
