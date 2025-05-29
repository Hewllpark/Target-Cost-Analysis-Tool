# Target-Cost Explorer

**Break-even Formulas**

Baseline total cost (Germany):

$$
C_{1}=c_{\text{ship}}+c_{\text{repair}}+c_{\text{return}}
     +\bigl(t_{\text{ship}}+\text{TAT}+t_{\text{return}}\bigr)\,d
$$

Alternative fixed costs (China):

$$
F = c_{\text{repair}}\times\text{discount}
  + c_{\text{inbound}}
  + c_{\text{return}}
  + \bigl(\text{TAT}_{\text{alt}} + t_{\text{return,alt}}\bigr)\,d
$$

Break-even shipping cost at $t=t_{\text{ship}}$:

$$
c_{\max}=C_{1}-F-t_{\text{ship}}\,d
$$

---

An interactive Flask web-app for evaluating the break-even shipping cost and time when moving component repairs from a baseline facility (e.g. Germany) to one or more alternative repair shops (e.g. China).

---

## 1. Features

| Function                    | Description                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------- |
| **Live parameter form**     | All cost / time inputs editable in the browser.                                                     |
| **Plotly chart**            | Interactive “Max Allowable Shipping Cost vs Transit Time” curve with hover tool-tips, zoom and pan. |
| **Multiple alternatives**   | Add unlimited alternative flows; each receives its own line and colour.                             |
| **Break-even marker**       | Yellow label shows the current break-even point for every alternative.                              |
| **Local history**           | One-click snapshot to PNG, stored in browser `localStorage`.                                        |
| **Side-by-side comparison** | Pick up to four saved graphs and view them in a grid, each captioned with its name.                 |

---

## 2. Quick start

### 2.1 Prerequisites

* Python 3.9 – 3.12
* `pip` or `pipx`

### 2.2 Install & run

```bash
cd CaseStudyApp-clean

python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

# Windows:
set FLASK_APP=app.py

# macOS/Linux:
export FLASK_APP=app.py

flask run
```

Point your browser to **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.

---

## 3. Project structure

```
├─ app.py               # Flask entry-point
├─ cost_model.py        # Cost functions and default parameters
├─ requirements.txt     # Python dependencies
└─ templates/
   └─ live.html         # Single-page front-end (HTML + CSS + JS)
```

---

## 4. Customising

| Area                         | How to adapt                                                                                  |
| ---------------------------- | --------------------------------------------------------------------------------------------- |
| **Corporate colours / logo** | Edit CSS variables at the top of `live.html`.                                                 |
| **Default parameters**       | Change the dicts `baseline` and `alternative` in `cost_model.py`.                             |
| **Max compare slots**        | Adjust the `MAX_COMPARE` constant in `live.html`’s script.                                    |
| **Security / auth**          | Place the app behind your existing SSO reverse proxy; no session state is stored server-side. |

---

## requirements.txt

```text
Flask>=3.0,<4.0
numpy>=1.24
gunicorn>=21.0     # optional, for production deployment
```
