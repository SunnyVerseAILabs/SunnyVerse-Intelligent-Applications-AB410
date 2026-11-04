# Optional Visual Design — DC Operations Command Center

[Return to Part 06 — Functional Build](../Build-Guide.md#part-06--build-the-operations-command-center-canvas-app)

This optional styling activity is for learners who want a more polished operations dashboard. Complete the working five-screen Canvas App and its functional tests first. **No formula, Dataverse table, permissions, lookup or app behavior needs to change** to apply the following style.

## Visual direction: trustworthy infrastructure operations

Use a restrained **navy + teal** palette, with amber for attention and clean, light neutral surfaces. The result should look like an enterprise operations interface: clear hierarchy, immediately readable data, and low visual noise. Color is an aid to comprehension, not the only way to indicate an alarm or status.

| Role | Color | Hex | Suggested use |
| --- | --- | --- | --- |
| **Primary — Deep navy** | Navy | `#123A56` | Header bar, primary actions and selected navigation |
| **Secondary — Operations teal** | Teal | `#147D86` | Active selection, focus and secondary actions |
| **Accent — Signal amber** | Amber | `#E7A43C` | Priority highlights and KPI accent bands; use **dark text** |
| Background | Soft cloud | `#F3F7FA` | All screen backgrounds |
| Surface | White | `#FFFFFF` | Galleries, forms, KPI cards |
| Primary text | Ink | `#12283F` | Titles, body content and text on amber |
| Muted text | Slate | `#526577` | Supporting text, descriptions |
| Dividers | Cool border | `#DAE4EC` | Card outlines, gallery separators |
| Critical status | Deep red | `#B42318` | P1/critical indicator and error states |
| Positive status | Green | `#137547` | Resolved/healthy state |
| Selected row | Pale teal | `#D9EDF0` | Selected gallery row |
| Warning surface | Soft amber | `#FFF5E5` | Warning/KPI background |

The palettes give strong text contrast when navy, teal, red or green appears on white. **Do not place white text on amber**; use `#12283F` there. Check text/control contrast, including hover and focus states, rather than relying on color alone.

## Apply the theme in Power Apps Studio

### D01 — Background and header

Open **DC Operations Command Center → Edit**. In **Tree view**, select each screen (`scrHome`, `scrIncidents`, `scrIncidentDetail`, `scrIncidentEdit` and `scrAlarms`). Set its **Fill** property to:

```powerfx
ColorValue("#F3F7FA")
```

For each screen, insert a **Rectangle** using **Insert → Icons/Shapes → Rectangle**, or the available Shapes menu. Rename the rectangle with a screen-specific identifier such as `shpHomeHeader` or `shpAlarmsHeader`. Place the rectangle behind the existing title; use **Reorder → Send to back** (or Tree view order). Set:

| Header rectangle property | Formula / value |
| --- | --- |
| X | `0` |
| Y | `0` |
| Width | `Parent.Width` |
| Height | `84` |
| Fill | `ColorValue("#123A56")` |
| BorderThickness | `0` |

Move the screen title label into the visible header area with `X = 32`, `Y = 18`, `Height = 48` and `Width = Parent.Width - 64`. On the title label, set **Color** to `ColorValue("#FFFFFF")`, **Fill** to `RGBA(0, 0, 0, 0)`, and **Font** to **Segoe UI** if available. Use size **26** with a bold weight. The header is a visual shape only; it must not cover buttons or forms.

### D02 — Buttons, text inputs, surfaces

Style all main navigation and action buttons in the five screens. Set each Classic button property using the formula bar:

| Button property | Formula / value |
| --- | --- |
| Fill | `ColorValue("#123A56")` |
| Color | `ColorValue("#FFFFFF")` |
| HoverFill | `ColorValue("#147D86")` |
| HoverColor | `ColorValue("#FFFFFF")` |
| PressedFill | `ColorValue("#0A5660")` |
| PressedColor | `ColorValue("#FFFFFF")` |
| BorderThickness | `0` |
| Height | `44` |
| Font | **Segoe UI**, if offered |
| RadiusTopLeft / TopRight / BottomLeft / BottomRight | `10` (where supported) |

For a secondary button such as **Refresh** or **Cancel**, choose `Fill = ColorValue("#147D86")` and keep white text. Keep every control's **Text** and **OnSelect** formulas from the main guide—this activity changes appearance only.

Use **white Fill**, **ink text** (`#12283F`), **cool border** (`#DAE4EC`) and a **teal focused border** (`#147D86`) for the incident/alarm search controls. Use the same clean white background and cool border for editable and display forms, when those properties are exposed.

### D03 — Home KPI cards

The Home screen already has `lblCountIncidents`, `lblCountAlarms` and `lblCountAssets`. Give those existing count labels a polished card treatment without duplicating them.

For each label, insert a **Rectangle** behind it, rename the rectangle `shpKpiIncidents`, `shpKpiAlarms` or `shpKpiAssets`, and configure:

| KPI card property | Formula / value |
| --- | --- |
| X | `lblCountIncidents.X - 8` (substitute the associated label for each card) |
| Y | `lblCountIncidents.Y - 8` |
| Width | `lblCountIncidents.Width + 16` |
| Height | `lblCountIncidents.Height + 16` |
| Fill | `ColorValue("#FFFFFF")` |
| BorderColor | `ColorValue("#DAE4EC")` |
| BorderThickness | `1` |

Use the corresponding label's dimensions for Alarm and Asset cards. **Send the rectangles backward**, leaving the existing KPI labels in front. Set the labels' **Color** to `ColorValue("#12283F")`, **Fill** to transparent and **Font size** to **22**; preserve the working `CountIf` formulas.

For extra hierarchy, insert a slim **4-pixel rectangle** along the left inside edge of each KPI card: teal for Incidents, amber for Alarms, and navy for Assets. Treat these as decorative strips and keep the numerical counts and captions readable.

### D04 — Galleries without placeholder images

In `galRecentIncidents`, `galIncidents` and `galAlarms`, keep only the readable title, subtitle/status labels and a selection chevron. There is no equipment photograph in the data model, so remove image placeholders.

| Gallery property | Formula / value |
| --- | --- |
| Fill | `ColorValue("#FFFFFF")` |
| TemplateFill | `If(ThisItem.IsSelected, ColorValue("#D9EDF0"), ColorValue("#FFFFFF"))` |
| TemplateSize | `78` (increase only if text clips) |
| BorderColor | `ColorValue("#DAE4EC")` |
| BorderThickness | `1` |

Set gallery title text to **ink** `#12283F`, subtitle text to **muted slate** `#526577`, and leave **OnSelect** intact. If a gallery label or chevron blocks selection, set its **OnSelect** property to `Select(Parent)`.

### D05 — Incident and alarm status indicators

For the **Incident Status** text label already inside `galIncidents`, optionally set its **Color** formula to reflect status and retain the text label itself:

```powerfx
Switch(
    Text(ThisItem.'Incident Status'),
    "New", ColorValue("#B42318"),
    "Assigned", ColorValue("#123A56"),
    "In Progress", ColorValue("#AF711D"),
    "Resolved", ColorValue("#137547"),
    "Closed", ColorValue("#526577"),
    ColorValue("#12283F")
)
```

For the **Alarm Severity** text label in `galAlarms`:

```powerfx
Switch(
    Text(ThisItem.'Alarm Severity'),
    "Critical", ColorValue("#B42318"),
    "High", ColorValue("#AF711D"),
    "Medium", ColorValue("#123A56"),
    "Low", ColorValue("#137547"),
    ColorValue("#12283F")
)
```

**Always display the written status/severity as well as its color.** Some users cannot distinguish hues, and colors must not be the only indication of urgency.

### D06 — Optional visual-only review

Preview each screen at the intended tablet size. The header should not overlap content, Home counts should remain legible, galleries should show several rows without large placeholders, the form controls should be easy to read, and buttons should have clear hover/focus states.

If any styling causes clipping, undo that individual change; do not alter validated Dataverse formulas to accommodate the theme. Check control contrast against [Microsoft's Canvas App accessibility guidance](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/accessible-apps-color). Save and publish the new styling only after the functional app still passes its main tests.
