import math
def calculate_pv(theta600: float, theta300: float) -> float:
    return theta600 - theta300
def calculate_av(theta600: float) -> float:
    return theta600 / 2
def calculate_yp(theta300: float, pv: float) -> float:
    return theta300 - pv
def calculate_ti(yp: float, pv: float) -> float:
    if pv <= 0:
        return 0.0
    return yp / pv
def calculate_n(theta600: float, theta300: float) -> float:
    if theta300 <= 0 or theta600 <= 0:
        return 0.0
    return 3.32 * math.log10(theta600 / theta300)
def calculate_k(theta300: float, n: float) -> float:
    denominator = 511 ** n
    if denominator <= 0:
        return 0.0
    return theta300 / (511 ** n)
def convert_mw(value: float, from_unit: str) -> dict:
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
    # calculate all other units from PPG
    return {
        'PPG': ppg,
        'SG': ppg / 8.33,
        'lb/ft³': ppg * 7.48,
        'kg/m³': ppg * 119.83,
        'psi/1000ft': ppg * 52.0
    }
def calculate_bf(mw_ppg: float) -> float:
    return 1 - (mw_ppg / 65.5)