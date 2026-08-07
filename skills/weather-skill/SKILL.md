---
name: weather-skill
description: Get current weather, forecasts, and conditions for any location using live weather data. Use this whenever the user asks about weather, temperature, rain, forecast, or general conditions — even if phrased indirectly (e.g. "what should I wear in Tokyo tomorrow", "do I need an umbrella", "is it a good day for a hike"). Always use this instead of guessing from memory, since weather data changes constantly and Claude's training data has no visibility into current conditions.
---

# Weather Skill

Fetches live weather data for a given location and reports it back in a clear, practical format.

## Why this matters

Claude has no live access to current weather — anything it "knows" about today's conditions from training data is stale or fabricated. Always call the `get_weather` tool below rather than estimating or guessing; a confidently wrong forecast is worse than admitting you don't know.

## Instructions

1. **Identify the location.** If the user doesn't name one explicitly, infer it from context (e.g. a trip they mentioned) or ask them directly — don't assume a default location.
2. **Handle ambiguous locations.** If the location could refer to multiple places (e.g. "Springfield", "Cambridge"), ask the user to clarify (state vs. country) before calling the tool.
3. **Call the `get_weather` tool** for each location of interest, passing the location as a string:

   ```python
   get_weather(location="<location>")
   ```

4. **If the tool call fails or returns an error**, tell the user plainly that the weather lookup failed — don't fall back to guessing conditions from memory.
5. **Call once per location.** For multi-location questions (e.g. "compare weather in Singapore and Tokyo"), call the tool separately for each one.

## Output format

Always report back:

- Current temperature (and "feels like" if available)
- Conditions (sunny, rainy, cloudy, etc.)
- One practical, one-line suggestion (umbrella, jacket, good day for outdoor plans, etc.)

Don't dump raw JSON on the user — summarize it in plain language.

## Examples

**Example 1**
Input: "What's the weather in Singapore?"
Action: Call `get_weather(location="Singapore")`
Output: "Singapore's at 31°C and humid with scattered thunderstorms expected this afternoon — bring an umbrella if you're heading out."

**Example 2**
Input: "Should I bring a jacket to Cambridge tomorrow?"
Action: Location is ambiguous (Cambridge, UK vs. Cambridge, MA) — ask the user which one before proceeding.

**Example 3**
Input: "Compare the weather in Tokyo and Seoul this weekend."
Action: Call the tool once for each city, then summarize both side by side.