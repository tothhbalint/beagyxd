from sympy import symbols, diff, solve
from typing import Union, Optional
import math

def format_scientific(num: float) -> str:
    """Format number in scientific notation if very small/large."""
    if abs(num) < 0.001 or abs(num) > 1000:
        return f"{num:.2e}"
    return f"{num:.4f}"

class PowerManagement:
    def __init__(self):
        # System constants
        self.fmax = 800  # MHz
        self.fmin = 50   # MHz
        self.target_value = 2e-5  # Joule
        
        # Custom values from problem
        self.a = 10
        self.b = 5 * 10**-6
        self.T = 192      # Period time
        self.c = 146.5    # Active process time
        self.N = 3      # Inactive times
        
        # Initialize symbolic variable
        self.f = symbols('f')
        self.function = self.a/self.f + self.b * self.f**2
        
    def find_optimal_frequency(self) -> Optional[float]:
        """Calculate optimal frequency for minimum energy consumption."""
        derivative = diff(self.function, self.f)
        critical_points = solve(derivative, self.f)
        real_positive_critical_points = [
            point for point in critical_points 
            if point.is_real and point > 0
        ]
        
        if not real_positive_critical_points:
            return None
        
        f_opt = float(real_positive_critical_points[0])
        minimum_value = float(self.function.subs(self.f, f_opt))
        return f_opt, minimum_value
    
    def calculate_breakeven_time(self) -> Union[float, str]:
        """Calculate the breakeven time for sleep mode."""
        P_fmin = self.a + self.b * self.fmin**3
        if P_fmin == 0:
            return "Cannot calculate: P(fmin) is zero"
        return (self.target_value / P_fmin) * 1e9  # Convert to μs
    
    def calculate_total_energy(self, f_opt: float) -> float:
        """Calculate total energy consumption for one hyperperiod."""
        return (self.a + self.b * f_opt**3) * self.c * 1e-3 + (self.N * (self.target_value * 1e3))

    def print_results(self):
        """Print formatted results with explanations."""
        print("\n=== Dynamic Power Management Analysis ===\n")
        
        # 3.1 Optimal Frequency
        f_opt, min_value = self.find_optimal_frequency()
        print("3.1 Optimal Operating Frequency:")
        print(f"  • f_opt = {format_scientific(f_opt)} MHz")
        print(f"  • Minimum energy at this frequency = {format_scientific(min_value)} mW")
        print()
        
        # 3.2 Breakeven Time
        t_min = self.calculate_breakeven_time()
        print("3.2 Sleep Mode Breakeven Time:")
        print(f"  • Minimum idle time for sleep mode = {format_scientific(t_min)} μs")
        print(f"  • This is the minimum time where P(f_min) * t ≥ {self.target_value:.0e} J")
        print()
        
        # 3.3 Total Energy Consumption
        total_energy = self.calculate_total_energy(f_opt)
        print("3.3 Total Energy Consumption per Hyperperiod:")
        print(f"  • Active energy: {format_scientific(self.a + self.b * f_opt**3 * self.c * 1e-3)} mJ")
        print(f"  • Sleep transition energy: {format_scientific(self.N * self.target_value * 1e3)} mJ")
        print(f"  • Total energy: {format_scientific(total_energy)} mJ")

# Run the analysis
if __name__ == "__main__":
    pm = PowerManagement()
    pm.print_results()