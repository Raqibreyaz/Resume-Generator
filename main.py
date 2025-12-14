# file which actually generates the info using the basic-info and jd-specific info

import yaml
import json
import subprocess

name = "Raquib_Reyaz"
yaml_file_name = f"{name}_CV.yaml"

# Load YAML files
with open("info/basic-info.yaml") as f:
    basic_info = yaml.safe_load(f)

with open("info/jd-specific.json") as f:
    jd_specific = json.load(f)
    
basic_info["cv"]["sections"] = {
    **jd_specific,
    **basic_info["cv"]["sections"]
    }

# Write to final file
with open(yaml_file_name, "w") as f:
    yaml.dump(basic_info, f, sort_keys=False, allow_unicode=True)

print(f"{yaml_file_name} generated...")

subprocess.run(["rendercv","render",yaml_file_name])

print(f"✅ {name}_CV.pdf generated!")