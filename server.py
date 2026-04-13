"""
NDIS Assistant MCP Server

Exposes NDIS knowledge as resources, tools, and prompts for use in
VS Code (Copilot/Claude) while developing the carers portal.

Transport: stdio (for local VS Code use)
"""

import json
from mcp.server.fastmcp import FastMCP

from ndis_knowledge import (
    LEGISLATION,
    PLAN_STRUCTURE,
    PROCESSES,
    SDA,
    SUPPORT_COORDINATION,
    ASSISTIVE_TECHNOLOGY,
    EVIDENCE_REPORTS,
    OT_REPORTS,
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
    """NDIS legislation hierarchy and critical legal distinctions (s34 reasonable and necessary, SDA vs SIL)"""
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
    """Return the s34 reasonable and necessary criteria checklist for evaluating whether an NDIS support meets the legal test."""
    return json.dumps({
        "section": "s34 NDIS Act 2013",
        "test": "A support is reasonable and necessary if it:",
        "criteria": [
            {"criterion": "Related to disability", "question": "Is the support related to the participant's disability?"},
            {"criterion": "Value for money", "question": "Does the support represent value for money compared to alternatives?"},
            {"criterion": "Effective and beneficial", "question": "Is the support likely to be effective and beneficial for the participant?"},
            {"criterion": "Informal supports", "question": "Does it take into account what informal supports (family, community) are reasonable to expect?"},
            {"criterion": "Not another system", "question": "Is the support NOT more appropriately funded by another system (health, education, housing, transport)?"},
        ],
        "note": "All five criteria must be satisfied. The burden shifts depending on context — in an IRoD or ART appeal, the NDIA must justify its decision against these criteria.",
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
def carers_portal_form_guidance(form_purpose: str) -> str:
    """Get NDIS-informed guidance for building a form in the carers portal.

    Args:
        form_purpose: What the form is for — e.g., "participant intake", "incident report", "support log", "CoC request", "daily care record"
    """
    return f"""You are helping build a carers portal web application. The user needs guidance on
building a form for: {form_purpose}

Provide:
1. Required fields based on NDIS requirements and best practice
2. Validation rules (what's mandatory, format constraints, NDIS-specific validation like NDIS number format)
3. Data that would be useful for NDIS evidence and submissions
4. Any NDIS-specific terminology or categories that should be used (support categories, plan types, etc.)
5. Accessibility considerations (the portal may be used by people with disabilities)

Reference the NDIS Act, Rules, and operational guidelines where relevant.
The NDIS number format is typically a 9-digit number.
Support categories should align with Core/Capacity Building/Capital structure.
Plan management types are: Agency-managed, Plan-managed, Self-managed."""


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
Reference s34 NDIS Act 2013 criteria in the recommendations section."""


def main():
    """Run the NDIS MCP server with stdio transport."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
