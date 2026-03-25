# Writing style demonstration

This section shows a short example of clear and consistent writing. The text uses direct language and avoids unnecessary complexity.

The system processes incoming data in real time, and the team reviews each report during the daily workflow.

The National Aeronautics and Space Administration (NASA) introduced a workflow. The guide explains each term before using it in examples.

The module activates when the system requires additional resources, and it deactivates after the task completes.

During the last run, the sensor recorded a temperature of minus seven degrees Celsius. The process continued without any errors.

The team completes a follow-up review at the end of each test cycle and documents the results in the internal report.


### Expected: Successful
https://www.iana.org/domains/reserved

### Expected: Excluded (due to mailto:, localhost, or file paths)
mailto:s******@example.com
http://localhost:3000
file:///Users/test/docs/index.md
ftp://example.com/resource

### Expected: Unsupported (schemes Lych test)
ssh://example.com
git://github.com/example/repo
tel:+1-800-555-1234
chrome://settings

### Expected: Redirected
http://example.com
http://github.com

### Expected: Errors
https://nonexistent.invalid
https://expired.badssl.com
https://this-domain-should-never-exist-12345.com
``