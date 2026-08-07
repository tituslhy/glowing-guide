---
name: forex-skill
description: Get live exchange rates between two currencies. Use this whenever the user asks about currency conversion, exchange rates, how much something costs in another currency, or comparisons like "is the dollar strong right now" — even if they don't use the words "forex" or "exchange rate" explicitly (e.g. "how much is 500 SGD in yen", "should I exchange money now or wait"). Always use this instead of guessing from memory, since exchange rates move constantly and Claude's training data has no visibility into current rates.
---

# Forex Skill

Fetches the live exchange rate between two currencies and reports it back in a clear, practical format.

## Why this matters

Claude has no live access to current exchange rates — anything it "knows" about today's rates from training data is stale or fabricated, and currency markets move by the minute. Always call the `get_exchange_rate` tool below rather than estimating or recalling a rate from memory; a confidently wrong rate is worse than admitting you don't know, especially if the user is about to make a real transaction.

## Instructions

1. **Identify both currencies.** Convert casual references to standard 3-letter ISO codes before calling the tool (e.g. "dollars" → ask which dollar: USD, SGD, AUD, etc.; "yen" → JPY; "pounds" → GBP).
2. **Handle ambiguous currency names.** If the user says something like "dollars" or "pounds" without specifying which country, ask them to clarify before calling the tool — don't assume USD/GBP by default.
3. **Call the `get_exchange_rate` tool**, passing both currency codes:

   ```python
   get_exchange_rate(currency_from="<code>", currency_to="<code>")
   ```

4. **If the tool call fails or returns an error**, tell the user plainly that the rate lookup failed — don't fall back to guessing a rate from memory.
5. **Call once per currency pair.** For multi-currency questions (e.g. "compare SGD to USD, EUR, and JPY"), call the tool separately for each pair.
6. **Do the math for the user.** If they gave an amount ("convert 500 SGD to JPY"), multiply it out yourself using the returned rate — don't just hand back the raw rate and leave them to calculate it.

## Output format

Always report back:

- The exchange rate itself (1 `currency_from` = X `currency_to`)
- The converted amount, if the user specified one
- Skip commentary about market trends or advice on whether to convert now vs. later — that drifts into financial advice, which isn't this skill's job

## Examples

**Example 1**
Input: "What's the exchange rate from SGD to USD?"
Action: Call `get_exchange_rate(currency_from="SGD", currency_to="USD")`
Output: "1 SGD = 0.74 USD."

**Example 2**
Input: "How much is 500 SGD in yen?"
Action: Call `get_exchange_rate(currency_from="SGD", currency_to="JPY")`, then multiply the rate by 500.
Output: "At the current rate, 500 SGD is about ¥58,000."

**Example 3**
Input: "How many dollars is 100 pounds?"
Action: "Dollars" and "pounds" are both ambiguous — ask the user to confirm (USD/SGD/AUD, GBP vs. another) before calling the tool.