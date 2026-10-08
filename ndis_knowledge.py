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
| **NDIS (Supports for Participants) Rules 2013** | Criteria for what supports are "reasonable and necessary" (e.g. value for money r 3.1, current good practice r 3.2–3.3) |
| **NDIS (Getting the NDIS Back on Track No. 1) (NDIS Supports) Transitional Rules 2024** | Schedule 1 lists supports that are NDIS supports; Schedule 2 lists supports that are not (s 10 definition of NDIS support) |
| **NDIS (Specialist Disability Accommodation) Rules 2020** | SDA eligibility, funding, design categories — separate from day-to-day living supports |
| **NDIS (Plan Management) Rules 2013** | Plan management options |
| **NDIS (Becoming a Participant) Rules 2016** | Access/eligibility requirements |
| **NDIS Support Catalogue** | Pricing limits, support item numbers, registration groups |
| **NDIS Operational Guidelines** | NDIA's internal policy (not law, but indicates how NDIA applies the rules) |

## Critical Distinctions

- **SDA ≠ SIL**: SDA is the *dwelling* (bricks and mortar); SIL is the *support model* (staffing for daily living). They are funded under different rules and assessed separately. SDA is Capital funding; SIL is Core funding.
- **"Day-to-day living cost"** does not apply to SDA under the SDA Rules 2020. If the NDIA cites this as a reason to deny SDA, it is applying incorrect legal reasoning.
- **Reasonable and necessary (s 34(1), as amended from 3 October 2024)**: The decision-maker must be satisfied of **all** of the following for each support:
  - (aa) necessary to address needs arising from an impairment for which the participant meets the disability (s 24) or early intervention (s 25) requirements
  - (a) assists the participant to pursue the goals in their statement of goals and aspirations
  - (b) assists the participant to undertake activities that facilitate social and economic participation
  - (c) represents value for money: costs are reasonable relative to the benefits and the cost of alternative support
  - (d) will be, or is likely to be, effective and beneficial, having regard to current good practice
  - (e) takes account of what it is reasonable to expect families, carers, informal networks and the community to provide
  - (f) is an NDIS support (s 10): within Schedule 1 and not excluded by Schedule 2 of the NDIS Supports Transitional Rules
- **Which version applies**: the amended s 34 applies to a plan (statement of participant supports) approved or varied on or after 3 October 2024, regardless of when the plan started (Amending Act Sch 1 item 129; *Butler* [2025] ARTA 1579 at [38]–[39]). Before the amendment, (f) was "most appropriately funded or provided through the NDIS" rather than another system, and there was no (aa).
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

## Funding
Support Coordination is funded under **Capacity Building — Improved Life Choices**. This line item is locked (not flexible with other Capacity Building categories).

## Changing Your Support Coordinator

A participant can change their Support Coordinator **at any time** — there is no lock-in period under the NDIS. NDIA approval is not required to switch providers.

### Process
1. **Find a new Support Coordinator** — Check they are registered (if agency-managed) or suitable (if plan/self-managed). Confirm they have capacity.
2. **Review your service agreement** — Check the notice period (typically 2–4 weeks). There may be a reasonable notice clause.
3. **Notify your current coordinator in writing** — Provide the required notice. Request a handover summary including current service bookings, outstanding actions or referrals, and any reports or assessments in progress.
4. **Sign a new service agreement** with the incoming coordinator.
5. **Update service bookings** — If agency-managed, the new coordinator creates a new service booking in the NDIA portal and the old booking is ended. If plan-managed, notify the plan manager.
6. **Handover** — The outgoing coordinator should provide a professional handover to the incoming one (with the participant's consent).

### Things to Watch
- **Remaining funding** — Both coordinators claim from the same Improved Life Choices line item. Check the balance before switching.
- **Cancellation fees** — The outgoing provider may charge for the notice period under PAPL cancellation rules.
- **Timing** — If the plan is close to reassessment, consider whether to switch now or wait for the new plan.
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

## Tribunal Scrutiny
Reports are weighed as expert evidence at the ART. Weak reports can be given "little weight" and the supports they back refused — see `ndis://report-quality` (Butler v NDIA [2025] ARTA 1579) before finalising any report. Do not simply transcribe the participant's list of requested supports; the Tribunal expects the author's own, independent clinical reasoning.
"""

REPORT_QUALITY = """
# Report Quality — Lessons from Butler v NDIA [2025] ARTA 1579

**Butler and National Disability Insurance Agency (NDIS) [2025] ARTA 1579** (28 August 2025, Senior Member B De Villiers, Perth). The Administrative Review Tribunal **affirmed** the NDIA's refusal of every disputed support: extra therapy hours, support worker hours, support coordination level 3, transport, low-cost AT and consumables, capital AT, and home modifications. Most items failed **s 34(1)(aa)** (necessary to address needs arising from the s 24 impairment) and **s 34(1)(c)** (value for money). In large part that was because the expert evidence behind them was given little weight.

Paragraph references below are to the decision. Practitioners are referred to by profession.

## The Statutory Frame the Reports Had to Meet
- The **amended s 34(1)** (Getting the NDIS Back on Track No 1) applied because the plan was determined after 3 October 2024 [39]. The criteria (aa)–(f) are **cumulative**. Failing any one is fatal [48], [83].
- The Tribunal must be **positively satisfied** of each criterion on the evidence [80]. The burden is effectively on the evidence put forward, not on the Agency to disprove need.
- Two-stage test (adopted from *FSWN* [2025] ARTA 114) [61]–[65]:
  1. Is the support excluded by **Schedule 2** of the NDIS Supports Transitional Rules? If not, is it within a **Schedule 1** category? Otherwise s 34(1)(f) fails.
  2. Does it satisfy each of s 34(1)(aa)–(e) and the Supports for Participants Rules (e.g. value for money r 3.1, current good practice r 3.2–3.3)?
- Where the participant **already receives** a support, the evidence must justify the **increase**, not just the general merit of the support type [104(a)].

## What the Tribunal Criticised in the Expert Evidence

| Problem | What the Tribunal found |
|---|---|
| **Copying the participant's list** | Several practitioners admitted they had received a written list of the supports the participant wanted and repeated it in their reports. The Agency called it "a cut-and-paste exercise" [18]. The experts "seem to reflect, without critical assessment, the wishes of the Applicant rather than assess independently" [112(b)]. See also [124(a)], [142(a)(iv)]. |
| **Recording symptoms ≠ recommending supports** | A GP "only repeated what she had been given" by the participant. "Recording symptoms as provided by the Applicant should not be confused with making expert recommendations about appropriate disability supports" [104(e)]. |
| **Opinions outside expertise** | The GP's recommendations on necessity and value for money "mostly fall outside of her expertise or her personal assessment", which "undermines the credibility" of the opinion [104(e)]. |
| **Limited or no direct assessment** | One report "collated information provided by others". Two others were "exclusively based on material provided … by the Applicant" with "limited interaction … via telehealth" [104(d)]. One physiotherapist's report was based solely on a **single telehealth consultation** [73(e)], yet concluded the supports were the "minimum" required [70]. |
| **Unverified AI drafting** | Reports were "produced with the assistance of an artificial intelligence program". The author could not explain a reference to the participant's **"rural" location, used to justify the recommended supports**, although she lived in an urban area. She could not say whether all citations had been checked, or who inserted the words "minimum necessary": possibly the AI program or her **supervisor**. Her evidence was "unconvincing" [104(d)]. |
| **Unchecked citations** | Citations used by a psychologist "had to be corrected" [104(d)]. |
| **Conclusions without a rational basis** | Conclusions were drawn "of which the rational basis could not be explained" [104(d)]. Repeatedly saying a support is in the participant's "best interest" does not establish necessity or value for money [104(a)]. |
| **Advocacy and lack of independence** | A treating psychologist "seemed to advocate for the Applicant and the support he offers, rather than provide an independent assessment". He described the NDIS as responsible for "bureaucratic punishment" [104(c)]. |
| **Conflict of interest** | Treating providers who would deliver, and benefit from, the recommended supports may describe them in terms that fit Schedule 1 [104(a)]. The Tribunal was "concerned that some of the witnesses who recommend the increased support are likely to benefit from any such increase" [112(b)]. |
| **Blurring s 24 disabilities with other conditions** | The participant had many health conditions outside her s 24 disabilities (e.g. long COVID, lipo-lymphoedema, PTSD, ADHD). Reports did not "adequately distinguish" them [104(b)], [129(a)]. Some recommended treatment targeted non-s 24 conditions [89], [118(e)]. There was "inadequate evidence about what proportion of the additional hours sought relates to the s 24 disabilities" [118(f)]. One justification relied on the participant's height, which "is not a s 24 disability" [142(d)(iv)]. |
| **Unsupported cost claims** | OT assertions that a support was "cost effective" or a "cost-effective alternative" were rejected because no cost assessment or calculation was provided [142(a)(iv)], [129(f)]. |
| **Ignoring existing supports and overlap** | Recommendations did not consider supports already in the plan, or overlapped with other requested supports [87]–[88], [112(a)], [112(e)], [129(c)]. |
| **Recommendations inconsistent with current function** | 415 hours/year of physio and exercise physiology implied "a high-intensity treatment regime" inconsistent with a participant described as largely bedbound [118(a)]–[118(b)], [104(e)]. |
| **Unreconciled contradictions** | Reports described inability to stand safely, but the participant drove a manual car and parked unassisted. Experts did not reconcile this [99(b)], [129(d)], [142(d)(i)]. |
| **AT not trialled; experts disagreeing** | No wheelchair had been trialled in the home, and the OTs disagreed on powered versus manual [142(c)]. A list of AT items read as "a general list of useful things to have rather than evidence-based supports" under s 34(1)(d) [138(b)]. |
| **Missing specifics** | Window tinting failed because the evidence did not show how often, how far or when the participant drove, her sun exposure, or what alternatives had been tried [142(b)]. Air-conditioning failed in part because cheaper options such as plug-in units were not assessed [146(a)]. |
| **Report-only evidence** | Report authors who were not called to give evidence could not clarify the nature of the support or its link to the s 24 disabilities [89], [118(e)]. |

## Generative AI — the Tribunal's Position (at [104(d)])
> "I did not take issue during the hearing or in the assessments with the principle of a practitioner utilising artificial intelligence to reduce to writing the observations and assessments made personally by the practitioner. The practitioner must, however, be responsible and accountable for the content of a report."

AI is acceptable for writing up the practitioner's **own** observations and assessments. It is not a substitute for them. The named author must be able to explain every statement, every citation and every conclusion, including anything a supervisor added.

## Six Lessons for Therapists, Participants and Support Coordinators
1. **AI is a tool, not a substitute — verify every word.** Check every fact and citation. Make sure the named author can explain every phrase, including supervisor edits.
2. **Check and correct errors.** Verify name, location, living situation, diagnoses, plan details and dates, especially any fact relied on to justify a recommendation.
3. **Base recommendations on direct assessment and observation.** State the nature and extent of contact. Distinguish observed, measured and self-reported information. Don't reach firm conclusions from a single telehealth session or from documents alone.
4. **Separate s 24 disabilities from other conditions.** Attribute each functional impact and each hour of support to the recognised impairment (s 34(1)(aa)). Where another condition contributes, say so and estimate the proportion.
5. **Show clear reasoning against every s 34(1) criterion.** Identify the Schedule 1 category and check Schedule 2. Justify any increase over existing supports. Address overlap. Show value for money with actual costings and the alternatives considered. Cite current good practice.
6. **Avoid an advocacy tone — be independent.** Form your own opinion rather than adopting the participant's list. Stay within your expertise. Disclose any interest in providing the recommended support. Acknowledge contrary evidence and limitations.

## What a Report the Tribunal Can Rely On Looks Like
- States the author's qualifications, expertise relevant to each opinion, and any interest in providing the recommended supports
- Records the assessment basis: face-to-face vs telehealth, number and length of sessions, settings observed, standardised tools, collateral sources
- Distinguishes **observed**, **measured**, and **reported** information
- Links each finding to a **s 24 impairment**, and identifies and excludes needs from other conditions
- For each recommended support: the Schedule 1 category, the functional need, why the current plan is insufficient, overlap with other supports, alternatives considered with costs, and current good practice evidence
- Matches the intensity of recommended supports to the participant's **current** functional capacity and tolerance
- Reconciles apparent contradictions in the evidence rather than ignoring them
- For AT: trial outcomes in the actual environment
- Uses citations the author has personally checked
- Acknowledges limitations
- Is written so the author can defend it under cross-examination. Authors should expect to be called.

## Practical Impact
- Participants and support coordinators: **do not give practitioners a list of supports to copy.** Give them the goals and functional concerns, and let them form their own view.
- Review drafts for errors, advocacy language and unexplained claims **before** submission.
- A short, accurate, independently reasoned report is worth more than a long one that the Tribunal discounts.
- If key evidence rests on self-report or a single telehealth session, arrange further direct assessment before relying on it at IRoD or the ART.
- Consider whether to agree to an independent assessment. In *Butler* the participant declined an independent rehabilitation physician examination the Agency proposed [17].

## Sources
- Butler and National Disability Insurance Agency (NDIS) [2025] ARTA 1579 (28 August 2025), Tribunal No. 2023/6289: https://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/cth/ARTA/2025/1579.html
- Bill Maddens, "NDIS expert reports and generative AI" (26 Sept 2025): https://billmaddens.wordpress.com/2025/09/26/ndis-expert-reports-generative-ai/
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
| **NDIS Pricing Schedule** (formerly PAPL) | PDF/DOCX | The rules — how price controls work, claiming rules. Renamed from "Pricing Arrangements and Price Limits" for 2026-27 |
| **NDIS Support Catalogue** | XLSX | The price list — every support item number, description, price limit |
| **AT/HM/Consumables Code Guide** | PDF/DOCX | Common AT and home modification support items |
| **DSW Cost Model** | DOCX | How the NDIA calculates disability support worker hourly costs |
| **SDA Pricing Arrangements** | Separate page | SDA-specific pricing and calculator |

Current version: **2026-27 v1.0**, effective 1 July 2026. From 2026-27 the catalogue lists a single **National** price limit per support item (the earlier per-state price columns were removed); remote and very remote loadings still apply separately.

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
- The s 34 "reasonable and necessary" test **was amended**: a new (aa) requires each support to be necessary for needs arising from the s 24/s 25 impairment, and (f) now asks whether the support is an "NDIS support" (Schedule 1 / Schedule 2 of the Transitional Rules) rather than whether another system should fund it. See `ndis://legislation`
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
