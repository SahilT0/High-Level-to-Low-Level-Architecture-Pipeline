# utils.py

import os
import json

def save_output(result, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)

    # Save modules
    with open(os.path.join(output_dir, "output_modules.txt"), "w") as f:
        for module in result["modules"]:
            f.write(f"- {module}\n")

    # Save schema
    with open(os.path.join(output_dir, "output_schema.json"), "w") as f:
        json.dump(result["schema"], f, indent=4)

    # Save pseudocode
    with open(os.path.join(output_dir, "output_pseudocode.py"), "w") as f:
        f.write(result["pseudocode"])
