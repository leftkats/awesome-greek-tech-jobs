import yaml
from collections import Counter


def generate():
    with open("data/companies.yaml", "r", encoding="utf-8") as f:
        companies_data = yaml.safe_load(f)

    with open("readme.yaml", "r", encoding="utf-8") as f:
        readme_data = yaml.safe_load(f)

    with open("data/queries.yaml", "r", encoding="utf-8") as f:
        queries_data = yaml.safe_load(f)

    # Logic: Sort and clean data
    all_companies = sorted(companies_data, key=lambda x: x["name"].lower())

    # Check for duplicate company names
    seen = set()
    duplicates = [
        c["name"] for c in all_companies if c["name"] in seen or seen.add(c["name"])
    ]
    if duplicates:
        raise ValueError(f"Duplicate company names found: {', '.join(set(duplicates))}")

    # Statistics Calculation
    total_companies = len(all_companies)
    loc_counts = Counter(
        [loc.strip().title() for c in all_companies for loc in c.get("locations", [])]
    )
    top_loc, top_count = loc_counts.most_common(1)[0] if loc_counts else ("N/A", 0)

    policy_counts = Counter(
        [c.get("work_policy", "N/A").strip().title() for c in all_companies]
    )
    remote_count = policy_counts.get("Remote", 0)
    hybrid_count = policy_counts.get("Hybrid", 0)

    # 1. Header & Dynamic Badges
    content = f"# {readme_data['title']}\n\n"
    content += f"![Companies](https://img.shields.io/badge/Companies-{total_companies}-blue?style=for-the-badge) "
    content += f"![Primary Hub](https://img.shields.io/badge/Main_Hub-{top_loc}-red?style=for-the-badge) "
    content += f"![Remote Friendly](https://img.shields.io/badge/Remote_Teams-{remote_count}-green?style=for-the-badge)\n\n"

    content += f"## Overview\n{readme_data['description']}\n\n"

    # 2. Professional Statistics Dashboard
    content += "### Insights\n"
    content += "| Metric | Data Point |\n| :--- | :--- |\n"
    content += (
        f"| **Total Organizations** | **{total_companies}** curated tech teams |\n"
    )
    content += f"| **Top Tech Hub** | **{top_loc}** ({top_count} offices) |\n"
    content += f"| **Work Flexibility** | **{remote_count}** Remote · **{hybrid_count}** Hybrid |\n\n"

    content += "---\n\n"

    # 3. Company directory: full table in a separate file, link from README
    hubs_filename = "engineering-hubs.md"
    hubs_lines = [
        "# Engineering Hubs & Career Portals\n",
        "\n",
        "Curated organizations, focus sectors, work policy, and talent links.\n",
        "\n",
        "| # | Organization | Focus Sectors | Policy | Talent Portals |\n",
        "| :--- | :--- | :--- | :--- | :--- |\n",
    ]

    for idx, c in enumerate(all_companies, start=1):
        company_name_md = f"[{c['name']}]({c['url']})" if c.get("url") else c["name"]

        policy = c.get("work_policy", "N/A").strip().lower().replace("-", "")

        p_color = {
            "remote": "brightgreen",
            "hybrid": "blue",
            "onsite": "orange",
        }.get(policy, "lightgrey")
        policy_badge = (
            f"![](https://img.shields.io/badge/-{policy}-{p_color}?style=flat-square)"
        )

        careers = f"[Careers]({c['careers_url']})" if c.get("careers_url") else "—"
        linkedin_id = c.get("linkedin_company_id", "")
        linkedin = (
            f"[LinkedIn](https://www.linkedin.com/company/{linkedin_id})"
            if linkedin_id
            else "—"
        )

        sectors = ", ".join([f"`{s}`" for s in c.get("sectors", [])])

        hubs_lines.append(
            f"| {idx:02} | **{company_name_md}** | {sectors} | {policy_badge} | {careers} • {linkedin} |\n"
        )

    with open(hubs_filename, "w", encoding="utf-8") as f:
        f.writelines(hubs_lines)

    content += "## Engineering Hubs & Career Portals\n\n"
    content += f"The full directory is in **[{hubs_filename}]({hubs_filename})** (markdown table).\n\n---\n"

    # 4. Search Queries (As before)
    if "queries" in queries_data:
        content += "## Useful Search Queries\n"
        for query in queries_data["queries"]:
            content += f"* [{query['name']}]({query['url']})\n"
        content += "\n---\n"

    # 5. Footer: Notes & Contributors
    if "footer" in readme_data:
        content += "## Useful Notes\n"
        if "notes" in readme_data["footer"]:
            content += "\n".join(
                [
                    f"- **{n['title']}:** {n['content']}"
                    for n in readme_data["footer"]["notes"]
                ]
            )
            content += "\n"

        content += "\n---\n"
        content += "### Contributors\n"
        if "description" in readme_data["footer"]:
            repo_path = "leftkats/awesome-greek-tech-jobs"
            content += f"[![Contributors](https://contrib.rocks/image?repo={repo_path})](https://github.com/{repo_path}/graphs/contributors)\n\n"
            content += f"\n{readme_data['footer']['description']}\n"

    # 6. Disclaimer & Mission
    content += "\n---\n"
    content += "### Disclaimer & Mission\n"
    if readme_data.get("disclaimer"):
        content += f"\n{readme_data['disclaimer']}\n"

    # Write to file
    with open("readme.md", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    generate()
    print("readme.md generated successfully!")
