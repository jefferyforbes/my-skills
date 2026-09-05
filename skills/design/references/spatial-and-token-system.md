# Spatial Grid & Design Token Systems Reference

This reference provides exact numerical scales, typography systems, and color token architectures for interface design.

---

## 1. 8pt / 4pt Spatial Grid
Use strictly defined intervals for paddings, margins, and component dimensions:
- **4dp**: Micro-spacing (icon to text gap, tag padding).
- **8dp**: Compact component padding (dense lists, small chips).
- **16dp**: Standard container margin and list item separation.
- **24dp**: Section separation and card gutter.
- **32dp / 48dp**: Page header spacing and hero element margins.

---

## 2. Semantic Color Token Hierarchy
Never use raw hex colors in UI code. Always map through tokens:
- \`surface.primary\`: Main background (light: #FFFFFF, dark: #121212).
- \`surface.variant\`: Elevated cards and modal surfaces.
- \`content.primary\`: High-emphasis text (contrast ratio $\ge 7:1$).
- \`content.secondary\`: Muted supporting captions (contrast ratio $\ge 4.5:1$).
- \`status.error\`: Critical failure banners and form validation errors.
