---
name: Sonic Utility Interface
colors:
  surface: '#16130b'
  surface-dim: '#16130b'
  surface-bright: '#3c392f'
  surface-container-lowest: '#100e06'
  surface-container-low: '#1e1b12'
  surface-container: '#221f16'
  surface-container-high: '#2d2a20'
  surface-container-highest: '#38352a'
  on-surface: '#e9e2d3'
  on-surface-variant: '#cfc6ae'
  inverse-surface: '#e9e2d3'
  inverse-on-surface: '#333026'
  outline: '#98907b'
  outline-variant: '#4c4735'
  surface-tint: '#e3c53b'
  primary: '#fff5da'
  on-primary: '#3a3000'
  primary-container: '#f7d84d'
  on-primary-container: '#6f5e00'
  inverse-primary: '#6f5d00'
  secondary: '#73d1ff'
  on-secondary: '#003548'
  secondary-container: '#00b0e6'
  on-secondary-container: '#003e54'
  tertiary: '#fff3f1'
  on-tertiary: '#680200'
  tertiary-container: '#ffcec6'
  on-tertiary-container: '#b12c1d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe263'
  primary-fixed-dim: '#e3c53b'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#534600'
  secondary-fixed: '#c1e8ff'
  secondary-fixed-dim: '#73d1ff'
  on-secondary-fixed: '#001e2b'
  on-secondary-fixed-variant: '#004d67'
  tertiary-fixed: '#ffdad4'
  tertiary-fixed-dim: '#ffb4a7'
  on-tertiary-fixed: '#400100'
  on-tertiary-fixed-variant: '#8f1107'
  background: '#16130b'
  on-background: '#e9e2d3'
  surface-variant: '#38352a'
typography:
  headline-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  body-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 14px
  label-caps:
    fontFamily: Inter
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 12px
    letterSpacing: 0.05em
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 12px
spacing:
  unit: 4px
  container-padding: 12px
  element-gap: 4px
  section-margin: 16px
---

## Brand & Style
This design system is engineered for deep integration within a digital audio workstation (DAW) environment. The personality is **Industrial, Technical, and Unobtrusive**. It prioritizes function over form, ensuring that the AI assistant feels like a native hardware expansion rather than a third-party overlay.

The style follows **Technical Minimalism**, characterized by:
- **High Density:** Maximizing information display in compact sidebars and floating panels.
- **Low Visual Friction:** Using flat surfaces and subtle tonal shifts to prevent distraction from the main arrangement view.
- **Instrument-Grade Precision:** Every UI element mimics the tactile reliability of high-end studio hardware—sharp, responsive, and systematic.

## Colors
The palette is derived directly from the Ableton Live 12 "Mid Dark" ecosystem. It utilizes a monochromatic foundation of neutral grays to manage visual hierarchy, accented by vibrant signal colors for status and interactivity.

- **Backgrounds:** `#242424` for the primary container; `#2e2e2e` for elevated panels.
- **Accents:** 
    - **Live Yellow (#f7d84d):** Used for primary actions, active AI processing states, and high-priority highlights.
    - **Ableton Blue (#3cc7ff):** Used for selection states, modulation indicators, and secondary interactive paths.
- **Typography:** `#cccccc` (Off-white) for primary labels to reduce eye strain in low-light studio environments; `#888888` for disabled or de-emphasized metadata.

## Typography
Typography is optimized for extreme legibility at small scales. **Inter** provides a neutral, modern clarity for the majority of the UI, while **JetBrains Mono** is introduced for parameter values and technical data to ensure character differentiation (e.g., distinguishing '0' from 'O').

- **Hierarchy:** Use Uppercase labels for section headers to mimic hardware faceplates.
- **Constraints:** Avoid any font size larger than 14px to maintain the professional DAW aesthetic. 
- **Rendering:** Ensure `antialiased` font-smoothing is active for all small-scale labels.

## Layout & Spacing
The layout follows a **Rigid Grid** philosophy based on 4px increments. The AI Assistant should exist primarily as a fixed-width sidebar (300px - 400px) or a collapsible bottom panel.

- **Density:** Elements are packed tightly. A standard vertical gap between controls should be 4px.
- **Alignment:** All text labels must align to the left edge of their respective control or input.
- **Responsive:** In the DAW context, the layout doesn't "reflow" so much as it "crops." Priority is given to the most essential controls (AI prompt input and generation results).

## Elevation & Depth
Depth is communicated through **Tonal Layers** and **1px Borders** rather than shadows. In a production environment, shadows create visual clutter.

- **Base Layer:** `#242424` (Main Assistant background).
- **Surface Layer:** `#2e2e2e` (Used for cards, input fields, and recessed areas).
- **Borders:** `1px solid #3d3d3d` is the universal separator. Use it to define the perimeter of all interactive components.
- **Active State:** Elements do not "lift"; they change color or gain a high-contrast border (Live Yellow or Blue).

## Shapes
This design system uses **Sharp (0px)** roundedness. Every button, input, and container is a perfect rectangle. This reinforces the industrial, grid-based nature of Ableton Live and maximizes pixel-perfect alignment in a high-density UI.

## Components
- **Buttons:** Completely flat. Default state matches the surface color (`#3d3d3d`). Hover state lightens the background. Primary "Generate" buttons use `Live Yellow` with black text.
- **Input Fields:** Recessed appearance using a darker background than the surface (`#1a1a1a`). 1px border. No rounded corners.
- **Knobs/Sliders:** Vertical or circular controls for AI parameters (e.g., "Creativity" or "Complexity"). Use a 2px stroke for the indicator in `Ableton Blue`.
- **Chips:** Used for genre or mood tags. Small (18px height), background `#3d3d3d`, text `#cccccc`.
- **Waveform Visualizers:** High-contrast line art using `#3cc7ff`. Use a semi-transparent fill for the area under the curve.
- **Status Indicators:** Small 6px squares. Green for "Ready", Pulsing Yellow for "Thinking", Blue for "Applying to Track".