# Auto-extracted from AI.py — aipy_math
# All functions are independent utilities with no AI.py-internal dependencies.

def conversion_extra_bytes_to_human():
    """Convert utility. (cmd 2848)"""
    try:
        n = float(input("Enter bytes: "))
    except (ValueError, EOFError):
        return "0 B"
    if n < 0: return "0 B"
    units = ["B", "KB", "MB", "GB", "TB", "PB", "EB"]
    i = 0
    while n >= 1024 and i < len(units) - 1:
        n /= 1024
        i += 1
    return "{:.2f} {}".format(n, units[i])


def conversion_extra_human_to_bytes():
    """Convert utility. (cmd 2849)"""
    try:
        s = input("Enter size: ")
    except (ValueError, EOFError):
        return 0
    s = s.strip().upper()
    units = {"B":1,"KB":1024,"MB":1048576,"GB":1073741824,"TB":1099511627776}
    for unit, mult in units.items():
        if s.endswith(unit):
            try:
                num = float(s[:len(s)-len(unit)].strip())
                return int(num * mult)
            except ValueError:
                return 0
    try: return int(float(s))
    except ValueError: return 0


def conversion_extra_celsius_to_kelvin():
    """Convert utility. (cmd 2850)"""
    try:
        c = float(input("Celsius: "))
    except (ValueError, EOFError):
        return 0.0
    if c < -273.15: c = -273.15
    return c + 273.15


def conversion_extra_kelvin_to_celsius():
    """Convert utility. (cmd 2851)"""
    try:
        k = float(input("Kelvin: "))
    except (ValueError, EOFError):
        return 0.0
    if k < 0: k = 0
    return k - 273.15


def conversion_extra_fahrenheit_to_kelvin():
    """Convert utility. (cmd 2852)"""
    name = "fahrenheit_to_kelvin"
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    if name == "fahrenheit_to_kelvin":
        return (val - 32) * 5/9 + 273.15
    return val * 9/5 - 459.67


def conversion_extra_kelvin_to_fahrenheit():
    """Convert utility. (cmd 2853)"""
    name = "kelvin_to_fahrenheit"
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    if name == "fahrenheit_to_kelvin":
        return (val - 32) * 5/9 + 273.15
    return val * 9/5 - 459.67


def conversion_extra_mph_to_knots():
    """Convert utility. (cmd 2854)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_knots_to_mph():
    """Convert utility. (cmd 2855)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_lightyears_to_km():
    """Convert utility. (cmd 2856)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_km_to_lightyears():
    """Convert utility. (cmd 2857)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_parsecs_to_ly():
    """Convert utility. (cmd 2858)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_ly_to_parsecs():
    """Convert utility. (cmd 2859)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_au_to_km():
    """Convert utility. (cmd 2860)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_km_to_au():
    """Convert utility. (cmd 2861)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_radians_to_degrees():
    """Convert utility. (cmd 2862)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_degrees_to_radians():
    """Convert utility. (cmd 2863)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_ev_to_joules():
    """Convert utility. (cmd 2864)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_joules_to_ev():
    """Convert utility. (cmd 2865)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_calories_to_joules():
    """Convert utility. (cmd 2866)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_joules_to_calories():
    """Convert utility. (cmd 2867)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_horsepower_to_watts():
    """Convert utility. (cmd 2868)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_watts_to_horsepower():
    """Convert utility. (cmd 2869)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_atm_to_pascal():
    """Convert utility. (cmd 2870)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_pascal_to_atm():
    """Convert utility. (cmd 2871)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_bar_to_psi():
    """Convert utility. (cmd 2872)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_psi_to_bar():
    """Convert utility. (cmd 2873)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_inches_to_cm():
    """Convert utility. (cmd 2874)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_cm_to_inches():
    """Convert utility. (cmd 2875)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_feet_to_meters():
    """Convert utility. (cmd 2876)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_meters_to_feet():
    """Convert utility. (cmd 2877)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_miles_to_km():
    """Convert utility. (cmd 2878)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_km_to_miles():
    """Convert utility. (cmd 2879)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_acres_to_hectares():
    """Convert utility. (cmd 2880)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_hectares_to_acres():
    """Convert utility. (cmd 2881)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_gallons_to_liters():
    """Convert utility. (cmd 2882)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_liters_to_gallons():
    """Convert utility. (cmd 2883)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_ounces_to_grams():
    """Convert utility. (cmd 2884)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_grams_to_ounces():
    """Convert utility. (cmd 2885)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_pounds_to_kg():
    """Convert utility. (cmd 2886)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_kg_to_pounds():
    """Convert utility. (cmd 2887)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_celsius_to_fahrenheit():
    """Convert utility. (cmd 2888)"""
    try:
        c = float(input("Celsius: "))
    except (ValueError, EOFError):
        return 0.0
    return c * 9/5 + 32


def conversion_extra_fahrenheit_to_celsius():
    """Convert utility. (cmd 2889)"""
    try:
        f = float(input("Fahrenheit: "))
    except (ValueError, EOFError):
        return 0.0
    return (f - 32) * 5/9


def conversion_extra_mph_to_kph():
    """Convert utility. (cmd 2890)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_kph_to_mph():
    """Convert utility. (cmd 2891)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_sqft_to_sqm():
    """Convert utility. (cmd 2892)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_sqm_to_sqft():
    """Convert utility. (cmd 2893)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_fl_oz_to_ml():
    """Convert utility. (cmd 2894)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_ml_to_fl_oz():
    """Convert utility. (cmd 2895)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_carats_to_grams():
    """Convert utility. (cmd 2896)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_grams_to_carats():
    """Convert utility. (cmd 2897)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_years_to_days():
    """Convert utility. (cmd 2898)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_days_to_years():
    """Convert utility. (cmd 2899)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_hours_to_minutes():
    """Convert utility. (cmd 2900)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_minutes_to_hours():
    """Convert utility. (cmd 2901)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_weeks_to_days():
    """Convert utility. (cmd 2902)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_days_to_weeks():
    """Convert utility. (cmd 2903)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_decades_to_years():
    """Convert utility. (cmd 2904)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_centuries_to_years():
    """Convert utility. (cmd 2905)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_millennia_to_years():
    """Convert utility. (cmd 2906)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_knots_to_kph():
    """Convert utility. (cmd 2907)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_kph_to_knots():
    """Convert utility. (cmd 2908)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_mach_to_kph():
    """Convert utility. (cmd 2909)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_kph_to_mach():
    """Convert utility. (cmd 2910)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_nautical_miles_to_km():
    """Convert utility. (cmd 2911)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_km_to_nautical_miles():
    """Convert utility. (cmd 2912)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_stones_to_kg():
    """Convert utility. (cmd 2913)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_kg_to_stones():
    """Convert utility. (cmd 2914)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_tons_to_kg():
    """Convert utility. (cmd 2915)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_kg_to_tons():
    """Convert utility. (cmd 2916)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_newtons_to_lbf():
    """Convert utility. (cmd 2917)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_lbf_to_newtons():
    """Convert utility. (cmd 2918)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_joules_to_kwh():
    """Convert utility. (cmd 2919)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_kwh_to_joules():
    """Convert utility. (cmd 2920)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_btu_to_joules():
    """Convert utility. (cmd 2921)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_joules_to_btu():
    """Convert utility. (cmd 2922)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_furlongs_to_meters():
    """Convert utility. (cmd 2923)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_meters_to_furlongs():
    """Convert utility. (cmd 2924)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_chains_to_meters():
    """Convert utility. (cmd 2925)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_meters_to_chains():
    """Convert utility. (cmd 2926)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_rods_to_meters():
    """Convert utility. (cmd 2927)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_meters_to_rods():
    """Convert utility. (cmd 2928)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_fathoms_to_meters():
    """Convert utility. (cmd 2929)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_meters_to_fathoms():
    """Convert utility. (cmd 2930)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_cubits_to_meters():
    """Convert utility. (cmd 2931)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)


def conversion_extra_meters_to_cubits():
    """Convert utility. (cmd 2932)"""
    try:
        value = float(input("Enter value: "))
    except (ValueError, EOFError):
        return 0.0
    conv = {
        "miles_to_km":1.609344,"km_to_miles":0.621371,
        "inches_to_cm":2.54,"cm_to_inches":0.393701,
        "feet_to_meters":0.3048,"meters_to_feet":3.28084,
        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,
        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,
        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,
        "mph_to_kph":1.60934,"kph_to_mph":0.621371,
        "mph_to_knots":0.868976,"knots_to_mph":1.15078,
        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,
        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,
        "au_to_km":149597870.7,"km_to_au":6.68459e-9,
        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,
        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,
        "calories_to_joules":4.184,"joules_to_calories":0.239006,
        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,
        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,
        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,
        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,
        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,
        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,
        "carats_to_grams":0.2,"grams_to_carats":5.0,
        "knots_to_kph":1.852,"kph_to_knots":0.539957,
        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,
        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,
        "stones_to_kg":6.35029,"kg_to_stones":0.157473,
        "tons_to_kg":907.185,"kg_to_tons":0.00110231,
        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,
        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,
        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,
        "years_to_days":365.25,"days_to_years":0.00273791,
        "hours_to_minutes":60,"minutes_to_hours":0.0166667,
        "weeks_to_days":7,"days_to_weeks":0.142857,
        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,
    }
    factor = conv.get(name, 1.0)
    result = value * factor
    return round(result, 6)



def statistics_extra_geometric_mean():
    """Stats utility. (cmd 3318)"""
    name = "geometric_mean"
    import math
    try: raw = input("Numbers: ")
    except: return 0.0
    try: nums=[float(x.strip()) for x in raw.split(",") if x.strip()]
    except: return 0.0
    if not nums: return 0.0; n=len(nums)
    if "geometric" in name:
        if any(x<=0 for x in nums): return 0.0
        return round(math.exp(sum(math.log(x) for x in nums)/n),4)
    if "harmonic" in name:
        if any(x==0 for x in nums): return 0.0
        return round(n/sum(1/x for x in nums),4)
    if "quadratic" in name: return round(math.sqrt(sum(x*x for x in nums)/n),4)
    if "trimmed" in name:
        prop = float(input("Trim proportion: ") or "0.1")
        s=sorted(nums); tr=int(n*prop/2); trim=s[tr:-tr] if tr>0 else s
        return round(sum(trim)/len(trim),4) if trim else 0.0
    wts = [float(x) for x in input("Weights: ").split(",") if x.strip()]
    if len(wts)!=n: wts=[1]*n
    return round(sum(v*w for v,w in zip(nums,wts))/sum(wts),4)


def statistics_extra_harmonic_mean():
    """Stats utility. (cmd 3319)"""
    name = "harmonic_mean"
    import math
    try: raw = input("Numbers: ")
    except: return 0.0
    try: nums=[float(x.strip()) for x in raw.split(",") if x.strip()]
    except: return 0.0
    if not nums: return 0.0; n=len(nums)
    if "geometric" in name:
        if any(x<=0 for x in nums): return 0.0
        return round(math.exp(sum(math.log(x) for x in nums)/n),4)
    if "harmonic" in name:
        if any(x==0 for x in nums): return 0.0
        return round(n/sum(1/x for x in nums),4)
    if "quadratic" in name: return round(math.sqrt(sum(x*x for x in nums)/n),4)
    if "trimmed" in name:
        prop = float(input("Trim proportion: ") or "0.1")
        s=sorted(nums); tr=int(n*prop/2); trim=s[tr:-tr] if tr>0 else s
        return round(sum(trim)/len(trim),4) if trim else 0.0
    wts = [float(x) for x in input("Weights: ").split(",") if x.strip()]
    if len(wts)!=n: wts=[1]*n
    return round(sum(v*w for v,w in zip(nums,wts))/sum(wts),4)


def statistics_extra_quadratic_mean():
    """Stats utility. (cmd 3320)"""
    name = "quadratic_mean"
    import math
    try: raw = input("Numbers: ")
    except: return 0.0
    try: nums=[float(x.strip()) for x in raw.split(",") if x.strip()]
    except: return 0.0
    if not nums: return 0.0; n=len(nums)
    if "geometric" in name:
        if any(x<=0 for x in nums): return 0.0
        return round(math.exp(sum(math.log(x) for x in nums)/n),4)
    if "harmonic" in name:
        if any(x==0 for x in nums): return 0.0
        return round(n/sum(1/x for x in nums),4)
    if "quadratic" in name: return round(math.sqrt(sum(x*x for x in nums)/n),4)
    if "trimmed" in name:
        prop = float(input("Trim proportion: ") or "0.1")
        s=sorted(nums); tr=int(n*prop/2); trim=s[tr:-tr] if tr>0 else s
        return round(sum(trim)/len(trim),4) if trim else 0.0
    wts = [float(x) for x in input("Weights: ").split(",") if x.strip()]
    if len(wts)!=n: wts=[1]*n
    return round(sum(v*w for v,w in zip(nums,wts))/sum(wts),4)


def statistics_extra_trimmed_mean():
    """Stats utility. (cmd 3321)"""
    name = "trimmed_mean"
    import math
    try: raw = input("Numbers: ")
    except: return 0.0
    try: nums=[float(x.strip()) for x in raw.split(",") if x.strip()]
    except: return 0.0
    if not nums: return 0.0; n=len(nums)
    if "geometric" in name:
        if any(x<=0 for x in nums): return 0.0
        return round(math.exp(sum(math.log(x) for x in nums)/n),4)
    if "harmonic" in name:
        if any(x==0 for x in nums): return 0.0
        return round(n/sum(1/x for x in nums),4)
    if "quadratic" in name: return round(math.sqrt(sum(x*x for x in nums)/n),4)
    if "trimmed" in name:
        prop = float(input("Trim proportion: ") or "0.1")
        s=sorted(nums); tr=int(n*prop/2); trim=s[tr:-tr] if tr>0 else s
        return round(sum(trim)/len(trim),4) if trim else 0.0
    wts = [float(x) for x in input("Weights: ").split(",") if x.strip()]
    if len(wts)!=n: wts=[1]*n
    return round(sum(v*w for v,w in zip(nums,wts))/sum(wts),4)


def statistics_extra_weighted_mean():
    """Stats utility. (cmd 3322)"""
    name = "weighted_mean"
    import math
    try: raw = input("Numbers: ")
    except: return 0.0
    try: nums=[float(x.strip()) for x in raw.split(",") if x.strip()]
    except: return 0.0
    if not nums: return 0.0; n=len(nums)
    if "geometric" in name:
        if any(x<=0 for x in nums): return 0.0
        return round(math.exp(sum(math.log(x) for x in nums)/n),4)
    if "harmonic" in name:
        if any(x==0 for x in nums): return 0.0
        return round(n/sum(1/x for x in nums),4)
    if "quadratic" in name: return round(math.sqrt(sum(x*x for x in nums)/n),4)
    if "trimmed" in name:
        prop = float(input("Trim proportion: ") or "0.1")
        s=sorted(nums); tr=int(n*prop/2); trim=s[tr:-tr] if tr>0 else s
        return round(sum(trim)/len(trim),4) if trim else 0.0
    wts = [float(x) for x in input("Weights: ").split(",") if x.strip()]
    if len(wts)!=n: wts=[1]*n
    return round(sum(v*w for v,w in zip(nums,wts))/sum(wts),4)


def statistics_extra_covariance():
    """Stats utility. (cmd 3323)"""
    name = "covariance"
    import math
    try:
        x=[float(v) for v in input("X: ").split(",") if v.strip()]
        y=[float(v) for v in input("Y: ").split(",") if v.strip()]
    except: return 0.0
    n=len(x);
    if n!=len(y) or n<2: return 0.0
    mx,my=sum(x)/n,sum(y)/n
    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))
    if "covariance" in name: return round(num/(n-1),4)
    dx=math.sqrt(sum((xi-mx)**2 for xi in x))
    dy=math.sqrt(sum((yi-my)**2 for yi in y))
    return round(num/(dx*dy),4) if dx*dy else 0.0


def statistics_extra_correlation_pearson():
    """Stats utility. (cmd 3324)"""
    name = "correlation_pearson"
    import math
    try:
        x=[float(v) for v in input("X: ").split(",") if v.strip()]
        y=[float(v) for v in input("Y: ").split(",") if v.strip()]
    except: return 0.0
    n=len(x);
    if n!=len(y) or n<2: return 0.0
    mx,my=sum(x)/n,sum(y)/n
    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))
    if "covariance" in name: return round(num/(n-1),4)
    dx=math.sqrt(sum((xi-mx)**2 for xi in x))
    dy=math.sqrt(sum((yi-my)**2 for yi in y))
    return round(num/(dx*dy),4) if dx*dy else 0.0


def statistics_extra_zscore():
    """Stats utility. (cmd 3325)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_standard_error():
    """Stats utility. (cmd 3326)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_confidence_interval_mean():
    """Stats utility. (cmd 3327)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_linear_regression():
    """Stats utility. (cmd 3328)"""
    name = "linear_regression"
    import math
    try:
        x=[float(v) for v in input("X: ").split(",") if v.strip()]
        y=[float(v) for v in input("Y: ").split(",") if v.strip()]
    except: return 0.0
    n=len(x);
    if n!=len(y) or n<2: return 0.0
    mx,my=sum(x)/n,sum(y)/n
    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))
    den=sum((xi-mx)**2 for xi in x)
    slope=num/den if den else 0
    intercept=my-slope*mx
    yp=[slope*xi+intercept for xi in x]
    if "linear" in name: return (round(slope,4),round(intercept,4))
    ss_res=sum((yi-ypi)**2 for yi,ypi in zip(y,yp))
    ss_tot=sum((yi-my)**2 for yi in y)
    if "r_squared" in name: return round(1-ss_res/ss_tot,4) if ss_tot else 0
    if "root" in name: return round(math.sqrt(ss_res/n),4)
    return round(sum(abs(yi-ypi) for yi,ypi in zip(y,yp))/n,4)


def statistics_extra_r_squared():
    """Stats utility. (cmd 3329)"""
    name = "r_squared"
    import math
    try:
        x=[float(v) for v in input("X: ").split(",") if v.strip()]
        y=[float(v) for v in input("Y: ").split(",") if v.strip()]
    except: return 0.0
    n=len(x);
    if n!=len(y) or n<2: return 0.0
    mx,my=sum(x)/n,sum(y)/n
    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))
    den=sum((xi-mx)**2 for xi in x)
    slope=num/den if den else 0
    intercept=my-slope*mx
    yp=[slope*xi+intercept for xi in x]
    if "linear" in name: return (round(slope,4),round(intercept,4))
    ss_res=sum((yi-ypi)**2 for yi,ypi in zip(y,yp))
    ss_tot=sum((yi-my)**2 for yi in y)
    if "r_squared" in name: return round(1-ss_res/ss_tot,4) if ss_tot else 0
    if "root" in name: return round(math.sqrt(ss_res/n),4)
    return round(sum(abs(yi-ypi) for yi,ypi in zip(y,yp))/n,4)


def statistics_extra_root_mean_sq_error():
    """Stats utility. (cmd 3330)"""
    name = "root_mean_sq_error"
    import math
    try:
        x=[float(v) for v in input("X: ").split(",") if v.strip()]
        y=[float(v) for v in input("Y: ").split(",") if v.strip()]
    except: return 0.0
    n=len(x);
    if n!=len(y) or n<2: return 0.0
    mx,my=sum(x)/n,sum(y)/n
    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))
    den=sum((xi-mx)**2 for xi in x)
    slope=num/den if den else 0
    intercept=my-slope*mx
    yp=[slope*xi+intercept for xi in x]
    if "linear" in name: return (round(slope,4),round(intercept,4))
    ss_res=sum((yi-ypi)**2 for yi,ypi in zip(y,yp))
    ss_tot=sum((yi-my)**2 for yi in y)
    if "r_squared" in name: return round(1-ss_res/ss_tot,4) if ss_tot else 0
    if "root" in name: return round(math.sqrt(ss_res/n),4)
    return round(sum(abs(yi-ypi) for yi,ypi in zip(y,yp))/n,4)


def statistics_extra_mean_abs_error():
    """Stats utility. (cmd 3331)"""
    name = "mean_abs_error"
    import math
    try:
        x=[float(v) for v in input("X: ").split(",") if v.strip()]
        y=[float(v) for v in input("Y: ").split(",") if v.strip()]
    except: return 0.0
    n=len(x);
    if n!=len(y) or n<2: return 0.0
    mx,my=sum(x)/n,sum(y)/n
    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))
    den=sum((xi-mx)**2 for xi in x)
    slope=num/den if den else 0
    intercept=my-slope*mx
    yp=[slope*xi+intercept for xi in x]
    if "linear" in name: return (round(slope,4),round(intercept,4))
    ss_res=sum((yi-ypi)**2 for yi,ypi in zip(y,yp))
    ss_tot=sum((yi-my)**2 for yi in y)
    if "r_squared" in name: return round(1-ss_res/ss_tot,4) if ss_tot else 0
    if "root" in name: return round(math.sqrt(ss_res/n),4)
    return round(sum(abs(yi-ypi) for yi,ypi in zip(y,yp))/n,4)


def statistics_extra_entropy_discrete():
    """Stats utility. (cmd 3332)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_gini_impurity():
    """Stats utility. (cmd 3333)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_bayes_theorem():
    """Stats utility. (cmd 3334)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_binomial_prob():
    """Stats utility. (cmd 3335)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_normal_pdf():
    """Stats utility. (cmd 3336)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_normal_cdf():
    """Stats utility. (cmd 3337)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_poisson_prob():
    """Stats utility. (cmd 3338)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_exponential_pdf():
    """Stats utility. (cmd 3339)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_uniform_pdf():
    """Stats utility. (cmd 3340)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_beta_pdf():
    """Stats utility. (cmd 3341)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_chisq_pdf():
    """Stats utility. (cmd 3342)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_weibull_pdf():
    """Stats utility. (cmd 3343)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_median_absolute_dev():
    """Stats utility. (cmd 3344)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_interquartile_range():
    """Stats utility. (cmd 3345)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_cohens_kappa():
    """Stats utility. (cmd 3346)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_kl_divergence():
    """Stats utility. (cmd 3347)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_mad():
    """Stats utility. (cmd 3348)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_range_stat():
    """Stats utility. (cmd 3349)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_variance_pop():
    """Stats utility. (cmd 3350)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_variance_sample():
    """Stats utility. (cmd 3351)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_std_dev_pop():
    """Stats utility. (cmd 3352)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_std_dev_sample():
    """Stats utility. (cmd 3353)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_skewness_sample():
    """Stats utility. (cmd 3354)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_kurtosis_sample():
    """Stats utility. (cmd 3355)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_effect_size_cohens_d():
    """Stats utility. (cmd 3356)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_effect_size_pearson_r():
    """Stats utility. (cmd 3357)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_contingency_chi_sq():
    """Stats utility. (cmd 3358)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_contingency_cramers_v():
    """Stats utility. (cmd 3359)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_contingency_phi():
    """Stats utility. (cmd 3360)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_odds_ratio():
    """Stats utility. (cmd 3361)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_risk_ratio():
    """Stats utility. (cmd 3362)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_moving_median():
    """Stats utility. (cmd 3363)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_exp_moving_average():
    """Stats utility. (cmd 3364)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_exp_moving_std():
    """Stats utility. (cmd 3365)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_autocorrelation():
    """Stats utility. (cmd 3366)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_cross_correlation():
    """Stats utility. (cmd 3367)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_deciles():
    """Stats utility. (cmd 3368)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_percentiles():
    """Stats utility. (cmd 3369)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_five_number_summary():
    """Stats utility. (cmd 3370)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_box_plot_stats():
    """Stats utility. (cmd 3371)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_outliers_iqr():
    """Stats utility. (cmd 3372)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_outliers_zscore():
    """Stats utility. (cmd 3373)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_shannon_index():
    """Stats utility. (cmd 3374)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_simpson_index():
    """Stats utility. (cmd 3375)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_diversity_metrics():
    """Stats utility. (cmd 3376)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result


def statistics_extra_frequency_table():
    """Stats utility. (cmd 3377)"""
    try:
        raw = input("Enter data (comma separated): ")
    except (ValueError, EOFError):
        return "No input provided"
    if not raw or not raw.strip():
        return "Empty input, nothing to analyze"
    items = [x.strip() for x in raw.split(",") if x.strip()]
    if len(items) == 0:
        return "No valid items found"
    # Convert to numbers if possible
    nums = []
    for x in items:
        try:
            nums.append(float(x))
        except ValueError:
            pass
    if not nums:
        return "Could not parse any numeric values"
    # Perform core analysis
    count = len(nums)
    total = sum(nums)
    mean_val = total / count
    sorted_vals = sorted(nums)
    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2
    variance = sum((x - mean_val)**2 for x in nums) / count
    std_val = variance ** 0.5
    min_val = min(nums)
    max_val = max(nums)
    # Format result
    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"
    result = result.format(count, mean_val, median_val, std_val)
    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)
    return result
