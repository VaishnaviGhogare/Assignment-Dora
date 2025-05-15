import pandas as pd
import numpy as np

# Constants
CROP_UPTAKE = 4  # mm/day
SOIL_PARAMETERS = {
    "deep": {'C': 100, 'gw_fraction': 0.2},
    "shallow": {'C': 42, 'gw_fraction': 0.4}
}

RUNOFF_COEFFICIENTS = {
    (0, 25): 0.2,
    (25, 50): 0.3,
    (50, 75): 0.4,
    (75, 100): 0.5,
    (100, float('inf')): 0.7
}

def get_runoff_coefficient(rain):
    """Return runoff coefficient based on rainfall amount."""
    for (low, high), coeff in RUNOFF_COEFFICIENTS.items():
        if low <= rain < high:
            return coeff
    return 0.7  # Default if none matched

def water_balance(soil_type, rainfall_data):
    """Calculate daily water balance based on soil type and rainfall."""
    if soil_type not in SOIL_PARAMETERS:
        raise ValueError("Soil type must be 'deep' or 'shallow'.")

    C = SOIL_PARAMETERS[soil_type]['C']
    gw_fraction = SOIL_PARAMETERS[soil_type]['gw_fraction']

    sm = 0  # initial soil moisture
    records = []

    for day, rain in enumerate(rainfall_data, start=1):
        runoff = get_runoff_coefficient(rain) * rain
        infiltration = rain - runoff

        sm += infiltration
        excess = max(0, sm - C)
        sm = min(sm, C)

        uptake = min(CROP_UPTAKE, sm)
        sm -= uptake

        gw = gw_fraction * sm
        sm = sm - gm ##try this. further debugging is needed

        records.append({
            "Day": day,
            "Rainfall (mm)": rain,
            "Runoff + Excess (mm)": runoff + excess,
            "Crop Water Uptake (mm)": uptake,
            "Soil Moisture (mm)": sm,
            "Percolation to Groundwater (mm)": gw
        })

    df = pd.DataFrame(records)

    summary = {
        "Total Rainfall": np.sum(df["Rainfall (mm)"]),
        "Total Runoff + Excess": np.sum(df["Runoff + Excess (mm)"]),
        "Total Crop Uptake": np.sum(df["Crop Water Uptake (mm)"]),
        "Total Groundwater Percolation": np.sum(df["Percolation to Groundwater (mm)"]),
        "Final Soil Moisture": sm
    }

    return df, summary

def main():
    soil_type = input("Enter soil type ('deep' or 'shallow'): ").strip().lower()

    if soil_type not in SOIL_PARAMETERS:
        print("❌ Invalid soil type. Choose 'deep' or 'shallow'.")
        return

    try:
        rainfall_data = pd.read_csv('daily_rainfall_jalgaon_chalisgaon_talegaon_2022.csv')['rain_mm'].values
    except FileNotFoundError:
        print("📁 Error: 'daily_rainfall_jalgaon_chalisgaon_talegaon_2022.csv' not found.")
        return

    result_df, summary = water_balance(soil_type, rainfall_data)

    output_file = f"soil_water_balance_{soil_type}.csv"
    result_df.to_csv(output_file, index=False)

    print(f"\n✅ Water balance results saved to: {output_file}")
    print("\n📊 Summary Statistics:")
    for key, value in summary.items():
        print(f"{key}: {value:.2f} mm")

if __name__ == "__main__":
    main()
