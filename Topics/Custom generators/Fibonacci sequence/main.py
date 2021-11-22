def fibonacci(n):
    fb0, fb1 = 0, 1
    for i in range(n):
        yield fb0
        fb1, fb0 = fb1 + fb0, fb1