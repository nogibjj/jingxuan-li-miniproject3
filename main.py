import polars as pl
import matplotlib.pyplot as plt
from mylib.lib import (
    load_and_preview_data,
    calculate_summary_statistics,
    calculate_descriptive_statistics,
    plot_age_distribution,
)


def g_describe(file):
    """
    Loads and previews data.
    """
    g = load_and_preview_data(file)
    return g


def save_to_md(text, filename="descriptive.md"):
    """
    Appends text to a markdown file.
    """
    with open(filename, "a") as file:
        file.write(text + "\n")


def insert_image_to_md(image_filename, markdown_filename="descriptive.md"):
    """
    Inserts the image reference into the markdown file.
    """
    save_to_md(f"![{image_filename}]({image_filename})", markdown_filename)


if __name__ == "__main__":
    file_path = "./Employee.csv"

    # Load and preview the data
    df = g_describe(file_path)

    # Save data overview in markdown
    save_to_md("# Employee Data Overview")
    save_to_md("## Data Head", "descriptive.md")
    save_to_md(
        df.head().to_pandas().to_markdown(), "descriptive.md"
    )  # Convert to Pandas for markdown

    # Calculate and save summary statistics
    save_to_md("## Summary Statistics", "descriptive.md")
    summary_stats = calculate_summary_statistics(df)
    save_to_md(
        summary_stats.to_pandas().to_markdown(), "descriptive.md"
    )  # Convert to Pandas for markdown

    # Calculate and save descriptive statistics for Age and Salary
    save_to_md("## Descriptive Statistics for Age and Salary", "descriptive.md")
    calculate_descriptive_statistics(df)

    # Plot and insert age distribution image
    plot_age_distribution(df)
    save_to_md("## Age Distribution Plot", "descriptive.md")
    insert_image_to_md("age.png")
