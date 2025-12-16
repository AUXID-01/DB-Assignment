const SHEET_NAME = "titanic_input";

/* =========================
   Row completeness
========================= */
function isRowComplete(p) {
  return p.PassengerId && p.Name && p.Sex && p.Pclass;
}

/* =========================
   Validation
========================= */
function validatePassenger(p) {
  const errors = [];

  if (!p.PassengerId || isNaN(p.PassengerId))
    errors.push("Invalid PassengerId");

  if (!p.Name)
    errors.push("Missing Name");

  if (!["male", "female"].includes(p.Sex))
    errors.push("Sex must be male or female");

  if (![1, 2, 3].includes(Number(p.Pclass)))
    errors.push("Pclass must be 1, 2, or 3");

  return errors;
}

/* =========================
   MAIN HANDLER
========================= */
function handlePassengerEdit(e) {
  Logger.log("🔔 Trigger fired");

  if (!e || !e.range) return;

  const sheet = e.range.getSheet();
  if (sheet.getName() !== SHEET_NAME) return;

  const row = e.range.getRow();
  const col = e.range.getColumn();
  if (row === 1) return;

  const headers = sheet
    .getRange(1, 1, 1, sheet.getLastColumn())
    .getValues()[0];

  const statusCol = headers.indexOf("Status") + 1;
  if (statusCol === 0 || col === statusCol) return;

  const values = sheet
    .getRange(row, 1, 1, headers.length)
    .getValues()[0];

  let passenger = {};
  headers.forEach((h, i) => passenger[h] = values[i]);

  Logger.log("👤 Passenger object: " + JSON.stringify(passenger));

  if (!isRowComplete(passenger)) {
    sheet.getRange(row, statusCol).setValue("INCOMPLETE");
    Logger.log("⏳ Row incomplete");
    return;
  }

  const errors = validatePassenger(passenger);

  if (errors.length > 0) {
  sheet.getRange(row, statusCol)
    .setValue("INVALID: " + errors.join(", "));
  Logger.log("❌ Validation failed: " + errors.join(", "));

  notifyInvalid(passenger, errors);
  return;
}


  sheet.getRange(row, statusCol).setValue("VALID");
  Logger.log("✅ Validation PASSED");

  // ⏭️ Backend call (next step will verify DB)
  sendToBackend(passenger);
}

/* =========================
   Backend call
========================= */
function sendToBackend(p) {
  const url =
    "https://hyperdiastolic-countably-leigha.ngrok-free.dev/register-passenger";

  const payload = {
    passenger_ref: Number(p.PassengerId),
    name: p.Name,
    sex: p.Sex,
    age: p.Age ? Number(p.Age) : null,
    pclass: Number(p.Pclass),
    fare: p.Fare ? Number(p.Fare) : null,
    survived: Boolean(Number(p.Survived))
  };

  Logger.log("📤 Sending to backend: " + JSON.stringify(payload));

  const res = UrlFetchApp.fetch(url, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  });

  Logger.log("📥 Backend response code: " + res.getResponseCode());
  Logger.log("📥 Backend response body: " + res.getContentText());
}
/* =========================
   Invalid row notification
========================= */
/* =========================
   Invalid row notification
========================= */
/* =========================
   Invalid row notification
========================= */
function notifyInvalid(passenger, errors) {
  const ADMIN_EMAIL = "ayush.24bcs10474@sst.scaler.com"; // 👈 put your email here

  const subject = "🚨 Invalid Titanic Passenger Entry";

  const body = `
An invalid Titanic passenger entry was detected in Google Sheets.

Passenger Details:
PassengerId: ${passenger.PassengerId || "N/A"}
Name: ${passenger.Name || "N/A"}
Sex: ${passenger.Sex || "N/A"}
Pclass: ${passenger.Pclass || "N/A"}
Age: ${passenger.Age || "N/A"}

Validation Errors:
- ${errors.join("\n- ")}

Please correct the row in the sheet.
`;

  MailApp.sendEmail(ADMIN_EMAIL, subject, body);
  Logger.log("📧 Invalid entry email sent to: " + ADMIN_EMAIL);
}
