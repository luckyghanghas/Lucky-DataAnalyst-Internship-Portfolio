"""
Sales Dashboard Mockup — fully formatted Excel with embedded charts.
Fixes: proper chart placement, no overlaps, clean spacing, correct column widths.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, PieChart, LineChart, Reference
from openpyxl.chart.series import DataPoint
from openpyxl.utils import get_column_letter

wb = Workbook()

# ── Palette ─────────────────────────────────────────────────────────────────
DARK_NAVY  = "0D1B2A"
TEAL_HDR   = "1B6CA8"
TEAL2      = "2F6F73"
PURPLE     = "5368A6"
ORANGE     = "C06000"
GREEN      = "1A7A4A"
RED        = "C0392B"
SLATE      = "4A5568"
LIGHT_ROW  = "EEF2F7"
WHITE      = "FFFFFF"
YELLOW_KPI = "F6C90E"

# ── Helpers ──────────────────────────────────────────────────────────────────

def set_title_row(ws, row, text, col_span, bg=DARK_NAVY, fg=WHITE, height=30, size=14):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=col_span)
    c = ws.cell(row=row, column=1, value=text)
    c.font      = Font(bold=True, color=fg, size=size, name="Calibri")
    c.fill      = PatternFill("solid", fgColor=bg)
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[row].height = height

def set_section_hdr(ws, row, col, text, span, bg=TEAL_HDR, fg=WHITE, height=20):
    ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col+span-1)
    c = ws.cell(row=row, column=col, value=text)
    c.font      = Font(bold=True, color=fg, size=11, name="Calibri")
    c.fill      = PatternFill("solid", fgColor=bg)
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[row].height = height

def set_col_hdr(ws, row, col, text, bg=TEAL2, fg=WHITE):
    c = ws.cell(row=row, column=col, value=text)
    c.font      = Font(bold=True, color=fg, size=9, name="Calibri")
    c.fill      = PatternFill("solid", fgColor=bg)
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin = Side(style="thin", color="AAAAAA")
    c.border    = Border(bottom=thin, right=thin)
    ws.row_dimensions[row].height = 28

def set_data(ws, row, col, value, align="left", fmt=None, bold=False, bg=None):
    c = ws.cell(row=row, column=col, value=value)
    c.font      = Font(bold=bold, color="111111", size=10, name="Calibri")
    c.alignment = Alignment(horizontal=align, vertical="center")
    if fmt:
        c.number_format = fmt
    thin = Side(style="thin", color="DDDDDD")
    c.border = Border(bottom=thin, right=Side(style="thin", color="EEEEEE"))
    if bg:
        c.fill = PatternFill("solid", fgColor=bg)
    return c

def stripe(ws, row, cols_range, even):
    fill = PatternFill("solid", fgColor=LIGHT_ROW if even else WHITE)
    for col in cols_range:
        ws.cell(row=row, column=col).fill = fill

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 1 — Executive Dashboard
# ═══════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "Executive Dashboard"
ws1.sheet_view.showGridLines = False
ws1.sheet_view.zoomScale = 85

# Column widths
col_widths = {"A":22,"B":16,"C":14,"D":16,"E":14,
              "F":3, "G":22,"H":16,"I":14,"J":16,"K":14}
for col, w in col_widths.items():
    ws1.column_dimensions[col].width = w

# ── Row 1: Main Title ────────────────────────────────────────────────────────
set_title_row(ws1, 1, "SALES PERFORMANCE EXECUTIVE DASHBOARD", 11, height=34, size=15)
ws1.row_dimensions[2].height = 6   # spacer

# ── Rows 3–5: KPI Cards (5 KPIs across cols A–E, one per column) ────────────
kpis = [
    ("TOTAL REVENUE",    "$5,328,492",  TEAL2),
    ("TOTAL ORDERS",     "1,250",       PURPLE),
    ("AVG ORDER VALUE",  "$4,262.79",   ORANGE),
    ("GROSS MARGIN",     "20.32%",      GREEN),
    ("RETURN RATE",      "5.20%",       RED),
]
kpi_cols = [1, 2, 3, 4, 5]
for i, (label, value, color) in enumerate(kpis):
    col = kpi_cols[i]
    # label
    lc = ws1.cell(row=3, column=col, value=label)
    lc.font      = Font(bold=True, color=WHITE, size=8, name="Calibri")
    lc.fill      = PatternFill("solid", fgColor=color)
    lc.alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[3].height = 16
    # value
    vc = ws1.cell(row=4, column=col, value=value)
    vc.font      = Font(bold=True, color=WHITE, size=15, name="Calibri")
    vc.fill      = PatternFill("solid", fgColor=color)
    vc.alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[4].height = 32
    # bottom accent
    bc = ws1.cell(row=5, column=col, value="")
    bc.fill = PatternFill("solid", fgColor=YELLOW_KPI)
    ws1.row_dimensions[5].height = 4

ws1.row_dimensions[6].height = 10  # spacer

# ── Rows 7–17: Top Products (cols A–E) ──────────────────────────────────────
set_section_hdr(ws1, 7,  1, "  TOP PRODUCTS BY REVENUE", 5, bg=TEAL2)
prod_hdrs = ["Product Name","Revenue ($)","Orders","Avg Price ($)","Return %"]
for i, h in enumerate(prod_hdrs):
    set_col_hdr(ws1, 8, i+1, h, bg=SLATE)

products = [
    ("Smart Watch",          1368209.84, 152, 6042.26, 0.0724),
    ("Mechanical Keyboard",   899189.76, 156, 3499.89, 0.0128),
    ("Webcam Pro",            798137.50, 169, 3170.67, 0.0473),
    ("Bluetooth Headphones",  655422.34, 151, 2654.19, 0.0530),
    ("Portable Speaker",      600264.00, 157, 2208.11, 0.0764),
    ("USB-C Hub",             506903.56, 161, 1911.33, 0.0683),
    ("Laptop Stand",          296637.20, 143, 1307.75, 0.0490),
    ("Wireless Mouse",        203728.20, 161,  798.97, 0.0373),
]
for r, (name, rev, ord_, avg, ret) in enumerate(products):
    row = 9 + r
    stripe(ws1, row, range(1,6), r % 2 == 0)
    set_data(ws1, row, 1, name,  "left")
    set_data(ws1, row, 2, rev,   "right", '$#,##0.00')
    set_data(ws1, row, 3, ord_,  "right")
    set_data(ws1, row, 4, avg,   "right", '$#,##0.00')
    set_data(ws1, row, 5, ret,   "right", '0.00%')
    ws1.row_dimensions[row].height = 16

ws1.row_dimensions[17].height = 8  # spacer

# ── Rows 7–12: Revenue by Channel (cols G–K) ─────────────────────────────────
set_section_hdr(ws1, 7,  7, "  REVENUE BY SALES CHANNEL", 5, bg=ORANGE)
ch_hdrs = ["Channel","Revenue ($)","Orders","Gross Profit ($)","Margin %"]
for i, h in enumerate(ch_hdrs):
    set_col_hdr(ws1, 8, i+7, h, bg=SLATE)

channels = [
    ("Website",      2464279.62, 592, 488850.64, 0.1984),
    ("Mobile App",   2054498.79, 456, 441586.34, 0.2149),
    ("Retail Store",  809713.99, 202, 152312.33, 0.1881),
]
for r, (ch, rev, ord_, gp, margin) in enumerate(channels):
    row = 9 + r
    stripe(ws1, row, range(7,12), r % 2 == 0)
    set_data(ws1, row, 7,  ch,     "left")
    set_data(ws1, row, 8,  rev,    "right", '$#,##0.00')
    set_data(ws1, row, 9,  ord_,   "right")
    set_data(ws1, row, 10, gp,     "right", '$#,##0.00')
    set_data(ws1, row, 11, margin, "right", '0.00%')
    ws1.row_dimensions[row].height = 16

ws1.row_dimensions[12].height = 8  # spacer

# ── Rows 13–18: Region (cols A–E) ────────────────────────────────────────────
set_section_hdr(ws1, 13, 1, "  PERFORMANCE BY REGION", 5, bg=GREEN)
reg_hdrs = ["Region","Revenue ($)","Orders","Gross Profit ($)","Return %"]
for i, h in enumerate(reg_hdrs):
    set_col_hdr(ws1, 14, i+1, h, bg=SLATE)

regions = [
    ("West",  1451298.87, 339, 273233.41, 0.0383),
    ("South", 1301485.12, 320, 250426.93, 0.0719),
    ("North", 1288064.81, 299, 315503.55, 0.0569),
    ("East",  1287643.60, 292, 243585.42, 0.0411),
]
for r, (reg, rev, ord_, gp, ret) in enumerate(regions):
    row = 15 + r
    stripe(ws1, row, range(1,6), r % 2 == 0)
    set_data(ws1, row, 1, reg,  "left")
    set_data(ws1, row, 2, rev,  "right", '$#,##0.00')
    set_data(ws1, row, 3, ord_, "right")
    set_data(ws1, row, 4, gp,   "right", '$#,##0.00')
    set_data(ws1, row, 5, ret,  "right", '0.00%')
    ws1.row_dimensions[row].height = 16

ws1.row_dimensions[19].height = 8  # spacer

# ── Rows 13–20: Campaigns (cols G–K) ─────────────────────────────────────────
set_section_hdr(ws1, 13, 7, "  MARKETING CAMPAIGN SUMMARY", 5, bg=PURPLE)
camp_hdrs = ["Campaign","Revenue ($)","Orders","Gross Profit ($)","Margin %"]
for i, h in enumerate(camp_hdrs):
    set_col_hdr(ws1, 14, i+7, h, bg=SLATE)

campaigns = [
    ("Search Ads",   1034918.19, 219, 276020.30, 0.2667),
    ("Organic",       946146.16, 217, 198461.91, 0.2098),
    ("Referral",      904176.23, 205, 185194.66, 0.2048),
    ("Email Offer",   844455.76, 222, 117325.28, 0.1389),
    ("Influencer",    809556.17, 191, 158623.78, 0.1959),
    ("Festive Sale",  789239.89, 196, 147123.38, 0.1864),
]
for r, (camp, rev, ord_, gp, margin) in enumerate(campaigns):
    row = 15 + r
    stripe(ws1, row, range(7,12), r % 2 == 0)
    set_data(ws1, row, 7,  camp,   "left")
    set_data(ws1, row, 8,  rev,    "right", '$#,##0.00')
    set_data(ws1, row, 9,  ord_,   "right")
    set_data(ws1, row, 10, gp,     "right", '$#,##0.00')
    set_data(ws1, row, 11, margin, "right", '0.00%')
    ws1.row_dimensions[row].height = 16

# ── Row 22 onward: CHARTS ────────────────────────────────────────────────────
# Pie chart — Revenue by Channel  (A22)
pie1 = PieChart()
pie1.title  = "Revenue by Sales Channel"
pie1.style  = 26
pie1.width  = 14
pie1.height = 11
labels_ch = Reference(ws1, min_col=7,  min_row=9,  max_row=11)
values_ch = Reference(ws1, min_col=8,  min_row=8,  max_row=11)
pie1.add_data(values_ch, titles_from_data=True)
pie1.set_categories(labels_ch)
for i, color in enumerate([TEAL2, PURPLE, ORANGE]):
    pt = DataPoint(idx=i)
    pt.graphicalProperties.solidFill = color
    pie1.series[0].dPt.append(pt)
ws1.add_chart(pie1, "A22")

# Bar chart — Top Products  (G22)
bar_prod = BarChart()
bar_prod.type            = "bar"
bar_prod.title           = "Top 8 Products by Revenue ($)"
bar_prod.y_axis.title    = "Product"
bar_prod.x_axis.title    = "Revenue ($)"
bar_prod.style           = 26
bar_prod.width           = 20
bar_prod.height          = 13
cats_p = Reference(ws1, min_col=1, min_row=9,  max_row=16)
vals_p = Reference(ws1, min_col=2, min_row=8,  max_row=16)
bar_prod.add_data(vals_p, titles_from_data=True)
bar_prod.set_categories(cats_p)
bar_prod.series[0].graphicalProperties.solidFill      = TEAL2
bar_prod.series[0].graphicalProperties.line.solidFill = TEAL2
ws1.add_chart(bar_prod, "G22")

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 2 — Monthly Trend
# ═══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("Monthly Trend")
ws2.sheet_view.showGridLines = False
ws2.sheet_view.zoomScale = 85

for col, w in {"A":13,"B":18,"C":13,"D":18,"E":18,"F":15}.items():
    ws2.column_dimensions[col].width = w

set_title_row(ws2, 1, "MONTHLY SALES AND PROFIT TREND", 6, height=30, size=14)
ws2.row_dimensions[2].height = 6

trend_hdrs = ["Order Month","Total Revenue ($)","Orders",
              "Total Cost ($)","Gross Profit ($)","Profit Margin %"]
for i, h in enumerate(trend_hdrs):
    set_col_hdr(ws2, 3, i+1, h, bg=TEAL_HDR)

monthly = [
    ("2025-01", 414508.30, 101, 336284.42,  78223.88, 0.1887),
    ("2025-02", 381797.56,  84, 282834.36,  98963.20, 0.2592),
    ("2025-03", 253183.26,  80, 204061.76,  49121.50, 0.1940),
    ("2025-04", 361993.81,  88, 299647.47,  62346.34, 0.1722),
    ("2025-05", 332373.01,  86, 270547.12,  61825.89, 0.1860),
    ("2025-06", 373196.49,  77, 305755.34,  67441.15, 0.1807),
    ("2025-07", 397458.33,  88, 318768.70,  78689.63, 0.1980),
    ("2025-08", 334842.66,  94, 275722.86,  59119.80, 0.1766),
    ("2025-09", 345674.85,  77, 279138.65,  66536.20, 0.1925),
    ("2025-10", 364085.70,  77, 292943.39,  71142.31, 0.1954),
    ("2025-11", 330265.79,  84, 264816.02,  65449.77, 0.1982),
    ("2025-12", 326024.85,  87, 264659.61,  61365.24, 0.1882),
    ("2026-01", 441892.25,  89, 307375.01, 134517.24, 0.3044),
    ("2026-02", 388410.22,  74, 317467.41,  70942.81, 0.1826),
    ("2026-03", 282785.32,  64, 225720.97,  57064.35, 0.2018),
]
for r, row_data in enumerate(monthly):
    row = 4 + r
    stripe(ws2, row, range(1,7), r % 2 == 0)
    set_data(ws2, row, 1, row_data[0], "center")
    set_data(ws2, row, 2, row_data[1], "right", '$#,##0.00')
    set_data(ws2, row, 3, row_data[2], "right")
    set_data(ws2, row, 4, row_data[3], "right", '$#,##0.00')
    set_data(ws2, row, 5, row_data[4], "right", '$#,##0.00')
    set_data(ws2, row, 6, row_data[5], "right", '0.00%')
    ws2.row_dimensions[row].height = 16

# Total row
tr = 19
for col in range(1, 7):
    c = ws2.cell(row=tr, column=col)
    c.font = Font(bold=True, color=WHITE, size=10, name="Calibri")
    c.fill = PatternFill("solid", fgColor=DARK_NAVY)
    c.alignment = Alignment(horizontal="right" if col > 1 else "center", vertical="center")
ws2.cell(row=tr, column=1).value = "TOTAL"
ws2.cell(row=tr, column=2).value = 5328492.40;  ws2.cell(row=tr, column=2).number_format = '$#,##0.00'
ws2.cell(row=tr, column=3).value = 1250
ws2.cell(row=tr, column=4).value = 4245778.09;  ws2.cell(row=tr, column=4).number_format = '$#,##0.00'
ws2.cell(row=tr, column=5).value = 1082548.82;  ws2.cell(row=tr, column=5).number_format = '$#,##0.00'
ws2.cell(row=tr, column=6).value = 0.2032;      ws2.cell(row=tr, column=6).number_format = '0.00%'
ws2.row_dimensions[tr].height = 20

ws2.row_dimensions[20].height = 10  # spacer before charts

# Line chart — Revenue & Profit  (A21)
line1 = LineChart()
line1.title           = "Monthly Revenue vs Gross Profit (Jan 2025 – Mar 2026)"
line1.y_axis.title    = "Amount ($)"
line1.x_axis.title    = "Month"
line1.style           = 26
line1.width           = 28
line1.height          = 14
cats_l = Reference(ws2, min_col=1, min_row=4, max_row=18)
vals_r = Reference(ws2, min_col=2, min_row=3, max_row=18)
vals_g = Reference(ws2, min_col=5, min_row=3, max_row=18)
line1.add_data(vals_r, titles_from_data=True)
line1.add_data(vals_g, titles_from_data=True)
line1.set_categories(cats_l)
line1.series[0].graphicalProperties.line.solidFill = PURPLE
line1.series[0].graphicalProperties.line.width     = 28000
line1.series[1].graphicalProperties.line.solidFill = GREEN
line1.series[1].graphicalProperties.line.width     = 28000
ws2.add_chart(line1, "A21")

# Column chart — Monthly Orders  (A39)
bar_ord = BarChart()
bar_ord.type          = "col"
bar_ord.title         = "Monthly Order Count"
bar_ord.y_axis.title  = "Orders"
bar_ord.x_axis.title  = "Month"
bar_ord.style         = 26
bar_ord.width         = 28
bar_ord.height        = 12
cats_o = Reference(ws2, min_col=1, min_row=4, max_row=18)
vals_o = Reference(ws2, min_col=3, min_row=3, max_row=18)
bar_ord.add_data(vals_o, titles_from_data=True)
bar_ord.set_categories(cats_o)
bar_ord.series[0].graphicalProperties.solidFill      = ORANGE
bar_ord.series[0].graphicalProperties.line.solidFill = ORANGE
ws2.add_chart(bar_ord, "A39")

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 3 — Category & Segments
# ═══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("Category & Segments")
ws3.sheet_view.showGridLines = False
ws3.sheet_view.zoomScale = 85

for col, w in {"A":16,"B":17,"C":12,"D":16,"E":17,"F":14,
               "G":3,"H":13,"I":17,"J":12,"K":17}.items():
    ws3.column_dimensions[col].width = w

set_title_row(ws3, 1, "CATEGORY & SEGMENT BREAKDOWNS", 11, height=30, size=14)
ws3.row_dimensions[2].height = 6

# Category table  (cols A–F)
set_section_hdr(ws3, 3, 1, "  SALES BY PRODUCT CATEGORY", 6, bg=TEAL2)
cat_hdrs = ["Category","Revenue ($)","Orders","Avg Price ($)","Gross Profit ($)","Margin %"]
for i, h in enumerate(cat_hdrs):
    set_col_hdr(ws3, 4, i+1, h, bg=SLATE)

categories = [
    ("Accessories", 1609821.52, 478, 2055.11, 345746.17, 0.2148),
    ("Wearables",   1368209.84, 152, 6042.26, 208448.69, 0.1524),
    ("Audio",       1255686.34, 308, 2426.80, 264390.68, 0.2106),
    ("Office",      1094774.70, 312, 2316.83, 264163.77, 0.2413),
]
for r, (cat, rev, ord_, avg, gp, margin) in enumerate(categories):
    row = 5 + r
    stripe(ws3, row, range(1,7), r % 2 == 0)
    set_data(ws3, row, 1, cat)
    set_data(ws3, row, 2, rev,    "right", '$#,##0.00')
    set_data(ws3, row, 3, ord_,   "right")
    set_data(ws3, row, 4, avg,    "right", '$#,##0.00')
    set_data(ws3, row, 5, gp,     "right", '$#,##0.00')
    set_data(ws3, row, 6, margin, "right", '0.00%')
    ws3.row_dimensions[row].height = 16

# Segment table  (cols H–K)
set_section_hdr(ws3, 3, 8, "  SALES BY CUSTOMER SEGMENT", 4, bg=PURPLE)
seg_hdrs = ["Age Group","Revenue ($)","Orders","Rev/Customer ($)"]
for i, h in enumerate(seg_hdrs):
    set_col_hdr(ws3, 4, i+8, h, bg=SLATE)

segments = [
    ("18-24", 884965.42,  210, 5746.53),
    ("25-34", 1032052.93, 246, 5639.63),
    ("35-44", 1206867.84, 268, 6004.32),
    ("45-54", 1059588.09, 267, 5271.58),
    ("55+",   1145018.12, 259, 6222.92),
]
for r, (age, rev, ord_, rpc) in enumerate(segments):
    row = 5 + r
    stripe(ws3, row, range(8,12), r % 2 == 0)
    set_data(ws3, row, 8,  age,  "center")
    set_data(ws3, row, 9,  rev,  "right", '$#,##0.00')
    set_data(ws3, row, 10, ord_, "right")
    set_data(ws3, row, 11, rpc,  "right", '$#,##0.00')
    ws3.row_dimensions[row].height = 16

ws3.row_dimensions[10].height = 10  # spacer before charts

# Bar chart — Category Revenue  (A11)
bar_cat = BarChart()
bar_cat.type          = "col"
bar_cat.title         = "Revenue by Product Category ($)"
bar_cat.y_axis.title  = "Revenue ($)"
bar_cat.style         = 26
bar_cat.width         = 18
bar_cat.height        = 12
cats_c = Reference(ws3, min_col=1, min_row=5, max_row=8)
vals_c = Reference(ws3, min_col=2, min_row=4, max_row=8)
bar_cat.add_data(vals_c, titles_from_data=True)
bar_cat.set_categories(cats_c)
bar_cat.series[0].graphicalProperties.solidFill      = TEAL2
bar_cat.series[0].graphicalProperties.line.solidFill = TEAL2
ws3.add_chart(bar_cat, "A11")

# Pie chart — Category Share  (A28)
pie_cat = PieChart()
pie_cat.title  = "Category Revenue Share"
pie_cat.style  = 26
pie_cat.width  = 14
pie_cat.height = 11
labels_c = Reference(ws3, min_col=1, min_row=5, max_row=8)
values_c = Reference(ws3, min_col=2, min_row=4, max_row=8)
pie_cat.add_data(values_c, titles_from_data=True)
pie_cat.set_categories(labels_c)
for i, color in enumerate([TEAL2, PURPLE, ORANGE, GREEN]):
    pt = DataPoint(idx=i)
    pt.graphicalProperties.solidFill = color
    pie_cat.series[0].dPt.append(pt)
ws3.add_chart(pie_cat, "A28")

# Bar chart — Rev per Customer by Age  (H11)
bar_seg = BarChart()
bar_seg.type          = "col"
bar_seg.title         = "Revenue per Customer by Age Group ($)"
bar_seg.y_axis.title  = "Revenue / Customer ($)"
bar_seg.style         = 26
bar_seg.width         = 18
bar_seg.height        = 12
cats_s = Reference(ws3, min_col=8,  min_row=5, max_row=9)
vals_s = Reference(ws3, min_col=11, min_row=4, max_row=9)
bar_seg.add_data(vals_s, titles_from_data=True)
bar_seg.set_categories(cats_s)
bar_seg.series[0].graphicalProperties.solidFill      = PURPLE
bar_seg.series[0].graphicalProperties.line.solidFill = PURPLE
ws3.add_chart(bar_seg, "H11")

# Bar chart — Revenue by Age  (H28)
bar_age = BarChart()
bar_age.type          = "col"
bar_age.title         = "Total Revenue by Age Group ($)"
bar_age.y_axis.title  = "Revenue ($)"
bar_age.style         = 26
bar_age.width         = 18
bar_age.height        = 11
cats_a = Reference(ws3, min_col=8, min_row=5, max_row=9)
vals_a = Reference(ws3, min_col=9, min_row=4, max_row=9)
bar_age.add_data(vals_a, titles_from_data=True)
bar_age.set_categories(cats_a)
bar_age.series[0].graphicalProperties.solidFill      = GREEN
bar_age.series[0].graphicalProperties.line.solidFill = GREEN
ws3.add_chart(bar_age, "H28")

# ── Save ──────────────────────────────────────────────────────────────────────
out = r"c:\Users\lucky\Downloads\Lucky-DataAnalyst-Internship-Portfolio\task-2-eda-business-intelligence\sales_dashboard_mockup.xlsx"
wb.save(out)
print(f"Saved → {out}")
