# calculations.py
import math

def calculate_pv(theta600: float, theta300: float) -> float:

    # Plastic Viscosity (PV) in cP.
    # Formula: theta600 - theta300
    
    return theta600 - theta300

def calculate_av(theta600: float) -> float:
    
    # Apparent Viscosity (AV) in cP.
    # Formula: theta600 / 2
    
    return theta600 / 2

def calculate_yp(theta300: float, pv: float) -> float:
    
    # Yield Point (YP) in lb/100 ft².
    # Formula: theta300 - PV
    
    return theta300 - pv

def calculate_ti(yp: float, pv: float) -> float:

    # Transport Index (TI) represented as YP / PV ratio.
    # Formula: YP / PV (Handle division by zero if PV is 0)

    if pv <= 0:
        return 0.0
    return yp / pv

def calculate_n(theta600: float, theta300: float) -> float:

    # Flow Behavior Index (n) (dimensionless).
    # Formula: 3.32 * log10(theta600 / theta300)

    if theta300 <= 0 or theta600 <= 0:
        return 0.0
    return 3.32 * math.log10(theta600 / theta300)

def calculate_k(theta300: float, n: float) -> float:
    
    # Consistency Index (k) in lb·sⁿ/100 ft².
    # Formula: theta300 / (511^n)
    
    denominator = 511 ** n
    if denominator <= 0:
        return 0.0
    return theta300 / (511 ** n)

def convert_mw(value: float, from_unit: str) -> dict:
  
    """ 
    Converts a Mud Weight (MW) from a given unit to all other units.
    Units: 'PPG', 'SG', 'lb/ft³', 'kg/m³', 'psi/1000ft'
    
    Conversion reference (using water density = 8.33 ppg):
    - PPG to SG: value / 8.33
    - PPG to lb/ft³: value * 7.48052 (approx 7.48)
    - PPG to kg/m³: (value / 8.33) * 1000 = value * 120.048 (commonly 119.83 using 8.345)
    - PPG to psi/1000ft: value * 0.052 * 1000 = value * 52  
    """
   
    # First, convert the input value from its unit to the base unit: PPG
    if from_unit == 'PPG':
        ppg = value
    elif from_unit == 'SG':
        ppg = value * 8.33
    elif from_unit == 'lb/ft³':
        ppg = value / 7.48
    elif from_unit == 'kg/m³':
        ppg = value / 119.83
    elif from_unit == 'psi/1000ft':
        ppg = value / 52.0
    else:
        ppg = value

    # Then calculate all other units from PPG
    return {
        'PPG': ppg,
        'SG': ppg / 8.33,
        'lb/ft³': ppg * 7.48,
        'kg/m³': ppg * 119.83,
        'psi/1000ft': ppg * 52.0
    }

def calculate_bf(mw_ppg: float) -> float:

    # Buoyancy Factor (BF) for steel tubulars.
    # Formula: 1 - (mw_ppg / 65.5)

    
    return 1 - (mw_ppg / 65.5)