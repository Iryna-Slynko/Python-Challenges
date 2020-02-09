def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  sum=0
  count=1
  while count<n:
    if n%count==0:
      sum+=count
    count+=1
  return sum

print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16
