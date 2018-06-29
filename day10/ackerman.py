def ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

print("ackerman (4, 0) is: %d" % ack(4, 0))
print("ackerman (3, 0) is: %d" % ack(3, 0))