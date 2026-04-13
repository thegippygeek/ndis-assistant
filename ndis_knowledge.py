"""
NDIS Knowledge Base — structured content for the MCP server.
Source: NDIS Act 2013, NDIS Rules, Operational Guidelines, Support Catalogue.
"""

LEGISLATION = """
# Key Legislation and Rules

The NDIS operates under a hierarchy of legal instruments. Always cite the correct source:

| Instrument | Scope |
|---|---|
| **NDIS Act 2013** (Cth) | Primary legislation — defines eligibility, reasonable and necessary criteria (s34), plan management, reviews, appeals |
| **NDIS (Supports for Participants) Rules 2013** | Criteria for what supports are "reasonable and necessary" |
| **NDIS (Specialist Disability Accommodation) Rules 2020** | SDA eligibility, funding, design categories — separate from day-to-day living supports |
| **NDIS (Plan Management) Rules 2013** | Plan management options |
| **NDIS (Becoming a Participant) Rules 2016** | Access/eligibility requirements |
| **NDIS Support Catalogue** | Pricing limits, support item numbers, registration groups |
| **NDIS Operational Guidelines** | NDIA's internal policy (not law, but indicates how NDIA applies the rules) |

## Critical Distinctions

- **SDA ≠ SIL**: SDA is the *dwelling* (bricks and mortar); SIL is the *support model* (staffing for daily living). They are funded under different rules and assessed separately. SDA is Capital funding; SIL is Core funding.
- **"Day-to-day living cost"** does not apply to SDA under the SDA Rules 2020. If the NDIA cites this as a reason to deny SDA, it is applying incorrect legal reasoning.
- **Reasonable and necessary (s34)**: A support must be (a) related to the participant's disability, (b) represent value for money, (c) likely to be effective and beneficial, (d) take into account informal supports, and (e) not be more appropriately funded by another system (health, education, etc.).
"""

PLAN_STRUCTURE = """
# NDIS Plan Structure

NDIS plans contain three funding categories:

## Core Supports
Day-to-day disability supports. Includes:
- **Assistance with Daily Life** (includes SIL, in-home support, community access support workers)
- **Consumables**
- **Assistance with Social and Community Participation**
- **Transport**

Core supports are generally **flexible** — funds can move between Core line items unless "stated" (locked to a specific item).

## Capacity Building
Goal-directed supports to build independence. Includes:
- Improved Living Arrangements
- Improved Daily Living (OT, physio, speech)
- Improved Relationships
- Improved Health and Wellbeing
- Improved Learning
- Finding and Keeping a Job
- Improved Life Choices (support coordination)
- Increased Social and Community Participation

Capacity Building is **not flexible** — each line item is locked.

## Capital Supports
One-off or high-cost items:
- Assistive Technology
- Home Modifications
- SDA

Capital is **not flexible** between categories but may be flexible within AT.
"""

PROCESSES = """
# Processes for Changing a Plan

## Outdated Terminology (do not use)
- "S100 form" — no longer used by the NDIA
- "Plan review" — the NDIA now distinguishes between reassessment, Change of Circumstances, and Internal Review

## Current Correct Processes

### 1. Change of Circumstances (CoC)
**Use when**: The participant's circumstances have genuinely changed since the current plan was made — e.g., increased support needs, change in living situation, loss of informal supports, new diagnoses, health deterioration.

**Process**:
- Contact the NDIA (phone 1800 800 110 or via plan manager / support coordinator)
- Explain the change and request a plan reassessment
- Provide supporting evidence (therapist reports, medical evidence, functional assessments, daily logs, incident reports)
- The NDIA will decide whether to reassess the plan

**Key evidence to include**:
- What has changed and when
- Impact on functional capacity and daily life
- Current support levels vs. what is needed (with data if available)
- Professional assessments and recommendations
- Cost analysis showing current plan is insufficient

### 2. Internal Review of Decision (IRoD)
**Use when**: You disagree with a specific NDIA decision — e.g., a denial of SDA, reduction in funding, refusal of a specific support.

**Timeframe**: Must be requested within **3 months** of receiving the decision letter. The clock starts from the date the participant (or their nominee) receives the letter, not the date on the letter.

**Process**:
- Write to the NDIA requesting an Internal Review under s100 of the NDIS Act 2013
- Clearly identify the decision being reviewed
- State the grounds — why the decision is incorrect, referencing the relevant legal criteria
- Provide evidence supporting why the decision should be changed
- A different NDIA delegate (not the original decision-maker) will review

**After Internal Review**: If the IRoD is unsuccessful, the participant can appeal to the **Administrative Review Tribunal (ART)** (formerly AAT, from late 2024).

### 3. Plan Reassessment (scheduled)
The NDIA schedules periodic plan reassessments (typically annually, but can be longer). The participant should prepare evidence in advance.
"""

SDA = """
# SDA (Specialist Disability Accommodation)

## Eligibility Criteria (SDA Rules 2020)
To be eligible for SDA funding, a participant must:
1. Meet the **access requirements** for the NDIS
2. Have an **extreme functional impairment** or **very high support needs**
3. Have housing needs that **cannot be met** by mainstream housing, even with home modifications
4. Require SDA to **reduce the risk** of harm to themselves or others, and/or to **enable delivery** of supports

## SDA Design Categories
- **Improved Liveability** — Improved physical access and features for people with sensory, intellectual, or cognitive disabilities
- **Fully Accessible** — High physical access for people who use wheelchairs or have significant mobility impairment
- **Robust** — Resilient fittings and design for participants whose behaviour may cause damage
- **High Physical Support** — Highest level of physical access, including ceiling hoists, assistive technology integration

## SDA Building Types
Apartment, Villa, Group Home (various sizes), or other configurations. Enrolled SDA dwellings must meet specific design standards.

## Common NDIA Errors in SDA Decisions
- Citing "day-to-day living cost" as a reason to deny SDA — this concept does not apply under the SDA Rules 2020
- Conflating SDA with SIL — they are separate funding streams with different eligibility criteria
- Failing to consider risk reduction as a standalone ground for SDA eligibility
- Requiring the participant to demonstrate they have *tried* mainstream housing first, when the evidence clearly shows it is unsuitable
"""

SUPPORT_COORDINATION = """
# Support Coordination

Three levels:
1. **Support Connection** — Light-touch help connecting to services
2. **Support Coordination** — Ongoing coordination, plan implementation, provider liaison
3. **Specialist Support Coordination** — For complex situations involving multiple systems (health, justice, housing, child protection)
"""

ASSISTIVE_TECHNOLOGY = """
# Assistive Technology (AT)

AT funding falls under Capital Supports. Categories by cost:
- **Low-cost AT** (under ~$1,500) — Generally approved within plan without quotes
- **Mid-cost AT** ($1,500–$15,000) — Requires OT assessment and one quote
- **High-cost AT** (over $15,000) — Requires OT assessment, multiple quotes, and NDIA approval
"""

EVIDENCE_REPORTS = """
# Writing NDIS Evidence Reports

## Structure
1. **Participant overview** — Name, NDIS number, age, disability, living situation
2. **Current plan summary** — Funding amounts, plan dates, plan management type
3. **Current support arrangements** — Who provides support, when, at what ratio (1:1, 2:1, active overnight, etc.)
4. **Functional impact** — How the disability affects daily life across all domains (mobility, communication, self-care, social, cognitive, behavioural, medical)
5. **Evidence of need** — Data from daily care records, incident logs, therapy assessments, medical reports
6. **Gap analysis** — Current funding vs. required funding, with costs
7. **Recommendations** — Specific, costed, tied to NDIS support items where possible

## Language and Tone
- Use **functional language** — describe what the participant *cannot do* without support, not just their diagnosis
- Be **specific and quantified** — "Xavier requires physical assistance from two support workers for all transfers, approximately 12 times per day" not "Xavier needs help moving around"
- Reference the **NDIS Act criteria** — link each recommendation back to why it is reasonable and necessary under s34
- Avoid emotional language — focus on objective, evidence-based descriptions
- Use participant-first language where appropriate, but prioritise clarity

## Common Support Ratios
- **1:1** — One support worker to one participant (standard)
- **2:1** — Two support workers to one participant (for complex physical or behavioural needs)
- **Active overnight** — A support worker who is awake and available throughout the night (as opposed to "sleepover")
"""

OT_REPORTS = """
# NDIS Occupational Therapy Report Writing

## Report Types

| Report Type | Primary Purpose |
|---|---|
| **Functional Capacity Assessment (FCA)** | Comprehensive assessment of functional abilities across all ADL domains |
| **Home Modification Report** | Assessment of the home environment with drawings, scope of works, and quotes |
| **SIL Assessment Report** | Assessment of support needs for Supported Independent Living funding |
| **SDA Assessment Report** | Assessment against SDA eligibility criteria |
| **Assistive Technology Report** | Assessment, trial documentation, and prescription of specific AT items |
| **Targeted/Focused Report** | Addressing a specific issue — e.g., supporting a 2:1 support ratio request |

## Standard OT Report Structure (FCA Template)

1. **Client Information** — Full name, DOB, address, phone, email, referred by, date of assessment/report, OT details
2. **NDIS Specific Details** — Support Coordinator, Plan Nominee, Plan Dates, NDIS Number, Goals, Budget, Plan management type
3. **Introduction** — Reason for referral, who was present
4. **Client Goals** — Goals as noted in the NDIS plan
5. **Primary Diagnosis** — Primary disability
6. **Medical Background** — Medical diagnoses and history
7. **Family and Social Support** — Who the person lives with, family proximity, social connections
8. **Services In Place** — Current formal NDIS services and informal supports
9. **Home Environment** (table format) — Property type, ownership/rental, access assessment
10. **Activities of Daily Living** (table format) — Grooming, bathing, dressing, etc.
11. **Physical Function** (table format) — Transfers, mobility, stairs, pressure areas
12. **Cognition** — Comprehension, expression, social interaction, planning, memory
13. **Equipment** — Current equipment and suitability
14. **Recommendations** — Each problem with specific recommendation and action plan
15. **Summary** — Succinct synopsis, consider ISBAR format

## OT Report Writing Principles

- Subjective sections use participant/family voice; objective sections use clinical language
- Use NDIS-specific terminology: "reasonable and necessary", "value for money", "assistive technology"
- Use SMART goal-setting (Specific, Measurable, Achievable, Relevant, Time-bound)
- Document value for money — short, medium, and long-term cost implications
"""

PRICING = """
# NDIS Pricing Arrangements and Support Catalogue

The NDIA publishes pricing at https://www.ndis.gov.au/providers/pricing-arrangements

## Key Documents (updated annually, sometimes mid-year)

| Document | Format | Purpose |
|---|---|---|
| **PAPL** | PDF/DOCX | The rules — how price controls work, claiming rules |
| **NDIS Support Catalogue** | XLSX | The price list — every support item number, description, price limit |
| **AT/HM/Consumables Code Guide** | PDF/DOCX | Common AT and home modification support items |
| **DSW Cost Model** | DOCX | How the NDIA calculates disability support worker hourly costs |
| **SDA Pricing Arrangements** | Separate page | SDA-specific pricing and calculator |

Current version: **2025-26 v1.1**, effective 24 November 2025.

## Key Pricing Concepts
- **Price limits** are maximums for registered providers (agency-managed or plan-managed). Self-managed can pay above.
- **TTP (Temporary Transformation Payment)** — additional percentage some providers can claim.
- **Cancellation charges** — providers can charge for short-notice cancellations under specific PAPL rules.
- **Provider travel** — claimable under specific conditions, separate from participant transport.
- **Group supports** — pricing is per participant per hour, not per group.

## Pricing varies by:
- Time of day (weekday daytime, evening, Saturday, Sunday, public holiday)
- Worker level (standard, higher intensity, complex/Level 3)
- Location (MMM 1-3 metro/regional, MMM 4-5 remote, MMM 6-7 very remote with loadings)
"""

LEGISLATIVE_AMENDMENTS = """
# Legislative Amendments (2024–2026)

## Getting the NDIS Back on Track No. 1 (effective 3 October 2024)

Key changes:
- **New definition of NDIS supports** — approved and prohibited support lists
- **Flexible budgets** — plans show total budget, funding components, and periods (up to 12 months)
- **Needs assessment** — new framework for determining reasonable and necessary budgets (co-design ongoing)
- **Claims time limit** — must be submitted within 2 years of support being provided
- **Impairment notices** — all new participants receive a notice outlining impairments (from 1 January 2025)
- **Unspent funds** — roll over within a plan but not between plans

## Integrity and Safeguarding Bill 2025 (introduced November 2025)

Strengthens NDIS Quality and Safeguards Commission with 10 amendments including stronger regulatory powers, provider compliance tools, and participant safeguards.

## Practical Impact for Advocates
- Always check whether the requested support is on the approved supports list
- Flexible budgets may change how cost analyses are structured — focus on total budget adequacy
- The fundamental s34 "reasonable and necessary" test has not changed
- Transitional arrangements exist for participants on existing plans
"""

KEY_RESOURCES = """
# Key Advocacy Resources

| Resource | URL | Use |
|---|---|---|
| NDIS main site | https://www.ndis.gov.au | Official participant and provider information |
| Our Guidelines | https://ourguidelines.ndis.gov.au | NDIA operational guidelines (new format) |
| Data & Research | https://dataresearch.ndis.gov.au | Public datasets, dashboards, research |
| NDIS Review | https://www.ndisreview.gov.au | Independent Review report and resources |
| NDIS Commission | https://www.ndiscommission.gov.au | Quality, safety, complaints, restrictive practices |
| Legislation | https://www.legislation.gov.au | NDIS Act, Rules, legislative instruments |
| Price search | https://mycarespace.com.au/pricelist | Quick NDIS support item price lookup |
| NDIA phone | 1800 800 110 | General NDIA enquiries |
| NDIS Commission complaints | 1800 035 544 | Provider quality or safety complaints |
"""

PRACTICAL_TIPS = """
# Practical Tips for Advocates

- **Data is powerful**: Daily care records, shift notes, incident logs, bowel/fluid charts, sleep records, mood tracking — all constitute evidence. Quantified data from care databases is particularly compelling.
- **Cost analysis wins arguments**: Show the NDIA exactly what the current plan costs vs. what is needed, broken down by support item with Price Guide references.
- **Professional reports matter**: OT functional capacity assessments, physiotherapy reports, and specialist recommendations carry significant weight.
- **Know the correct process**: Using the wrong pathway (e.g., requesting a CoC when an IRoD is needed) wastes time and may prejudice the outcome.
- **Deadlines are hard**: The 3-month window for an Internal Review is strict. Mark it from the date the decision letter is received.
- **Watermark drafts**: Mark documents as "DRAFT — CONFIDENTIAL" until finalised.
- **Redacted versions**: Consider separate versions for different audiences — full for NDIA, redacted for DSW teams.
"""

# Structured lookup data for tools

SUPPORT_CATEGORIES = {
    "assistance_with_daily_life": {
        "category": "Core",
        "flexible": True,
        "note": "Flexible within Core unless stated. Includes SIL, in-home support, community access.",
        "includes": ["SIL", "in-home support", "community access support workers"],
    },
    "consumables": {
        "category": "Core",
        "flexible": True,
        "note": "Flexible within Core.",
    },
    "social_community_participation": {
        "category": "Core",
        "flexible": True,
        "note": "Flexible within Core.",
    },
    "transport": {
        "category": "Core",
        "flexible": True,
        "note": "Flexible within Core.",
    },
    "improved_living_arrangements": {
        "category": "Capacity Building",
        "flexible": False,
        "note": "Locked to this line item.",
    },
    "improved_daily_living": {
        "category": "Capacity Building",
        "flexible": False,
        "note": "OT, physio, speech therapy. Locked to this line item.",
    },
    "improved_relationships": {
        "category": "Capacity Building",
        "flexible": False,
        "note": "Locked to this line item.",
    },
    "improved_health_wellbeing": {
        "category": "Capacity Building",
        "flexible": False,
        "note": "Locked to this line item.",
    },
    "improved_learning": {
        "category": "Capacity Building",
        "flexible": False,
        "note": "Locked to this line item.",
    },
    "finding_keeping_job": {
        "category": "Capacity Building",
        "flexible": False,
        "note": "Locked to this line item.",
    },
    "improved_life_choices": {
        "category": "Capacity Building",
        "flexible": False,
        "note": "Support coordination. Locked to this line item.",
    },
    "increased_social_community_participation": {
        "category": "Capacity Building",
        "flexible": False,
        "note": "Locked to this line item.",
    },
    "assistive_technology": {
        "category": "Capital",
        "flexible": False,
        "note": "Not flexible between categories. May be flexible within AT.",
    },
    "home_modifications": {
        "category": "Capital",
        "flexible": False,
        "note": "Not flexible.",
    },
    "sda": {
        "category": "Capital",
        "flexible": False,
        "note": "SDA is the dwelling (bricks and mortar), NOT the support model. Separate from SIL.",
    },
}

SDA_DESIGN_CATEGORIES = {
    "improved_liveability": {
        "name": "Improved Liveability",
        "description": "Improved physical access and features for people with sensory, intellectual, or cognitive disabilities",
    },
    "fully_accessible": {
        "name": "Fully Accessible",
        "description": "High physical access for people who use wheelchairs or have significant mobility impairment",
    },
    "robust": {
        "name": "Robust",
        "description": "Resilient fittings and design for participants whose behaviour may cause damage",
    },
    "high_physical_support": {
        "name": "High Physical Support",
        "description": "Highest level of physical access, including ceiling hoists, assistive technology integration",
    },
}

AT_TIERS = {
    "low_cost": {
        "name": "Low-cost AT",
        "threshold": "Under ~$1,500",
        "requirements": "Generally approved within plan without quotes",
    },
    "mid_cost": {
        "name": "Mid-cost AT",
        "threshold": "$1,500–$15,000",
        "requirements": "Requires OT assessment and one quote",
    },
    "high_cost": {
        "name": "High-cost AT",
        "threshold": "Over $15,000",
        "requirements": "Requires OT assessment, multiple quotes, and NDIA approval",
    },
}

SUPPORT_COORDINATION_LEVELS = {
    "support_connection": {
        "level": 1,
        "name": "Support Connection",
        "description": "Light-touch help connecting to services",
    },
    "support_coordination": {
        "level": 2,
        "name": "Support Coordination",
        "description": "Ongoing coordination, plan implementation, provider liaison",
    },
    "specialist_support_coordination": {
        "level": 3,
        "name": "Specialist Support Coordination",
        "description": "For complex situations involving multiple systems (health, justice, housing, child protection)",
    },
}
