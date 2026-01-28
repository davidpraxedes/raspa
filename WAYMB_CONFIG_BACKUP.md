# Working WayMB Configuration (Verified 2026-01-27)

## Status
✅ Client-Side: **SUCCESS**
✅ API Response: `200 OK` (generatedMBWay: true)
✅ Credential Status: **VALID**

## Successful Payload Structure
This is the specific JSON structure that the API accepted. Use EXACTLY this in the backend.

```json
{
  "client_id": "modderstore_c18577a3",
  "client_secret": "850304b9-8f36-4b3d-880f-36ed75514cc7",
  "account_email": "modderstore@gmail.com",
  "amount": 9.00,
  "method": "mbway",
  "payer": {
    "name": "Verification User",
    "document": "999999990",
    "phone": "912345678"
  }
}
```

## Critical Notes for Backend Implementation
1. **Amount Type**: MUST be `float` (`9.00`), NOT integer (`9`) and NOT string (`"9.00"`).
2. **Currency Field**: **DO NOT SEND**. Sending `"currency": "EUR"` caused 500/400 errors previously.
3. **Phone Number**: 
   - Format: String 9 digits (e.g., `"912345678"`). 
   - Note: The previous failure was likely due to the browser sending `"910000000"` or invalid data. The backend should ideally sanitize or validate this field strictly.
4. **Headers**:
   - `Content-Type`: `application/json`
   - `User-Agent`: Mimic a real browser (e.g., Chrome/Windows) to avoid bot detection.
   - `Referer`: `https://worten.pt/` (Helps with trust score).
