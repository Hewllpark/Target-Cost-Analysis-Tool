"""
Cost-model utilities for the Target Cost Analysis tool.
Defines baseline (Germany) and alternative (China) parameter
dictionaries plus helper functions for total cost and
break-even shipping-cost calculation.
"""

# ──────────────────────────────────────────────────────────────
# 1) Baseline parameters – Germany flow
# ──────────────────────────────────────────────────────────────
baseline = {
    "ship_time":   4.65,   # days from Korea to Germany
    "ship_cost":   150.0,  # €
    "tat":         16.0,   # turnaround time in shop (days)
    "return_time": 2.70,   # days Germany → HK warehouse
    "return_cost": 110.0,  # €
    "repair_cost": 598.0,  # € repair fee in Germany
    "delay_cost":  10.0    # € per day component is unavailable
}

# ──────────────────────────────────────────────────────────────
# 2) Alternative parameters – China flow (shipping in unknown)
# ──────────────────────────────────────────────────────────────
alternative = {
    "tat":         14.2,   # days
    "return_time": 1.2,    # days China → HK warehouse
    "return_cost": 80.0,   # €
    "inbound_fee": 25.0,   # € system-booking fee per unit
    "discount":    0.90,   # 10 % discount on Germany repair cost
    "delay_cost":  10.0    # € per day component is unavailable
}

# ──────────────────────────────────────────────────────────────
# Helper functions
# ──────────────────────────────────────────────────────────────
def total_cost(p: dict) -> float:
    """
    Return total cost for a given process dictionary *p*.
    Required keys: ship_time, ship_cost, tat, repair_cost,
    return_time, return_cost, delay_cost.
    """
    days_out = p["ship_time"] + p["tat"] + p["return_time"]
    return (
        p["ship_cost"]
        + p["repair_cost"]
        + p["return_cost"]
        + days_out * p["delay_cost"]
    )


def max_allowed_cost(base: dict, alt: dict, t: float) -> float:
    """
    Given baseline *base*, alternative *alt*, and candidate
    shipping time *t* for the alternative route, return the
    maximum shipping cost (c_max) that keeps the alternative
    total ≤ baseline total.
    """
    # Baseline total
    C_base = total_cost(base)

    # Alternative cost block independent of shipping price/time
    fixed_alt = (
        base["repair_cost"] * alt["discount"]
        + alt["inbound_fee"]
        + alt["return_cost"]
        + (alt["tat"] + alt["return_time"]) * base["delay_cost"]
    )

    # Solve: C_base >= c_max + t*delay_cost + fixed_alt
    return C_base - fixed_alt - t * base["delay_cost"]
