"""
NDIS Assistant MCP Server

Exposes NDIS knowledge as resources, tools, and prompts for use in
VS Code (Copilot/Claude) and Claude Code.

Transport: stdio
"""

import json
from mcp.server.fastmcp import FastMCP

from pydantic import BaseModel, Field

from catalogue import search_items, compare_rate, CATALOGUE_VERSION
from ndis_knowledge import (
    LEGISLATION,
    PLAN_STRUCTURE,
    PROCESSES,
    SDA,
    SUPPORT_COORDINATION,
    ASSISTIVE_TECHNOLOGY,
    EVIDENCE_REPORTS,
    OT_REPORTS,
    REPORT_QUALITY,
    PRICING,
    LEGISLATIVE_AMENDMENTS,
    KEY_RESOURCES,
    PRACTICAL_TIPS,
    SUPPORT_CATEGORIES,
    SDA_DESIGN_CATEGORIES,
    AT_TIERS,
    SUPPORT_COORDINATION_LEVELS,
)

mcp = FastMCP(
    "NDIS Assistant",
    instructions=(
        "You are an NDIS knowledge assistant for Australian disability support. "
        "Use the provided resources for accurate, legally grounded information "
        "about the NDIS Act 2013, NDIS Rules, support categories, SDA, SIL, "
        "plan processes, and evidence report writing. "
        "Always cite the correct legal instrument when referencing legislation."
    ),
)


# ──────────────────────────────────────────────
# Resources — read-only reference material
# ──────────────────────────────────────────────

@mcp.resource("ndis://legislation")
def legislation() -> str:
    """NDIS legislation hierarchy and critical legal distinctions (amended s 34 reasonable and necessary, SDA vs SIL)"""
    return LEGISLATION


@mcp.resource("ndis://plan-structure")
def plan_structure() -> str:
    """NDIS plan structure — Core, Capacity Building, and Capital supports with flexibility rules"""
    return PLAN_STRUCTURE


@mcp.resource("ndis://processes")
def processes() -> str:
    """How to change an NDIS plan — Change of Circumstances, Internal Review of Decision, and scheduled reassessment"""
    return PROCESSES


@mcp.resource("ndis://sda")
def sda() -> str:
    """Specialist Disability Accommodation — eligibility, design categories, building types, and common NDIA errors"""
    return SDA


@mcp.resource("ndis://support-coordination")
def support_coordination() -> str:
    """Support coordination levels — Support Connection, Coordination, and Specialist"""
    return SUPPORT_COORDINATION


@mcp.resource("ndis://assistive-technology")
def assistive_technology() -> str:
    """Assistive Technology funding tiers and approval requirements"""
    return ASSISTIVE_TECHNOLOGY


@mcp.resource("ndis://evidence-reports")
def evidence_reports() -> str:
    """How to write NDIS evidence reports — structure, language, support ratios"""
    return EVIDENCE_REPORTS


@mcp.resource("ndis://ot-reports")
def ot_reports() -> str:
    """OT report types and standard FCA template structure"""
    return OT_REPORTS


@mcp.resource("ndis://report-quality")
def report_quality() -> str:
    """What makes an evidence report carry weight at the Tribunal — lessons from Butler v NDIA [2025] ARTA 1579"""
    return REPORT_QUALITY


@mcp.resource("ndis://pricing")
def pricing() -> str:
    """NDIS pricing arrangements, Support Catalogue reference, and key pricing concepts"""
    return PRICING


@mcp.resource("ndis://legislative-amendments")
def legislative_amendments() -> str:
    """2024-2026 legislative amendments including Getting the NDIS Back on Track and Integrity Bill"""
    return LEGISLATIVE_AMENDMENTS


@mcp.resource("ndis://key-resources")
def key_resources() -> str:
    """Key NDIS advocacy URLs, phone numbers, and data portals"""
    return KEY_RESOURCES


@mcp.resource("ndis://practical-tips")
def practical_tips() -> str:
    """Practical tips for NDIS advocates — evidence, cost analysis, processes, deadlines"""
    return PRACTICAL_TIPS


# ──────────────────────────────────────────────
# Tools — callable functions for lookups
# ──────────────────────────────────────────────

@mcp.tool()
def lookup_support_category(category_key: str) -> str:
    """Look up an NDIS support category to find its funding bucket (Core/Capacity Building/Capital) and flexibility rules.

    Args:
        category_key: The support category key. Valid keys:
            Core: assistance_with_daily_life, consumables, social_community_participation, transport
            Capacity Building: improved_living_arrangements, improved_daily_living, improved_relationships,
                improved_health_wellbeing, improved_learning, finding_keeping_job, improved_life_choices,
                increased_social_community_participation
            Capital: assistive_technology, home_modifications, sda
    """
    cat = SUPPORT_CATEGORIES.get(category_key)
    if cat:
        return json.dumps(cat, indent=2)
    # Try fuzzy match
    matches = [k for k in SUPPORT_CATEGORIES if category_key.lower().replace(" ", "_") in k]
    if matches:
        results = {k: SUPPORT_CATEGORIES[k] for k in matches}
        return json.dumps(results, indent=2)
    return json.dumps({
        "error": "Category not found",
        "available_keys": list(SUPPORT_CATEGORIES.keys()),
    }, indent=2)


@mcp.tool()
def list_support_categories() -> str:
    """List all NDIS support categories grouped by funding bucket (Core, Capacity Building, Capital) with flexibility rules."""
    grouped: dict[str, list[dict]] = {"Core": [], "Capacity Building": [], "Capital": []}
    for key, val in SUPPORT_CATEGORIES.items():
        grouped[val["category"]].append({"key": key, "flexible": val["flexible"], "note": val["note"]})
    return json.dumps(grouped, indent=2)


@mcp.tool()
def lookup_sda_design_category(category_key: str) -> str:
    """Look up an SDA design category (improved_liveability, fully_accessible, robust, high_physical_support).

    Args:
        category_key: One of: improved_liveability, fully_accessible, robust, high_physical_support
    """
    cat = SDA_DESIGN_CATEGORIES.get(category_key)
    if cat:
        return json.dumps(cat, indent=2)
    return json.dumps({
        "error": "Category not found",
        "available_keys": list(SDA_DESIGN_CATEGORIES.keys()),
    }, indent=2)


@mcp.tool()
def lookup_at_tier(tier_key: str) -> str:
    """Look up an Assistive Technology funding tier and its approval requirements.

    Args:
        tier_key: One of: low_cost, mid_cost, high_cost
    """
    tier = AT_TIERS.get(tier_key)
    if tier:
        return json.dumps(tier, indent=2)
    return json.dumps({
        "error": "Tier not found",
        "available_keys": list(AT_TIERS.keys()),
    }, indent=2)


@mcp.tool()
def lookup_support_coordination_level(level_key: str) -> str:
    """Look up a support coordination level and its description.

    Args:
        level_key: One of: support_connection, support_coordination, specialist_support_coordination
    """
    level = SUPPORT_COORDINATION_LEVELS.get(level_key)
    if level:
        return json.dumps(level, indent=2)
    return json.dumps({
        "error": "Level not found",
        "available_keys": list(SUPPORT_COORDINATION_LEVELS.keys()),
    }, indent=2)


@mcp.tool()
def which_process(situation: str) -> str:
    """Determine the correct NDIS process (Change of Circumstances, Internal Review of Decision, or scheduled reassessment) based on a situation description.

    Args:
        situation: Description of the situation — e.g., "funding was reduced", "needs have increased", "NDIA denied SDA"
    """
    situation_lower = situation.lower()

    # Keywords that suggest IRoD
    irod_keywords = [
        "denied", "refused", "rejected", "reduced", "cut",
        "disagree", "incorrect", "wrong", "unfair", "appeal",
        "decision", "declined",
    ]

    # Keywords that suggest CoC
    coc_keywords = [
        "changed", "increased", "worsened", "deteriorated", "new diagnosis",
        "moved", "lost", "hospital", "more support", "different needs",
        "circumstances", "situation changed",
    ]

    irod_score = sum(1 for kw in irod_keywords if kw in situation_lower)
    coc_score = sum(1 for kw in coc_keywords if kw in situation_lower)

    if irod_score > coc_score:
        return json.dumps({
            "recommended_process": "Internal Review of Decision (IRoD)",
            "reason": "The situation suggests disagreement with a specific NDIA decision.",
            "timeframe": "Must be requested within 3 months of receiving the decision letter.",
            "legal_basis": "s100 of the NDIS Act 2013",
            "next_step_if_unsuccessful": "Appeal to Administrative Review Tribunal (ART)",
            "key_action": "Write to the NDIA identifying the specific decision, stating grounds with legal references, and providing supporting evidence.",
        }, indent=2)
    elif coc_score > irod_score:
        return json.dumps({
            "recommended_process": "Change of Circumstances (CoC)",
            "reason": "The situation suggests the participant's circumstances have genuinely changed.",
            "how_to_request": "Contact NDIA on 1800 800 110 or via plan manager / support coordinator.",
            "key_evidence": [
                "What has changed and when",
                "Impact on functional capacity and daily life",
                "Current support levels vs. what is needed (with data)",
                "Professional assessments and recommendations",
                "Cost analysis showing current plan is insufficient",
            ],
        }, indent=2)
    else:
        return json.dumps({
            "note": "Could not determine the best process from the description provided.",
            "options": {
                "Change of Circumstances (CoC)": "Use when circumstances have genuinely changed since the plan was made.",
                "Internal Review of Decision (IRoD)": "Use when you disagree with a specific NDIA decision. Must be within 3 months.",
                "Scheduled Reassessment": "Periodic reassessment scheduled by the NDIA (typically annual).",
            },
            "tip": "Using the wrong pathway wastes time and may prejudice the outcome. If unsure, seek advice from a support coordinator or advocate.",
        }, indent=2)


@mcp.tool()
def reasonable_and_necessary_checklist() -> str:
    """Return the s 34(1) reasonable and necessary criteria checklist (as amended from 3 October 2024) for evaluating whether an NDIS support meets the legal test."""
    return json.dumps({
        "section": "s 34(1) NDIS Act 2013 (as amended by the Getting the NDIS Back on Track No 1 Act 2024)",
        "test": "For each support, the decision-maker must be satisfied of all of the following:",
        "criteria": [
            {"para": "(aa)", "criterion": "Necessary for the s 24/s 25 impairment", "question": "Is the support necessary to address needs arising from an impairment for which the participant meets the disability (s 24) or early intervention (s 25) requirements?"},
            {"para": "(a)", "criterion": "Goals", "question": "Will the support assist the participant to pursue the goals, objectives and aspirations in their statement of goals and aspirations?"},
            {"para": "(b)", "criterion": "Social and economic participation", "question": "Will the support assist the participant to undertake activities that facilitate their social and economic participation?"},
            {"para": "(c)", "criterion": "Value for money", "question": "Are the costs reasonable relative to both the benefits achieved and the cost of alternative support? (Supports for Participants Rules r 3.1)"},
            {"para": "(d)", "criterion": "Effective and beneficial", "question": "Will the support be, or is it likely to be, effective and beneficial, having regard to current good practice? (r 3.2-3.3)"},
            {"para": "(e)", "criterion": "Informal supports", "question": "Does the funding take account of what it is reasonable to expect families, carers, informal networks and the community to provide?"},
            {"para": "(f)", "criterion": "NDIS support", "question": "Is it an NDIS support under s 10, i.e. within Schedule 1 and not excluded by Schedule 2 of the NDIS Supports Transitional Rules 2024?"},
        ],
        "applying_the_test": [
            "The criteria are cumulative: failing any one is fatal (Butler [2025] ARTA 1579 at [48], [83]).",
            "Check s 34(1)(f) first: Schedule 2 exclusions, then Schedule 1 categories (FSWN [2025] ARTA 114, adopted in Butler at [61]-[65]).",
            "The decision-maker (including the ART on review) must be positively satisfied of each criterion on the evidence (Butler at [80]). Where a support is already funded, the evidence must justify the increase (Butler at [104(a)]).",
            "Needs from impairments that do not meet s 24 may be relevant only insofar as they affect needs arising from the s 24 impairment (s 34(1) Note (b)); they do not themselves ground supports (Butler at [10]).",
        ],
        "which_version": "The amended s 34 applies to a plan approved or varied on or after 3 October 2024, regardless of when the plan started (Amending Act Sch 1 item 129). The pre-amendment test had no (aa), and its (f) asked whether the support is most appropriately funded through the NDIS rather than another system.",
        "see_also": ["ndis://legislation", "ndis://report-quality", "report_quality_checklist"],
    }, indent=2)


@mcp.tool()
def report_quality_checklist() -> str:
    """Return a pre-submission quality checklist for therapist/evidence reports, based on why the Tribunal gave expert reports little weight in Butler v NDIA [2025] ARTA 1579. Each check cites the paragraph of the decision it comes from."""
    return json.dumps({
        "source": "Butler and National Disability Insurance Agency (NDIS) [2025] ARTA 1579 (28 August 2025)",
        "source_url": "https://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/cth/ARTA/2025/1579.html",
        "outcome": "Decision affirmed; every disputed support refused, mostly for failing s 34(1)(aa) (necessary for s 24 impairment) and s 34(1)(c) (value for money).",
        "ai_position": "'The practitioner must, however, be responsible and accountable for the content of a report.' [104(d)]",
        "checks": [
            {
                "lesson": "AI is a tool, not a substitute",
                "questions": [
                    "If AI assisted drafting, does it only write up the author's own observations and assessments? [104(d)]",
                    "Can the named author explain and defend every phrase, including anything added by AI or a supervisor? [104(d)]",
                    "Has the author personally checked every citation? [104(d)]",
                ],
            },
            {
                "lesson": "Check and correct errors",
                "questions": [
                    "Are location, living situation, diagnoses, plan details and dates correct, especially facts relied on to justify a recommendation? [104(d)]",
                    "Are there copy-paste remnants from other reports or templates?",
                    "Are apparent contradictions in the evidence (e.g. functional limits vs activities the participant still does) reconciled? [99(b)], [142(d)(i)]",
                ],
            },
            {
                "lesson": "Base recommendations on direct assessment and observation",
                "questions": [
                    "Does the report state the nature and extent of contact: face-to-face vs telehealth, number and length of sessions, settings? [73(e)], [104(d)]",
                    "Is observed or measured information distinguished from self-report? [104(e)]",
                    "Are conclusions proportionate to the assessment (not 'minimum necessary' after a single telehealth session)? [70]",
                    "Has AT been trialled in the participant's actual environment? [142(c)]",
                ],
            },
            {
                "lesson": "Separate s 24 disabilities from other conditions",
                "questions": [
                    "Is each functional impact and support attributed to an impairment for which the participant meets s 24 (s 34(1)(aa))? [104(b)], [129(a)]",
                    "Are needs from other health conditions identified and excluded, with the proportion of hours relating to s 24 disabilities estimated? [118(e)], [118(f)]",
                    "Does any justification rely on attributes that are not s 24 disabilities? [142(d)(iv)]",
                ],
            },
            {
                "lesson": "Provide clear reasoning against every s 34(1) criterion",
                "questions": [
                    "Is the support within a Schedule 1 category and not excluded by Schedule 2 of the NDIS Supports Transitional Rules (s 34(1)(f))? [61]-[65]",
                    "Is it the author's own clinical opinion, not a repeat of a list supplied by the participant? [18], [104(e)], [112(b)]",
                    "If the participant already receives this support, does the report justify the increase rather than the general merit of the support? [104(a)]",
                    "Are existing plan supports and overlap with other requested supports addressed? [88], [112(a)], [129(c)]",
                    "Is value for money shown with actual costings and alternatives, not just asserted as 'cost effective'? [142(a)(iv)], [129(f)], [146(a)]",
                    "Is the recommended intensity consistent with the participant's current functional capacity and tolerance? [118(a)]-[118(b)]",
                    "Is current good practice evidence cited (s 34(1)(d))? [138(b)]",
                    "Are specifics given: frequency, duration, alternatives already tried? [142(b)]",
                ],
            },
            {
                "lesson": "Avoid an advocacy tone; be independent",
                "questions": [
                    "Is the language neutral and clinical, free of criticism of the NDIA or persuasive framing? [104(c)]",
                    "Are opinions confined to the author's expertise and personal assessment? [104(e)]",
                    "Is any interest in providing the recommended supports disclosed? [104(a)], [112(b)]",
                    "Are limitations and contrary evidence acknowledged?",
                    "Is the author prepared to be cross-examined on the report? [89], [104(d)]",
                ],
            },
        ],
        "see_also": ["ndis://report-quality", "ndis://evidence-reports", "reasonable_and_necessary_checklist"],
    }, indent=2)


@mcp.tool()
def lookup_support_item(query: str, state: str = "", limit: int = 20) -> str:
    """Search the NDIS Support Catalogue for support items by item number or keyword.

    Returns pricing, unit, registration group, and claiming rules.

    Args:
        query: Support item number (e.g. '01_002_0107_1_1') or keyword(s) to search item names (e.g. 'self-care weekday')
        state: Deprecated from 2026-27 — price limits are now National, so this no longer changes the price returned. Retained for backward compatibility.
        limit: Maximum number of results to return (default 20)
    """
    results = search_items(query, state=state, limit=limit)
    if not results:
        return json.dumps({
            "error": "No matching support items found",
            "catalogue_version": CATALOGUE_VERSION,
            "tip": "Try broader keywords or a partial item number",
        }, indent=2)
    return json.dumps({
        "catalogue_version": CATALOGUE_VERSION,
        "result_count": len(results),
        "items": results,
    }, indent=2)


class PriceLine(BaseModel):
    item_number: str = Field(description="Exact support item number, e.g. '01_011_0107_1_1'")
    rate: float = Field(description="Rate charged per unit (e.g. per hour)")
    quantity: float = Field(default=0, description="Units charged (optional; enables totals)")


@mcp.tool()
def benchmark_prices(lines: list[PriceLine], location: str = "national", management_type: str = "") -> str:
    """Benchmark rates charged for NDIS support items against the Support Catalogue price limits.

    Use for a single quoted rate or a whole invoice/service agreement. Flags lines over the price limit and totals any overcharge.

    Args:
        lines: One entry per support item: item_number, rate charged per unit, and optional quantity
        location: national (MMM 1-5), remote (MMM 6) or very_remote (MMM 7)
        management_type: agency, plan or self — determines whether the price limit is binding (optional)
    """
    results = [compare_rate(l.item_number, l.rate, l.quantity, location) for l in lines]
    over = [r for r in results if r["status"] == "over_limit"]
    summary = {
        "lines": len(results),
        "over_limit": len(over),
        "not_benchmarkable": sum(r["status"] in ("quote_based", "dollar_value_item", "no_price_limit", "not_found") for r in results),
    }
    if any(r.get("total_charged") is not None for r in results):
        summary["total_charged"] = round(sum(r.get("total_charged", 0) for r in results), 2)
        summary["total_at_limit"] = round(sum(r.get("total_at_limit", 0) for r in results), 2)
        summary["total_over_limit"] = round(sum(r.get("total_over_limit", 0) for r in results), 2)

    mt = management_type.lower()
    if mt.startswith(("agency", "ndia", "plan")):
        binding = "Price limits are binding: amounts over the limit cannot be claimed from the plan."
    elif mt.startswith("self"):
        binding = "Self-managed: price limits are not binding, but paying above them uses more of the budget and is relevant to value for money (s 34(1)(c))."
    else:
        binding = "Price limits are binding for agency- and plan-managed participants; self-managed participants may pay above them."

    return json.dumps({
        "catalogue_version": CATALOGUE_VERSION,
        "summary": summary,
        "price_limit_rule": binding,
        "results": results,
        "notes": [
            "Rates for the wrong time of day or day of week will compare against the wrong item: check the item number matches when the support was delivered.",
            "Remote/very remote limits apply by the participant's MMM location, not the provider's.",
            "Pricing Schedule rules (cancellations, provider travel, non-face-to-face) can change what is claimable even when the rate is within the limit.",
        ],
    }, indent=2)


# ──────────────────────────────────────────────
# Prompts — pre-crafted templates
# ──────────────────────────────────────────────

@mcp.prompt()
def coc_submission(
    participant_name: str,
    ndis_number: str,
    change_description: str,
    current_plan_end_date: str = "",
) -> str:
    """Generate a Change of Circumstances submission letter for the NDIA.

    Args:
        participant_name: Full name of the NDIS participant
        ndis_number: The participant's NDIS number
        change_description: What has changed and why a plan reassessment is needed
        current_plan_end_date: When the current plan ends (optional)
    """
    return f"""Draft a Change of Circumstances (CoC) submission letter to the NDIA for:

Participant: {participant_name}
NDIS Number: {ndis_number}
Current Plan End Date: {current_plan_end_date or "Not specified"}

Change description: {change_description}

Use the following structure:
1. Opening — request a plan reassessment due to a change of circumstances
2. What has changed — specific, dated, factual
3. Functional impact — how the change affects daily life across relevant domains
4. Current vs required supports — gap analysis with costs if available
5. Evidence summary — list of attached evidence documents
6. Requested outcome — what the participant needs in their revised plan

Tone: Professional, objective, evidence-based. Use functional language.
Reference s34 NDIS Act 2013 (reasonable and necessary) where appropriate.
Do NOT use emotional language. Quantify everything possible."""


@mcp.prompt()
def irod_submission(
    participant_name: str,
    ndis_number: str,
    decision_description: str,
    decision_date: str = "",
) -> str:
    """Generate an Internal Review of Decision (IRoD) submission for the NDIA.

    Args:
        participant_name: Full name of the NDIS participant
        ndis_number: The participant's NDIS number
        decision_description: The specific NDIA decision being challenged and why it is incorrect
        decision_date: Date the decision letter was received (for 3-month deadline tracking)
    """
    return f"""Draft an Internal Review of Decision (IRoD) submission under s100 of the NDIS Act 2013 for:

Participant: {participant_name}
NDIS Number: {ndis_number}
Decision received: {decision_date or "Date not specified — NOTE: the 3-month deadline runs from receipt of the decision letter"}

Decision being reviewed: {decision_description}

Use the following structure:
1. Opening — formally request an Internal Review under s100 NDIS Act 2013
2. Identify the decision — state the exact decision, date, and delegate (if known)
3. Grounds for review — why the decision is incorrect, referencing:
   - s34 reasonable and necessary criteria
   - Relevant NDIS Rules (SDA Rules 2020, Supports for Participants Rules 2013, etc.)
   - NDIS Operational Guidelines (where the NDIA's own policy supports the participant)
   - Any common NDIA errors relevant to this type of decision
4. Evidence — summarise supporting evidence and list attachments
5. Requested outcome — what decision should replace the current one
6. Note — if the IRoD is unsuccessful, the participant intends to exercise their right to appeal to the Administrative Review Tribunal (ART)

Tone: Formal, legally precise, evidence-based. Cite specific sections of legislation and Rules.
Do NOT use emotional language."""


@mcp.prompt()
def evidence_report_template(
    report_type: str,
    participant_name: str = "",
) -> str:
    """Generate a structured evidence report template for an NDIS submission.

    Args:
        report_type: Type of report — e.g., "functional capacity assessment", "SDA application", "SIL assessment", "cost analysis", "gap analysis"
        participant_name: Participant name (optional, for personalisation)
    """
    return f"""Generate a structured template for an NDIS {report_type} report{f' for {participant_name}' if participant_name else ''}.

Include all required sections with placeholder text explaining what should go in each section.
Follow the standard NDIS evidence report structure:
1. Participant overview
2. Current plan summary
3. Current support arrangements
4. Functional impact across all domains
5. Evidence of need (data-driven)
6. Gap analysis (current vs required, with costs)
7. Recommendations (specific, costed, tied to NDIS support items)

Use professional, clinical language. Include prompts for NDIS-specific data points.
Reference s34 NDIS Act 2013 criteria in the recommendations section.

Build in the Tribunal's expectations from Butler v NDIA [2025] ARTA 1579 (see ndis://report-quality):
- An assessment methods section recording the nature and extent of contact (face-to-face vs telehealth, sessions, settings, standardised tools, collateral sources)
- Prompts to distinguish observed, measured and self-reported information
- Prompts to attribute each functional impact to a specific NDIS-recognised impairment, separate from other health conditions
- For each recommendation, reasoning against every s34 criterion and alternatives considered
- A limitations section
- Neutral expert tone — the author is an independent expert, not an advocate"""


@mcp.prompt()
def review_report(report_text: str, report_type: str = "") -> str:
    """Review a draft NDIS therapist/evidence report for weaknesses the Tribunal identified in Butler v NDIA [2025] ARTA 1579.

    Args:
        report_text: The full text of the draft report to review
        report_type: Type of report (optional) — e.g., "OT functional capacity assessment", "physiotherapy report"
    """
    return f"""Review the following draft NDIS {report_type or "evidence"} report as the Administrative Review Tribunal would weigh it as expert evidence.

Use the lessons from Butler and National Disability Insurance Agency (NDIS) [2025] ARTA 1579 (ndis://report-quality). There the Tribunal gave expert reports little weight and refused the supports they backed, mostly under s 34(1)(aa) and (c) of the amended NDIS Act 2013. Assess the report against each of the six lessons:

1. AI drafting: flag generic, unexplained or out-of-place phrasing the author may not be able to defend, and citations that need checking [104(d)]
2. Errors and contradictions: flag factual errors, internal inconsistencies, copy-paste remnants, and unreconciled contradictions between stated limitations and what the participant still does [99(b)], [104(d)]
3. Basis of assessment: is the nature and extent of contact stated? Is observed or measured information distinguished from self-report? Are conclusions proportionate to the assessment? [73(e)], [104(e)]
4. Disability attribution: is each functional impact and support linked to an impairment meeting s 24, with other health conditions identified and excluded? [104(b)], [118(f)]
5. Reasoning: for each recommended support, check:
   - the Schedule 1 / Schedule 2 position
   - justification for any increase over existing supports
   - overlap with other supports
   - value for money with actual costings and alternatives
   - intensity matched to current function
   - current good practice evidence
   Flag any support that appears to be transcribed from the participant's own list [18], [104(a)], [112(b)], [142(a)(iv)]
6. Independence and tone: flag advocacy, emotive or NDIA-critical language, opinions outside the author's expertise, and any undisclosed interest in providing the supports [104(c)], [104(e)]

Output:
- Overall rating of likely evidentiary weight (strong / moderate / weak) with a one-paragraph rationale
- A table of issues: location in report, lesson, issue, suggested fix
- A list of recommended supports with a verdict on whether each is adequately reasoned
- Information the author needs to add or verify before submission

Do not invent facts to fill gaps — identify them as gaps.

--- REPORT START ---
{report_text}
--- REPORT END ---"""


def main():
    """Run the NDIS MCP server with stdio transport."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
