import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Create canvas and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide axes

# Helper function: draw rounded rectangle with label
def draw_box(x, y, text, width=2.2, height=1.2, fontsize=10):
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.1",
                         edgecolor='black', facecolor='lightblue')
    ax.add_patch(box)
    ax.text(x + width / 2, y + height / 2, text, ha='center', va='center', fontsize=fontsize)

# Draw system components
draw_box(1, 8.2, "PV Module")
draw_box(6.5, 8.2, "Load Module")
draw_box(3.8, 6.2, "Simulation Core\n(SOC & Efficiency)")
draw_box(3.8, 4.2, "Battery System")
draw_box(1, 2.2, "Grid Import")
draw_box(6.5, 2.2, "Summary Metrics")
draw_box(3.8, 0.5, "Streamlit UI")

# Draw arrows between components
def draw_arrow(x1, y1, x2, y2):
    ax.annotate("",
                xy=(x2, y2), xycoords='data',
                xytext=(x1, y1), textcoords='data',
                arrowprops=dict(arrowstyle="->", lw=1.5))

# Define connections
draw_arrow(2.2, 8.2, 4.8, 7.4)   # PV → Core
draw_arrow(7.5, 8.2, 5.6, 7.4)   # Load → Core
draw_arrow(5, 6.2, 5, 5.4)       # Core → Battery
draw_arrow(5, 4.2, 2.5, 3.4)     # Battery → Grid
draw_arrow(5, 4.2, 7.5, 3.4)     # Battery → Summary
draw_arrow(2.1, 2.2, 4.3, 1.2)   # Grid → UI
draw_arrow(7.6, 2.2, 5.2, 1.2)   # Summary → UI

# Save and show figure
plt.tight_layout()
plt.savefig("system_architecture_diagram_en.png", dpi=300)
plt.show()
