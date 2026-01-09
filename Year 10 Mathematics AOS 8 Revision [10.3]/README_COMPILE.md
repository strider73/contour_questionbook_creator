# How to Compile the Version B Test to PDF

## Required Software

You need a LaTeX distribution installed. Options:

### macOS:
```bash
# Install MacTeX (full distribution)
brew install --cask mactex

# OR install BasicTeX (smaller)
brew install --cask basictex
```

### After Installation:
```bash
# Update package database
sudo tlmgr update --self
sudo tlmgr update --all
```

## Compilation Steps

1. **Navigate to the directory:**
```bash
cd "/Volumes/Programming HD/Study/claude-code/skill/pdf"
```

2. **Compile (run twice for proper cross-references):**
```bash
pdflatex Year_10_AOS8_Mock_CAT_1_Version_B.tex
pdflatex Year_10_AOS8_Mock_CAT_1_Version_B.tex
```

3. **Open the PDF:**
```bash
open Year_10_AOS8_Mock_CAT_1_Version_B.pdf
```

## Alternative: Online Compilation

If you don't want to install LaTeX locally:

1. Go to **Overleaf** (https://www.overleaf.com)
2. Create a new project
3. Upload the `.tex` file
4. Upload the `new_images/` folder
5. Click "Recompile"
6. Download the PDF

## File Structure Required

The compiler needs:
```
.
├── Year_10_AOS8_Mock_CAT_1_Version_B.tex
└── new_images/
    ├── q5.png
    ├── q10.png
    ├── q12.png
    └── q14e.png
```

## Expected Output

- **Year_10_AOS8_Mock_CAT_1_Version_B.pdf** - The final test document
- Auxiliary files (.aux, .log) - Can be deleted after compilation

## Troubleshooting

**Error: "File not found"**
- Check that `new_images/` folder is in the same directory as the .tex file
- Verify all diagram files exist (q5.png, q10.png, q12.png, q14e.png)

**Error: "Missing package"**
- Install missing package: `sudo tlmgr install <package-name>`
- Common packages needed: geometry, amsmath, amssymb, graphicx, enumitem, fancyhdr

**Diagrams not appearing:**
- Run pdflatex twice (first pass creates references, second inserts them)
- Check file paths in \includegraphics commands match actual files

## Quick Compilation Script

Create a script to automate:
```bash
#!/bin/bash
cd "/Volumes/Programming HD/Study/claude-code/skill/pdf"
pdflatex -interaction=nonstopmode Year_10_AOS8_Mock_CAT_1_Version_B.tex
pdflatex -interaction=nonstopmode Year_10_AOS8_Mock_CAT_1_Version_B.tex
rm -f *.aux *.log *.out  # Clean up auxiliary files
open Year_10_AOS8_Mock_CAT_1_Version_B.pdf
```

Save as `compile_test.sh`, make executable with `chmod +x compile_test.sh`, then run `./compile_test.sh`
