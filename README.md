# NDIS Assistant MCP Server

An MCP (Model Context Protocol) server that exposes NDIS knowledge as tools, resources, and prompts for use in VS Code and Claude Code.

## What's Included

### Resources (reference material)
- `ndis://legislation` — Act, Rules, and critical legal distinctions
- `ndis://plan-structure` — Core / Capacity Building / Capital with flexibility rules
- `ndis://processes` — CoC, IRoD, and scheduled reassessment
- `ndis://sda` — Eligibility, design categories, common NDIA errors
- `ndis://support-coordination` — Three levels
- `ndis://assistive-technology` — Funding tiers and requirements
- `ndis://evidence-reports` — Report structure and writing principles
- `ndis://ot-reports` — OT report types and FCA template
- `ndis://pricing` — Support Catalogue, pricing concepts
- `ndis://legislative-amendments` — 2024–2026 changes
- `ndis://key-resources` — URLs, phone numbers, data portals
- `ndis://practical-tips` — Advocacy tips

### Tools (callable functions)
- `lookup_support_category` — Find funding bucket and flexibility rules for a support type
- `list_support_categories` — List all categories grouped by Core/CB/Capital
- `lookup_sda_design_category` — SDA design category details
- `lookup_at_tier` — AT funding tier and approval requirements
- `lookup_support_coordination_level` — Coordination level details
- `which_process` — Determine the right process (CoC vs IRoD vs reassessment) from a situation description
- `reasonable_and_necessary_checklist` — s34 criteria checklist

### Prompts (templates)
- `coc_submission` — Draft a Change of Circumstances letter
- `irod_submission` — Draft an Internal Review of Decision submission
- `evidence_report_template` — Generate a structured evidence report template

## Setup

### 1. Install dependencies

```bash
cd ndis-mcp-server
pip install -e .
```

Or with uv (recommended):

```bash
cd ndis-mcp-server
uv pip install -e .
```

### 2. Test locally

```bash
# Quick smoke test — should print available tools/resources
python -c "from server import mcp; print('Server OK:', mcp.name)"

# Run with MCP inspector (if mcp CLI is installed)
mcp dev server.py
```

### 3. Configure VS Code

Create or edit `.vscode/mcp.json` in your project:

```json
{
  "servers": {
    "ndis-assistant": {
      "type": "stdio",
      "command": "python",
      "args": ["/path/to/ndis-mcp-server/server.py"]
    }
  }
}
```

If using **uv** (cleaner, handles venv automatically):

```json
{
  "servers": {
    "ndis-assistant": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "--directory", "/path/to/ndis-mcp-server", "python", "server.py"]
    }
  }
}
```

### 4. Using with Claude Code

If you also want this in Claude Code, add to your Claude Code MCP config:

```bash
claude mcp add ndis-assistant -- python /path/to/ndis-mcp-server/server.py
```

## Example Usage in VS Code

Once configured, the MCP tools and resources will be available to your AI assistant (Copilot/Claude) in VS Code. You can ask things like:

- "What NDIS support category does SIL fall under?" → triggers `lookup_support_category`
- "The participant's SDA was denied, what process should we use?" → triggers `which_process`
- "What are the s34 reasonable and necessary criteria?" → triggers `reasonable_and_necessary_checklist`

## Extending

To add more knowledge or tools:

1. Add content to `ndis_knowledge.py` (new constants or lookup data)
2. Add `@mcp.resource()`, `@mcp.tool()`, or `@mcp.prompt()` decorated functions in `server.py`
3. Restart VS Code to pick up changes

### Ideas for Future Tools
- Query the NDIS Support Catalogue XLSX for live price lookups
- Query NDIS data for benchmark comparisons
- Validate NDIS number format (Luhn check or regex)
- Calculate annual support costs from a roster/schedule
