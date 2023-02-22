import re

import yaml
from yaml.loader import SafeLoader
from tabulate import tabulate

DOMAIN_ORDER = [
    "Wikipedia",
    "News",
    "Web",
    "Mixed",
    "Books",
    "Education",
    "Medical",
    "Clinical",
    "Talks",
]

HEADER = [
    "Dataset",
    "Lang",
    "Domain",
    "Kind",
    "Level",
    "Instances",
    "Refs.",
    "Link",
]

# More compact
LEVEL_MAP = {
    'Sentence': 'Sent',
    'Paragraph': 'Par',
    'Document': 'Doc',
}


def record_to_row(d: dict):
    if d["link"]:
        link = f"[Link]({d['link']})"
    else:
        link = "n/a"
    if d["linkNote"]:
        link += f" ({d['linkNote']})"

    author_year = f"{d['author']} ({d['year']})"
    author_year_link = f"[{author_year}]({d['paper']})"
    name = f"**{d['name']} - {author_year_link}"
    return [
        name,
        d["language"],
        d["domain"],
        d["kind"],
        LEVEL_MAP.get(d["level"]),
        d["instances"],
        d["references"],
        link,
    ]


with open("data.yml") as f:
    datasets = yaml.load(f, Loader=SafeLoader)

datasets = datasets["datasets"].values()
datasets = sorted(datasets, key=lambda d: (DOMAIN_ORDER.index(d["domain"]), d["year"]))
rows = map(record_to_row, datasets)

table = tabulate(rows, headers=HEADER, tablefmt="github")
table = re.sub(" +", " ", table)  # more compact
table = re.sub("-+", "-", table)  # more compact

with open("README.template.md") as fin:
    text = fin.read()

text = text.replace("{{datasets}}", table)

with open("README.md", "w") as fout:
    fout.write(text)
