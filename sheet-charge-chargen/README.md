# sheet-charge-chargen

Joins the Charge sheet to character applications (`chargen`):

- A player gives out their own action dots only while their `+app` application is theirs to
  change: not while it is submitted, and not once it is approved, waitlisted or retired. Details,
  momentum, stress and condition stay theirs to keep.
- Application reviewers (`softcode.chargen.review`) read the sheet of anyone with an application.
- The sheet's messages say that `+app/submit` sends the sheet in with the application.

A bridge between [`sheet-charge`](../sheet-charge/) and `chargen`. Uninstalling it brings back the plain rule:
a player gives out their action dots until they are approved.
