"""
Flask app – now serves only HTML; all plotting done client-side with Plotly.
"""

from flask import Flask, render_template, request
from cost_model import baseline, alternative

app = Flask(__name__)

# Field definitions for baseline block (unchanged)
BASE_FIELDS = [
    ("ship_time",   "Origin → repair transit time (days)", baseline["ship_time"]),
    ("ship_cost",   "Origin → repair shipping cost (€)",   baseline["ship_cost"]),
    ("tat",         "Repair shop turnaround time (days)",  baseline["tat"]),
    ("repair_cost", "Repair cost (€)",                     baseline["repair_cost"]),
    ("return_time", "Repair → warehouse transit time (days)", baseline["return_time"]),
    ("return_cost", "Repair → warehouse shipping cost (€)",   baseline["return_cost"]),
    ("delay_cost",  "Cost per day of TAT (€)",                baseline["delay_cost"]),
]

# Defaults for a first alternative card
ALT_DEFAULT = alternative

TEXT_DEFS = [
    ("origin_label",   "Origin country",   "Korea"),
    ("baseline_label", "Baseline country", "Germany"),
]

@app.route("/", methods=["GET"])
def live():
    # Send baseline defaults & one template alternative
    vals = {k: request.args.get(k, d) for k, _, d in BASE_FIELDS}
    texts = {k: request.args.get(k, d) for k, _, d in TEXT_DEFS}
    return render_template(
        "live.html",
        base_fields=BASE_FIELDS,
        base_values=vals,
        text_fields=TEXT_DEFS,
        text_values=texts,
        alt_default=ALT_DEFAULT,
    )

if __name__ == "__main__":
    app.run(debug=True)
