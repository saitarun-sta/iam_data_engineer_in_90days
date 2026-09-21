Yes, you're right. You've already implemented that function and demonstrated that you understand it. We shouldn't repeat it.

### Current status

You've now covered:

* Validation of required columns
* Validation of required values
* Type conversion
* Normalization
* Multiple validation errors
* Raw vs normalized data
* Rejected/quarantined records
* Separation of validation from processing
* ETL control flow
* Debugging the valid/invalid branching

So let's move forward.

---

# Step 9 — A real ETL problem: duplicate records

Now we introduce the next realistic data-quality problem.

Suppose your validated data contains:

```python
rows = [
    {"name": "Rahul", "age": 25, "country": "India"},
    {"name": "Priya", "age": 30, "country": "India"},
    {"name": "Rahul", "age": 25, "country": "India"},
    {"name": "Amit", "age": 28, "country": "India"},
]
```

We have **two identical Rahul records**.

This is a duplicate.

But here's the important engineering question:

> How do we know whether two rows are actually duplicates?

We need to define a **duplicate key / uniqueness rule**.

For this exercise, assume:

```text
name + age + country
```

together identify a unique customer record.

### Your challenge

Without writing code yet, explain:

1. What makes the two Rahul rows duplicates?
2. Should we remove duplicates **before or after validation**?
3. What could go wrong if we simply use `set(rows)` to remove duplicates?

Think it through first.

1. Why are Rahul rows duplicates? ✅

Correct.

Under our defined rule:

name + age + country

both rows have the same values:

Rahul + 25 + India

So they represent the same customer according to our chosen uniqueness rule.

The important DE lesson is:

A duplicate is defined by a business/data rule, not simply by "the rows look similar."

2. Remove duplicates before validation? ⚠️

Not necessarily.

A safer pipeline is often:

Raw data
   ↓
Validation / parsing
   ↓
Normalization
   ↓
Duplicate detection
   ↓
Clean dataset

Why?

Consider:

{"name": " Rahul ", "age": "25", "country": "India"}
{"name": "Rahul", "age": 25, "country": " India "}

These may represent the same record, but before normalization, they aren't identical representations.

After normalization:

{"name": "Rahul", "age": 25, "country": "India"}

Now duplicate detection can recognize them.

So for our pipeline, we'll generally do:

validate → normalize → deduplicate

There can be cases where early duplicate detection is useful, but it depends on the data and business rules.

3. set(rows) ❌ — here's the important Python detail

Your conclusion that set() doesn't actually remove duplicates isn't correct.

A set does remove duplicate values from the set itself.

The problem is that dictionaries are unhashable, so this won't work:

set(rows)

with a list of dictionaries.

You'll get:

TypeError: unhashable type: 'dict'

And even if we converted the dictionaries into something hashable, blindly using a set would not necessarily implement our business definition of duplicate.

For example, our rule is specifically:

name + age + country

So we want to explicitly define that key.