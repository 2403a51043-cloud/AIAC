
# The calculation in factr is incorrect for factorial; it should be n * factr(n - 1)
def factr_correct(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factr_correct(n - 1)

print(factr_correct(5))
