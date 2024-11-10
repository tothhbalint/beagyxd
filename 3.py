from sympy import symbols, diff, solve

# Define the variable
f = symbols('f')

#custom values
a = 40
b1 = 2.5 
b2 = -6
b = b1*10**b2

#2.1 eredmenyei
#periodus ido
T = 64
#aktiv proc ido
c = 48.4
#inaktiv idok
N = 21

# contants for everyone
fmax = 800 # mhz
fmin = 50 #mhz
target_value = 3 * 10 ** -5 # joule

# Define the function to minimize
function = a/f + b * f**2

#3.1
# Step 1: Differentiate the function with respect to f
derivative = diff(function, f)

# Step 2: Find the critical points by setting the derivative to zero
critical_points = solve(derivative, f)

# Step 3: Filter out the real, positive critical points
real_positive_critical_points = [point for point in critical_points if point.is_real and point > 0]

f_opt = 0

# Step 4: Calculate the minimum value by evaluating the function at the critical point
if real_positive_critical_points:
    min_f = real_positive_critical_points[0]  # In this case, only one positive critical point exists
    minimum_value = function.subs(f, min_f)
    print(f"The minimum occurs at f = {min_f}, where the function value is {minimum_value:.4f}")
else:
    print("No real positive critical points found.")
    
f_opt = min_f

#3.2
# Calculate P(fmin)
P_fmin = a + b * fmin**3

# Solve for t in the inequality P(fmin) * t >= 3 * 10^-5
# Rearrange to get t >= target_value / P_fmin
if P_fmin != 0:  # Avoid division by zero
    t_min = target_value / P_fmin * 1000000000
    print(f"The solution is {t_min:.2f}μs")
else:
    print("P(fmin) is zero, cannot solve for t.")
    
#3.3

# ugly ass shit
E = (a + b*f_opt ** 3)*c*10**-3 + (N * (target_value*10**3))

print(E)