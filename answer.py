def solution(A, D):
  # the current balance
  balance = 0
  # empty disctionary to store payment counts
  card_payments = {}
  # total incomes without card payments
  total_income = 0
  # looping through the transactions
  for i in range(len(A)):
    amount = A[i]
    date_str = D[i]
    year,month,_ = map(int,date_str.split('-') ) 
    
    # updating balance by adding 
    balance+=(amount)
    # updating the card payment
    if amount < 0:
      if  (year, month) not in card_payments.keys():
        card_payments[(year, month)]= amount
      else:
        card_payments[(year, month)]+= amount
        
    # updating the total income
    if amount >=0:
      total_income +=amount 
    # calculating the total fee per month
    # Calculate the fee for each month
    month_fee = sum(3 for month, count in card_payments.items() if count < 5 or (month, 0) not in card_payments or total_income - 100 < 100)
  
    # subtracting monthly fee from balance
    balance -= month_fee
    
    return balance
  
# testing
A = [100, 100, 100, -10]
D = ["2020-12-22", "2020-12-03", "2020-12-29"]
print(solution(A, D)) 
      
        
      