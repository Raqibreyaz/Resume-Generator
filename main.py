# file which actually generates the info using the basic-info and jd-specific info

import yaml
import json
import subprocess

name = "Raquib_Reyaz"
yaml_file_name = f"{name}_CV.yaml"

# Load YAML files
with open("basic-info.yaml") as f:
    basic_info = yaml.safe_load(f)

resume_version = 'complete-info'
jd_specific = {}

with open(f"{resume_version}/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()
    if summary and len(summary) > 0:
        jd_specific["summary"] = [summary]
with open(f"{resume_version}/skills.json", "r", encoding="utf-8") as f:
    jd_specific["Technical Skills"] = json.load(f)
with open(f"{resume_version}/projects.json", "r", encoding="utf-8") as f:
    jd_specific["projects"] = json.load(f)
with open(f"{resume_version}/achievements.json", "r", encoding="utf-8") as f:
    jd_specific["Achievements"] = json.load(f)

basic_info["cv"]["sections"] = {**jd_specific, **basic_info["cv"]["sections"]}

# Write to final file
with open(yaml_file_name, "w") as f:
    yaml.dump(basic_info, f, sort_keys=False, allow_unicode=True)

print(f"{yaml_file_name} generated...")

subprocess.run(["rendercv", "render", yaml_file_name])

print(f"✅ {name}_CV.pdf generated!")
