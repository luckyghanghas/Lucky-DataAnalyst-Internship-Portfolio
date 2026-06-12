"""
Sales Dashboard Mockup — clean Excel with correct number formatting and proper layout.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, PieChart, LineChart, Reference
from openpyxl.chart.series import DataPoint
from openpyxl.utils import get_column_letter

wb = Workbook()

# ── Palette ──────────────────────────────────────────────────────────────────
DARK_NAVY  = "0D1B2A"
TEAL       = "1B6CA8"
TEAL2      = "2F6F73"
PURPLE     = "5368A6"
ORANGE     = "C06000"
GREEN      = "1A7A4A"
RED        = "C0392B"
SLATE      = "455A64"
LIGHT_ROW  = "EEF2F7"
WHITE      = "FFFFFF"
GOLD       = "F9A825"

# ── Number formats (US standard, no Indian grouping) ─────────────────────────
FMT_USD    = '#,##0.00'          # $2,464,279.62
FMT_USD2   = '#,##0'             # $5,328,492
FMT_PCT    = '0.00%'
FMT_INT    = '#,##0'

# ── Style helpers ─────────────────────────────────────────────────────────────
def title_row(ws, row, text, span, bg=DARK_NAVY, fg=WHITE, size=14, height=32):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span)
    c = ws.cell(row=row, column=1, value=text)
    c.font      = Font(bold=True, color=fg, size=size, name="Calibri")
    c.fill      = PatternFill("solid", fgColor=bg)
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[row].height = height

def sec_hdr(ws, row, col, text, span, bg=TEAL2, fg=WHITE, height=20):
    ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col+span-1)
    c = ws.cell(row=row, column=col, value=text)
    c.font      = Font(bold=True, color=fg, size=10, name="Calibri")
    c.fill      = PatternFill("solid", fgColor=bg)
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[row].height = height

def col_hdr(ws, row, col, text, bg=SLATE, fg=WHITE):
    c = ws.cell(row=row, column=col, value=text)
    c.font      = Font(bold=True, color=fg, size=9, name="Calibri")
    c.fill      = PatternFill("solid", fgColor=bg)
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin = Side(style="thin", color="AAAAAA")
    c.border    = Border(bottom=thin, right=thin, left=thin, top=thin)
    ws.row_dimensions[row].height = 24

def cell(ws, row, col, value, align="left", fmt=None, bold=False, bg=None, fg="111111"):
    c = ws.cell(row=row, column=col, value=value)
    c.font      = Font(bold=bold, color=fg, size=10, name="Calibri")
    c.alignment = Alignment(horizontal=align, vertical="center")
    if fmt:
        c.number_format = fmt
    thin = Side(style="thin", color="DDDDDD")
    c.border    = Border(bottom=thin, right=thin)
    if bg:
        c.fill = PatternFill("solid", fgColor=bg)
    return c

def stripe(ws, row, cols, even):
    bg = LIGHT_ROW if even else WHITE
    for col in cols:
        if not ws.cell(row=row, column=col).fill.fgColor.rgb not in (bg,):
            ws.cell(row=row, column=col).fill = PatternFill("solid", fgColor=bg)

def kpi_block(ws, row_lbl, row_val, col, label, value, bg):
    # label cell
    lc = ws.cell(row=row_lbl, column=col, value=label)
    lc.font      = Font(bold=True, color=WHITE, size=8, name="Calibri")
    lc.fill      = PatternFill("solid", fgColor=bg)
    lc.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.merge_cells(start_row=row_lbl, start_column=col, end_row=row_lbl, end_column=col+1)
    # value cell
    vc = ws.cell(row=row_val, column=col, value=value)
    vc.font      = Font(bold=True, color=WHITE, size=16, name="Calibri")
    vc.fill      = PatternFill("solid", fgColor=bg)
    vc.alignment = Alignment(horizontal="center", vertical="center")
    ws.merge_cells(start_row=row_val, start_column=col, end_row=row_val, end_column=col+1)
    # gold accent bar
    ac = ws.cell(row=row_val+1, column=col, value="")
    ac.fill = PatternFill("solid", fgColor=GOLD)
    ws.merge_cells(start_row=row_val+1, start_column=col, end_row=row_val+1, end_column=col+1)

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 1 — Executive Dashboard
# Layout: cols A-J (10 cols)
#   A-E  = left panel (Products, Region)
#   F    = spacer (width=2)
#   G-K  = right panel (Channel, Campaign)
# ═══════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "Executive Dashboard"
ws1.sheet_view.showGridLines = False
ws1.sheet_view.zoomScale = 90

# Column widths — carefully sized so numbers don't get cut
ws1.column_dimensions["A"].width = 22   # product name
ws1.column_dimensions["B"].width = 15   # revenue
ws1.column_dimensions["C"].width = 8    # orders
ws1.column_dimensions["D"].width = 14   # avg price
ws1.column_dimensions["E"].width = 10   # return %
ws1.column_dimensions["F"].width = 2    # spacer
ws1.column_dimensions["G"].width = 14   # channel/campaign
ws1.column_dimensions["H"].width = 15   # revenue
ws1.column_dimensions["I"].width = 8    # orders
ws1.column_dimensions["J"].width = 15   # gross profit
ws1.column_dimensions["K"].width = 10   # margin %

# ── Row 1: Main title ────────────────────────────────────────────────────────
title_row(ws1, 1, "SALES PERFORMANCE EXECUTIVE DASHBOARD", 11, height=34, size=15)
ws1.row_dimensions[2].height = 5   # spacer

# ── Rows 3–5: KPI cards (5 KPIs) ─────────────────────────────────────────────
ws1.row_dimensions[3].height = 16
ws1.row_dimensions[4].height = 34
ws1.row_dimensions[5].height = 5

kpis = [
    (1,  "TOTAL REVENUE",   "$5,328,492",  TEAL2),
    (3,  "TOTAL ORDERS",    "1,250",       PURPLE),
    (5,  "AVG ORDER VALUE", "$4,262.79",   ORANGE),
    (7,  "GROSS MARGIN",    "20.32%",      GREEN),
    (9,  "RETURN RATE",     "5.20%",       RED),
]
for col, label, value, bg in kpis:
    kpi_block(ws1, 3, 4, col, label, value, bg)

ws1.row_dimensions[6].height = 8  # spacer before tables

# ── Rows 7–17: TOP PRODUCTS (cols A–E) ───────────────────────────────────────
sec_hdr(ws1, 7, 1, "  TOP PRODUCTS BY REVENUE", 5, bg=TEAL2)
for i, h in enumerate(["Product Name", "Revenue ($)", "Orders", "Avg Price ($)", "Return %"]):
    col_hdr(ws1, 8, i+1, h)

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
    bg  = LIGHT_ROW if r % 2 == 0 else WHITE
    ws1.row_dimensions[row].height = 15
    cell(ws1, row, 1, name,  "left",   bg=bg)
    cell(ws1, row, 2, rev,   "right",  FMT_USD,  bg=bg)
    cell(ws1, row, 3, ord_,  "center", FMT_INT,  bg=bg)
    cell(ws1, row, 4, avg,   "right",  FMT_USD,  bg=bg)
    cell(ws1, row, 5, ret,   "center", FMT_PCT,  bg=bg)

ws1.row_dimensions[17].height = 8  # spacer

# ── Rows 7–12: REVENUE BY CHANNEL (cols G–K) ─────────────────────────────────
sec_hdr(ws1, 7, 7, "  REVENUE BY SALES CHANNEL", 5, bg=ORANGE)
for i, h in enumerate(["Channel", "Revenue ($)", "Orders", "Gross Profit ($)", "Margin %"]):
    col_hdr(ws1, 8, i+7, h)

channels = [
    ("Website",      2464279.62, 592, 488850.64, 0.1984),
    ("Mobile App",   2054498.79, 456, 441586.34, 0.2149),
    ("Retail Store",  809713.99, 202, 152312.33, 0.1881),
]
for r, (ch, rev, ord_, gp, margin) in enumerate(channels):
    row = 9 + r
    bg  = LIGHT_ROW if r % 2 == 0 else WHITE
    ws1.row_dimensions[row].height = 15
    cell(ws1, row, 7,  ch,     "left",   bg=bg)
    cell(ws1, row, 8,  rev,    "right",  FMT_USD, bg=bg)
    cell(ws1, row, 9,  ord_,   "center", FMT_INT, bg=bg)
    cell(ws1, row, 10, gp,     "right",  FMT_USD, bg=bg)
    cell(ws1, row, 11, margin, "center", FMT_PCT, bg=bg)

ws1.row_dimensions[12].height = 8  # spacer

# ── Rows 18–23: PERFORMANCE BY REGION (cols A–E) ─────────────────────────────
sec_hdr(ws1, 18, 1, "  PERFORMANCE BY REGION", 5, bg=GREEN)
for i, h in enumerate(["Region", "Revenue ($)", "Orders", "Gross Profit ($)", "Return %"]):
    col_hdr(ws1, 19, i+1, h)

regions = [
    ("West",  1451298.87, 339, 273233.41, 0.0383),
    ("South", 1301485.12, 320, 250426.93, 0.0719),
    ("North", 1288064.81, 299, 315503.55, 0.0569),
    ("East",  1287643.60, 292, 243585.42, 0.0411),
]
for r, (reg, rev, ord_, gp, ret) in enumerate(regions):
    row = 20 + r
    bg  = LIGHT_ROW if r % 2 == 0 else WHITE
    ws1.row_dimensions[row].height = 15
    cell(ws1, row, 1, reg,  "left",   bg=bg)
    cell(ws1, row, 2, rev,  "right",  FMT_USD, bg=bg)
    cell(ws1, row, 3, ord_, "center", FMT_INT, bg=bg)
    cell(ws1, row, 4, gp,   "right",  FMT_USD, bg=bg)
    cell(ws1, row, 5, ret,  "center", FMT_PCT, bg=bg)

ws1.row_dimensions[24].height = 8  # spacer

# ── Rows 13–20: MARKETING CAMPAIGN SUMMARY (cols G–K) ────────────────────────
sec_hdr(ws1, 13, 7, "  MARKETING CAMPAIGN SUMMARY", 5, bg=PURPLE)
for i, h in enumerate(["Campaign", "Revenue ($)", "Orders", "Gross Profit ($)", "Margin %"]):
    col_hdr(ws1, 14, i+7, h)

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
    bg  = LIGHT_ROW if r % 2 == 0 else WHITE
    ws1.row_dimensions[row].height = 15
    cell(ws1, row, 7,  camp,   "left",   bg=bg)
    cell(ws1, row, 8,  rev,    "right",  FMT_USD, bg=bg)
    cell(ws1, row, 9,  ord_,   "center", FMT_INT, bg=bg)
    cell(ws1, row, 10, gp,     "right",  FMT_USD, bg=bg)
    cell(ws1, row, 11, margin, "center", FMT_PCT, bg=bg)

# ── Row 25+: CHARTS ───────────────────────────────────────────────────────────
# Pie chart — Channel Revenue  placed at A25
pie1 = PieChart()
pie1.title  = "Revenue by Sales Channel"
pie1.style  = 10
pie1.width  = 14
pie1.height = 12
pie1.add_data(Reference(ws1, min_col=8, min_row=8, max_row=11), titles_from_data=True)
pie1.set_categories(Reference(ws1, min_col=7, min_row=9, max_row=11))
for i, color in enumerate([TEAL2, PURPLE, ORANGE]):
    pt = DataPoint(idx=i)
    pt.graphicalProperties.solidFill = color
    pie1.series[0].dPt.append(pt)
ws1.add_chart(pie1, "A25")

# Bar chart — Top Products  placed at G25
bar1 = BarChart()
bar1.type  = "bar"
bar1.title = "Top 8 Products by Revenue"
bar1.style = 10
bar1.width = 20
bar1.height = 13
bar1.add_data(Reference(ws1, min_col=2, min_row=8, max_row=16), titles_from_data=True)
bar1.set_categories(Reference(ws1, min_col=1, min_row=9, max_row=16))
bar1.series[0].graphicalProperties.solidFill      = TEAL2
bar1.series[0].graphicalProperties.line.solidFill = TEAL2
ws1.add_chart(bar1, "G25")

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 2 — Monthly Trend
# ═══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("Monthly Trend")
ws2.sheet_view.showGridLines = False
ws2.sheet_view.zoomScale = 90

for col, w in {"A":12,"B":18,"C":10,"D":18,"E":18,"F":14}.items():
    ws2.column_dimensions[col].width = w

title_row(ws2, 1, "MONTHLY SALES AND PROFIT TREND", 6, height=30)
ws2.row_dimensions[2].height = 5

for i, h in enumerate(["Order Month","Total Revenue ($)","Orders","Total Cost ($)","Gross Profit ($)","Profit Margin %"]):
    col_hdr(ws2, 3, i+1, h, bg=TEAL)

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
for r, d in enumerate(monthly):
    row = 4 + r
    bg  = LIGHT_ROW if r % 2 == 0 else WHITE
    ws2.row_dimensions[row].height = 15
    cell(ws2, row, 1, d[0], "center", bg=bg)
    cell(ws2, row, 2, d[1], "right",  FMT_USD, bg=bg)
    cell(ws2, row, 3, d[2], "center", FMT_INT, bg=bg)
    cell(ws2, row, 4, d[3], "right",  FMT_USD, bg=bg)
    cell(ws2, row, 5, d[4], "right",  FMT_USD, bg=bg)
    cell(ws2, row, 6, d[5], "center", FMT_PCT, bg=bg)

# Total row
tr = 19
ws2.row_dimensions[tr].height = 18
for col in range(1, 7):
    c = ws2.cell(row=tr, column=col)
    c.font      = Font(bold=True, color=WHITE, size=10, name="Calibri")
    c.fill      = PatternFill("solid", fgColor=DARK_NAVY)
    c.alignment = Alignment(horizontal="right" if col > 1 else "center", vertical="center")
ws2.cell(row=tr, column=1).value  = "TOTAL"
ws2.cell(row=tr, column=2).value  = 5328492.40;  ws2.cell(row=tr,column=2).number_format = FMT_USD
ws2.cell(row=tr, column=3).value  = 1250;         ws2.cell(row=tr,column=3).number_format = FMT_INT
ws2.cell(row=tr, column=4).value  = 4245778.09;  ws2.cell(row=tr,column=4).number_format = FMT_USD
ws2.cell(row=tr, column=5).value  = 1082548.82;  ws2.cell(row=tr,column=5).number_format = FMT_USD
ws2.cell(row=tr, column=6).value  = 0.2032;       ws2.cell(row=tr,column=6).number_format = FMT_PCT

ws2.row_dimensions[20].height = 8

# Line chart — Revenue vs Profit
line1 = LineChart()
line1.title          = "Monthly Revenue vs Gross Profit"
line1.y_axis.title   = "Amount ($)"
line1.x_axis.title   = "Month"
line1.style          = 10
line1.width          = 28
line1.height         = 14
line1.add_data(Reference(ws2, min_col=2, min_row=3, max_row=18), titles_from_data=True)
line1.add_data(Reference(ws2, min_col=5, min_row=3, max_row=18), titles_from_data=True)
line1.set_categories(Reference(ws2, min_col=1, min_row=4, max_row=18))
line1.series[0].graphicalProperties.line.solidFill = PURPLE
line1.series[0].graphicalProperties.line.width     = 25000
line1.series[1].graphicalProperties.line.solidFill = GREEN
line1.series[1].graphicalProperties.line.width     = 25000
ws2.add_chart(line1, "A21")

# Column chart — Order Count
bar2 = BarChart()
bar2.type          = "col"
bar2.title         = "Monthly Order Count"
bar2.y_axis.title  = "Orders"
bar2.x_axis.title  = "Month"
bar2.style         = 10
bar2.width         = 28
bar2.height        = 12
bar2.add_data(Reference(ws2, min_col=3, min_row=3, max_row=18), titles_from_data=True)
bar2.set_categories(Reference(ws2, min_col=1, min_row=4, max_row=18))
bar2.series[0].graphicalProperties.solidFill      = ORANGE
bar2.series[0].graphicalProperties.line.solidFill = ORANGE
ws2.add_chart(bar2, "A39")

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 3 — Category & Segments
# ═══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("Category & Segments")
ws3.sheet_view.showGridLines = False
ws3.sheet_view.zoomScale = 90

for col, w in {"A":14,"B":16,"C":9,"D":14,"E":16,"F":12,
               "G":2, "H":12,"I":16,"J":9,"K":16}.items():
    ws3.column_dimensions[col].width = w

title_row(ws3, 1, "CATEGORY & SEGMENT BREAKDOWNS", 11, height=30)
ws3.row_dimensions[2].height = 5

# Category table A–F
sec_hdr(ws3, 3, 1, "  SALES BY PRODUCT CATEGORY", 6, bg=TEAL2)
for i, h in enumerate(["Category","Revenue ($)","Orders","Avg Price ($)","Gross Profit ($)","Margin %"]):
    col_hdr(ws3, 4, i+1, h)

categories = [
    ("Accessories", 1609821.52, 478, 2055.11, 345746.17, 0.2148),
    ("Wearables",   1368209.84, 152, 6042.26, 208448.69, 0.1524),
    ("Audio",       1255686.34, 308, 2426.80, 264390.68, 0.2106),
    ("Office",      1094774.70, 312, 2316.83, 264163.77, 0.2413),
]
for r, (cat, rev, ord_, avg, gp, margin) in enumerate(categories):
    row = 5 + r
    bg  = LIGHT_ROW if r % 2 == 0 else WHITE
    ws3.row_dimensions[row].height = 15
    cell(ws3, row, 1, cat,    "left",   bg=bg)
    cell(ws3, row, 2, rev,    "right",  FMT_USD, bg=bg)
    cell(ws3, row, 3, ord_,   "center", FMT_INT, bg=bg)
    cell(ws3, row, 4, avg,    "right",  FMT_USD, bg=bg)
    cell(ws3, row, 5, gp,     "right",  FMT_USD, bg=bg)
    cell(ws3, row, 6, margin, "center", FMT_PCT, bg=bg)

# Segment table H–K
sec_hdr(ws3, 3, 8, "  SALES BY CUSTOMER SEGMENT", 4, bg=PURPLE)
for i, h in enumerate(["Age Group","Revenue ($)","Orders","Rev/Customer ($)"]):
    col_hdr(ws3, 4, i+8, h)

segments = [
    ("18-24", 884965.42,  210, 5746.53),
    ("25-34", 1032052.93, 246, 5639.63),
    ("35-44", 1206867.84, 268, 6004.32),
    ("45-54", 1059588.09, 267, 5271.58),
    ("55+",   1145018.12, 259, 6222.92),
]
for r, (age, rev, ord_, rpc) in enumerate(segments):
    row = 5 + r
    bg  = LIGHT_ROW if r % 2 == 0 else WHITE
    ws3.row_dimensions[row].height = 15
    cell(ws3, row, 8,  age,  "center", bg=bg)
    cell(ws3, row, 9,  rev,  "right",  FMT_USD, bg=bg)
    cell(ws3, row, 10, ord_, "center", FMT_INT, bg=bg)
    cell(ws3, row, 11, rpc,  "right",  FMT_USD, bg=bg)

ws3.row_dimensions[10].height = 8

# Bar chart — Category Revenue  A11
bar3 = BarChart()
bar3.type          = "col"
bar3.title         = "Revenue by Product Category ($)"
bar3.y_axis.title  = "Revenue ($)"
bar3.style         = 10
bar3.width         = 18
bar3.height        = 12
bar3.add_data(Reference(ws3, min_col=2, min_row=4, max_row=8), titles_from_data=True)
bar3.set_categories(Reference(ws3, min_col=1, min_row=5, max_row=8))
bar3.series[0].graphicalProperties.solidFill      = TEAL2
bar3.series[0].graphicalProperties.line.solidFill = TEAL2
ws3.add_chart(bar3, "A11")

# Pie chart — Category share  A28
pie2 = PieChart()
pie2.title  = "Category Revenue Share"
pie2.style  = 10
pie2.width  = 14
pie2.height = 11
pie2.add_data(Reference(ws3, min_col=2, min_row=4, max_row=8), titles_from_data=True)
pie2.set_categories(Reference(ws3, min_col=1, min_row=5, max_row=8))
for i, color in enumerate([TEAL2, PURPLE, ORANGE, GREEN]):
    pt = DataPoint(idx=i)
    pt.graphicalProperties.solidFill = color
    pie2.series[0].dPt.append(pt)
ws3.add_chart(pie2, "A28")

# Bar chart — Rev per Customer  H11
bar4 = BarChart()
bar4.type          = "col"
bar4.title         = "Revenue per Customer by Age Group"
bar4.y_axis.title  = "Revenue / Customer ($)"
bar4.style         = 10
bar4.width         = 18
bar4.height        = 12
bar4.add_data(Reference(ws3, min_col=11, min_row=4, max_row=9), titles_from_data=True)
bar4.set_categories(Reference(ws3, min_col=8, min_row=5, max_row=9))
bar4.series[0].graphicalProperties.solidFill      = PURPLE
bar4.series[0].graphicalProperties.line.solidFill = PURPLE
ws3.add_chart(bar4, "H11")

# Bar chart — Total Revenue by Age  H28
bar5 = BarChart()
bar5.type          = "col"
bar5.title         = "Total Revenue by Age Group ($)"
bar5.y_axis.title  = "Revenue ($)"
bar5.style         = 10
bar5.width         = 18
bar5.height        = 11
bar5.add_data(Reference(ws3, min_col=9, min_row=4, max_row=9), titles_from_data=True)
bar5.set_categories(Reference(ws3, min_col=8, min_row=5, max_row=9))
bar5.series[0].graphicalProperties.solidFill      = GREEN
bar5.series[0].graphicalProperties.line.solidFill = GREEN
ws3.add_chart(bar5, "H28")

# ── Save ──────────────────────────────────────────────────────────────────────
out = r"c:\Users\lucky\Downloads\Lucky-DataAnalyst-Internship-Portfolio\task-2-eda-business-intelligence\sales_dashboard_mockup.xlsx"
wb.save(out)
print(f"Saved → {out}")
