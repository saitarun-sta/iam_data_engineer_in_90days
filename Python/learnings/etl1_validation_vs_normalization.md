Validation

You said:

validating whether the data is accurate as per standards

More precisely:

Validation checks whether the data satisfies the defined rules/requirements.

Example:

age = "25"

Validation asks:

Is this a valid age?
Is it within 0–120?

If yes → acceptable.

If:

age = "abc"

→ invalid.

Normalization

Your explanation is also correct.

Normalization transforms acceptable raw values into a consistent representation.

For example:

"  Rahul  " → "Rahul"
" India "   → "India"
"25"        → 25

So remember:

VALIDATION
    ↓
"Is this acceptable?"

NORMALIZATION
    ↓
"How should this acceptable value be represented?"
Important distinction

Normalization doesn't necessarily make invalid data valid.

For example:

"abc" → ?

We shouldn't invent:

"abc" → 0

Instead:

"abc" → invalid age

That distinction becomes very important when we build production ETL pipelines.