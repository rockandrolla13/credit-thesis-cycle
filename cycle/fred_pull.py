"""Pull market readings from FRED. No key, no model. Usage: fred_pull.py <out.json>"""
import csv
import datetime
import io
import json
import statistics
import sys
import subprocess

SERIES = {"IG": "BAMLC0A0CM", "AAA": "BAMLC0A1CAAA", "AA": "BAMLC0A2CAA", "A": "BAMLC0A3CA", "BBB": "BAMLC0A4CBBB",
          "HY": "BAMLH0A0HYM2", "BB": "BAMLH0A1HYBB", "B": "BAMLH0A2HYB", "CCC": "BAMLH0A3HYC",
          "fed_upper": "DFEDTARU", "ust2y": "DGS2", "ust10y": "DGS10", "vix": "VIXCLS",
          "breakeven10y": "T10YIE", "wti": "DCOILWTICO", "sp500": "SP500", "sloos_large": "DRTSCILM"}
START = (datetime.date.today() - datetime.timedelta(days=3 * 365)).isoformat()


def load(sid):
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd={START}"
    # curl, not urllib: FRED drops requests that carry an unusual client name.
    text = subprocess.run(["/usr/bin/curl", "-s", "-f", "-m", "30", url], capture_output=True, text=True, check=True).stdout
    out = {}
    for row in csv.reader(io.StringIO(text)):
        try:
            out[row[0]] = float(row[1])
        except (ValueError, IndexError):
            pass
    return out


def stats(d, spread=False):
    ks = sorted(d)
    vals = [d[k] for k in ks]
    last = vals[-1]
    k = 100 if spread else 1
    prev = next((d[x] for x in reversed(ks) if x <= (datetime.date.fromisoformat(ks[-1]) - datetime.timedelta(days=2)).isoformat()), last)
    out = {"date": ks[-1], "value": round(last * k, 3), "two_days_before": round(prev * k, 3),
           "min_3y": round(min(vals) * k, 3), "max_3y": round(max(vals) * k, 3),
           "percentile_3y": round(100 * sum(v <= last for v in vals) / len(vals))}
    # The last print at or before the latest print date minus 30 days. None when the history is too short.
    cut = (datetime.date.fromisoformat(ks[-1]) - datetime.timedelta(days=30)).isoformat()
    mk = next((x for x in reversed(ks) if x <= cut), None)
    out["month_before"] = round(d[mk] * k, 3) if mk else None
    out["month_before_date"] = mk
    return out


def main():
    out, data, errors = {"pulled": datetime.datetime.now().isoformat(timespec="seconds"), "unit": "spreads in basis points"}, {}, []
    for name, sid in SERIES.items():
        try:
            data[name] = load(sid)
            out[name] = dict(series=sid, **stats(data[name], spread=name in ("IG", "AAA", "AA", "A", "BBB", "HY", "BB", "B", "CCC")))
        except Exception as e:  # report, do not hide
            errors.append(f"{name} ({sid}): {e}")
    if "AA" in data and "BBB" in data:
        ks = sorted(set(data["AA"]) & set(data["BBB"]))
        r = {k: data["AA"][k] / data["BBB"][k] for k in ks if data["BBB"][k]}
        v = list(r.values())
        mean, sd = statistics.mean(v), statistics.pstdev(v)
        s = stats(r)
        s.update(series="BAMLC0A2CAA / BAMLC0A4CBBB", mean_3y=round(mean, 3), z_3y=round((v[-1] - mean) / sd, 2),
                 max_date=max(r, key=r.get))
        out["axis_AA_over_BBB"] = s
    out["errors"] = errors
    json.dump(out, open(sys.argv[1], "w"), indent=1)
    print(f"readings: {len(out) - 3} series, {len(errors)} errors")


if __name__ == "__main__":
    main()
