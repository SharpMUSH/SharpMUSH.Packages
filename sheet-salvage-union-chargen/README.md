# sheet-salvage-union-chargen

Joins the Salvage Union sheet to character applications (`chargen`):

- A player changes their own sheet and mech only while their `+app` application is theirs to change:
  not while it is submitted, and not once it is approved, waitlisted or retired.
- Application reviewers (`softcode.chargen.review`) read the sheet of anyone with an application.
- The sheet's messages say that `+app/submit` sends the sheet in with the application.

A bridge between [`sheet-salvage-union`](../sheet-salvage-union/) and `chargen`. Uninstalling it brings back the plain
rule: a player builds their pilot and mech until they are approved.
