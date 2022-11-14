current_x = 2
rate = 0.01
precision = 0.000001
previous_step_size = 1
max_iters = 1000
iters = 0
df= lambda x: 2*(x+3)
while previous_step_size > precision and iters < max_iters:
    previous_x = current_x
    current_x = current_x - rate*df(previous_x)
    previous_step_size = abs(current_x - previous_x)
    iters = iters+1
    print("Iterations", iters, "\nX value is", current_x)
print("The local minium occurs at", current_x)
