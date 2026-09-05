# UX Flows & Accessibility Checklist

## 1. User Journey Mapping Template

When designing a user flow, document:
1. **Trigger / Entry Point**: Where does the user arrive from? (Deep link, push notification, primary nav).
2. **User Goal**: What is the singular objective they are trying to achieve?
3. **Core Step Sequence**: The minimal path of steps from entry to completion.
4. **Friction Points & Edge Cases**: What happens on network disconnect? Unsaved changes back-press? Validation failure?
5. **Success State & Next Step**: What clear feedback confirms completion, and where does the user transition next?

---

## 2. WCAG 2.1 AA Compliance Checklist

### Visual
- [ ] Text contrast meets minimum 4.5:1 (normal text) or 3:1 (large text / UI components).
- [ ] Color is never the sole indicator of status (always pair color with an icon or text label).
- [ ] Text can scale up to 200% without clipping or breaking container boundaries.

### Interaction & Touch
- [ ] Touch targets are at least 48x48dp / 44x44pt.
- [ ] At least 8dp spacing between interactive touch areas.
- [ ] No gesture-only actions without an alternative single-tap or button equivalent.

### Assistive Technology
- [ ] All icon buttons have explicit, meaningful accessibility labels.
- [ ] Form fields are linked with explicit `<label>` / accessibility label elements.
- [ ] Status updates and dynamic errors use live regions (`aria-live="polite"` or platform announce).
- [ ] Keyboard focus ring is prominent and never removed via `outline: none` without replacement.
