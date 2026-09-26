---
name: pricing
description: "Design or audit product pricing, packaging, tiers, value metrics, trials, price changes, and pricing-page readability. Use paywalls for in-app upgrade screens and offers for service or course packaging."
metadata:
  version: 2.1.0
---

# Pricing strategy

## Before starting

**Check for product marketing context first.**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Business context
- What type of product? (SaaS, marketplace, e-commerce, service)
- What's your current pricing (if any)?
- What's your target market? (SMB, mid-market, enterprise)
- What's your go-to-market motion? (self-serve, sales-led, hybrid)

### 2. Value & competition
- What's the primary value you deliver?
- What alternatives do customers consider?
- How do competitors price?

### 3. Current performance
- What's your current conversion rate?
- What's your ARPU and churn rate?
- Any feedback on pricing from customers/prospects?

### 4. Goals
- Optimizing for growth, revenue, or profitability?
- Moving upmarket or expanding downmarket?

---

## Pricing fundamentals

### The three pricing axes

**1. Packaging.** Define what's included at each tier.
- Features, limits, support level
- How tiers differ from each other

**2. Pricing metric.** Decide what you charge for.
- Per user, per usage, flat fee
- How price scales with value

**3. Price point.** Set the amount you charge.
- The actual dollar amounts
- Perceived value vs. cost

### Value-based pricing

Price should be based on value delivered, not cost to serve:

- **Customer's perceived value.** The ceiling
- **Your price.** Between alternatives and perceived value
- **Next best alternative.** The floor for differentiation
- **Your cost to serve.** Only a baseline, not the basis

**Key insight.** Price between the next best alternative and perceived value.

---

## Value metrics

### What is a value metric?

The value metric is what you charge for. It should scale with the value customers receive.

**Good value metrics.**
- Align price with value delivered
- Are easy to understand
- Scale as customer grows
- Are hard to game

### Common value metrics

| Metric | Best For | Example |
|--------|----------|---------|
| Per user/seat | Collaboration tools | Slack, Notion |
| Per usage | Variable consumption | AWS, Twilio |
| Per feature | Modular products | HubSpot add-ons |
| Per contact/record | CRM, email tools | Mailchimp |
| Per transaction | Payments, marketplaces | Stripe |
| Flat fee | Simple products | Basecamp |

### Choosing your value metric

Ask: "As a customer uses more of [metric], do they get more value?"
- If yes → good value metric
- If no → price doesn't align with value

---

## Tier structure overview

### Good-better-best framework

**Good tier (Entry).** Core features, limited usage, low price
**Better tier (Recommended).** Full features, reasonable limits, anchor price
**Best tier (Premium).** Everything, advanced features, 2-3x Better price

### Tier differentiation

- **Feature gating.** Basic vs. advanced features
- **Usage limits.** Same features, different limits
- **Support level.** Email → Priority → Dedicated
- **Access.** API, SSO, custom branding

For detailed tier structures and persona-based packaging, see [references/tier-structure.md](references/tier-structure.md).

---

## Pricing research

### Van Westendorp method

Four questions that identify acceptable price range:
1. Too expensive (wouldn't consider)
2. Too cheap (question quality)
3. Expensive but might consider
4. A bargain

Analyze intersections to find optimal pricing zone.

### MaxDiff analysis

Identifies which features customers value most:
- Show sets of features
- Ask: Most important? Least important?
- Results inform tier packaging

For detailed research methods, see [references/research-methods.md](references/research-methods.md).

---

## When to raise prices

### Signs it's time

**Market signals.**
- Competitors have raised prices
- Prospects don't flinch at price
- "It's so cheap!" feedback

**Business signals.**
- Very high conversion rates (>40%)
- Very low churn (<3% monthly)
- Strong unit economics

**Product signals.**
- Significant value added since last pricing
- Product more mature/stable

### Price increase strategies

1. **Grandfather existing.** New price for new customers only
2. **Delayed increase.** Announce 3-6 months out
3. **Tied to value.** Raise price but add features
4. **Plan restructure.** Change plans entirely

---

## Pricing page best practices

### Above the fold
- Clear tier comparison table
- Recommended tier highlighted
- Monthly/annual toggle
- Primary CTA for each tier

### Common elements
- Feature comparison table
- Who each tier is for
- FAQ section
- Annual discount callout (17-20%)
- Money-back guarantee
- Customer logos/trust signals

### Pricing psychology
- **Anchoring.** Show higher-priced option first
- **Decoy effect.** Middle tier should be best value
- **Charm pricing.** $49 vs. $50 (for value-focused)
- **Round pricing.** $50 vs. $49 (for premium)

---

## Pricing page teardown

When someone wants to audit an existing pricing *page* for **clarity, transparency, and AI-readability** (not the pricing strategy itself or conversion-rate optimization), run a **teardown** that scores it across two axes and returns prioritized fixes. Use `cro` for conversion-rate optimization:

- **Human buyer experience.** Value-prop clarity, plan differentiation, cognitive load, trust signals, pricing psychology, and price transparency.
- **AI-agent readiness.** Whether the LLMs and agents that increasingly shortlist and compare tools can actually read and quote your pricing: machine-readable prices (not locked in an image or behind "Contact us"), extractable FAQ/objection coverage, per-tier depth stated in text, and structured data. Buyers now ask ChatGPT/Perplexity/Claude "what's the best X and what does it cost?" *before* visiting, a pricing page an agent can't parse loses deals you never see.

Run the 30-second "paste test." Give the pricing URL to a browsing-capable AI (Perplexity, ChatGPT with search, or Claude with web), or paste the rendered page text, and ask "what are the plans and prices?" A clean miss means agents fetching your page will struggle too. This is a heuristic, not proof that every agent fails.

The AI-readiness fixes are usually high-impact, low-effort (put prices in text, add `Offer` schema). Hand implementation to **schema** (Product/Offer JSON-LD) and **ai-seo** (extractability, AI-bot access, `llms.txt`).

**For the full 10-dimension rubric, scoring, and report template.** See [references/pricing-page-teardown.md](references/pricing-page-teardown.md). *(AI-agent-readiness lens adapted from Kyle Poyar / Growth Unhinged.)*

---

## Pricing checklist

### Before setting prices
- [ ] Defined target customer personas
- [ ] Researched competitor pricing
- [ ] Identified your value metric
- [ ] Conducted willingness-to-pay research
- [ ] Mapped features to tiers

### Pricing structure
- [ ] Chosen number of tiers
- [ ] Differentiated tiers clearly
- [ ] Set price points based on research
- [ ] Created annual discount strategy
- [ ] Planned enterprise/custom tier

---

## Task-specific questions

1. What pricing research have you done?
2. What's your current ARPU and conversion rate?
3. What's your primary value metric?
4. Who are your main pricing personas?
5. Are you self-serve, sales-led, or hybrid?
6. What pricing changes are you considering?

---

## Related skills

- **churn-prevention.** For cancel flows, save offers, and reducing revenue churn
- **cro.** For optimizing pricing page conversion
- **ai-seo.** For making the pricing page extractable/citable by AI (the teardown's AI-agent-readiness axis)
- **schema.** For Product/Offer structured data so machines can read your tiers and prices
- **copywriting.** For pricing page copy
- **marketing-psychology.** For pricing psychology principles
- **ab-testing.** For testing pricing changes
- **revops.** For deal desk processes and pipeline pricing
- **sales-enablement.** For proposal templates and pricing presentations

Complete the work only when every recommendation states the customer evidence or assumption behind it, the expected tradeoff, and the metric that would confirm or reject it.
