#!/usr/bin/env python3
"""
Generate SDK Reference section for README.md from the OpenAPI spec.

This script parses the OpenAPI spec and generates markdown tables
documenting all available methods with descriptions from the spec.

New tags added to the OpenAPI spec are auto-discovered and included
in the README. Only special cases need explicit configuration below.

Method names use Go PascalCase convention matching oapi-codegen output.
"""

import re
import sys
from pathlib import Path

import yaml

# Tags that should be merged into another resource instead of getting their own section
TAG_MERGE: dict[str, str] = {
    "GMB Reviews": "Accounts",
    "LinkedIn Mentions": "Accounts",
}

# Tags to skip entirely (no SDK methods)
SKIP_TAGS: set[str] = {
    "Inbox Access",
}

# Override display names (tag -> display name). Unmatched tags use the tag name as-is.
DISPLAY_NAME_OVERRIDES: dict[str, str] = {
    "Connect": "Connect (OAuth)",
    "Reddit Search": "Reddit",
    "Messages": "Messages (Inbox)",
    "Comments": "Comments (Inbox)",
    "Reviews": "Reviews (Inbox)",
}

# Preferred ordering for known resources. Auto-discovered resources appear after these.
PREFERRED_ORDER: list[str] = [
    "Posts",
    "Accounts",
    "Profiles",
    "Analytics",
    "Account Groups",
    "Queue",
    "Webhooks",
    "API Keys",
    "Media",
    "Tools",
    "Users",
    "Usage",
    "Logs",
    "Connect",
    "Reddit Search",
]

# Resources that should always appear last, in this order
LAST_RESOURCES: list[str] = [
    "Invites",
]


def to_pascal_case(name: str) -> str:
    """Convert camelCase operationId to PascalCase Go function name."""
    if not name:
        return name
    return name[0].upper() + name[1:]


def get_method_sort_key(method_name: str) -> tuple:
    """Generate a sort key for consistent method ordering (CRUD-style)."""
    name_lower = method_name.lower()

    if name_lower.startswith("list") or name_lower.startswith("getall"):
        return (0, method_name)
    elif name_lower.startswith("bulk") or name_lower.startswith("create"):
        return (1, method_name)
    elif name_lower.startswith("get") and not name_lower.startswith("getall"):
        return (2, method_name)
    elif name_lower.startswith("update"):
        return (3, method_name)
    elif name_lower.startswith("delete"):
        return (4, method_name)
    else:
        return (5, method_name)


def load_openapi_spec(spec_path: Path) -> dict:
    """Load and parse the OpenAPI spec."""
    with open(spec_path) as f:
        return yaml.safe_load(f)


def extract_methods_from_spec(
    spec: dict,
) -> tuple[dict[str, list[tuple[str, str]]], list[str], dict[str, str]]:
    """
    Extract methods and descriptions from OpenAPI spec.

    Returns (resources, resource_order, display_names).
    Uses tag names as resource keys (preserving original casing).
    """
    resources: dict[str, list[tuple[str, str]]] = {}
    display_names: dict[str, str] = {}
    discovered: set[str] = set()

    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method not in ("get", "post", "put", "patch", "delete"):
                continue

            tags = operation.get("tags", [])
            if not tags:
                continue

            tag = tags[0]
            if tag in SKIP_TAGS:
                continue

            operation_id = operation.get("operationId", "")
            if not operation_id:
                continue

            # Resolve the resource key: merged tags go to their parent
            resource_key = TAG_MERGE.get(tag, tag)
            discovered.add(resource_key)

            # Track display name (non-merged tags only)
            if tag not in TAG_MERGE:
                display_names[resource_key] = DISPLAY_NAME_OVERRIDES.get(tag, tag)

            if resource_key not in resources:
                resources[resource_key] = []

            # Convert operationId to PascalCase Go method name
            method_name = to_pascal_case(operation_id)

            summary = operation.get("summary", "")
            description = summary if summary else method_name

            resources[resource_key].append((method_name, description))

    # Build final order: preferred first, then auto-discovered, then last resources
    preferred_set = set(PREFERRED_ORDER)
    last_set = set(LAST_RESOURCES)
    auto_discovered = sorted(
        r for r in discovered if r not in preferred_set and r not in last_set
    )

    resource_order = [
        *[r for r in PREFERRED_ORDER if r in discovered],
        *auto_discovered,
        *[r for r in LAST_RESOURCES if r in discovered],
    ]

    # Sort methods within each resource
    for resource_key in resource_order:
        if resource_key in resources:
            resources[resource_key] = sorted(
                resources[resource_key], key=lambda x: get_method_sort_key(x[0])
            )

    return resources, resource_order, display_names


def generate_reference_section(
    resources: dict[str, list[tuple[str, str]]],
    resource_order: list[str],
    display_names: dict[str, str],
) -> str:
    """Generate the SDK Reference section markdown."""
    lines = ["## SDK Reference", ""]

    for resource_key in resource_order:
        methods = resources.get(resource_key, [])
        if not methods:
            continue

        display_name = display_names.get(resource_key, resource_key)

        lines.append(f"### {display_name}")
        lines.append("| Method | Description |")
        lines.append("|--------|-------------|")

        for method_name, description in methods:
            lines.append(f"| `client.{method_name}WithResponse()` | {description} |")

        lines.append("")

    return "\n".join(lines)


def update_readme(readme_path: Path, reference_section: str) -> None:
    """Update the README.md file with the new SDK Reference section."""
    content = readme_path.read_text()

    # Find the SDK Reference section and replace it
    # It starts with "## SDK Reference" and ends before "## Documentation" or "## License"
    pattern = r"## SDK Reference\n.*?(?=## (?:Documentation|License))"
    replacement = reference_section + "\n"

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if new_content == content:
        # Section doesn't exist yet, insert before ## Documentation or ## License
        for marker in ["## Documentation", "## License"]:
            if marker in content:
                new_content = content.replace(marker, reference_section + "\n" + marker)
                break

    if new_content != content:
        readme_path.write_text(new_content)
        print(f"Updated {readme_path}")
    else:
        print("No changes needed")


def main():
    script_dir = Path(__file__).parent
    spec_path = script_dir.parent / "openapi.yaml"
    readme_path = script_dir.parent / "README.md"

    spec = load_openapi_spec(spec_path)
    resources, resource_order, display_names = extract_methods_from_spec(spec)
    reference_section = generate_reference_section(resources, resource_order, display_names)

    if "--print" in sys.argv:
        print(reference_section)
    else:
        update_readme(readme_path, reference_section)


if __name__ == "__main__":
    main()
