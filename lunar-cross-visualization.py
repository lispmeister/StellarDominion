import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# ================================================
# Scientifically Accurate Lunar Laser Cross Visualization
# Exact naked-eye angular scales (no artistic enlargement)
# ================================================

fig = plt.figure(figsize=(14, 9), facecolor='black')
ax = fig.add_subplot(111)
ax.set_facecolor('black')

# Set angular coordinate system (degrees on sky)
# x = horizontal angular position (degrees)
# y = vertical angular position (degrees above horizon)
ax.set_xlim(-2.0, 2.0)
ax.set_ylim(0.0, 1.5)          # Moon low at ~15° but scaled for visual clarity
ax.set_aspect('equal')         # True angular proportions

# Remove axes spines and ticks for clean sky look
ax.axis('off')

# ==================== STARS ====================
np.random.seed(42)  # reproducible star field
n_stars = 300
star_x = np.random.uniform(-2.0, 2.0, n_stars)
star_y = np.random.uniform(0.0, 1.5, n_stars)
ax.scatter(star_x, star_y, color='white', s=np.random.uniform(0.5, 3, n_stars), 
           alpha=np.random.uniform(0.6, 1.0, n_stars), edgecolor='none')

# ==================== HORIZON ====================
ax.axhline(y=0.0, color='#1e3a5f', linewidth=6, zorder=1, label='Horizon')
ax.text(-1.95, 0.03, 'Horizon', color='white', fontsize=12, fontfamily='monospace')

# ==================== SCALE BAR (1°) ====================
ax.plot([-1.0, 0.0], [0.08, 0.08], color='white', linewidth=2)
ax.plot([-1.0, -1.0], [0.06, 0.10], color='white', linewidth=2)
ax.plot([0.0, 0.0], [0.06, 0.10], color='white', linewidth=2)
ax.text(-0.5, 0.12, '1°', color='white', fontsize=14, ha='center', fontfamily='monospace')
ax.text(-1.95, 0.15, 'Observers on Earth\n(looking up)', color='white', fontsize=11, 
        ha='left', va='top', fontfamily='monospace')

# ==================== FULL MOON (exactly 0.5° diameter) ====================
moon_center_x = 0.0
moon_center_y = 0.35
moon_radius = 0.25   # = 0.5° diameter

moon = Circle((moon_center_x, moon_center_y), moon_radius, 
              facecolor='#f8f1e9', edgecolor='#e5d9c8', linewidth=2, zorder=10)
ax.add_patch(moon)

# Slight lunar surface shading for realism
ax.add_patch(Circle((moon_center_x - 0.08, moon_center_y + 0.08), 0.12, 
                    facecolor='#e5d9c8', alpha=0.4, zorder=11))

# Label for Moon
ax.text(moon_center_x, moon_center_y - 0.42, 'FULL MOON\n(exactly 0.5° apparent diameter)', 
        color='white', fontsize=13, ha='center', va='top', fontfamily='monospace')

# ==================== EMERALD-GREEN LASER CROSS ====================
# Center of cross = lunar northern limb (top of Moon)
cross_center_x = moon_center_x
cross_center_y = moon_center_y + moon_radius   # exactly at top limb

# Cross total span = 0.7° (matches continental US angular width from Moon)
# Each arm: 0.7° long × 0.05° thick (matches README solid-angle calculation)
cross_half_span = 0.35        # half of 0.7°
cross_half_thickness = 0.025  # half of 0.05°

# Horizontal arm (filled rectangle in data coordinates)
ax.fill([cross_center_x - cross_half_span, cross_center_x + cross_half_span,
         cross_center_x + cross_half_span, cross_center_x - cross_half_span],
        [cross_center_y - cross_half_thickness, cross_center_y - cross_half_thickness,
         cross_center_y + cross_half_thickness, cross_center_y + cross_half_thickness],
        color='#00ff9d', zorder=20)

# Vertical arm (filled rectangle in data coordinates, symmetric 0.7° span)
ax.fill([cross_center_x - cross_half_thickness, cross_center_x + cross_half_thickness,
         cross_center_x + cross_half_thickness, cross_center_x - cross_half_thickness],
        [cross_center_y - cross_half_span, cross_center_y - cross_half_span,
         cross_center_y + cross_half_span, cross_center_y + cross_half_span],
        color='#00ff9d', zorder=20)

# Label for the cross
ax.text(cross_center_x + 0.05, cross_center_y + cross_half_span + 0.28,
        'EMERALD-GREEN LASER CROSS\n(~0.7° angular span from lunar north pole)\n'
        'Visible simultaneously across the entire continental US',
        color='#00ff9d', fontsize=14, ha='left', va='top', fontfamily='monospace',
        bbox=dict(boxstyle="round,pad=0.5", facecolor='black', alpha=0.7))

# Title
ax.text(0.0, 1.42, 'Scientifically Accurate Visualization\n'
                   'Lunar Laser Cross Projection from Northern Pole\n'
                   '(Exact naked-eye angular scales — no artistic enlargement)',
        color='white', fontsize=16, ha='center', fontfamily='monospace', weight='bold')

# ==================== SAVE / SHOW ====================
plt.tight_layout()
plt.savefig('lunar_cross_scientific_visualization_proper_cross.png', dpi=300, bbox_inches='tight')
plt.show()

