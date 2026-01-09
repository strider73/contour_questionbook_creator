# Diagram Extraction Reference

## What to Extract

**✅ Extract ONLY printed source diagrams**:
- Tables, Venn diagrams, box plots, scatter plots, geometric figures
- 3D shapes (cones, cylinders, spheres, prisms, pyramids)
- Clean, professional diagrams that are part of the question
- Any visual elements essential to understanding the problem

**❌ Never extract**:
- Student's handwritten answers
- Student's sketches or working
- Blank answer spaces
- Question numbering or headers (unless part of the diagram)

## How the Script Works

The extraction script uses Vision-identified coordinates to crop diagram regions from page images:

```python
# 1. Vision identifies: "Table at 20-60% vertical, 15-85% horizontal"

# 2. Script loads page and calculates pixel coordinates
page_img = Image.open("temp_pages/page_03.png")
width, height = page_img.size

left = int(width * 0.15)   # 15% from left edge
top = int(height * 0.20)    # 20% from top edge
right = int(width * 0.85)   # 85% from left edge (15% from right)
bottom = int(height * 0.60) # 60% from top edge (40% from bottom)

# 3. Crop to diagram region ONLY
diagram = page_img.crop((left, top, right, bottom))

# 4. Save to images/ folder relative to source location
# Example: temp_pages/page_03.png → images/diagram_page03_table.png
output_path = Path(page_path).parent.parent / "images"
output_path.mkdir(parents=True, exist_ok=True)
diagram.save(output_path / "diagram_page03_table.png")
```

**Result**: Diagram file contains ONLY the diagram region, without question text or surrounding content. Saved in the same parent directory structure as the source images.

## Understanding Coordinates

### Percentage-Based System
Coordinates use percentages (0.0 to 1.0) relative to the page dimensions:

- **Vertical (top/bottom)**:
  - 0.0 = top of page
  - 1.0 = bottom of page
  - Example: `top_pct=0.20` means 20% down from top

- **Horizontal (left/right)**:
  - 0.0 = left edge of page
  - 1.0 = right edge of page
  - Example: `right_pct=0.85` means 85% across from left

### Vision Workflow
1. Use Vision to view the page image
2. Identify the diagram's position visually
3. Estimate percentages based on visual location:
   - Top 1/4 of page? → top_pct ≈ 0.25
   - Centered horizontally? → left_pct ≈ 0.20, right_pct ≈ 0.80
   - Bottom half? → top_pct ≈ 0.50

4. Run extraction script with these coordinates
5. Check output and adjust if needed

## Command Syntax

```bash
python3 .claude/skills/diagram-extractor/scripts/extract_diagram.py \
  <page_path> \
  <diagram_type> \
  <top_pct> <bottom_pct> <left_pct> <right_pct>
```

**Example**:
```bash
python3 .claude/skills/diagram-extractor/scripts/extract_diagram.py \
  "temp_pages/page_08.png" \
  "cone" \
  0.15 0.55 0.20 0.65
```

**Arguments**:
- `page_path`: Path to page image (e.g., "temp_pages/page_08.png")
- `diagram_type`: Type identifier (e.g., "cone", "table", "venn")
- `top_pct`: Top boundary (0.0-1.0)
- `bottom_pct`: Bottom boundary (0.0-1.0)
- `left_pct`: Left boundary (0.0-1.0)
- `right_pct`: Right boundary (0.0-1.0)

## Naming Convention

Format: `diagram_page{N}_{type}.png`

**Examples**:
- `diagram_page03_table.png`
- `diagram_page04_venn.png`
- `diagram_page12_geometry.png`
- `diagram_page08_cone.png`
- `diagram_page15_boxplot.png`

**Output Directory**: Diagrams saved to `images/` directory in the same parent folder as the source `temp_pages/` directory (auto-created)

**Path Logic**:
- Source: `WorkbookName/temp_pages/page_08.png`
- Output: `WorkbookName/images/diagram_page08_cone.png`

## Common Diagram Types

Use descriptive type names that make diagrams easy to identify:

**2D Shapes & Figures**:
- `table` - Data tables
- `venn` - Venn diagrams
- `plot` - Scatter plots, line graphs
- `boxplot` - Box and whisker plots
- `geometry` - Generic geometric figures
- `triangle`, `square`, `circle` - Specific shapes

**3D Shapes**:
- `cone` - Cones
- `cylinder` - Cylinders
- `sphere` - Spheres
- `prism` - Prisms
- `pyramid` - Pyramids
- `composite` - Composite 3D shapes

**Mathematical Diagrams**:
- `graph` - Function graphs
- `numberline` - Number lines
- `coordinate` - Coordinate planes
- `angle` - Angle diagrams

## Quality Standards

Every extracted diagram must meet these criteria:

### ✅ Completeness
- ALL diagram content visible (no cut-off edges)
- All labels and annotations included
- All axes, gridlines, or reference marks intact

### ✅ Isolation
- No question text or instructions
- No student work or annotations
- No page numbers or headers (unless essential)
- Clean white background around diagram

### ✅ Margins
- 5-10 pixel white space around all edges
- Prevents visual crowding when embedded
- Better than too tight (can always crop more)

### ✅ Resolution
- Minimum 150 DPI for clarity
- Text and numbers clearly legible
- Lines and shapes crisp and distinct

### ✅ Orientation
- Diagram right-side up
- Labels readable without rotation
- Standard mathematical orientation (if applicable)

## Common Issues & Fixes

### Bottom row cut off (tables)
**Symptom**: Last row of table missing or partially visible

**Cause**: Bottom boundary too high

**Fix**: Increase `bottom_pct` value
```bash
# Before: bottom_pct=0.58
# After:  bottom_pct=0.65
```

### Question text included
**Symptom**: Question number or instructions appear above diagram

**Cause**: Top boundary too high (includes text above diagram)

**Fix**: Decrease `top_pct` value (move down)
```bash
# Before: top_pct=0.10
# After:  top_pct=0.15
```

### Sides cut off
**Symptom**: Left or right edges of diagram truncated

**Cause**: Left/right boundaries too narrow

**Fix**: Expand boundaries
```bash
# Before: left_pct=0.25, right_pct=0.75
# After:  left_pct=0.20, right_pct=0.80
```

### Blurry diagram
**Symptom**: Diagram appears fuzzy or pixelated

**Cause**: Low source image resolution

**Fix**: Re-generate page images with higher DPI
```bash
# Increase DPI when converting PDF to PNG
pdftoppm -png -r 300 input.pdf temp_pages/page
# (previously: -r 200)
```

### Too much white space
**Symptom**: Large white margins around diagram

**Cause**: Boundaries too generous

**Fix**: Tighten boundaries slightly (prefer this over cutting off content)
```bash
# Reduce margins incrementally
# Before: left_pct=0.10, right_pct=0.90
# After:  left_pct=0.15, right_pct=0.85
```

### Multiple diagrams on same page
**Symptom**: Need to extract 2+ diagrams from one page

**Solution**: Run script multiple times with different coordinates and types
```bash
# First diagram
python3 scripts/extract_diagram.py temp_pages/page_05.png table1 0.10 0.40 0.15 0.85

# Second diagram
python3 scripts/extract_diagram.py temp_pages/page_05.png table2 0.50 0.80 0.15 0.85
```

## Workflow Best Practices

### 1. Vision First
Always use Vision to view the page image before running extraction:
- Understand diagram layout visually
- Identify exact boundaries
- Note any potential issues (rotation, multiple diagrams, etc.)

### 2. Be Generous with Margins
When in doubt, include extra white space rather than risk cutting off content:
- Easier to crop later if needed
- Preserves all essential information
- Prevents accidental data loss

### 3. Check Output Immediately
After extraction, verify the output file:
```bash
# View the extracted diagram
open images/diagram_page08_cone.png
```

Look for:
- All content visible?
- Clean isolation from surrounding page?
- Adequate margins?
- Acceptable resolution?

### 4. Iterate if Needed
If extraction isn't perfect, adjust coordinates and re-run:
- Small adjustments: ±0.05 (5%)
- Medium adjustments: ±0.10 (10%)
- Large adjustments: ±0.20 (20%)

### 5. Document Diagram Types
Use clear, descriptive type names:
- Helps with organization
- Makes diagrams searchable
- Enables batch processing later

## Integration with Workbook Processing

### In EXTRACTED.md
Reference diagrams using relative paths:
```markdown
**Question 8**
Calculate the volume of the cone shown below.

![Cone diagram](../images/diagram_page08_cone.png)

**Answer**: 628 cm³
```

### In PRACTICE.md and VARIATIONS.md
Reuse extracted diagrams or reference generated variations:
```markdown
**Practice 5 (Type 1 - Different Numbers)**
Calculate the volume of the cone shown below.

![Cone diagram](../images/diagram_q5_var_cone6x15.png)
```

## Advanced Techniques

### Cropping Complex Layouts
For pages with mixed content (text + diagrams):
1. Extract each diagram separately
2. Use descriptive type names to distinguish
3. Reference diagrams individually in markdown

### Handling Rotated Diagrams
If diagram appears rotated on page:
1. Extract with appropriate coordinates
2. Rotate extracted image using ImageMagick if needed:
```bash
magick images/diagram_page10_triangle.png -rotate 90 images/diagram_page10_triangle.png
```

### Batch Extraction
For multiple similar diagrams:
1. Note coordinates for first diagram
2. If diagrams follow a pattern, script multiple extractions
3. Adjust coordinates incrementally for each

## Troubleshooting Checklist

Before reporting issues, verify:

- [ ] Page image file exists and is readable
- [ ] PIL (Pillow) package installed: `pip3 install Pillow`
- [ ] Coordinates are decimals (0.0-1.0), not percentages (0-100)
- [ ] All 6 parameters provided in correct order
- [ ] `images/` directory writable
- [ ] Source page image has sufficient resolution (≥150 DPI)

## Script Output Interpretation

Successful extraction shows:
```
✓ Diagram extracted: images/diagram_page08_cone.png
  - Type: cone
  - Size: 450x380 pixels
  - Region: 20-65% horizontal, 15-55% vertical
```

**Size**: Pixel dimensions of extracted diagram
**Region**: Confirmation of coordinate boundaries used
