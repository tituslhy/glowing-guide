---
name: weather-skill
description: Get current weather for a location. Use when the user asks about weather, temperature, or conditions anywhere.
---

# Get weather skill

To get the weather of a location, run:

```bash
python scripts/get_weather.py "<location>"
```

Returns JSON with weather condition. Parse and present naturally.

Run this script on each location that the user has requested the weather for one at a time.
