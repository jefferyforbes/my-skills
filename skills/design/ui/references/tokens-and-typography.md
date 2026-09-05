# UI Tokens & Typography Reference

## 1. Modular Typography Scales

Major Third (1.250) or Perfect Fourth (1.333) scales for screen layouts:

| Token Name | Font Size | Line Height | Letter Spacing | Font Weight | Typical Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `display-lg` | 40px / 2.5rem | 1.15 | -0.02em | 700 / Bold | Hero marketing / Landing headers |
| `display-sm` | 32px / 2.0rem | 1.20 | -0.015em | 700 / Bold | Page titles / Dashboard headers |
| `heading-lg` | 24px / 1.5rem | 1.25 | -0.01em | 600 / SemiBold | Major section headers / Modal titles |
| `heading-md` | 20px / 1.25rem| 1.30 | 0.0em | 600 / SemiBold | Card titles / Group headers |
| `body-lg` | 16px / 1.0rem | 1.50 | 0.0em | 400 / Regular | Default body copy / Input text |
| `body-md` | 14px / 0.875rem | 1.45 | 0.0em | 400 / Regular | Compact tables / Secondary list items |
| `caption` | 12px / 0.75rem | 1.40 | +0.02em | 500 / Medium | Timestamps / Field helpers / Footnotes |
| `overline` | 11px / 0.6875rem | 1.35 | +0.06em | 700 / Bold | Category tags / Sub-status labels (Uppercase) |

---

## 2. Standard Semantic Token Schema

```json
{
  "surface": {
    "base": "Neutral canvas background",
    "subtle": "Grouped background / subtle container",
    "raised": "Cards, sheets, elevated panels",
    "overlay": "Modals, popovers, dropdown menus"
  },
  "content": {
    "primary": "High-contrast headings, active text",
    "secondary": "Body text, supporting metadata",
    "muted": "Disabled text, subtle placeholders",
    "inverse": "High-contrast text on dark/brand surfaces"
  },
  "border": {
    "subtle": "Dividers, card outlines, neutral gutters",
    "focus": "Focus ring indicator (high contrast)",
    "error": "Invalid field perimeter"
  },
  "status": {
    "success": "Confirmations, active sync, completed states",
    "warning": "Pending actions, rate limit alerts, non-blocking errors",
    "danger": "Irreversible actions, validation errors, system outages",
    "info": "Informational callouts, neutral highlights"
  }
}
```

---

## 3. Visual Depth & Elevation

- **Level 0 (Flat)**: Content flush with canvas (`surface-base`).
- **Level 1 (Subtle)**: `box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05)`. Cards, resting containers.
- **Level 2 (Interactive Hover / Float)**: `box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)`. Dropdowns, active cards.
- **Level 3 (Overlays)**: `box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)`. Modals, floating sheets.
