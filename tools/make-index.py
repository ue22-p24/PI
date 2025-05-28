"""
scans all markdown files in subjects/*
that match the pattern projet-p24*.md
and create a sphinx index for them

the (h1) title of each markdown is expected to contain
a number on 2 digits, which is used to sort the subjects
"""

# pylint: disable=invalid-name

import re
from pathlib import Path
from string import Template

PREFIX = "p24-"

topgit = Path(__file__).parent.parent

output = topgit / "sphinx/index.md"
output_csv = topgit / "sphinx/index-projects.csv"

md_files = sorted(topgit.glob(f"subjects/*/{PREFIX}*.md"))
print(f"{len(md_files)} files detected : ")
margin = max(len(p.stem) for p in md_files) - len(PREFIX)

subjects = []

with open(output_csv, 'w', encoding="UTF-8") as fout:
    print("company,person,stem,index,title", file=fout)
    for md_file in md_files:
        md_relpath = md_file.relative_to(topgit)
        # xx patchy part
        # tentatively find company and person based on UPPERCASE-lowercase
        directory = md_relpath.parent
        match_company = re.match(r"^([A-Z-]+)-.*", directory.name)
        company = match_company.group(1) if match_company else "???"
        person = directory.name.replace(company+"-", "")
        # match_person = re.match(r".*-([a-z0-9_-]+)$", dir.name)
        # person = match_person.group(1) if match_person else "???"
        # remove PREFIX from filename for conciseness
        stem = md_relpath.stem.replace(PREFIX, "")
        # print(f">{company:10}< >{person:10}< ", end="")
        print(f"{stem:>{margin}} ", end="")
        title = None
        md_index = 999
        with md_file.open() as fin:
            for line in fin:
                if not line.startswith("# "):
                    continue
                match = re.match(r"^# (\d+) (.*)", line)
                try:
                    md_index = int(match.group(1))
                except (ValueError, AttributeError):
                    md_index = 0
                title = match.group(2) if match else line[2:]
                break
        if md_index == 999:
            print(f"index not found <= {md_index} ", end="")
        else:
            print(f"index={md_index:03} ", end="")
        if not title:
            print("NO title", end="")
        else:
            print(f"title={title[:25]}...", end="")
        # remove space around guillemets in the TOC area
        # because it is rather narrow and we often see the titles
        # cut in the wrong places
        title = title.replace("« ", "«").replace(" »", "»")
        # record a tuple index, title
        subjects.append((md_index,
                         f"{md_index:02d} {title.strip()} <{md_relpath}>"))
        print()
        # write csv
        print(company, person, stem, md_index, title, file=fout, sep=',')

subjects.sort(key=lambda s: s[0])

with (topgit / "sphinx/index-template.md").open('r') as fin:
    temp = Template(fin.read())

with output.open('w') as fout:
    print(temp.substitute(
            how_many=len(subjects),
            subjects='\n'.join(s[1] for s in subjects)), file=fout, end="")

print(f"(over)wrote {output}")
print(f"(over)wrote {output_csv}")
