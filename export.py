import os

# Define the directory where the repo is located
REPO_DIR = os.getcwd()  # Assumes the script is run from the repo root
OUTPUT_FILE = "help_centre.md"

def find_mdx_files(directory):
    """Recursively find all .mdx files in the repo."""
    mdx_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".mdx"):
                mdx_files.append(os.path.join(root, file))
    return mdx_files

def combine_mdx_files(mdx_files, output_file):
    """Combine all .mdx files into one .md file."""
    with open(output_file, "w", encoding="utf-8") as outfile:
        for mdx_file in sorted(mdx_files):  # Sorting ensures consistent order
            with open(mdx_file, "r", encoding="utf-8") as infile:
                content = infile.read()
                outfile.write(f"\n\n# {os.path.basename(mdx_file)}\n\n")  # Section title
                outfile.write(content)
                outfile.write("\n\n---\n\n")  # Separator for readability
    print(f"Combined documentation saved to {output_file}")

if __name__ == "__main__":
    mdx_files = find_mdx_files(REPO_DIR)
    if mdx_files:
        combine_mdx_files(mdx_files, OUTPUT_FILE)
    else:
        print("No .mdx files found in the repository.")