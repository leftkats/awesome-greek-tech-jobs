# `_data`

This directory holds **structured source data** for the Greek Software Ecosystem project. The static site, generated Markdown, and badges are built from these YAML files (plus the repo root `readme.yaml`).

| Path | Purpose |
| :--- | :--- |
| **`companies/`** | One `.yaml` file per employer: name, sectors, careers URL, LinkedIn company id, locations, work policy, and related fields. Filenames are a slug (e.g. `my-company.yaml`); each file is a single mapping. |
| **`queries.yaml`** | Curated job boards, portals, and awesome-list links, grouped into **sections**. Feeds the job-search page and **[search-queries-and-resources.md](../search-queries-and-resources.md)**. Tips & notes on that page come from **`readme.yaml`** → `footer.notes`, not from this file. |
| **`podcasts.yaml`** | Greek tech & startup podcasts (intro, disclaimer, and a `podcasts` list with titles, descriptions, and listen links). Drives **[greek-tech-podcasts.md](../greek-tech-podcasts.md)** and **`podcasts.html`**. |
| **`open_source_projects.yaml`** | Greek-related **open source** GitHub projects (`title`, `url`, `description`). Feeds **[generated/open-source-projects.md](../generated/open-source-projects.md)** and the main readme overview. |
| **`cafe_resources.yaml`** | Laptop-friendly **cafés** and **directory** sites (`kind: cafe` vs `kind: directory`). Feeds **[generated/remote-cafe-resources.md](../generated/remote-cafe-resources.md)** and the Resources page. |
| **`workable_counts.yaml`** | **Generated** snapshot of open-role counts from Workable’s public API (per slug, totals, timestamps). Refreshed by **`just fetch`** / CI—do not edit by hand unless you know what you are doing. |

For contribution rules, validation, and examples, see **[contributing.md](../contributing.md)**.
