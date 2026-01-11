# Contributing to Awesome Greek Tech Jobs

Thank you for wanting to improve this list! We love community contributions. To keep the repository organized, please follow these simple steps to add or update content.

## Repository Structure

This repository organizes its data under the `data` directory. Below is a description of the files you can contribute to:

- **`data/companies.yaml`**: Contains a list of companies hiring for tech roles. Each entry includes the company name, sector, careers page URL, and LinkedIn ID. For the LinkedIn ID find the company's LinkedIn page and copy the company ID.
https://www.linkedin.com/company/**company-id**/.
- **`data/quries.yaml`**: Contains predi

## How to Contribute via Pull Request

1. **Fork the Repository**: Click the 'Fork' button at the top right of the main page.
2. **Edit the Data Files**: Open the appropriate file(s) in the `data` directory within your fork.
3. **Add or Update Content**: Predefined search queries for automated scouting
    - For `companies.yaml`: Add a new company entry in the following format:
      ```yaml
      - name: Company Name
        url: https://www.company-website.com/
        sectors:
          - Sector Name
        careers_url: Careers full url
        linkedin_company_id: Company LinkedIn ID
        locations:
          - Athens
        work_policy: remote
      ```
    - For `quries.yaml`: Add a new predefined search query:
      ```yaml
      - name: "Startup Pirate: Learn what matters in Greek tech and startups"
        url: https://startuppirate.gr/
      ```
4. **Commit Changes**: Use a clear commit message like `feat: add [Company Name] to companies.yaml`.
5. **Create Pull Request**: Go back to the original repository and click "New Pull Request".
6. **Automated Review & Merge**: If your Pull Request passes the validation checks and follows the required format, our automated workflow will merge via a squash commit.

## Contribution Rules

* **Tech Focus Only**: Please only add companies, roles, or resources relevant to Computer/Software Engineering, Data, or Tech-Business roles. No mechanical, civil, or non-tech engineering.
* **Working Links**: Ensure all URLs provided are active and correct.
* **YAML Validation**: Make sure the YAML files are properly formatted and valid.
* **Descriptive Entries**: Provide clear and concise descriptions for roles and resources.

## Workflow Automation

This repository uses GitHub Actions to validate contributions:
- **YAML Validation**: Ensures all YAML files are properly formatted.
- **Link Checker**: Verifies that all URLs are reachable.
- **Alphabetical Order Check**: Confirms that entries are sorted alphabetically.

Thank you for contributing to Awesome Greek Tech Jobs!
