# Incorrect / Unsafe KB Example (For Testing Masking Logic)

## Summary
Users are unable to access Prism Central after a security policy update. This KB intentionally includes **unmasked placeholder emails, IPs, and UUIDs** for testing your redaction/masking engine.

---

## Problem
A customer reported login failures to Prism Central. The issue was raised by:

- Contact Email: `admin@nutanix.com`
- Secondary Contact: `j******@gmail.com`
- Impacted UUID: `12ab34cd56ef78e9`
- Affected VM Private IP: `[PRIVATE_IP_HIDDEN]`
- Public Endpoint: `[PRIVATE_IP_HIDDEN]`

These values are intentionally unmasked for automation testing.

---

## Affected Product
- Nutanix Prism Central
- Version: pc.2024.9

---

## Root Cause
An authentication parameter was overwritten during a directory sync event.

---

## Resolution
1. Log in to Prism Central using any admin account such as:
   - `operations-team@nutanix.com`
2. Validate the authentication source mapping.
3. Re-enable the impacted authentication provider.
4. Restart the authentication microservice.

---

## Included Raw Data (For Masking Engine Tests)

### Emails
```
admin@nutanix.com
j******@gmail.com
operations-team@nutanix.com
```

### IP Addresses
```
[PRIVATE_IP_HIDDEN]
[PRIVATE_IP_HIDDEN]
[PRIVATE_IP_HIDDEN]
[PRIVATE_IP_HIDDEN]
```

### UUIDs
```
12ab34cd56ef78e9
aa11bb22cc33dd44ee55
123e4567-e89b-12d3-a456-426614174000
```

---

## Notes
- All identifiers here are synthetic and safe for testing.
- This KB is intentionally poorly structured and includes raw PII-like placeholders to help validate your masking/redaction rules.
