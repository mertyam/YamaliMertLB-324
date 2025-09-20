---
name: Anforderung
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

Feature request
Suggest an idea for this project
Template name
Feature request
This file lives in feature_request.md
About
Suggest an idea for this project
 Styling with Markdown is supported
Template content
name: Anforderung
description: Vorlage für eine neue Anforderung (Feature oder Bugfix)
title: "[ANF] <Kurzer Titel>"
labels: []
body:
  - type: textarea
    id: anforderung
    attributes:
      label: Anforderung (Schema)
      description: >
        Beschreibe die Anforderung im folgenden Schema:
        Zielsystem + Priorität + Systemaktivität + Ergänzungen + Funktionalität + Bedingungen
      placeholder: >
        Beispiel:
        Reflect Media Player muss dem Benutzer die Möglichkeit bieten,
        J3D Szenengraphen aus einer wrml-Datei über das Netzwerk zu laden,
        falls der Benutzer eingeschrieben ist.
    validations:
      required: true

  - type: dropdown
    id: typ
    attributes:
      label: Typ der Anforderung
      options:
        - Funktionale Anforderung
        - Qualitätsanforderung
        - Randanforderung
    validations:
      required: true

Optional additional items
Issue default title
This will be suggested as the issue title
Add a placeholder for issue title, ex. [BUG]
Assignees
No one—
Labels
Funktionale Anforderung
Qualitaetsanforderung
Randanforderung
