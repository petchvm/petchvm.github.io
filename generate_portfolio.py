import json
import sys
from datetime import UTC, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# Configuration
CONFIG = {
    "data_file": "portfolio.json",
    "index_template": "index_template.html",
    "resume_template": "resume_template.html",
    "output_index": "index.html",
    "output_resume": "resume.html",
}


def load_portfolio_data(data_file: str) -> dict:
    """Load and parse portfolio data from JSON file."""
    try:
        with Path(data_file).open(encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {data_file} not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {data_file}: {e}")
        sys.exit(1)
    return data


def load_svg_icons(data: dict) -> None:
    """Load SVG icon data for social links."""
    if "social_links" not in data:
        return

    for link in data["social_links"]:
        if link.get("svg_path"):
            try:
                with Path(link["svg_path"]).open(encoding="utf-8") as svg_file:
                    link["svg_data"] = svg_file.read()
            except FileNotFoundError:
                print(f"Warning: SVG icon not found: {link['svg_path']}")
                link["svg_data"] = ""


def render_templates(data: dict) -> tuple[str, str]:
    """Render HTML templates with portfolio data."""
    try:
        env = Environment(loader=FileSystemLoader("."), autoescape=True)
        index_template = env.get_template(CONFIG["index_template"])
        resume_template = env.get_template(CONFIG["resume_template"])

        html_output = index_template.render(**data)
        resume_output = resume_template.render(**data)

        return html_output, resume_output
    except Exception as e:
        print(f"Error rendering templates: {e}")
        sys.exit(1)


def write_output_files(html_output: str, resume_output: str) -> None:
    """Write rendered HTML to output files."""
    try:
        with Path(CONFIG["output_index"]).open("w", encoding="utf-8") as f:
            f.write(html_output)

        with Path(CONFIG["output_resume"]).open("w", encoding="utf-8") as f:
            f.write(resume_output)

        print("HTML files generated successfully!")
    except IOError as e:
        print(f"Error writing output files: {e}")
        sys.exit(1)


def main():
    """Main function to generate portfolio HTML files."""
    # Load portfolio data
    data = load_portfolio_data(CONFIG["data_file"])

    # Add current year for copyright
    data["current_year"] = datetime.now(tz=UTC).year

    # Load SVG icons for social links
    load_svg_icons(data)

    # Render templates
    html_output, resume_output = render_templates(data)

    # Write output files
    write_output_files(html_output, resume_output)


if __name__ == "__main__":
    main()
