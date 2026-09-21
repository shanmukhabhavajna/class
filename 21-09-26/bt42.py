import numpy as np
import matplotlib.pyplot as plt
import os

# --- Parameters ---
V0 = 1.0
tau = 40.0

t = np.linspace(0, 5 * tau, 500)
v_out = V0 * (1 - np.exp(-t / tau))

# Print Theoretical Values
n_values = [0, 1, 2, 3, 4, 5]
for n in n_values:
    tp = n * tau
    vt = V0 * (1 - np.exp(-tp / tau))
    print(f"{n}τ ({tp:.0f}s): {vt:.4f} V ({vt/V0*100:.2f}%)")

# --- Plotting ---
plt.figure(figsize=(8, 4.5))
plt.plot(t, v_out, color='blue', linewidth=2)
plt.axhline(y=V0, color='red', linestyle='--')
plt.title('First-Order RC Circuit Step Response')
plt.xlabel('Time (s)')
plt.ylabel('v_out (V)')
plt.grid(True)

# Save image instead of showing window
file_name = "rc_graph.png"
plt.savefig(file_name, dpi=300, bbox_inches='tight')
print(f"\nGraph saved as {file_name}")

# Open automatically in Android Image Viewer
os.system(f"termux-open {file_name}")

