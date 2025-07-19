# main.py

from requirement_parser import parse_requirement
from utils import save_output

def main():
    print("🛠️ High-Level to Low-Level Architecture Generator")
    requirement = input("📥 Enter your high-level business requirement:\n> ")

    # Process the requirement using parser
    result = parse_requirement(requirement)

    # Display output in console
    print("\n🔍 Modules Identified:")
    print(result['modules'])

    print("\n🗃️ Suggested Schema:")
    print(result['schema'])

    print("\n🧠 Generated Pseudocode:")
    print(result['pseudocode'])

    # Save outputs to files
    save_output(result)

    print("\n✅ Output saved to 'output/' folder.")

if __name__ == "__main__":
    main()
