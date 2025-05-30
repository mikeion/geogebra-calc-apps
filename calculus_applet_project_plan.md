# Calculus Interactive Applet Project Plan

## Overview
This project aims to design and build a website where students work through five interactive activities, each focused on a core calculus concept. Each activity will:
- Present both informal and formal definitions.
- Feature an interactive applet (GeoGebra recommended for smoothness and flexibility).
- Scaffold student reflection and conceptual understanding.

## Core Concepts / Activities
1. **Derivative at a Point**
2. **Derivative as a Function**
3. **Continuity (at a point and on an interval)**
4. **Integral (as area/limit of sums)**
5. **Sequences and Series (with convergence/limits)**

Each activity should:
- Visualize how limits underpin the concept.
- Allow for direct manipulation (sliders, draggable points, etc.).
- Include prompts for prediction, reflection, and explanation.

## Technology Stack
- **Applets:** GeoGebra (customized and embedded) for interactivity.
- **Website:** NiceGUI, Streamlit, or a static site generator (Next.js, SvelteKit, etc.) for navigation and scaffolding.

## Prototyping Steps
1. **Customize GeoGebra Applets:**
   - Find or build an applet for each concept.
   - Adjust function, sliders, prompts, and visuals as needed.
   - Save and publish each applet to your GeoGebra account.
2. **Scaffold the Website:**
   - Create a multi-page site (one activity per page).
   - Embed each applet via iframe.
   - Present informal/formal definitions and reflection prompts.
3. **Add Research/Assessment Features:**
   - Optionally log student responses (Google Forms, backend, etc.).
   - Include pre/post questions for each activity.

## Sample Page Structure
```
---------------------------------------------------
| Title: [Concept]                                |
---------------------------------------------------
| Informal definition: ...                        |
| Formal definition: ...                          |
---------------------------------------------------
| [Embedded GeoGebra Applet]                      |
---------------------------------------------------
| Reflection/Prediction Prompt:                   |
| [Text input box]                                |
---------------------------------------------------
| [Next Activity]                                 |
---------------------------------------------------
```

## Recommendations for Customization
- Start with "Derivative at a Point" as a prototype.
- For each applet, clarify:
  - Default function(s)
  - Required interactivity (sliders, draggable points, etc.)
  - Prompts/questions for students
- Use GeoGebra's editor to customize and save each applet.
- Embed and scaffold each activity on the site.

## Next Steps
1. Finalize the features/prompts for the first applet.
2. Customize/build the GeoGebra applet.
3. Scaffold the first web page with the applet, definitions, and prompts.
4. Replicate for the remaining four concepts.

---

This plan can be referenced and updated as you build and iterate on the project.
