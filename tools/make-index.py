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

numbers = {}
with open(topgit / "subjects/00-NUMBERS", 'r', encoding="UTF-8") as reader:
    for line in reader:
        if line.startswith("#"):
            continue
        number, filename = line.strip().split()
        if filename.startswith(PREFIX):
            numbers[filename] = int(number)
        else:
            print(f"WARNING: {filename} does not start with {PREFIX}, skipping")

with open(output_csv, 'w', encoding="UTF-8") as fout:
    print("company,person,stem,index,title", file=fout)
    for md_file in md_files:
        md_relpath = md_file.relative_to(topgit)
        # xx patchy part
        # tentatively find company and person based on UPPERCASE-lowercase
        directory = md_relpath.parent
        if not (match := re.match(r"^([A-Z-]+)-(.*)", directory.name)):
            print(f"WARNING: {directory} does not match expected pattern, skipping")
            continue
        company = match.group(1)
        person = match.group(2)

        stem = md_relpath.stem
        name = md_relpath.name
        if name not in numbers:
            print(f"WARNING: {stem} not found in subjects/00-NUMBERS, skipping")
            continue
        index = numbers[name]

        # write a possibly modified version
        md_modified = md_file.with_suffix(".tmp")
        adopt_modified = False
        title_found = False
        title = "???"

        with md_modified.open('w', encoding="UTF-8") as writer:
            with md_file.open() as reader:
                for line in reader:
                    if title_found or not line.startswith("# "):
                        writer.write(line)
                        continue
                    title_found = True
                    if (match := re.match(r"^# (?P<index>\d+) (« )?(?P<title>.*)( »)?", line)):
                        md_index = int(match.group("index"))
                        title = match.group("title")
                        sep1 = match.group(2)
                        sep2 = match.group(3)
                        if md_index != index or not sep1 or not sep2:
                            adopt_modified = True
                            writer.write(f"# {index:02d} « {title} »\n")
                    elif (match := re.match(r"^# (« )?(?P<title>.*)( »)?", line)):
                        title = match.group("title")
                        adopt_modified = True
                        writer.write(f"# {index:02d} « {title} »\n")
                    else:
                        print(f"WARNING: {md_file} cannot spot title from line: {line.strip()} - bailing out")
                        exit(1)
        if adopt_modified:
            print(f"adopting modified title in {md_file}")
            md_modified.rename(md_file)
        else:
            md_modified.unlink()
        print(f"index={md_index:03} ", end="")
        print(f"title={title[:25]}...", end="")
        # remove space around guillemets in the TOC area
        # because it is rather narrow and we often see the titles
        # cut in the wrong places
        title = title.replace("« ", "«").replace(" »", "»")
        # record a tuple index, title
        subjects.append(
            (md_index, f"{index:02d} {title.strip()} <{md_relpath}>"))
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
