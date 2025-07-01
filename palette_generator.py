import random
import json
import webbrowser
import os

# Predefined palettes with color names
PALETTES = {
    "school": [
        {"hex": "#1E90FF", "name": "Dodger Blue"},
        {"hex": "#FFD700", "name": "Gold"},
        {"hex": "#FF4500", "name": "Orange Red"},
        {"hex": "#32CD32", "name": "Lime Green"},
        {"hex": "#FFFFFF", "name": "White"}
    ],
    "university": [
        {"hex": "#00274C", "name": "Navy Blue"},
        {"hex": "#FFCB05", "name": "Maize Yellow"},
        {"hex": "#6A0DAD", "name": "Purple"},
        {"hex": "#A6A6A6", "name": "Gray"},
        {"hex": "#FFFFFF", "name": "White"}
    ],
    "corporate": [
        {"hex": "#003366", "name": "Dark Blue"},
        {"hex": "#006699", "name": "Medium Blue"},
        {"hex": "#3399CC", "name": "Light Blue"},
        {"hex": "#CCCCCC", "name": "Light Gray"},
        {"hex": "#FFFFFF", "name": "White"}
    ],
    "healthcare": [
        {"hex": "#4CAF50", "name": "Green"},
        {"hex": "#81C784", "name": "Light Green"},
        {"hex": "#E0F2F1", "name": "Mint"},
        {"hex": "#FFFFFF", "name": "White"},
        {"hex": "#455A64", "name": "Dark Gray"}
    ],
    "technology": [
        {"hex": "#0D47A1", "name": "Indigo"},
        {"hex": "#1976D2", "name": "Blue"},
        {"hex": "#42A5F5", "name": "Light Blue"},
        {"hex": "#90CAF9", "name": "Pale Blue"},
        {"hex": "#ECEFF1", "name": "Light Gray"}
    ],
    "sports": [
        {"hex": "#FF0000", "name": "Red"},
        {"hex": "#000000", "name": "Black"},
        {"hex": "#FFFFFF", "name": "White"},
        {"hex": "#FFA500", "name": "Orange"},
        {"hex": "#008000", "name": "Green"}
    ]
}

def get_palette(theme):
    theme = theme.lower()
    if theme in PALETTES:
        return PALETTES[theme]
    else:
        print("⚠️ Theme not recognized. Generating a random palette.\n")
        return [
            {"hex": f"#{random.randint(0, 0xFFFFFF):06X}", "name": "Random Color"}
            for _ in range(5)
        ]

def print_palette(palette):
    print("\n🎨 Suggested Color Palette:\n")
    for color in palette:
        print(f"{color['name']}: {color['hex']}")

def save_palette_json(palette, filename):
    with open(filename, "w") as f:
        json.dump(palette, f, indent=2)
    print(f"\n✅ Palette saved to {filename}")

def generate_html_preview(palette, filename):
    html = "<html><head><title>Color Palette Preview</title></head><body style='font-family:sans-serif;'>"
    html += "<h2>Color Palette Preview</h2>"
    for color in palette:
        html += f"""
        <div style='display:flex;align-items:center;margin-bottom:10px;'>
            <div style='width:60px;height:60px;background:{color['hex']};border:1px solid #000;'></div>
            <div style='margin-left:10px;'>{color['name']} ({color['hex']})</div>
        </div>
        """
    html += "</body></html>"

    with open(filename, "w") as f:
        f.write(html)

    print(f"\n✅ HTML preview saved to {filename}")
    webbrowser.open('file://' + os.path.realpath(filename))

def main():
    print("🎨 Advanced Theme-Based Color Palette Generator 🎨\n")
    print("Available themes:")
    for key in PALETTES:
        print(f" - {key}")
    theme = input("\nEnter a theme for the palette: ").strip()

    palette = get_palette(theme)
    print_palette(palette)

    # Save JSON
    save_json = input("\nWould you like to save this palette as JSON? (y/n): ").strip().lower()
    if save_json == 'y':
        filename = input("Enter JSON filename (e.g., palette.json): ").strip()
        save_palette_json(palette, filename)

    # Save HTML preview
    save_html = input("\nGenerate HTML preview? (y/n): ").strip().lower()
    if save_html == 'y':
        html_filename = input("Enter HTML filename (e.g., preview.html): ").strip()
        generate_html_preview(palette, html_filename)

if __name__ == "__main__":
    main()
