---
name: cro
description: "Audit marketing pages and lead or contact forms for conversion problems. Use for CRO reviews, form abandonment, or a URL shared for conversion feedback. Use signup for account creation, onboarding for activation, and popups for overlays."
metadata:
  version: 2.0.0
---

# Conversion rate optimization (CRO)

## Initial assessment

**Check for product marketing context first.**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before providing recommendations, identify:

1. **Page type.** Homepage, landing page, pricing, feature, blog, about, or another page
2. **Primary conversion goal.** Sign up, request a demo, purchase, subscribe, download, or contact sales
3. **Traffic context.** Where are visitors coming from? (organic, paid, email, or social)

---

## CRO analysis framework

Analyze the page across these dimensions, in order of impact:

### 1. Value proposition clarity (highest impact)

**Check for.**
- Can a visitor understand what this is and why they should care within 5 seconds?
- Is the primary benefit clear, specific, and differentiated?
- Is it written in the customer's language (not company jargon)?

**Common issues.**
- Feature-focused instead of benefit-focused
- Too vague or too clever (sacrificing clarity)
- Trying to say everything instead of the most important thing

### 2. Headline effectiveness

**Evaluate.**
- Does it communicate the core value proposition?
- Is it specific enough to be meaningful?
- Does it match the traffic source's messaging?

**Strong headline patterns.**
- Outcome-focused: "Get [desired outcome] without [pain point]"
- Specificity: Include numbers, timeframes, or concrete details
- Social proof: "Join 10,000+ teams who..."

### 3. CTA placement, copy, and hierarchy

**Primary CTA assessment.**
- Is there one clear primary action?
- Is it visible without scrolling?
- Does the button copy communicate value, not just action?
  - Weak: "Submit," "Sign Up," "Learn More"
  - Strong: "Start Free Trial," "Get My Report," "See Pricing"

**CTA hierarchy.**
- Is there a logical primary vs. secondary CTA structure?
- Are CTAs repeated at key decision points?

### 4. Visual hierarchy and scannability

**Check.**
- Can someone scanning get the main message?
- Are the most important elements visually prominent?
- Is there enough white space?
- Do images support or distract from the message?

### 5. Trust signals and social proof

**Types to look for.**
- Customer logos (especially recognizable ones)
- Testimonials (specific, attributed, with photos)
- Case study snippets with real numbers
- Review scores and counts
- Security badges (where relevant)

**Placement.** Near CTAs and after benefit claims

### 6. Objection handling

**Common objections to address.**
- Price/value concerns
- "Will this work for my situation?"
- Implementation difficulty
- "What if it doesn't work?"

**Address through.** FAQ sections, guarantees, comparison content, process transparency

### 7. Friction points

**Look for.**
- Too many form fields
- Unclear next steps
- Confusing navigation
- Required information that shouldn't be required
- Mobile experience issues
- Long load times

---

## Output format

Structure your recommendations as:

### Quick wins (implement now)
Easy changes with likely immediate impact.

### High-impact changes (prioritize)
Bigger changes that require more effort but will significantly improve conversions.

### Test ideas
Hypotheses worth A/B testing rather than assuming.

### Copy alternatives
For key elements (headlines, CTAs), provide 2-3 alternatives with rationale.

---

## Page-specific frameworks

### Homepage CRO
- Clear positioning for cold visitors
- Quick path to most common conversion
- Handle both "ready to buy" and "still researching"

### Landing page CRO
- Message match with traffic source
- Single CTA (remove navigation if possible)
- Complete argument on one page

### Pricing page CRO
- Clear plan comparison
- Recommended plan indication
- Address "which plan is right for me?" anxiety

### Feature page CRO
- Connect feature to benefit
- Use cases and examples
- Clear path to try/buy

### Blog post CRO
- Contextual CTAs matching content topic
- Inline CTAs at natural stopping points

---

## Experiment ideas

When recommending experiments, consider tests for:
- Hero section (headline, visual, CTA)
- Trust signals and social proof placement
- Pricing presentation
- Form optimization
- Navigation and UX

For experiment ideas by page type, see [references/experiments.md](references/experiments.md).

---

## Task-specific questions

1. What's your current conversion rate and goal?
2. Where is traffic coming from?
3. What does your signup/purchase flow look like after this page?
4. Do you have user research, heatmaps, or session recordings?
5. What have you already tried?

---

## Related skills

- **signup.** If the issue is in the signup process itself
- **popups.** If considering popups as part of the strategy
- **copywriting.** If the page needs a complete copy rewrite
- **ab-testing.** To properly test recommended changes

---

## Form optimization

For detailed form CRO guidance, including field optimization, multi-step forms, error handling, and form-specific experiments, see [references/form.md](references/form.md).

Complete the review only when each recommendation names the observed problem, its priority, and either the evidence behind the change or the hypothesis to test. State any missing analytics or page context.
