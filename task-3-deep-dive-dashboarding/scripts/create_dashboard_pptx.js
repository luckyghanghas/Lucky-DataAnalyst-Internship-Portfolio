const fs = require("fs");
const path = require("path");

let pptxgen;
try {
  pptxgen = require("pptxgenjs");
} catch {
  pptxgen = require("C:/Users/lucky/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/.pnpm/pptxgenjs@4.0.1/node_modules/pptxgenjs");
}

const ROOT = path.resolve(__dirname, "..");
const DATA_PATH = path.join(ROOT, "data", "sales_transactions_cleaned.csv");
const OUTPUT_PATH = path.join(ROOT, "dashboard", "retail_sales_dashboard.pptx");

function parseCsvLine(line) {
  const cells = [];
  let current = "";
  let quoted = false;
  for (let i = 0; i < line.length; i += 1) {
    const ch = line[i];
    if (ch === '"') {
      quoted = !quoted;
    } else if (ch === "," && !quoted) {
      cells.push(current);
      current = "";
    } else {
      current += ch;
    }
  }
  cells.push(current);
  return cells;
}

function readCsv(filePath) {
  const lines = fs.readFileSync(filePath, "utf8").trim().split(/\r?\n/);
  const headers = parseCsvLine(lines[0]);
  return lines.slice(1).map((line) => {
    const cells = parseCsvLine(line);
    return Object.fromEntries(headers.map((header, idx) => [header, cells[idx]]));
  });
}

function sum(rows, key) {
  return rows.reduce((total, row) => total + Number(row[key] || 0), 0);
}

function group(rows, key) {
  const out = new Map();
  rows.forEach((row) => {
    const name = row[key];
    if (!out.has(name)) out.set(name, []);
    out.get(name).push(row);
  });
  return [...out.entries()].map(([name, items]) => ({ name, rows: items }));
}

function money(value) {
  return `$${Math.round(value).toLocaleString("en-US")}`;
}

function pct(value) {
  return `${(value * 100).toFixed(1)}%`;
}

function addTitle(slide, title, subtitle) {
  slide.addText(title, {
    x: 0.45,
    y: 0.28,
    w: 8.4,
    h: 0.35,
    fontFace: "Aptos Display",
    fontSize: 20,
    bold: true,
    color: "17343A",
    margin: 0,
  });
  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.45,
      y: 0.66,
      w: 8.9,
      h: 0.25,
      fontFace: "Aptos",
      fontSize: 8.5,
      color: "66736D",
      margin: 0,
    });
  }
  slide.addShape(pptx.ShapeType.line, {
    x: 0.45,
    y: 0.98,
    w: 12.4,
    h: 0,
    line: { color: "D9DED8", width: 1 },
  });
}

function addKpi(slide, x, y, label, value, accent) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x,
    y,
    w: 2.35,
    h: 0.92,
    rectRadius: 0.08,
    fill: { color: "FFFFFF" },
    line: { color: "D9DED8", width: 1 },
  });
  slide.addShape(pptx.ShapeType.rect, {
    x,
    y,
    w: 0.07,
    h: 0.92,
    fill: { color: accent },
    line: { color: accent },
  });
  slide.addText(label, {
    x: x + 0.18,
    y: y + 0.14,
    w: 1.9,
    h: 0.2,
    fontSize: 7.5,
    color: "66736D",
    margin: 0,
  });
  slide.addText(value, {
    x: x + 0.18,
    y: y + 0.43,
    w: 1.95,
    h: 0.32,
    fontSize: 18,
    bold: true,
    color: "172126",
    margin: 0,
    fit: "shrink",
  });
}

function addBarChart(slide, title, data, x, y, w, h, color, valueFormatter = money) {
  slide.addText(title, {
    x,
    y,
    w,
    h: 0.25,
    fontSize: 12,
    bold: true,
    color: "172126",
    margin: 0,
  });
  const maxValue = Math.max(...data.map((item) => item.value));
  const rowH = (h - 0.42) / data.length;
  data.forEach((item, idx) => {
    const rowY = y + 0.43 + idx * rowH;
    const barW = (w - 1.55) * item.value / maxValue;
    slide.addText(item.name, {
      x,
      y: rowY + 0.03,
      w: 1.2,
      h: 0.18,
      fontSize: 7.2,
      color: "40504A",
      margin: 0,
      fit: "shrink",
    });
    slide.addShape(pptx.ShapeType.roundRect, {
      x: x + 1.25,
      y: rowY,
      w: Math.max(barW, 0.08),
      h: 0.16,
      rectRadius: 0.04,
      fill: { color },
      line: { color },
    });
    slide.addText(valueFormatter(item.value), {
      x: x + 1.25 + barW + 0.08,
      y: rowY - 0.01,
      w: 0.75,
      h: 0.18,
      fontSize: 6.8,
      color: "66736D",
      margin: 0,
      fit: "shrink",
    });
  });
}

function addPanel(slide, x, y, w, h) {
  slide.addShape(pptx.ShapeType.roundRect, {
    x,
    y,
    w,
    h,
    rectRadius: 0.06,
    fill: { color: "FFFFFF" },
    line: { color: "DDE2DC", width: 1 },
  });
}

const rows = readCsv(DATA_PATH);
const revenue = sum(rows, "revenue");
const grossProfit = sum(rows, "gross_profit");
const orders = rows.length;
const aov = revenue / orders;
const returnRate = sum(rows, "returned_flag") / orders;
const rating = sum(rows, "customer_rating") / orders;

const channels = group(rows, "sales_channel")
  .map((g) => ({ name: g.name, value: sum(g.rows, "revenue"), orders: g.rows.length }))
  .sort((a, b) => b.value - a.value);
const categories = group(rows, "category")
  .map((g) => ({ name: g.name, value: sum(g.rows, "revenue"), returnRate: sum(g.rows, "returned_flag") / g.rows.length }))
  .sort((a, b) => b.value - a.value);
const regions = group(rows, "region")
  .map((g) => ({ name: g.name, value: sum(g.rows, "returned_flag") / g.rows.length, orders: g.rows.length }))
  .sort((a, b) => b.value - a.value);
const monthly = group(rows, "month")
  .map((g) => ({ name: g.name, value: sum(g.rows, "revenue") }))
  .sort((a, b) => a.name.localeCompare(b.name))
  .slice(-8);

const pptx = new pptxgen();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "luckyghanghas";
pptx.subject = "Task 3 Data Analytics Dashboard";
pptx.title = "Retail Sales Dashboard";
pptx.company = "ApexPlanet Data Analytics Internship";
pptx.lang = "en-US";
pptx.theme = {
  headFontFace: "Aptos Display",
  bodyFontFace: "Aptos",
  lang: "en-US",
};
pptx.defineLayout({ name: "LAYOUT_WIDE", width: 13.333, height: 7.5 });

const slide1 = pptx.addSlide();
slide1.background = { color: "F6F7F4" };
addTitle(slide1, "Retail Sales Performance Dashboard", "Task 3 - KPI dashboard built from cleaned sales transaction data");
addKpi(slide1, 0.48, 1.25, "Revenue", money(revenue), "2F6F73");
addKpi(slide1, 2.98, 1.25, "Orders", orders.toLocaleString("en-US"), "A35C2D");
addKpi(slide1, 5.48, 1.25, "AOV", money(aov), "5368A6");
addKpi(slide1, 7.98, 1.25, "Gross Margin", pct(grossProfit / revenue), "789262");
addKpi(slide1, 10.48, 1.25, "Return Rate", pct(returnRate), "B74D4A");
addPanel(slide1, 0.48, 2.45, 5.9, 3.95);
addPanel(slide1, 6.62, 2.45, 6.25, 3.95);
addBarChart(slide1, "Revenue by Sales Channel", channels, 0.78, 2.78, 5.25, 2.55, "2F6F73");
addBarChart(slide1, "Recent Monthly Revenue Trend", monthly, 6.92, 2.78, 5.5, 2.95, "5368A6");
slide1.addText("Decision signal: Website leads revenue, while Mobile App is close enough to justify retention investment.", {
  x: 0.78,
  y: 5.78,
  w: 5.2,
  h: 0.28,
  fontSize: 8.5,
  color: "40504A",
  margin: 0,
});
slide1.addText(`Customer satisfaction average: ${rating.toFixed(2)} / 5`, {
  x: 6.92,
  y: 5.95,
  w: 5.1,
  h: 0.28,
  fontSize: 8.5,
  color: "40504A",
  margin: 0,
});

const slide2 = pptx.addSlide();
slide2.background = { color: "F6F7F4" };
addTitle(slide2, "Channel and Category Deep Dive", "Where the business should focus next");
addPanel(slide2, 0.55, 1.25, 5.95, 4.85);
addPanel(slide2, 6.83, 1.25, 5.95, 4.85);
addBarChart(slide2, "Category Revenue", categories, 0.86, 1.62, 5.25, 2.75, "2F6F73");
addBarChart(slide2, "Return Rate by Region", regions.map((r) => ({ name: r.name, value: r.value })), 7.14, 1.62, 5.25, 2.75, "B74D4A", pct);
slide2.addText("Category note", { x: 0.86, y: 4.75, w: 1.2, h: 0.2, fontSize: 8, bold: true, color: "172126", margin: 0 });
slide2.addText("Accessories and Wearables provide strong revenue pools. Audio needs extra product education because return risk is higher.", {
  x: 0.86,
  y: 5.0,
  w: 5.0,
  h: 0.48,
  fontSize: 8.5,
  color: "40504A",
  margin: 0,
  fit: "shrink",
});
slide2.addText("Region note", { x: 7.14, y: 4.75, w: 1.1, h: 0.2, fontSize: 8, bold: true, color: "172126", margin: 0 });
slide2.addText("South has the highest return rate. Review delivery timing, product mix, and expectations in this region first.", {
  x: 7.14,
  y: 5.0,
  w: 5.0,
  h: 0.48,
  fontSize: 8.5,
  color: "40504A",
  margin: 0,
  fit: "shrink",
});

const slide3 = pptx.addSlide();
slide3.background = { color: "17343A" };
slide3.addText("Dashboard Recommendations", {
  x: 0.62,
  y: 0.48,
  w: 8.8,
  h: 0.48,
  fontFace: "Aptos Display",
  fontSize: 24,
  bold: true,
  color: "FFFFFF",
  margin: 0,
});
const recs = [
  ["Invest in digital retention", "Website is the largest revenue driver and Mobile App is close behind, so loyalty campaigns should prioritize both digital channels."],
  ["Reduce category return risk", "Audio and high-return regions need better product detail pages, clearer expectations, and faster support loops."],
  ["Track profit and experience together", "Revenue alone is not enough. Weekly leadership reporting should pair revenue with gross margin, return rate, and rating."],
];
recs.forEach((rec, idx) => {
  const y = 1.45 + idx * 1.55;
  slide3.addShape(pptx.ShapeType.roundRect, {
    x: 0.75,
    y,
    w: 11.8,
    h: 1.05,
    rectRadius: 0.08,
    fill: { color: idx === 0 ? "FFFFFF" : idx === 1 ? "EAF1EE" : "F4E8DD" },
    line: { color: "FFFFFF", transparency: 100 },
  });
  slide3.addText(String(idx + 1).padStart(2, "0"), {
    x: 1.05,
    y: y + 0.22,
    w: 0.55,
    h: 0.3,
    fontSize: 15,
    bold: true,
    color: "A35C2D",
    margin: 0,
  });
  slide3.addText(rec[0], {
    x: 1.75,
    y: y + 0.18,
    w: 3.2,
    h: 0.28,
    fontSize: 13,
    bold: true,
    color: "172126",
    margin: 0,
  });
  slide3.addText(rec[1], {
    x: 5.2,
    y: y + 0.18,
    w: 6.7,
    h: 0.52,
    fontSize: 9.2,
    color: "40504A",
    margin: 0,
    fit: "shrink",
  });
});
slide3.addText("Prepared for Task 3 - Deep-Dive Analysis & Interactive Dashboarding", {
  x: 0.75,
  y: 6.82,
  w: 7.0,
  h: 0.22,
  fontSize: 8.5,
  color: "C8D6D1",
  margin: 0,
});

fs.mkdirSync(path.dirname(OUTPUT_PATH), { recursive: true });
pptx.writeFile({ fileName: OUTPUT_PATH });
console.log(`Dashboard PPTX written to ${OUTPUT_PATH}`);
