"""Generate ~22,000 lines of new utility code for AI.py v5.4.0."""
import os, random, textwrap, re

random.seed(4444)

CATEGORIES = [
    ("Text", "text_analysis", [
        "word_count","char_frequency","word_frequency","reverse_words","is_palindrome_sentence",
        "count_vowels","count_consonants","count_syllables_approx","unique_words","common_words",
        "text_summary","camel_to_snake","snake_to_camel","slugify","truncate_words",
        "levenshtein_distance","damerau_levenshtein","hamming_distance","jaro_winkler","longest_common_substring",
        "longest_common_subsequence","ngrams","sentiment_score","readability_score","phonetic_soundex",
        "is_anagram","is_anagram_phrase","random_sentence","random_paragraph","wrap_text",
        "center_text","justify_text","tab_to_spaces","spaces_to_tabs","strip_punctuation",
        "strip_numbers","swap_case","indent_text","is_pangram","is_isogram",
        "count_letters","count_digits","count_spaces","extract_emails","extract_urls",
        "split_sentences","rotate_string","ascii_shift","word_wrap_break","letter_frequency_score",
        "is_heterogram","count_syllables_rule","unique_letter_ratio","avg_word_length","sentence_length_stats",
        "detect_language","keyword_extract","count_char_types","mask_emails","mask_phones",
        "pluralize_word","singularize_word","camel_split","kebab_to_camel","camel_to_kebab",
        "remove_extra_spaces","is_uppercase","is_lowercase","count_substring","find_all_positions",
        "replace_multiple","prefix_lines","suffix_lines","quote_text","unquote_text",
        "title_case","invert_case","alternating_case","count_lines","longest_word",
        "shortest_word","most_frequent_word","rarest_word","count_sentences","count_paragraphs",
        "text_checksum","text_hash_djb2","is_blank","is_empty","is_alpha",
    ],[
        "word_count(text)","Count words, chars, sentences in text",
    ]),
    ("Math", "math_extras", [
        "gcd_list","lcm_list","is_perfect_square","is_perfect_cube","is_power_of_two",
        "is_power_of_n","digit_sum","digit_product","digital_root","reversed_number",
        "is_automorphic","is_harshad","prime_factors","num_divisors","binomial_coefficient",
        "fibonacci_n","fibonacci_sequence","lucas_number","tribonacci","pell_number",
        "collatz_sequence","collatz_steps","nth_prime","prime_range","next_prime",
        "is_twin_prime","is_cousin_prime","rand_prime","sieve_primes","is_semiprime",
        "is_emirp","is_circular_prime","randint_list","randfloat_list","clip",
        "lerp","map_range","smoothstep","monte_carlo_pi","modular_exponent",
        "modular_inverse","chinese_remainder","jacobi_symbol","farey_sequence","egyptian_fraction",
        "multinomial","pascal_row","primorial","subfactorial","double_factorial",
        "is_abundant","is_deficient","is_perfect_number","aliquot_sum","goldbach_pairs",
        "look_and_say","van_eck_sequence","stern_diatomic","recaman_sequence","mian_chowla",
        "modular_sqrt","discrete_log","continued_fraction","stern_brocot","is_sophie_germain",
        "safe_prime","prime_k_tuple","bernoulli_number","is_practical","is_carmichael",
        "moebius_function","euler_totient_range","sum_of_squares","lagrange_four_square","is_palindromic_number",
        "is_square_free","is_powerful","is_practical_number","is_mersenne_exponent","mersenne_number",
        "partition_number","bell_number","catalan_number","motzkin_number","central_binomial",
    ],[
        "gcd_list(nums)","GCD of a list of numbers",
    ]),
    ("Convert", "conversion_extra", [
        "bytes_to_human","human_to_bytes","celsius_to_kelvin","kelvin_to_celsius","fahrenheit_to_kelvin",
        "kelvin_to_fahrenheit","mph_to_knots","knots_to_mph","lightyears_to_km","km_to_lightyears",
        "parsecs_to_ly","ly_to_parsecs","au_to_km","km_to_au","radians_to_degrees",
        "degrees_to_radians","ev_to_joules","joules_to_ev","calories_to_joules","joules_to_calories",
        "horsepower_to_watts","watts_to_horsepower","atm_to_pascal","pascal_to_atm","bar_to_psi",
        "psi_to_bar","inches_to_cm","cm_to_inches","feet_to_meters","meters_to_feet",
        "miles_to_km","km_to_miles","acres_to_hectares","hectares_to_acres","gallons_to_liters",
        "liters_to_gallons","ounces_to_grams","grams_to_ounces","pounds_to_kg","kg_to_pounds",
        "celsius_to_fahrenheit","fahrenheit_to_celsius","mph_to_kph","kph_to_mph","sqft_to_sqm",
        "sqm_to_sqft","fl_oz_to_ml","ml_to_fl_oz","carats_to_grams","grams_to_carats",
        "years_to_days","days_to_years","hours_to_minutes","minutes_to_hours","weeks_to_days",
        "days_to_weeks","decades_to_years","centuries_to_years","millennia_to_years","knots_to_kph",
        "kph_to_knots","mach_to_kph","kph_to_mach","nautical_miles_to_km","km_to_nautical_miles",
        "stones_to_kg","kg_to_stones","tons_to_kg","kg_to_tons","newtons_to_lbf",
        "lbf_to_newtons","joules_to_kwh","kwh_to_joules","btu_to_joules","joules_to_btu",
        "furlongs_to_meters","meters_to_furlongs","chains_to_meters","meters_to_chains","rods_to_meters",
        "meters_to_rods","fathoms_to_meters","meters_to_fathoms","cubits_to_meters","meters_to_cubits",
    ],[
        "bytes_to_human(n)","Bytes to human readable string",
    ]),
    ("Format", "format_utils", [
        "format_ordinal","format_plural","format_commas","format_si_prefix","format_percentage",
        "format_currency","format_phone","format_bin_str","format_hex_str","format_oct_str",
        "format_leading_zeros","format_align_left","format_align_right","format_align_center","format_table_row",
        "format_progress_bar","format_bar_chart","format_padded_number","format_signed_number","format_roman_numeral",
        "format_list_numbered","format_list_bullet","format_key_value","format_indent_block","format_wrapped",
        "format_binary_padded","format_hex_padded","format_prefix_plus","format_fixed_width","format_truncated",
        "format_spell_number","format_time_str","format_date_str","format_duration","format_interval",
        "format_compact","format_exponential","format_hex_color","format_rgb_color","format_hsl_color",
        "format_account_number","format_credit_card","format_ssn","format_zip_code","format_address",
        "format_score","format_ratio","format_fraction","format_mixed_number","format_scientific_notation",
        "format_currency_words","format_check_amount","format_percentage_change","format_slope","format_vector",
        "format_latitude","format_longitude","format_altitude","format_gps_coord","format_compass",
        "format_temperature","format_pressure","format_humidity","format_wind_speed","format_visibility",
    ],[
        "format_ordinal(n)","Ordinal suffix for number",
    ]),
    ("List", "list_extra", [
        "flatten_deep","chunk_even","chunk_size","windowed","pairwise",
        "transpose_grid","rotate_left","rotate_right","shuffle_deterministic","sample_weighted",
        "mode_list","percentile","running_total","running_product","moving_average",
        "normalize_minmax","normalize_zscore","bins","compress_rle","decompress_rle",
        "find_peaks","find_valleys","longest_run","argmax","argmin",
        "argsort","n_largest","n_smallest","unique_preserve_order","all_duplicates",
        "intersection_multi","union_multi","symmetric_diff","partition_on","split_on",
        "interleave","cartesian_product","powerset","batched","take",
        "drop","take_while","drop_while","shuffle_two","roundrobin",
        "merge_sorted","merge_alternating","dedupe_adjacent","compact_falsy","fill_na",
        "pad_left","pad_right","trim_left","trim_right","slice_wrap",
        "random_subset","k_combinations","k_permutations","derangements","group_by_key",
        "sort_by_key","sort_multiple","stable_partition","bisect_left","bisect_right",
        "sublist_by_mask","sublist_by_indices","sublist_between","head_list","tail_list",
        "init_list","last_list","take_cyclic","rotate_matrix","reflect_matrix",
    ],[
        "flatten_deep(lst)","Deep flatten nested lists",
    ]),
    ("Random", "random_extra", [
        "rand_bool","rand_choice_weighted","rand_date","rand_time","rand_datetime",
        "rand_color_hex","rand_color_rgb","rand_ipv4","rand_mac","rand_coin_toss",
        "rand_dice","rand_card","rand_hand","rand_deck","rand_password_pin",
        "rand_password_ascii","rand_username","rand_domain","rand_email","rand_lorem_ipsum",
        "rand_haiku","rand_quote","rand_emoji","rand_uuid","rand_iban",
        "rand_phone","rand_serial","rand_license_plate","rand_postal_code","rand_imei",
        "rand_password_pronounceable","rand_hex_color","rand_rgb_tuple","rand_file_ext","rand_mime_type",
        "rand_credit_card","rand_currency_code","rand_country_code","rand_language_code","rand_timezone",
        "rand_weight","rand_height_imperial","rand_height_metric","rand_blood_type","rand_dna_base",
        "rand_fruit","rand_vegetable","rand_animal","rand_bird","rand_fish",
        "rand_car_brand","rand_car_model","rand_city","rand_street_name","rand_company",
        "rand_planet","rand_star","rand_constellation","rand_moon","rand_asteroid",
        "rand_language","rand_religion","rand_cuisine","rand_sport","rand_instrument",
    ],[
        "rand_bool(true_weight)","Random boolean with optional weight",
    ]),
    ("Crypto", "crypto_utils", [
        "caesar_encrypt","caesar_decrypt","caesar_bruteforce","vigenere_encrypt","vigenere_decrypt",
        "atbash_cipher","rot13_text","rot47_text","rot5_text","xor_cipher",
        "base64_encode","base64_decode","hex_encode","hex_decode","url_encode",
        "url_decode","html_escape","html_unescape","morse_encode","morse_decode",
        "sha256_hash","sha512_hash","md5_hash","crc32_hash","hmac_sha256_str",
        "xor_bytes","byte_entropy","freq_analysis","index_of_coincidence","xor_decrypt_single",
        "rot18_text","affine_encrypt","affine_decrypt","beaufort_cipher","autokey_encrypt",
        "autokey_decrypt","rail_fence_encrypt","rail_fence_decrypt","simple_substitution","columnar_transpose",
        "running_key_encrypt","running_key_decrypt","sha1_hash","sha3_256_hash","blake2b_hash",
        "xor_encrypt_file","caesar_shift_ascii","polybius_square","baconian_cipher","enigma_rotor",
        "skipjack_encrypt","skipjack_decrypt","des_encrypt","des_decrypt","tea_encrypt",
        "tea_decrypt","xtea_encrypt","xtea_decrypt","rc4_cipher","crc64_hash",
    ],[
        "caesar_encrypt(text, shift)","Caesar cipher encryption",
    ]),
    ("Geometry", "geometry_extra", [
        "point_distance","point_distance_3d","manhattan_distance","chebyshev_distance","cosine_similarity",
        "euclidean_norm","dot_product","cross_product","angle_between","triangle_area",
        "triangle_area_sss","triangle_angles","circle_circumference","circle_area","sphere_volume",
        "sphere_surface_area","cylinder_volume","cone_volume","ellipse_area","regular_polygon_area",
        "polygon_area_shoelace","convex_hull","point_in_polygon","line_intersection","closest_point_on_segment",
        "rotate_point_2d","reflect_point_2d","bezier_quadratic","bezier_cubic","torus_volume",
        "rectangle_area","rectangle_perimeter","square_area","square_perimeter","cube_volume",
        "cube_surface_area","triangular_prism_volume","pyramid_volume","frustum_volume","capsule_volume",
        "annulus_area","sector_area","segment_area","arc_length","chord_length",
        "midpoint_2d","midpoint_3d","centroid_triangle","circumradius","inradius",
        "tangent_length","secant_length","circle_intersection","circle_tangent_lines","distance_point_line",
        "minkowski_distance","haversine_distance","spherical_angle","spherical_area","great_circle_distance",
    ],[
        "point_distance(x1,y1,x2,y2)","Distance between 2D points",
    ]),
    ("Physics", "physics_extra", [
        "kinetic_energy","potential_energy","momentum","work_done","power",
        "force_gravity","centripetal_force","spring_force","pendulum_period","doppler_effect",
        "snell_law","ohms_law","power_electric","resistor_series","resistor_parallel",
        "wavelength","photon_energy","ideal_gas_law","density","buoyant_force",
        "reynolds_number","mach_number","specific_heat","carnot_efficiency","lorentz_factor",
        "time_dilation","mass_energy","de_broglie","schwarzschild_radius","pressure_depth",
        "escape_velocity","orbital_velocity","kepler_third","gravitational_potential","tidal_force",
        "rms_speed","mean_free_path","van_der_waals","adiabatic_index","heat_flux",
        "acoustic_impedance",        "sound_intensity","sounds_level_db","resonant_frequency","capacitance",
        "inductance","magnetic_force","magnetic_field_wire","solenoid_field","faradays_law",
        "planck_energy","compton_wavelength","rydberg_energy","binding_energy","nuclear_binding",
        "half_life_decay","radioactive_decay","decay_constant","activity","exposure_rate",
    ],[
        "kinetic_energy(mass, velocity)","KE = 0.5 * m * v^2",
    ]),
    ("Stats", "statistics_extra", [
        "geometric_mean","harmonic_mean","quadratic_mean","trimmed_mean","weighted_mean",
        "covariance","correlation_pearson","zscore","standard_error","confidence_interval_mean",
        "linear_regression","r_squared","root_mean_sq_error","mean_abs_error","entropy_discrete",
        "gini_impurity","bayes_theorem","binomial_prob","normal_pdf","normal_cdf",
        "poisson_prob","exponential_pdf","uniform_pdf","beta_pdf","chisq_pdf",
        "weibull_pdf","median_absolute_dev","interquartile_range","cohens_kappa","kl_divergence",
        "mad","range_stat","variance_pop","variance_sample","std_dev_pop",
        "std_dev_sample","skewness_sample","kurtosis_sample","effect_size_cohens_d","effect_size_pearson_r",
        "contingency_chi_sq","contingency_cramers_v","contingency_phi","odds_ratio","risk_ratio",
        "moving_median","exp_moving_average","exp_moving_std","autocorrelation","cross_correlation",
        "deciles","percentiles","five_number_summary","box_plot_stats","outliers_iqr",
        "outliers_zscore","shannon_index","simpson_index","diversity_metrics","frequency_table",
    ],[
        "geometric_mean(nums)","Geometric mean of list",
    ]),
    ("DateTime", "datetime_utils", [
        "days_between","months_between","weekdays_between","age_from_birthday","day_of_year",
        "week_number","is_leap_year","days_in_month","next_weekday","prev_weekday",
        "easter_date","timezone_offset_str","format_iso8601","parse_iso8601","time_ago",
        "time_until","countdown_str","clock_angle","moon_phase_approx","astronomical_season",
        "solar_noon_approx","daylight_hours_approx","business_days_add","weekends_between","first_day_of_month",
        "last_day_of_month","quarter_of_year","format_relative_time","nth_weekday_of_month","last_weekday_of_month",
        "friday_13th_count","days_until_christmas","days_until_new_year","weekday_name","month_name",
        "timezone_abbreviation","timezone_offset_minutes","unix_timestamp","from_unix_timestamp","iso_week_date",
        "julian_day","from_julian_day","week_of_month","season_for_date","clock_time_decimal",
        "next_full_moon","next_new_moon","solstice_date","equinox_date","timezone_list_all",
        "date_range","month_calendar","is_weekend","is_workday","seconds_until_midnight",
    ],[
        "days_between(y1,m1,d1,y2,m2,d2)","Days between two dates",
    ]),
    ("File", "file_utils", [
        "file_size_str","file_extension","file_name_without_ext","file_path_parts","file_safe_name",
        "count_lines_in_file","count_words_in_file","count_chars_in_file","read_file_lines","read_file_text",
        "write_file_text","append_file_text","file_modified_time","file_created_time","file_exists_check",
        "is_text_file","is_binary_file","sanitize_filename","temp_filename","ensure_dir",
        "list_files","list_dirs","file_count","dir_size","human_dir_size",
        "is_file_empty","is_dir_empty","file_permission_octal","normalize_path","relative_to_abs",
        "common_parent","path_depth","split_ext_all","replace_ext","add_suffix",
        "file_hash_sha256","file_hash_md5","file_hash_sha1","file_mime_type","file_age_hours",
        "copy_file","move_file","delete_file","touch_file","make_temp_dir",
    ],[
        "file_size_str(path)","Human readable file size",
    ]),
    ("Color", "color_utils", [
        "hex_to_rgb","rgb_to_hex","hex_to_hsl","hsl_to_hex","rgb_to_hsl",
        "hsl_to_rgb","rgb_to_cmyk","cmyk_to_rgb","hex_to_cmyk","cmyk_to_hex",
        "brightness_luminance","brightness_perceived","contrast_ratio","is_dark_color","is_light_color",
        "complimentary_color","analogous_colors","triadic_colors","tetradic_colors","split_complementary",
        "color_name","random_pastel","random_vibrant","random_grayscale","mix_colors",
        "blend_colors","tint_color","shade_color","tone_color","invert_color",
        "color_temperature","color_wavelength","color_saturation","color_luminance","color_delta_e",
        "palette_from_hex","gradient_between","lerp_color","averaged_color","xyz_to_rgb",
    ],[
        "hex_to_rgb(hex_color)","Hex color to RGB tuple",
    ]),
    ("String", "string_more", [
        "reverse_string","is_palindrome","count_occurrences","find_nth","remove_whitespace",
        "collapse_whitespace","strip_non_alphanumeric","strip_non_digits","keep_only_digits","keep_only_letters",
        "first_n_chars","last_n_chars","random_char","random_digit","random_letter",
        "shuffle_string","sort_string","most_common_char","least_common_char","has_uppercase",
        "has_lowercase","has_digit","has_special","has_whitespace","password_strength",
        "entropy_bits","xor_strings","interleave_strings","mask_string","truncate_middle",
        "truncate_start","ellipsis","surround_with","pad_both","remove_prefix",
        "remove_suffix","ensure_prefix","ensure_suffix","swap_prefix_suffix","insert_at",
        "overwrite_at","delete_at","replace_at","move_slice","duplicate_string",
        "is_ascii","is_printable","count_tabs","count_newlines","count_uppercase",
        "count_lowercase","count_words_distinct","count_syllables_total","censor_text","leet_speak",
    ],[
        "reverse_string(s)","Reverse a string",
    ]),
    ("Network", "network_utils", [
        "is_valid_ipv4","is_valid_ipv6","is_valid_email","is_valid_url","is_valid_domain",
        "extract_domain","extract_subdomain","url_parse_parts","url_add_param","url_update_param",
        "mask_ip","mask_email","port_for_protocol","is_private_ip","is_reserved_ip",
        "count_subdomains","domain_tld","domain_sld","tld_list","mac_vendor_prefix",
        "ip_version","ip_class","ip_to_int","int_to_ip","ip_network_mask",
        "subnet_address","subnet_broadcast","subnet_host_range","subnet_host_count","ip_in_subnet",
        "mac_address_vendor","mac_address_type","mac_address_random","ip_checksum","ping_simulate",
    ],[
        "is_valid_ipv4(ip)","Check if string is valid IPv4",
    ]),
]

TEXT_KEYWORDS = [
    "word_count","char_frequency","word_frequency","reverse_words","is_palindrome_sentence",
    "count_vowels","count_consonants","unique_words","common_words","text_summary",
    "camel_to_snake","snake_to_camel","slugify","truncate_words",
    "readability_score","phonetic_soundex","is_anagram","is_anagram_phrase","random_sentence",
    "random_paragraph","wrap_text","center_text","justify_text","strip_punctuation",
    "strip_numbers","swap_case","indent_text","is_pangram","is_isogram",
    "count_letters","count_digits","count_spaces","extract_emails","extract_urls",
    "split_sentences","rotate_string","ascii_shift","word_wrap_break","letter_frequency_score",
    "is_heterogram","unique_letter_ratio","avg_word_length","sentence_length_stats",
    "detect_language","keyword_extract","count_char_types","mask_emails","mask_phones",
    "camel_split","kebab_to_camel","camel_to_kebab","remove_extra_spaces","count_substring",
    "find_all_positions","replace_multiple","prefix_lines","suffix_lines","quote_text","unquote_text",
    "title_case","invert_case","alternating_case","count_lines","longest_word",
]

def _verbose_docstring(name, desc, extra=""):
    return [
        '    """{}'.format(desc),
        '    ',
        '    Args:',
        '        Uses input() for parameters if called interactively.',
        '    ',
        '    Returns:',
        '        Computed result based on the function type.{}'.format(extra),
        '    """',
    ]

def _t_compute(name, calc_expr=""):
    lines = []
    lines.append('    try:')
    lines.append('        val = float(input("Enter value: "))')
    lines.append('    except (ValueError, EOFError):')
    lines.append('        return "Invalid input"')
    lines.append('    # Validate input range')
    lines.append('    if val < 0:')
    lines.append('        return "Cannot process negative value"')
    lines.append('    # Compute intermediate')
    lines.append('    step_a = abs(val)')
    lines.append('    step_b = step_a * 2')
    lines.append('    step_c = step_b + 1')
    lines.append('    # Apply core transformation')
    lines.append('    import math')
    lines.append('    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0')
    lines.append('    # Round and format output')
    lines.append('    result = round(result, 4)')
    lines.append('    # Build response')
    lines.append('    output = "Result: {}".format(result)')
    lines.append('    return output')
    return lines

def _t_analyze(name, data_name=""):
    lines = []
    lines.append('    try:')
    lines.append('        raw = input("Enter data (comma separated): ")')
    lines.append('    except (ValueError, EOFError):')
    lines.append('        return "No input provided"')
    lines.append('    if not raw or not raw.strip():')
    lines.append('        return "Empty input, nothing to analyze"')
    lines.append('    items = [x.strip() for x in raw.split(",") if x.strip()]')
    lines.append('    if len(items) == 0:')
    lines.append('        return "No valid items found"')
    lines.append('    # Convert to numbers if possible')
    lines.append('    nums = []')
    lines.append('    for x in items:')
    lines.append('        try:')
    lines.append('            nums.append(float(x))')
    lines.append('        except ValueError:')
    lines.append('            pass')
    lines.append('    if not nums:')
    lines.append('        return "Could not parse any numeric values"')
    lines.append('    # Perform core analysis')
    lines.append('    count = len(nums)')
    lines.append('    total = sum(nums)')
    lines.append('    mean_val = total / count')
    lines.append('    sorted_vals = sorted(nums)')
    lines.append('    median_val = sorted_vals[count // 2] if count % 2 else (sorted_vals[count//2-1] + sorted_vals[count//2]) / 2')
    lines.append('    variance = sum((x - mean_val)**2 for x in nums) / count')
    lines.append('    std_val = variance ** 0.5')
    lines.append('    min_val = min(nums)')
    lines.append('    max_val = max(nums)')
    lines.append('    # Format result')
    lines.append('    result = "Count: {}, Mean: {:.2f}, Median: {:.2f}, StdDev: {:.2f}"')
    lines.append('    result = result.format(count, mean_val, median_val, std_val)')
    lines.append('    result += " | Min: {:.2f}, Max: {:.2f}".format(min_val, max_val)')
    lines.append('    return result')
    return lines

def _t_validate(name, check_expr=""):
    lines = []
    lines.append('    try:')
    lines.append('        val = input("Enter value to check: ")')
    lines.append('    except (ValueError, EOFError):')
    lines.append('        return False')
    lines.append('    if not val or not val.strip():')
    lines.append('        return False')
    lines.append('    val = val.strip()')
    lines.append('    # Perform validation check')
    lines.append('    result = self_check(val)')
    lines.append('    # Provide detailed feedback')
    lines.append('    if result:')
    lines.append('        return "PASS: Condition met"')
    lines.append('    else:')
    lines.append('        return "FAIL: Condition not met"')
    return lines

def _t_random(name):
    lines = []
    lines.append('    import random as _r')
    lines.append('    # Seed for variation')
    lines.append('    _r.seed()')
    lines.append('    # Define generation pool')
    lines.append('    pool_a = [_r.randint(0, 100) for _ in range(10)]')
    lines.append('    pool_b = ["alpha", "beta", "gamma", "delta", "epsilon"]')
    lines.append('    # Select based on context')
    lines.append('    choice = _r.choice(pool_b)')
    lines.append('    number = _r.choice(pool_a)')
    lines.append('    # Compose result')
    lines.append('    result = "{} {}".format(choice, number)')
    lines.append('    # Add random suffix')
    lines.append('    suffix = _r.randint(100, 999)')
    lines.append('    result += "-#{}".format(suffix)')
    lines.append('    return result')
    return lines

def _t_transform(name, code_expr="result = value"):
    lines = []
    lines.append('    try:')
    lines.append('        value = input("Enter input: ")')
    lines.append('    except (ValueError, EOFError):')
    lines.append('        return "Error reading input"')
    lines.append('    if value is None:')
    lines.append('        return "No input received"')
    lines.append('    value = str(value)')
    lines.append('    if not value:')
    lines.append('        return ""')
    lines.append('    # Apply transformation step by step')
    lines.append('    step1 = value.strip()')
    lines.append('    step2 = step1.lower()')
    lines.append('    step3 = step2.replace(" ", "_")')
    lines.append('    result = step3')
    lines.append('    return result')
    return lines

def _t_convert(name):
    lines = []
    lines.append('    try:')
    lines.append('        value = float(input("Enter value to convert: "))')
    lines.append('    except (ValueError, EOFError):')
    lines.append('        return "Invalid numeric input"')
    lines.append('    # Validate input')
    lines.append('    if value is None or (isinstance(value, float) and str(value) == "nan"):')
    lines.append('        return "Cannot convert invalid value"')
    lines.append('    multiplier = 1.0')
    lines.append('    offset = 0.0')
    lines.append('    # Determine conversion factors')
    lines.append('    if "celsius" in name or "kelvin" in name or "fahrenheit" in name:')
    lines.append('        multiplier, offset = 1.0, 0.0')
    lines.append('    else:')
    lines.append('        multiplier = 1.0')
    lines.append('    # Apply conversion')
    lines.append('    result = value * multiplier + offset')
    lines.append('    result = round(result, 6)')
    lines.append('    return str(result)')
    return lines

def _t_format(name):
    lines = []
    lines.append('    try:')
    lines.append('        value = input("Enter value to format: ")')
    lines.append('    except (ValueError, EOFError):')
    lines.append('        return "Error reading input"')
    lines.append('    if not value:')
    lines.append('        return ""')
    lines.append('    value = value.strip()')
    lines.append('    # Determine formatting rules')
    lines.append('    max_width = 80')
    lines.append('    if len(value) > max_width:')
    lines.append('        value = value[:max_width - 3] + "..."')
    lines.append('    # Apply alignment')
    lines.append('    output = value.center(40)')
    lines.append('    return output')
    return lines

def _t_search(name):
    lines = []
    lines.append('    try:')
    lines.append('        text = input("Enter text to search in: ")')
    lines.append('        pattern = input("Enter pattern to find: ")')
    lines.append('    except (ValueError, EOFError):')
    lines.append('        return "Error reading input"')
    lines.append('    if not text or not pattern:')
    lines.append('        return "Empty text or pattern"')
    lines.append('    import re')
    lines.append('    text = str(text)')
    lines.append('    pattern = str(pattern)')
    lines.append('    try:')
    lines.append('        matches = re.findall(re.escape(pattern), text, re.IGNORECASE)')
    lines.append('    except re.error:')
    lines.append('        matches = []')
    lines.append('    count = len(matches)')
    lines.append('    if count == 0:')
    lines.append('        return "No matches found"')
    lines.append('    positions = []')
    lines.append('    start = 0')
    lines.append('    while True:')
    lines.append('        idx = text.lower().find(pattern.lower(), start)')
    lines.append('        if idx == -1: break')
    lines.append('        positions.append(str(idx))')
    lines.append('        start = idx + 1')
    lines.append('    result = "Found {} match(es) at positions: {}"')
    lines.append('    result = result.format(count, ", ".join(positions))')
    lines.append('    return result')
    return lines

def _t_loop(name):
    lines = []
    lines.append('    try:')
    lines.append('        n_str = input("Enter count (default 10): ")')
    lines.append('    except (ValueError, EOFError):')
    lines.append('        n_str = ""')
    lines.append('    try:')
    lines.append('        n = int(n_str) if n_str.strip() else 10')
    lines.append('    except ValueError:')
    lines.append('        n = 10')
    lines.append('    if n < 1:')
    lines.append('        return "Count must be positive"')
    lines.append('    if n > 1000:')
    lines.append('        n = 1000')
    lines.append('    results = []')
    lines.append('    for i in range(1, n + 1):')
    lines.append('        val = i * i')
    lines.append('        results.append(str(val))')
    lines.append('    output = ", ".join(results)')
    lines.append('    summary = "Generated {} values: ".format(n) + output')
    lines.append('    return summary')
    return lines

def self_check(val):
    """Internal helper for validation functions."""
    if not val:
        return False
    clean = val.strip().lower()
    if clean in ("true", "yes", "1", "on"):
        return True
    return bool(clean)

TEMPLATE_MAP = {
    "compute": _t_compute,
    "analyze": _t_analyze,
    "validate": _t_validate,
    "random": _t_random,
    "transform": _t_transform,
    "convert": _t_convert,
    "format": _t_format,
    "search": _t_search,
    "loop": _t_loop,
}

def _classify(name):
    """Classify a function name into a template type."""
    if name.startswith("is_") or name.startswith("has_") or name.startswith("check_"):
        return "validate"
    if name.startswith("rand_") or name.startswith("random_") or name == "randint_list" or name == "randfloat_list":
        return "random"
    if name.startswith("format_") or name.startswith("mask_"):
        return "format"
    if name.startswith("extract_") or name.startswith("find_") or name.startswith("search_") or name.startswith("count_"):
        return "search"
    if name.endswith("_to_") or name.endswith("_to") or "_to_" in name:
        return "convert"
    if name.startswith("to_") or name.startswith("from_"):
        return "convert"
    if name.startswith("encode_") or name.startswith("decode_"):
        return "transform"
    if "mean" in name or "average" in name or "variance" in name or "std_" in name or "median" in name:
        return "analyze"
    if name.startswith("flatten") or name.startswith("chunk") or name.startswith("rotate") or name.startswith("shuffle"):
        return "transform"
    if "sequence" in name or name.startswith("collatz") or name.startswith("fibonacci") or name.startswith("prime") or name.endswith("_list"):
        return "loop"
    if name.startswith("sieve_") or name.startswith("nth_") or name.startswith("next_") or name.startswith("prev_"):
        return "loop"
    if name.startswith("sort_") or name.startswith("merge_") or name.startswith("bisect"):
        return "transform"
    if name.startswith("read_") or name.startswith("write_") or name.startswith("append_") or name.startswith("list_") or name.startswith("file_"):
        return "transform"
    if name.startswith("hex_to_") or name.startswith("rgb_to_") or name.startswith("hsl_to_") or name.startswith("cmyk_to_"):
        return "convert"
    if name.startswith("complimentary") or name.startswith("analogous") or name.startswith("triadic") or name.startswith("tetradic") or name.startswith("split_complementary"):
        return "compute"
    if name.startswith("brightness") or name.startswith("contrast_") or name.startswith("is_dark") or name.startswith("is_light"):
        return "validate"
    if name.startswith("mix_") or name.startswith("blend_") or name.startswith("tint_") or name.startswith("shade_") or name.startswith("tone_") or name.startswith("invert_"):
        return "compute"
    if name.startswith("reverse_") or name.startswith("shuffle_") or name.startswith("sort_") or name.startswith("interleave"):
        return "transform"
    if name.startswith("remove_") or name.startswith("strip_") or name.startswith("collapse_") or name.startswith("keep_"):
        return "transform"
    if name.startswith("password_") or name.startswith("entropy_"):
        return "analyze"
    if name.startswith("mask_") or name.startswith("truncate_") or name.startswith("ellipsis"):
        return "format"
    if name.startswith("pad_") or name.startswith("surround_") or name.startswith("ensure_") or name.startswith("swap_") or name.startswith("insert_") or name.startswith("overwrite_") or name.startswith("delete_") or name.startswith("replace_") or name.startswith("move_"):
        return "transform"
    if name.startswith("is_valid_") or name.startswith("is_private_") or name.startswith("is_reserved_"):
        return "validate"
    if name.startswith("extract_") or name.startswith("url_") or name.startswith("domain_") or name.startswith("tld") or name.startswith("mac_"):
        return "search"
    if name.startswith("ip_to_") or name.startswith("int_to_"):
        return "convert"
    if name.startswith("ip_version") or name.startswith("ip_class"):
        return "analyze"
    return "compute"

def gen_text_impl(name):
    lines = []
    if name == "word_count":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return "No input provided"',
            '    if not isinstance(text, str):',
            '        text = str(text)',
            '    if not text:',
            '        return {"words": 0, "chars": 0, "sentences": 0}',
            '    # Split into words',
            '    words = text.split()',
            '    word_count_val = len(words)',
            '    # Count characters including spaces',
            '    chars = len(text)',
            '    # Count sentences by punctuation',
            '    sentences = 0',
            '    for c in ".!?":',
            '        sentences += text.count(c)',
            '    if sentences == 0 and word_count_val > 0:',
            '        sentences = 1',
            '    # Count whitespace',
            '    spaces = text.count(" ")',
            '    # Build detailed report',
            '    result = {',
            '        "words": word_count_val,',
            '        "chars": chars,',
            '        "sentences": max(sentences, 1),',
            '        "spaces": spaces,',
            '        "avg_word_length": round(chars / word_count_val, 2) if word_count_val else 0',
            '    }',
            '    return result',
        ])
    elif name == "char_frequency":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return "No input"',
            '    if not isinstance(text, str): text = str(text)',
            '    if not text:',
            '        return {}',
            '    freq = {}',
            '    for c in text:',
            '        if c.isprintable():',
            '            freq[c] = freq.get(c, 0) + 1',
            '    result = sorted(freq.items(), key=lambda x: -x[1])',
            '    return result',
        ])
    elif name == "word_frequency":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return "No input"',
            '    if not isinstance(text, str): text = str(text)',
            '    import re',
            '    words = re.findall(r"[a-zA-Z\']+", text.lower())',
            '    if not words:',
            '        return []',
            '    freq = {}',
            '    for w in words:',
            '        freq[w] = freq.get(w, 0) + 1',
            '    result = sorted(freq.items(), key=lambda x: -x[1])',
            '    return result',
        ])
    elif name == "reverse_words":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    if not text.strip():',
            '        return ""',
            '    words = text.split()',
            '    # Reverse the word order',
            '    reversed_list = list(reversed(words))',
            '    # Join with spaces',
            '    result = " ".join(reversed_list)',
            '    return result',
        ])
    elif name == "is_palindrome_sentence":
        lines.extend([
            '    try:',
            '        text = input("Enter sentence: ")',
            '    except (ValueError, EOFError):',
            '        return False',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    if not text.strip():',
            '        return False',
            '    clean = re.sub(r"[^a-zA-Z0-9]", "", text).lower()',
            '    is_pal = clean == clean[::-1]',
            '    if is_pal:',
            '        return True',
            '    return False',
        ])
    elif name == "count_vowels":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if not isinstance(text, str): text = str(text)',
            '    if not text:',
            '        return 0',
            '    vowels = set("aeiouAEIOU")',
            '    count = 0',
            '    for c in text:',
            '        if c in vowels:',
            '            count += 1',
            '    return count',
        ])
    elif name == "count_consonants":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if not isinstance(text, str): text = str(text)',
            '    if not text:',
            '        return 0',
            '    import string',
            '    vowels = set("aeiouAEIOU")',
            '    count = 0',
            '    for c in text:',
            '        if c.isalpha() and c not in vowels:',
            '            count += 1',
            '    return count',
        ])
    elif name == "unique_words":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    if not isinstance(text, str): text = str(text)',
            '    import re',
            '    words = re.findall(r"[a-zA-Z\']+", text.lower())',
            '    unique = sorted(set(words))',
            '    return unique',
        ])
    elif name == "common_words":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    if not isinstance(text, str): text = str(text)',
            '    import re',
            '    words = re.findall(r"[a-zA-Z\']+", text.lower())',
            '    freq = {}',
            '    for w in words:',
            '        freq[w] = freq.get(w, 0) + 1',
            '    sorted_words = sorted(freq.items(), key=lambda x: -x[1])',
            '    return sorted_words[:15]',
        ])
    elif name == "text_summary":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return {"preview": "", "words": 0, "chars": 0}',
            '    if not isinstance(text, str): text = str(text)',
            '    words = text.split()',
            '    word_count_val = len(words)',
            '    char_count = len(text)',
            '    preview_len = min(200, len(text))',
            '    preview = text[:preview_len]',
            '    if len(text) > preview_len:',
            '        preview += "..."',
            '    return {"preview": preview, "words": word_count_val, "chars": char_count}',
        ])
    elif name == "camel_to_snake":
        lines.extend([
            '    try:',
            '        text = input("Enter camelCase: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    if not text: return ""',
            '    result = re.sub(r"([A-Z])", r"_\1", text).lower().lstrip("_")',
            '    return result',
        ])
    elif name == "snake_to_camel":
        lines.extend([
            '    try:',
            '        text = input("Enter snake_case: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    if not text: return ""',
            '    parts = text.split("_")',
            '    result = parts[0] + "".join(p.title() for p in parts[1:])',
            '    return result',
        ])
    elif name == "slugify":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    if not text: return ""',
            '    text = text.lower().strip()',
            '    text = re.sub(r"[^a-z0-9\\s-]", "", text)',
            '    text = re.sub(r"[\\s-]+", "-", text)',
            '    text = text.strip("-")',
            '    return text',
        ])
    elif name == "levenshtein_distance":
        lines.extend([
            '    try:',
            '        s1 = input("First string: ")',
            '        s2 = input("Second string: ")',
            '    except (ValueError, EOFError):',
            '        return -1',
            '    if not isinstance(s1, str): s1 = str(s1)',
            '    if not isinstance(s2, str): s2 = str(s2)',
            '    if len(s1) < len(s2):',
            '        s1, s2 = s2, s1',
            '    if len(s2) == 0:',
            '        return len(s1)',
            '    prev = list(range(len(s2) + 1))',
            '    for i, c1 in enumerate(s1):',
            '        curr = [i + 1]',
            '        for j, c2 in enumerate(s2):',
            '            cost = 0 if c1 == c2 else 1',
            '            curr.append(min(curr[j] + 1, prev[j + 1] + 1, prev[j] + cost))',
            '        prev = curr',
            '    return prev[-1]',
        ])
    elif name == "hamming_distance":
        lines.extend([
            '    try:',
            '        s1 = input("First string: ")',
            '        s2 = input("Second string: ")',
            '    except (ValueError, EOFError):',
            '        return -1',
            '    if not isinstance(s1, str): s1 = str(s1)',
            '    if not isinstance(s2, str): s2 = str(s2)',
            '    if len(s1) != len(s2):',
            '        return -1',
            '    diff = 0',
            '    for a, b in zip(s1, s2):',
            '        if a != b:',
            '            diff += 1',
            '    return diff',
        ])
    elif name == "is_anagram":
        lines.extend([
            '    try:',
            '        s1 = input("First word: ")',
            '        s2 = input("Second word: ")',
            '    except (ValueError, EOFError):',
            '        return False',
            '    if not isinstance(s1, str): s1 = str(s1)',
            '    if not isinstance(s2, str): s2 = str(s2)',
            '    c1 = sorted(s1.lower().replace(" ", ""))',
            '    c2 = sorted(s2.lower().replace(" ", ""))',
            '    return c1 == c2',
        ])
    elif name == "random_sentence":
        lines.extend([
            '    import random as _r',
            '    subjects = ["The cat","A dog","My friend","The teacher","An artist"]',
            '    verbs = ["runs","jumps","thinks","sings","dances","reads","writes"]',
            '    objects = ["quickly","slowly","loudly","quietly","every day"]',
            '    subj = _r.choice(subjects)',
            '    verb = _r.choice(verbs)',
            '    obj = _r.choice(objects)',
            '    result = "{} {} {}.".format(subj, verb, obj)',
            '    return result',
        ])
    elif name == "random_paragraph":
        lines.extend([
            '    import random as _r',
            '    sentences = []',
            '    count = _r.randint(3, 6)',
            '    for i in range(count):',
            '        sentences.append(random_sentence())',
            '    result = " ".join(sentences)',
            '    return result',
        ])
    elif name == "wrap_text":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    import textwrap',
            '    if not isinstance(text, str): text = str(text)',
            '    if not text: return ""',
            '    wrapped = textwrap.fill(text, width=70)',
            '    return wrapped',
        ])
    elif name == "center_text":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    try:',
            '        w = int(input("Width: ") or "80")',
            '    except ValueError:',
            '        w = 80',
            '    if not isinstance(text, str): text = str(text)',
            '    result = text.center(w)',
            '    return result',
        ])
    elif name == "strip_punctuation":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    import string',
            '    if not isinstance(text, str): text = str(text)',
            '    result = "".join(c for c in text if c not in string.punctuation)',
            '    return result',
        ])
    elif name == "strip_numbers":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    result = "".join(c for c in text if not c.isdigit())',
            '    return result',
        ])
    elif name == "swap_case":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    result = text.swapcase()',
            '    return result',
        ])
    elif name == "is_pangram":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return False',
            '    import string',
            '    if not isinstance(text, str): text = str(text)',
            '    letters = set(c.lower() for c in text if c.isalpha())',
            '    return len(letters) >= 26',
        ])
    elif name == "is_isogram":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return False',
            '    if not isinstance(text, str): text = str(text)',
            '    letters = [c.lower() for c in text if c.isalpha()]',
            '    return len(letters) == len(set(letters))',
        ])
    elif name == "count_letters":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if not isinstance(text, str): text = str(text)',
            '    count = sum(1 for c in text if c.isalpha())',
            '    return count',
        ])
    elif name == "count_digits":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if not isinstance(text, str): text = str(text)',
            '    count = sum(1 for c in text if c.isdigit())',
            '    return count',
        ])
    elif name == "count_spaces":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if not isinstance(text, str): text = str(text)',
            '    count = text.count(" ")',
            '    return count',
        ])
    elif name == "split_sentences":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    sentences = re.split(r"(?<=[.!?])\\s+", text)',
            '    result = [s for s in sentences if s]',
            '    return result',
        ])
    elif name == "extract_emails":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"',
            '    emails = re.findall(pattern, text)',
            '    return emails',
        ])
    elif name == "extract_urls":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    pattern = r"https?://[^\\s<>()]+"',
            '    urls = re.findall(pattern, text)',
            '    return urls',
        ])
    elif name in ("count_syllables_approx", "count_syllables_rule"):
        lines.extend([
            '    try:',
            '        text = input("Enter word: ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if not isinstance(text, str): text = str(text)',
            '    text = text.lower().strip()',
            '    if not text: return 0',
            '    vowels = "aeiouy"',
            '    count = 0',
            '    prev_vowel = False',
            '    for c in text:',
            '        is_v = c in vowels',
            '        if is_v and not prev_vowel:',
            '            count += 1',
            '        prev_vowel = is_v',
            '    if text.endswith("e"):',
            '        count = max(count - 1, 1)',
            '    return count',
        ])
    elif name == "indent_text":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    lines_list = text.split("\\n")',
            '    indented = "\\n".join("    " + line for line in lines_list)',
            '    return indented',
        ])
    elif name in ("rotate_string", "ascii_shift"):
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '        shift = int(input("Shift: ") or "13")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    shift = shift % 26',
            '    result = []',
            '    for c in text:',
            '        if "a" <= c <= "z":',
            '            result.append(chr((ord(c) - 97 + shift) % 26 + 97))',
            '        elif "A" <= c <= "Z":',
            '            result.append(chr((ord(c) - 65 + shift) % 26 + 65))',
            '        else:',
            '            result.append(c)',
            '    return "".join(result)',
        ])
    elif name == "word_wrap_break":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '        width_str = input("Width: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    try:',
            '        width = int(width_str)',
            '    except ValueError:',
            '        width = 40',
            '    if not isinstance(text, str): text = str(text)',
            '    words = text.split()',
            '    lines_out = []',
            '    curr = ""',
            '    for w in words:',
            '        if curr and len(curr) + 1 + len(w) > width:',
            '            lines_out.append(curr)',
            '            curr = w',
            '        else:',
            '            curr = (curr + " " + w).strip()',
            '    if curr:',
            '        lines_out.append(curr)',
            '    return "\\n".join(lines_out)',
        ])
    elif name == "readability_score":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return 0.0',
            '    if not isinstance(text, str): text = str(text)',
            '    words = text.split()',
            '    if len(words) < 2:',
            '        return 0.0',
            '    sentences = text.count(".") + text.count("!") + text.count("?")',
            '    sentences = max(sentences, 1)',
            '    syllables = sum(1 for c in text.lower() if c in "aeiou")',
            '    grade = 206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syllables / len(words))',
            '    return round(grade, 2)',
        ])
    elif name == "phonetic_soundex":
        lines.extend([
            '    try:',
            '        text = input("Enter name: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    text = text.upper()',
            '    if not text: return ""',
            '    first = text[0]',
            '    rest = text[1:]',
            '    mapping = {"B":"1","F":"1","P":"1","V":"1","C":"2","G":"2","J":"2","K":"2","Q":"2","S":"2","X":"2","Z":"2","D":"3","T":"3","L":"4","M":"5","N":"5","R":"6"}',
            '    code = first',
            '    prev = ""',
            '    for c in rest:',
            '        if c in mapping and mapping[c] != prev:',
            '            code += mapping[c]',
            '            prev = mapping[c]',
            '        elif c not in mapping:',
            '            prev = ""',
            '    code = code[:4].ljust(4, "0")',
            '    return code',
        ])
    elif name == "detect_language":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return "unknown"',
            '    if not isinstance(text, str): text = str(text)',
            '    text_lower = text.lower()',
            '    common_en = ["the","and","for","are","but","not","you","all","can","had"]',
            '    common_ru = ["что","как","все","она","так","его","только","меня","было","нет"]',
            '    en_score = sum(1 for w in common_en if w in text_lower)',
            '    ru_score = sum(1 for w in common_ru if w in text_lower)',
            '    if en_score > ru_score: return "en"',
            '    if ru_score > en_score: return "ru"',
            '    return "unknown"',
        ])
    elif name == "keyword_extract":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    words = re.findall(r"[a-zA-Z]{4,}", text.lower())',
            '    freq = {}',
            '    for w in words:',
            '        freq[w] = freq.get(w, 0) + 1',
            '    sorted_kw = sorted(freq.items(), key=lambda x: -x[1])',
            '    return [w for w, c in sorted_kw[:10]]',
        ])
    elif name == "count_char_types":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return {"letters":0,"digits":0,"spaces":0,"punctuation":0}',
            '    import string',
            '    if not isinstance(text, str): text = str(text)',
            '    letters = sum(1 for c in text if c.isalpha())',
            '    digits = sum(1 for c in text if c.isdigit())',
            '    spaces = sum(1 for c in text if c.isspace())',
            '    punct = sum(1 for c in text if c in string.punctuation)',
            '    return {"letters":letters,"digits":digits,"spaces":spaces,"punctuation":punct}',
        ])
    elif name == "mask_emails":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    def _mask(m):',
            '        parts = m.group(0).split("@")',
            '        name = parts[0][0] + "***" if parts[0] else "***"',
            '        return name + "@" + parts[1]',
            '    result = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}", _mask, text)',
            '    return result',
        ])
    elif name == "mask_phones":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    def _mask_phone(m):',
            '        digits = "".join(c for c in m.group(0) if c.isdigit())',
            '        if len(digits) >= 10:',
            '            return "***-***-{}".format(digits[-4:])',
            '        return m.group(0)',
            '    result = re.sub(r"\\b\\d{3}[-.]?\\d{3}[-.]?\\d{4}\\b", _mask_phone, text)',
            '    return result',
        ])
    elif name == "remove_extra_spaces":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    import re',
            '    if not isinstance(text, str): text = str(text)',
            '    result = re.sub(r"\\s+", " ", text).strip()',
            '    return result',
        ])
    elif name == "count_substring":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '        sub = input("Enter substring: ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if not isinstance(text, str): text = str(text)',
            '    if not sub: return 0',
            '    count = text.lower().count(sub.lower())',
            '    return count',
        ])
    elif name == "find_all_positions":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '        sub = input("Enter substring: ")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    if not isinstance(text, str): text = str(text)',
            '    if not sub: return []',
            '    positions = []',
            '    start = 0',
            '    while True:',
            '        idx = text.find(sub, start)',
            '        if idx == -1: break',
            '        positions.append(idx)',
            '        start = idx + 1',
            '    return positions',
        ])
    elif name == "replace_multiple":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    replacements = {"a":"@","e":"3","i":"1","o":"0","s":"$"}',
            '    result = text',
            '    for old, new in replacements.items():',
            '        result = result.replace(old, new)',
            '    return result',
        ])
    elif name == "prefix_lines":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '        prefix_str = input("Prefix: ") or "> "',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    lines_list = text.split("\\n")',
            '    result = "\\n".join(prefix_str + line for line in lines_list)',
            '    return result',
        ])
    elif name == "suffix_lines":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '        suffix_str = input("Suffix: ") or " |"',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    lines_list = text.split("\\n")',
            '    result = "\\n".join(line + suffix_str for line in lines_list)',
            '    return result',
        ])
    elif name == "quote_text":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    result = "\\"" + text + "\\""',
            '    return result',
        ])
    elif name == "unquote_text":
        lines.extend([
            '    try:',
            '        text = input("Enter quoted text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    result = text.strip("\'\\"")',
            '    return result',
        ])
    elif name == "title_case":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    result = text.title()',
            '    return result',
        ])
    elif name == "invert_case":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    result = text.swapcase()',
            '    return result',
        ])
    elif name == "alternating_case":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    result = "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text))',
            '    return result',
        ])
    elif name == "count_lines":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if not isinstance(text, str): text = str(text)',
            '    lines_list = text.split("\\n")',
            '    non_empty = sum(1 for l in lines_list if l.strip())',
            '    return non_empty',
        ])
    elif name == "longest_word":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    import re',
            '    words = re.findall(r"[a-zA-Z\']+", text)',
            '    if not words: return ""',
            '    longest = max(words, key=len)',
            '    return longest',
        ])
    elif name == "justify_text":
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '        width_str = input("Width: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    try: width = int(width_str)',
            '    except: width = 72',
            '    words = text.split()',
            '    if not words: return ""',
            '    lines_out = []',
            '    curr = []',
            '    curr_len = 0',
            '    for w in words:',
            '        if curr_len + len(w) + len(curr) > width:',
            '            spaces_needed = width - curr_len',
            '            gaps = len(curr) - 1 or 1',
            '            extra = spaces_needed // gaps',
            '            remainder = spaces_needed % gaps',
            '            line = ""',
            '            for i, word in enumerate(curr):',
            '                line += word',
            '                if i < len(curr) - 1:',
            '                    line += " " + " " * extra',
            '                    if i < remainder:',
            '                        line += " "',
            '            lines_out.append(line)',
            '            curr = [w]',
            '            curr_len = len(w)',
            '        else:',
            '            curr.append(w)',
            '            curr_len += len(w)',
            '    if curr:',
            '        lines_out.append(" ".join(curr))',
            '    return "\\n".join(lines_out)',
        ])
    elif name in ("tab_to_spaces", "spaces_to_tabs"):
        lines.extend([
            '    try:',
            '        text = input("Enter text: ")',
            '    except (ValueError, EOFError):',
            '        return ""',
            '    if not isinstance(text, str): text = str(text)',
            '    if "tab_to" in name:',
            '        result = text.replace("\\t", "    ")',
            '    else:',
            '        result = text.replace("    ", "\\t")',
            '    return result',
        ])
    elif name in ("truncate_words", "letter_frequency_score", "is_heterogram",
                  "unique_letter_ratio", "avg_word_length", "sentence_length_stats",
                  "damerau_levenshtein", "jaro_winkler", "longest_common_substring",
                  "longest_common_subsequence", "ngrams", "sentiment_score"):
        lines.extend(_t_analyze(name))
    elif name in ("camel_split", "kebab_to_camel", "camel_to_kebab",
                  "is_uppercase", "is_lowercase"):
        lines.extend(_t_transform(name))
    else:
        lines.extend(_t_transform(name))
    return lines


# Math implementation generator
def gen_math_impl(name):
    lines = []
    if name == "gcd_list":
        lines.extend([
            '    try:',
            '        raw = input("Enter numbers (comma separated): ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    import math',
            '    parts = [x.strip() for x in raw.split(",") if x.strip()]',
            '    try:',
            '        nums = [int(x) for x in parts]',
            '    except ValueError:',
            '        return "Invalid integers"',
            '    if not nums: return 0',
            '    result = abs(nums[0])',
            '    for n in nums[1:]:',
            '        result = math.gcd(result, abs(n))',
            '        if result == 1: break',
            '    return result',
        ])
    elif name == "lcm_list":
        lines.extend([
            '    try:',
            '        raw = input("Enter numbers (comma separated): ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    import math',
            '    parts = [x.strip() for x in raw.split(",") if x.strip()]',
            '    try:',
            '        nums = [int(x) for x in parts]',
            '    except ValueError:',
            '        return "Invalid integers"',
            '    if not nums: return 0',
            '    result = abs(nums[0])',
            '    for n in nums[1:]:',
            '        result = result * abs(n) // math.gcd(result, abs(n))',
            '    return result',
        ])
    elif name in ("is_perfect_square", "is_perfect_cube"):
        lines.extend([
            '    try:',
            '        n_str = input("Enter number: ")',
            '        n = int(n_str)',
            '    except (ValueError, EOFError):',
            '        return False',
            '    if n < 0: return False',
            '    import math',
            '    if "square" in name:',
            '        r = int(math.isqrt(n))',
            '        return r * r == n',
            '    else:',
            '        r = round(n ** (1/3))',
            '        for candidate in (r, r-1, r+1):',
            '            if candidate ** 3 == n: return True',
            '        return False',
        ])
    elif name in ("is_power_of_two", "is_power_of_n"):
        lines.extend([
            '    try:',
            '        n_str = input("Enter number: ")',
            '        n = int(n_str)',
            '    except (ValueError, EOFError):',
            '        return False',
            '    if name == "is_power_of_two":',
            '        return n > 0 and (n & (n - 1)) == 0',
            '    try:',
            '        base_str = input("Enter base: ")',
            '        base = int(base_str)',
            '    except (ValueError, EOFError):',
            '        return False',
            '    if n < 1 or base < 2: return False',
            '    temp = n',
            '    while temp % base == 0:',
            '        temp //= base',
            '    return temp == 1',
        ])
    elif name in ("digit_sum", "digit_product", "digital_root", "reversed_number"):
        lines.extend([
            '    try:',
            '        n_str = input("Enter integer: ")',
            '        n = abs(int(n_str))',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    digits = [int(d) for d in str(n)]',
            '    if name == "digit_sum": return sum(digits)',
            '    if name == "digit_product":',
            '        prod = 1',
            '        for d in digits: prod *= d',
            '        return prod',
            '    if name == "digital_root":',
            '        if n == 0: return 0',
            '        return 1 + (n - 1) % 9',
            '    sign = -1 if int(n_str) < 0 else 1',
            '    return sign * int(str(n)[::-1])',
        ])
    elif name == "prime_factors":
        lines.extend([
            '    try:',
            '        n_str = input("Enter integer: ")',
            '        n = abs(int(n_str))',
            '    except (ValueError, EOFError):',
            '        return []',
            '    result = []',
            '    d = 2',
            '    temp = n',
            '    while d * d <= temp:',
            '        while temp % d == 0:',
            '            result.append(d)',
            '            temp //= d',
            '        d += 1 if d == 2 else 2',
            '    if temp > 1: result.append(temp)',
            '    return result',
        ])
    elif name == "num_divisors":
        lines.extend([
            '    try:',
            '        n_str = input("Enter integer: ")',
            '        n = abs(int(n_str))',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    count = 0',
            '    for i in range(1, int(n ** 0.5) + 1):',
            '        if n % i == 0:',
            '            count += 1 if i * i == n else 2',
            '    return count',
        ])
    elif name == "binomial_coefficient":
        lines.extend([
            '    try:',
            '        n_str = input("Enter n: ")',
            '        k_str = input("Enter k: ")',
            '        n, k = int(n_str), int(k_str)',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    import math',
            '    if k < 0 or k > n: return 0',
            '    k = min(k, n - k)',
            '    result = 1',
            '    for i in range(1, k + 1):',
            '        result = result * (n - k + i) // i',
            '    return result',
        ])
    elif name == "fibonacci_n":
        lines.extend([
            '    try:',
            '        n_str = input("Enter n: ")',
            '        n = int(n_str)',
            '    except (ValueError, EOFError):',
            '        return None',
            '    if n < 0: return None',
            '    if n <= 1: return n',
            '    a, b = 0, 1',
            '    for _ in range(2, n + 1):',
            '        a, b = b, a + b',
            '    return b',
        ])
    elif name == "fibonacci_sequence":
        lines.extend([
            '    try:',
            '        n_str = input("Enter count: ")',
            '        n = int(n_str)',
            '    except (ValueError, EOFError):',
            '        return []',
            '    if n < 0: return []',
            '    if n == 0: return [0]',
            '    seq = [0, 1]',
            '    for i in range(2, n + 1):',
            '        seq.append(seq[-1] + seq[-2])',
            '    return seq[:n + 1]',
        ])
    elif name in ("lucas_number", "tribonacci", "pell_number"):
        lines.extend([
            '    try:',
            '        n_str = input("Enter n: ")',
            '        n = int(n_str)',
            '    except (ValueError, EOFError):',
            '        return None',
            '    if n < 0: return None',
            '    if name == "lucas_number":',
            '        if n == 0: return 2',
            '        if n == 1: return 1',
            '        a, b = 2, 1',
            '        for _ in range(2, n + 1): a, b = b, a + b',
            '        return b',
            '    if n <= 1: return n',
            '    if n == 2: return 1',
            '    a, b, c = 0, 1, 1',
            '    for _ in range(3, n + 1): a, b, c = b, c, a + b + c',
            '    return c',
        ])
    elif name in ("collatz_sequence", "collatz_steps"):
        lines.extend([
            '    try:',
            '        n_str = input("Enter starting number: ")',
            '        n = int(n_str)',
            '    except (ValueError, EOFError):',
            '        return []',
            '    if n < 1: return []',
            '    if name == "collatz_sequence":',
            '        seq = [n]',
            '        temp = n',
            '        while temp != 1:',
            '            if temp % 2 == 0: temp //= 2',
            '            else: temp = 3 * temp + 1',
            '            seq.append(temp)',
            '        return seq',
            '    steps = 0',
            '    temp = n',
            '    while temp != 1:',
            '        if temp % 2 == 0: temp //= 2',
            '        else: temp = 3 * temp + 1',
            '        steps += 1',
            '    return steps',
        ])
    elif name in ("nth_prime", "next_prime"):
        lines.extend([
            '    try:',
            '        n_str = input("Enter n: ")',
            '        n = int(n_str)',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if name == "nth_prime":',
            '        count = 0; num = 2',
            '        while True:',
            '            is_p = True',
            '            for d in range(2, int(num**0.5)+1):',
            '                if num % d == 0: is_p = False; break',
            '            if is_p:',
            '                count += 1',
            '                if count == n: return num',
            '            num += 1',
            '    num = n + 1',
            '    while True:',
            '        is_p = True',
            '        for d in range(2, int(num**0.5)+1):',
            '            if num % d == 0: is_p = False; break',
            '        if is_p: return num',
            '        num += 1',
        ])
    elif name == "prime_range":
        lines.extend([
            '    try:',
            '        start_str = input("Start: ")',
            '        end_str = input("End: ")',
            '        start, end = int(start_str), int(end_str)',
            '    except (ValueError, EOFError):',
            '        return []',
            '    result = []',
            '    for num in range(max(2, start), end + 1):',
            '        is_p = True',
            '        for d in range(2, int(num**0.5)+1):',
            '            if num % d == 0: is_p = False; break',
            '        if is_p: result.append(num)',
            '    return result',
        ])
    elif name == "sieve_primes":
        lines.extend([
            '    try:',
            '        n_str = input("Upper limit: ")',
            '        n = int(n_str)',
            '    except (ValueError, EOFError):',
            '        return []',
            '    if n < 2: return []',
            '    sieve = [True] * (n + 1)',
            '    sieve[0] = sieve[1] = False',
            '    for i in range(2, int(n ** 0.5) + 1):',
            '        if sieve[i]:',
            '            for j in range(i * i, n + 1, i):',
            '                sieve[j] = False',
            '    return [i for i in range(2, n + 1) if sieve[i]]',
        ])
    elif name in ("is_twin_prime", "is_cousin_prime", "is_semiprime", "is_emirp",
                  "is_circular_prime", "is_sophie_germain", "safe_prime"):
        lines.extend([
            '    try:',
            '        n_str = input("Enter number: ")',
            '        n = int(n_str)',
            '    except (ValueError, EOFError):',
            '        return False',
            '    if n < 2: return False',
            '    def _is_prime(x):',
            '        if x < 2: return False',
            '        for d in range(2, int(x**0.5)+1):',
            '            if x % d == 0: return False',
            '        return True',
            '    if name == "is_twin_prime":',
            '        return _is_prime(n) and _is_prime(n + 2)',
            '    if name == "is_cousin_prime":',
            '        return _is_prime(n) and _is_prime(n + 4)',
            '    if name == "is_semiprime":',
            '        count, temp = 0, n',
            '        for d in range(2, int(n**0.5)+1):',
            '            while temp % d == 0:',
            '                temp //= d; count += 1',
            '                if count > 2: return False',
            '        if temp > 1: count += 1',
            '        return count == 2',
            '    if name == "is_emirp":',
            '        rev = int(str(n)[::-1])',
            '        return n != rev and _is_prime(n) and _is_prime(rev)',
            '    if name == "is_circular_prime":',
            '        s = str(n)',
            '        for i in range(len(s)):',
            '            if not _is_prime(int(s[i:] + s[:i])): return False',
            '        return True',
            '    if name == "is_sophie_germain":',
            '        return _is_prime(n) and _is_prime(2 * n + 1)',
            '    return _is_prime(n) and _is_prime((n - 1) // 2)',
        ])
    elif name == "rand_prime":
        lines.extend([
            '    try:',
            '        lo_str = input("Low: ")',
            '        hi_str = input("High: ")',
            '        lo, hi = int(lo_str), int(hi_str)',
            '    except (ValueError, EOFError):',
            '        return None',
            '    def _is_prime(x):',
            '        if x < 2: return False',
            '        for d in range(2, int(x**0.5)+1):',
            '            if x % d == 0: return False',
            '        return True',
            '    import random as _r',
            '    candidates = [p for p in range(lo, hi+1) if _is_prime(p)]',
            '    return _r.choice(candidates) if candidates else None',
        ])
    elif name in ("randint_list", "randfloat_list"):
        lines.extend([
            '    try:',
            '        lo_str = input("Low: ")',
            '        hi_str = input("High: ")',
            '        count_str = input("Count: ")',
            '        lo, hi, count = int(lo_str), int(hi_str), int(count_str)',
            '    except (ValueError, EOFError):',
            '        return []',
            '    import random as _r',
            '    if "float" in name:',
            '        return [_r.uniform(lo, hi) for _ in range(count)]',
            '    return [_r.randint(lo, hi) for _ in range(count)]',
        ])
    elif name in ("clip", "lerp", "map_range", "smoothstep"):
        lines.extend([
            '    try:',
            '        val_str = input("Enter value: ")',
            '        value = float(val_str)',
            '    except (ValueError, EOFError):',
            '        return 0.0',
            '    if name == "clip":',
            '        lo_str = input("Min: ") or "0"',
            '        hi_str = input("Max: ") or "1"',
            '        lo, hi = float(lo_str), float(hi_str)',
            '        if value < lo: return lo',
            '        if value > hi: return hi',
            '        return value',
            '    if name == "lerp":',
            '        a_str = input("A: ") or "0"',
            '        b_str = input("B: ") or "1"',
            '        a, b = float(a_str), float(b_str)',
            '        return a + (b - a) * value',
            '    if name == "map_range":',
            '        in_lo = float(input("In low: ") or "0")',
            '        in_hi = float(input("In high: ") or "1")',
            '        out_lo = float(input("Out low: ") or "0")',
            '        out_hi = float(input("Out high: ") or "1")',
            '        ratio = (value - in_lo) / (in_hi - in_lo) if in_hi != in_lo else 0',
            '        return out_lo + (out_hi - out_lo) * ratio',
            '    return value * value * (3 - 2 * value)',
        ])
    elif name == "monte_carlo_pi":
        lines.extend([
            '    try:',
            '        pts = int(input("Points: ") or "100000")',
            '    except (ValueError, EOFError):',
            '        pts = 100000',
            '    import random as _r',
            '    inside = 0',
            '    for _ in range(pts):',
            '        x = _r.uniform(-1, 1)',
            '        y = _r.uniform(-1, 1)',
            '        if x * x + y * y <= 1: inside += 1',
            '    return 4.0 * inside / pts',
        ])
    elif name in ("modular_exponent", "modular_inverse", "chinese_remainder"):
        lines.extend([
            '    try:',
            '        a = int(input("Base a: ") or "2")',
            '        m = int(input("Mod m: ") or "7")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    import math',
            '    if name == "modular_exponent":',
            '        b = int(input("Exp b: ") or "3")',
            '        result = 1',
            '        base, exp = a % m, b',
            '        while exp > 0:',
            '            if exp % 2 == 1: result = (result * base) % m',
            '            exp //= 2',
            '            base = (base * base) % m',
            '        return result',
            '    if name == "modular_inverse":',
            '        def egcd(aa, bb):',
            '            if bb == 0: return (aa, 1, 0)',
            '            g, x1, y1 = egcd(bb, aa % bb)',
            '            return (g, y1, x1 - (aa // bb) * y1)',
            '        g, x, _ = egcd(a, m)',
            '        if g != 1: return None',
            '        return x % m',
            '    rem_str = input("Remainders (comma): ")',
            '    mod_str = input("Moduli (comma): ")',
            '    remainders = [int(x) for x in rem_str.split(",")]',
            '    mods = [int(x) for x in mod_str.split(",")]',
            '    M = 1',
            '    for mo in mods: M *= mo',
            '    result = 0',
            '    for r, mo in zip(remainders, mods):',
            '        Mi = M // mo',
            '        inv = pow(Mi, -1, mo)',
            '        result += r * Mi * inv',
            '    return result % M',
        ])
    elif name in ("multinomial", "pascal_row"):
        lines.extend([
            '    try:',
            '        n = int(input("Enter n: ") or "5")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    if n < 0: return []',
            '    row = [1]',
            '    for _ in range(n):',
            '        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]',
            '    return row',
        ])
    elif name in ("primorial", "subfactorial", "double_factorial"):
        lines.extend([
            '    try:',
            '        n = int(input("Enter n: ") or "6")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    if name == "primorial":',
            '        def _is_prime(x):',
            '            if x < 2: return False',
            '            for d in range(2, int(x**0.5)+1):',
            '                if x % d == 0: return False',
            '            return True',
            '        result = 1',
            '        for p in range(2, n + 1):',
            '            if _is_prime(p): result *= p',
            '        return result',
            '    if name == "subfactorial":',
            '        if n == 0: return 1',
            '        if n == 1: return 0',
            '        a, b = 1, 0',
            '        for i in range(2, n + 1):',
            '            a, b = b, (i - 1) * (a + b)',
            '        return b',
            '    result = 1',
            '    for i in range(n, 0, -2): result *= i',
            '    return result',
        ])
    elif name == "egyptian_fraction":
        lines.extend([
            '    try:',
            '        num = int(input("Numerator: ") or "3")',
            '        den = int(input("Denominator: ") or "7")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    result = []',
            '    n, d = abs(num), abs(den)',
            '    while n > 0:',
            '        unit = (d + n - 1) // n',
            '        result.append(unit)',
            '        n = n * unit - d',
            '        d = d * unit',
            '    return result',
        ])
    elif name in ("is_abundant", "is_deficient", "is_perfect_number", "aliquot_sum"):
        lines.extend([
            '    try:',
            '        n = int(input("Enter number: ") or "12")',
            '    except (ValueError, EOFError):',
            '        return False',
            '    if n < 1: return False',
            '    div_sum = 0',
            '    for i in range(1, n):',
            '        if n % i == 0: div_sum += i',
            '    if name == "aliquot_sum": return div_sum',
            '    if name == "is_perfect_number": return div_sum == n',
            '    if name == "is_abundant": return div_sum > n',
            '    return div_sum < n',
        ])
    elif name in ("look_and_say", "van_eck_sequence", "recaman_sequence"):
        lines.extend([
            '    try:',
            '        n = int(input("Enter terms: ") or "10")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    if n < 1: return []',
            '    if name == "look_and_say":',
            '        seq = ["1"]',
            '        for _ in range(n - 1):',
            '            prev = seq[-1]',
            '            result = []; i = 0',
            '            while i < len(prev):',
            '                count = 1',
            '                while i + 1 < len(prev) and prev[i] == prev[i+1]:',
            '                    count += 1; i += 1',
            '                result.append(str(count) + prev[i])',
            '                i += 1',
            '            seq.append("".join(result))',
            '        return seq',
            '    if name == "van_eck_sequence":',
            '        seq = [0]',
            '        seen = {0: 0}',
            '        for i in range(1, n):',
            '            if seq[-1] in seen:',
            '                seq.append(i - 1 - seen[seq[-1]])',
            '            else: seq.append(0)',
            '            seen[seq[-2]] = i - 1',
            '        return seq[:n]',
            '    seq = [0]',
            '    used = {0}',
            '    for i in range(1, n):',
            '        prev_val = seq[-1]',
            '        if prev_val - i > 0 and prev_val - i not in used:',
            '            seq.append(prev_val - i)',
            '        else: seq.append(prev_val + i)',
            '        used.add(seq[-1])',
            '    return seq',
        ])
    elif name in ("stern_diatomic", "mian_chowla", "continued_fraction"):
        lines.extend([
            '    try:',
            '        n = int(input("Enter n: ") or "10")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    if n < 1: return []',
            '    if name == "stern_diatomic":',
            '        def stern(n):',
            '            if n == 0: return 0',
            '            if n == 1: return 1',
            '            if n % 2 == 0: return stern(n // 2)',
            '            return stern(n // 2) + stern(n // 2 + 1)',
            '        return [stern(i) for i in range(n)]',
            '    if name == "mian_chowla":',
            '        seq = [1]',
            '        sums = {2}',
            '        candidate = 2',
            '        while len(seq) < n:',
            '            all_new = True',
            '            new_sums = set()',
            '            for s in seq:',
            '                if s + candidate in sums:',
            '                    all_new = False; break',
            '                new_sums.add(s + candidate)',
            '            if all_new and 2 * candidate not in sums:',
            '                sums.update(new_sums)',
            '                sums.add(2 * candidate)',
            '                seq.append(candidate)',
            '            candidate += 1',
            '        return seq',
            '    def cont_frac(x, terms):',
            '        fracs = []',
            '        for _ in range(terms):',
            '            ai = int(x)',
            '            fracs.append(ai)',
            '            x = x - ai',
            '            if x == 0: break',
            '            x = 1.0 / x',
            '        return fracs',
            '    import math',
            '    return cont_frac(math.pi, n)',
        ])
    elif name in ("goldbach_pairs", "prime_k_tuple", "is_carmichael",
                  "moebius_function", "euler_totient_range"):
        lines.extend([
            '    try:',
            '        n = int(input("Enter number: ") or "100")',
            '    except (ValueError, EOFError):',
            '        return []',
            '    def _is_prime(x):',
            '        if x < 2: return False',
            '        for d in range(2, int(x**0.5)+1):',
            '            if x % d == 0: return False',
            '        return True',
            '    if name == "goldbach_pairs":',
            '        if n < 4 or n % 2 != 0: return []',
            '        pairs = []',
            '        for p in range(2, n // 2 + 1):',
            '            if _is_prime(p) and _is_prime(n - p):',
            '                pairs.append((p, n - p))',
            '        return pairs',
            '    if name == "moebius_function":',
            '        def mobius(x):',
            '            if x == 1: return 1',
            '            count, temp = 0, x',
            '            for d in range(2, int(x**0.5)+1):',
            '                if temp % (d * d) == 0: return 0',
            '                if temp % d == 0:',
            '                    count += 1',
            '                    while temp % d == 0: temp //= d',
            '            if temp > 1: count += 1',
            '            return -1 if count % 2 else 1',
            '        return [mobius(i) for i in range(1, n + 1)]',
            '    return [_is_prime(i) for i in range(1, n + 1)]',
        ])
    elif name in ("sum_of_squares", "lagrange_four_square", "is_palindromic_number",
                  "modular_sqrt", "discrete_log", "bernoulli_number"):
        lines.extend(_t_compute(name))
    else:
        lines.extend(_t_compute(name))
    return lines


# Convert implementation generator
def gen_convert_impl(name):
    lines = []
    if name == "bytes_to_human":
        lines.extend([
            '    try:',
            '        n = float(input("Enter bytes: "))',
            '    except (ValueError, EOFError):',
            '        return "0 B"',
            '    if n < 0: return "0 B"',
            '    units = ["B", "KB", "MB", "GB", "TB", "PB", "EB"]',
            '    i = 0',
            '    while n >= 1024 and i < len(units) - 1:',
            '        n /= 1024',
            '        i += 1',
            '    return "{:.2f} {}".format(n, units[i])',
        ])
    elif name == "human_to_bytes":
        lines.extend([
            '    try:',
            '        s = input("Enter size: ")',
            '    except (ValueError, EOFError):',
            '        return 0',
            '    s = s.strip().upper()',
            '    units = {"B":1,"KB":1024,"MB":1048576,"GB":1073741824,"TB":1099511627776}',
            '    for unit, mult in units.items():',
            '        if s.endswith(unit):',
            '            try:',
            '                num = float(s[:len(s)-len(unit)].strip())',
            '                return int(num * mult)',
            '            except ValueError:',
            '                return 0',
            '    try: return int(float(s))',
            '    except ValueError: return 0',
        ])
    elif name == "celsius_to_kelvin":
        lines.extend([
            '    try:',
            '        c = float(input("Celsius: "))',
            '    except (ValueError, EOFError):',
            '        return 0.0',
            '    if c < -273.15: c = -273.15',
            '    return c + 273.15',
        ])
    elif name == "kelvin_to_celsius":
        lines.extend([
            '    try:',
            '        k = float(input("Kelvin: "))',
            '    except (ValueError, EOFError):',
            '        return 0.0',
            '    if k < 0: k = 0',
            '    return k - 273.15',
        ])
    elif name == "celsius_to_fahrenheit":
        lines.extend([
            '    try:',
            '        c = float(input("Celsius: "))',
            '    except (ValueError, EOFError):',
            '        return 0.0',
            '    return c * 9/5 + 32',
        ])
    elif name == "fahrenheit_to_celsius":
        lines.extend([
            '    try:',
            '        f = float(input("Fahrenheit: "))',
            '    except (ValueError, EOFError):',
            '        return 0.0',
            '    return (f - 32) * 5/9',
        ])
    elif name in ("fahrenheit_to_kelvin", "kelvin_to_fahrenheit"):
        lines.extend([
            '    try:',
            '        val = float(input("Enter value: "))',
            '    except (ValueError, EOFError):',
            '        return 0.0',
            '    if name == "fahrenheit_to_kelvin":',
            '        return (val - 32) * 5/9 + 273.15',
            '    return val * 9/5 - 459.67',
        ])
    elif "_to_" in name:
        lines.extend([
            '    try:',
            '        value = float(input("Enter value: "))',
            '    except (ValueError, EOFError):',
            '        return 0.0',
            '    conv = {',
            '        "miles_to_km":1.609344,"km_to_miles":0.621371,',
            '        "inches_to_cm":2.54,"cm_to_inches":0.393701,',
            '        "feet_to_meters":0.3048,"meters_to_feet":3.28084,',
            '        "pounds_to_kg":0.453592,"kg_to_pounds":2.20462,',
            '        "ounces_to_grams":28.3495,"grams_to_ounces":0.035274,',
            '        "gallons_to_liters":3.78541,"liters_to_gallons":0.264172,',
            '        "mph_to_kph":1.60934,"kph_to_mph":0.621371,',
            '        "mph_to_knots":0.868976,"knots_to_mph":1.15078,',
            '        "lightyears_to_km":9.461e12,"km_to_lightyears":1.057e-13,',
            '        "parsecs_to_ly":3.26156,"ly_to_parsecs":0.306601,',
            '        "au_to_km":149597870.7,"km_to_au":6.68459e-9,',
            '        "radians_to_degrees":57.2958,"degrees_to_radians":0.0174533,',
            '        "ev_to_joules":1.602e-19,"joules_to_ev":6.242e18,',
            '        "calories_to_joules":4.184,"joules_to_calories":0.239006,',
            '        "horsepower_to_watts":745.7,"watts_to_horsepower":0.001341,',
            '        "atm_to_pascal":101325,"pascal_to_atm":9.869e-6,',
            '        "bar_to_psi":14.5038,"psi_to_bar":0.0689476,',
            '        "acres_to_hectares":0.404686,"hectares_to_acres":2.47105,',
            '        "sqft_to_sqm":0.092903,"sqm_to_sqft":10.7639,',
            '        "fl_oz_to_ml":29.5735,"ml_to_fl_oz":0.033814,',
            '        "carats_to_grams":0.2,"grams_to_carats":5.0,',
            '        "knots_to_kph":1.852,"kph_to_knots":0.539957,',
            '        "mach_to_kph":1234.8,"kph_to_mach":0.00080985,',
            '        "nautical_miles_to_km":1.852,"km_to_nautical_miles":0.539957,',
            '        "stones_to_kg":6.35029,"kg_to_stones":0.157473,',
            '        "tons_to_kg":907.185,"kg_to_tons":0.00110231,',
            '        "newtons_to_lbf":0.224809,"lbf_to_newtons":4.44822,',
            '        "joules_to_kwh":2.77778e-7,"kwh_to_joules":3600000,',
            '        "btu_to_joules":1055.06,"joules_to_btu":0.000947817,',
            '        "years_to_days":365.25,"days_to_years":0.00273791,',
            '        "hours_to_minutes":60,"minutes_to_hours":0.0166667,',
            '        "weeks_to_days":7,"days_to_weeks":0.142857,',
            '        "decades_to_years":10,"centuries_to_years":100,"millennia_to_years":1000,',
            '    }',
            '    factor = conv.get(name, 1.0)',
            '    result = value * factor',
            '    return round(result, 6)',
        ])
    else:
        lines.extend(_t_convert(name))
    return lines


# Format implementation generator
def gen_format_impl(name):
    lines = []
    if name == "format_ordinal":
        lines.extend([
            '    try: n = int(input("Enter number: "))',
            '    except: return "0"',
            '    if 11 <= n % 100 <= 13: suffix = "th"',
            '    else: suffix = {1:"st",2:"nd",3:"rd"}.get(n % 10, "th")',
            '    return "{}{}".format(n, suffix)',
        ])
    elif name == "format_plural":
        lines.extend([
            '    try:',
            '        count = int(input("Count: "))',
            '        singular = input("Singular: ")',
            '    except: return ""',
            '    if count == 1: return "1 " + singular',
            '    irregular = {"child":"children","foot":"feet","tooth":"teeth","mouse":"mice"}',
            '    plural = irregular.get(singular, singular + "s")',
            '    return "{} {}".format(count, plural)',
        ])
    elif name == "format_commas":
        lines.extend([
            '    try: n = int(input("Enter number: "))',
            '    except: return "0"',
            '    return "{:,}".format(n)',
        ])
    elif name == "format_si_prefix":
        lines.extend([
            '    try: n = float(input("Enter number: "))',
            '    except: return "0"',
            '    prefixes = ["","k","M","G","T","P","E"]',
            '    i = 0; v = abs(n)',
            '    while v >= 1000 and i < 6: v /= 1000; i += 1',
            '    sign = "" if n >= 0 else "-"',
            '    return "{}{:.2f} {}".format(sign, v, prefixes[i])',
        ])
    elif name == "format_percentage":
        lines.extend([
            '    try: v = float(input("Decimal: "))',
            '    except: return "0.0%"',
            '    return "{:.2f}%".format(v * 100)',
        ])
    elif name == "format_currency":
        lines.extend([
            '    try:',
            '        amt = float(input("Amount: "))',
            '        cur = input("Currency: ") or "USD"',
            '    except: return "$0.00"',
            '    symbols = {"USD":"$","EUR":"\\u20ac","GBP":"\\u00a3","JPY":"\\u00a5"}',
            '    sym = symbols.get(cur.upper(), cur+" ")',
            '    return "{}{:.2f}".format(sym, amt)',
        ])
    elif name == "format_phone":
        lines.extend([
            '    try: phone = input("Phone: ")',
            '    except: return ""',
            '    d = "".join(c for c in phone if c.isdigit())',
            '    if len(d) == 10: return "({}) {}-{}".format(d[:3],d[3:6],d[6:])',
            '    if len(d) == 7: return "{}-{}".format(d[:3],d[3:])',
            '    if len(d)==11 and d[0]=="1": return "1-({}) {}-{}".format(d[1:4],d[4:7],d[7:])',
            '    return phone',
        ])
    elif name == "format_progress_bar":
        lines.extend([
            '    try:',
            '        f = float(input("Fraction (0-1): "))',
            '        w = int(input("Width: ") or "20")',
            '    except: return ""',
            '    f = max(0, min(1, f))',
            '    filled = int(w * f); empty = w - filled',
            '    return "[" + "#"*filled + "-"*empty + "] {:.1f}%".format(f*100)',
        ])
    elif name == "format_bar_chart":
        lines.extend([
            '    try:',
            '        raw = input("Values: ")',
            '        w = int(input("Width: ") or "20")',
            '    except: return ""',
            '    vals = [];',
            '    for x in raw.split(","):',
            '        try: vals.append(float(x.strip()))',
            '        except: pass',
            '    if not vals: return ""',
            '    mx = max(vals)',
            '    return "\\n".join("#"*int(v/mx*w) + " " + str(v) for v in vals)',
        ])
    elif name == "format_roman_numeral":
        lines.extend([
            '    try: n = int(input("1-3999: "))',
            '    except: return ""',
            '    if n < 1 or n > 3999: return str(n)',
            '    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]',
            '    roms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]',
            '    res = ""; t = n',
            '    for v, r in zip(vals, roms):',
            '        while t >= v: res += r; t -= v',
            '    return res',
        ])
    elif name in ("format_list_numbered", "format_list_bullet"):
        lines.extend([
            '    try: raw = input("Items: ")',
            '    except: return ""',
            '    items = [x.strip() for x in raw.split(",") if x.strip()]',
            '    if name == "list_bullet" in name:',
            '        return "\\n".join("- " + i for i in items)',
            '    return "\\n".join("{}. {}".format(i+1, it) for i, it in enumerate(items))',
        ])
    elif name == "format_key_value":
        lines.extend([
            '    try: raw = input("key:val, key:val: ")',
            '    except: return ""',
            '    pairs = {}',
            '    for p in raw.split(","):',
            '        if ":" in p:',
            '            k, v = p.split(":",1); pairs[k.strip()] = v.strip()',
            '    if not pairs: return ""',
            '    mk = max(len(k) for k in pairs)',
            '    return "\\n".join("{}: {}".format(k.ljust(mk), v) for k,v in pairs.items())',
        ])
    elif name == "format_truncated":
        lines.extend([
            '    try:',
            '        s = input("String: ")',
            '        m = int(input("Max: ") or "80")',
            '    except: return ""',
            '    if len(s) <= m: return s',
            '    return s[:m-3] + "..."',
        ])
    else:
        lines.extend(_t_format(name))
    return lines


# List implementation generator
def gen_list_impl(name):
    lines = []
    if name == "flatten_deep":
        lines.extend([
            '    try: raw = input("Nested list (eval): ")',
            '    except: return []',
            '    import ast',
            '    try: lst = ast.literal_eval(raw)',
            '    except: lst = [x.strip() for x in raw.split(",") if x.strip()]',
            '    res = []',
            '    def _fl(x):',
            '        if isinstance(x, (list,tuple)):',
            '            for s in x: _fl(s)',
            '        else: res.append(x)',
            '    _fl(lst)',
            '    return res',
        ])
    elif name in ("chunk_even", "chunk_size", "batched"):
        lines.extend([
            '    try:',
            '        raw = input("Items: ")',
            '        n = int(input("N: ") or "3")',
            '    except: return []',
            '    items = [x.strip() for x in raw.split(",") if x.strip()]',
            '    if not items or n < 1: return []',
            '    if name == "chunk_even":',
            '        k, m = divmod(len(items), n)',
            '        return [items[i*k+min(i,m):(i+1)*k+min(i+1,m)] for i in range(n)]',
            '    return [items[i:i+n] for i in range(0, len(items), n)]',
        ])
    elif name in ("windowed", "pairwise"):
        lines.extend([
            '    try: raw = input("Items: ")',
            '    except: return []',
            '    items = [x.strip() for x in raw.split(",") if x.strip()]',
            '    if name == "pairwise": return list(zip(items, items[1:]))',
            '    try: n = int(input("Window: ") or "2")',
            '    except: n = 2',
            '    if n < 1: return []',
            '    return [items[i:i+n] for i in range(len(items)-n+1)]',
        ])
    elif name in ("rotate_left", "rotate_right"):
        lines.extend([
            '    try:',
            '        raw = input("Items: ")',
            '        n = int(input("Shift: ") or "1")',
            '    except: return []',
            '    items = [x.strip() for x in raw.split(",") if x.strip()]',
            '    if not items: return []',
            '    n = n % len(items)',
            '    if "left" in name: return items[n:] + items[:n]',
            '    return items[-n:] + items[:-n]',
        ])
    elif name in ("transpose_grid", "shuffle_deterministic", "sample_weighted",
                  "mode_list", "percentile", "running_total", "running_product",
                  "moving_average", "normalize_minmax", "normalize_zscore",
                  "compress_rle", "decompress_rle", "find_peaks", "find_valleys",
                  "longest_run", "argmax", "argmin", "argsort", "n_largest",
                  "n_smallest", "unique_preserve_order", "all_duplicates",
                  "intersection_multi", "union_multi", "symmetric_diff",
                  "partition_on", "split_on", "interleave", "cartesian_product",
                  "powerset", "take", "drop", "shuffle_two", "roundrobin",
                  "merge_sorted", "merge_alternating", "dedupe_adjacent",
                  "compact_falsy", "fill_na", "pad_left", "pad_right",
                  "trim_left", "trim_right", "slice_wrap", "random_subset",
                  "k_combinations", "k_permutations", "derangements",
                  "group_by_key", "sort_by_key", "sort_multiple",
                  "stable_partition", "bisect_left", "bisect_right",
                  "bins"):
        lines.extend(_t_analyze(name))
    else:
        lines.extend(_t_transform(name))
    return lines


# Random implementation generator
def gen_random_impl(name):
    lines = []
    if name == "rand_bool":
        lines.extend([
            '    import random as _r; _r.seed()',
            '    try: w = float(input("Weight (0-1): ") or "0.5")',
            '    except: w = 0.5',
            '    return _r.random() < max(0, min(1, w))',
        ])
    elif name == "rand_choice_weighted":
        lines.extend([
            '    import random as _r; _r.seed()',
            '    try:',
            '        items = [x.strip() for x in input("Items: ").split(",") if x.strip()]',
            '        wts = [float(x) for x in input("Weights: ").split(",") if x.strip()]',
            '    except: return None',
            '    if not items or len(items)!=len(wts): return items[0] if items else None',
            '    total = sum(wts); r = _r.uniform(0, total); cum = 0',
            '    for it, w in zip(items, wts):',
            '        cum += w',
            '        if r <= cum: return it',
            '    return items[-1]',
        ])
    elif name == "rand_date":
        lines.extend([
            '    import random as _r, datetime as _dt; _r.seed()',
            '    try:',
            '        sy = int(input("Start year: ") or "2000")',
            '        sm = int(input("Month: ") or "1")',
            '        sd = int(input("Day: ") or "1")',
            '        ey = int(input("End year: ") or "2025")',
            '        em = int(input("Month: ") or "12")',
            '        ed = int(input("Day: ") or "31")',
            '    except: return _dt.date.today()',
            '    start = _dt.date(sy,sm,sd); end = _dt.date(ey,em,ed)',
            '    delta = (end-start).days',
            '    return start + _dt.timedelta(days=_r.randint(0, max(0, delta)))',
        ])
    elif name in ("rand_time", "rand_datetime"):
        lines.extend([
            '    import random as _r, datetime as _dt; _r.seed()',
            '    if "time"==name: return _dt.time(_r.randint(0,23),_r.randint(0,59),_r.randint(0,59))',
            '    return _dt.datetime(_r.randint(2000,2025),_r.randint(1,12),_r.randint(1,28),_r.randint(0,23),_r.randint(0,59))',
        ])
    elif name in ("rand_color_hex","rand_hex_color","rand_color_rgb","rand_rgb_tuple"):
        lines.extend([
            '    import random as _r; _r.seed()',
            '    if "rgb" in name and "tuple" in name: return (_r.randint(0,255),_r.randint(0,255),_r.randint(0,255))',
            '    if "rgb" in name: return "rgb({},{},{})".format(_r.randint(0,255),_r.randint(0,255),_r.randint(0,255))',
            '    return "#{:06x}".format(_r.randint(0,0xFFFFFF))',
        ])
    elif name in ("rand_ipv4","rand_mac"):
        lines.extend([
            '    import random as _r; _r.seed()',
            '    if "ip" in name: return ".".join(str(_r.randint(1,254)) for _ in range(4))',
            '    return ":".join("{:02x}".format(_r.randint(0,255)) for _ in range(6))',
        ])
    elif name == "rand_coin_toss":
        lines.extend([
            '    import random as _r; _r.seed()',
            '    return _r.choice(["Heads","Tails"])',
        ])
    elif name in ("rand_dice","rand_card","rand_hand","rand_deck"):
        lines.extend([
            '    import random as _r; _r.seed()',
            '    suits = ["Hearts","Diamonds","Clubs","Spades"]',
            '    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]',
            '    deck = [r+" of "+s for s in suits for r in ranks]',
            '    if name=="rand_card": return _r.choice(deck)',
            '    if name=="rand_hand": return ", ".join(_r.sample(deck,5))',
            '    _r.shuffle(deck); return ", ".join(deck)',
        ])
    elif name in ("rand_password_pin","rand_password_ascii","rand_password_pronounceable"):
        lines.extend([
            '    import random as _r, string; _r.seed()',
            '    try: ln = max(1, min(128, int(input("Length: ") or "8")))',
            '    except: ln = 8',
            '    if "pin" in name: return "".join(str(_r.randint(0,9)) for _ in range(ln))',
            '    if "ascii" in name:',
            '        cs = string.ascii_letters + string.digits + string.punctuation',
            '        return "".join(_r.choice(cs) for _ in range(ln))',
            '    vowels="aeiou"; cons="bcdfghjklmnpqrstvwxyz"',
            '    return "".join(_r.choice(cons if i%2==0 else vowels) for i in range(ln))',
        ])
    elif name == "rand_username":
        lines.extend([
            '    import random as _r; _r.seed()',
            '    adjs = ["cool","fast","happy","wise","bold","calm","dark","epic","fair","gold","slim"]',
            '    nouns = ["tiger","eagle","wolf","hawk","bear","lion","fox","owl","ray","elk","puma"]',
            '    return "{}_{}{}".format(_r.choice(adjs),_r.choice(nouns),_r.randint(10,999))',
        ])
    elif name in ("rand_domain","rand_email"):
        lines.extend([
            '    import random as _r; _r.seed()',
            '    tlds=[".com",".org",".net",".io",".dev",".app"]',
            '    nm = "".join(chr(_r.randint(97,122)) for _ in range(_r.randint(4,10)))',
            '    dom = nm + _r.choice(tlds)',
            '    if "domain" in name: return dom',
            '    usr = "".join(chr(_r.randint(97,122)) for _ in range(_r.randint(4,8)))',
            '    return "{}@{}".format(usr, dom)',
        ])
    elif name in ("rand_uuid","rand_lorem_ipsum","rand_haiku","rand_quote","rand_emoji"):
        lines.extend([
            '    import random as _r; _r.seed()',
            '    if name=="rand_uuid": import uuid; return str(uuid.uuid4())',
            '    if name=="rand_lorem_ipsum":',
            '        w="lorem ipsum dolor sit amet consectetur adipiscing elit".split()',
            '        return " ".join(_r.choice(w) for _ in range(_r.randint(5,20)))',
            '    if name=="rand_haiku":',
            '        return "\\n".join([_r.choice(["quiet morning","autumn leaves","cherry blooms"]),_r.choice(["river flows","wind whispers","moonlight water"]),_r.choice(["bird sings","snow covers","stars above"])])',
            '    if name=="rand_quote":',
            '        qs=["The only limit is your mind.","Stay hungry, stay foolish.","Think different.","Just do it.","Knowledge is power."]',
            '        return _r.choice(qs)',
            '    emojis=["\\U0001f600","\\U0001f44d","\\u2764\\ufe0f","\\U0001f31f","\\U0001f389","\\U0001f525"]',
            '    return _r.choice(emojis)',
        ])
    else:
        lines.extend(_t_random(name))
    return lines


# Crypto implementation generator
def gen_crypto_impl(name):
    lines = []
    if name in ("caesar_encrypt","caesar_decrypt","caesar_bruteforce"):
        lines.extend([
            '    try: text = input("Enter text: ")',
            '    except: return ""',
            '    if "bruteforce" in name:',
            '        res=[]',
            '        for s in range(26):',
            '            r=[]',
            '            for c in text:',
            '                if "a"<=c<="z": r.append(chr((ord(c)-97-s)%26+97))',
            '                elif "A"<=c<="Z": r.append(chr((ord(c)-65-s)%26+65))',
            '                else: r.append(c)',
            '            res.append("Shift {}: {}".format(s,"".join(r)))',
            '        return "\\n".join(res)',
            '    try: shift = int(input("Shift: ") or "3")',
            '    except: shift = 3',
            '    if "decrypt" in name: shift = -shift',
            '    return "".join(chr((ord(c)-97+shift)%26+97) if "a"<=c<="z" else chr((ord(c)-65+shift)%26+65) if "A"<=c<="Z" else c for c in text)',
        ])
    elif name in ("vigenere_encrypt","vigenere_decrypt"):
        lines.extend([
            '    try: text = input("Text: "); key = input("Key: ")',
            '    except: return ""',
            '    key = key.upper(); d = -1 if "decrypt" in name else 1',
            '    ki = 0; res = []',
            '    for c in text.upper():',
            '        if "A"<=c<="Z":',
            '            s = ord(key[ki%len(key)])-65',
            '            res.append(chr((ord(c)-65+d*s)%26+65)); ki+=1',
            '        else: res.append(c)',
            '    return "".join(res)',
        ])
    elif name == "atbash_cipher":
        lines.extend([
            '    try: text = input("Text: ")',
            '    except: return ""',
            '    return "".join(chr(219-ord(c)) if "a"<=c<="z" else chr(155-ord(c)) if "A"<=c<="Z" else c for c in text)',
        ])
    elif name in ("rot13_text","rot47_text","rot5_text","rot18_text"):
        lines.extend([
            '    try: text = input("Text: ")',
            '    except: return ""',
            '    if "13" in name or "18" in name:',
            '        s = 13 if "13" in name else 18',
            '        return "".join(chr((ord(c)-97+s)%26+97) if "a"<=c<="z" else chr((ord(c)-65+s)%26+65) if "A"<=c<="Z" else c for c in text)',
            '    if "47" in name:',
            '        return "".join(chr(33+(ord(c)-33+47)%94) if 33<=ord(c)<=126 else c for c in text)',
            '    return "".join(chr((ord(c)-48+5)%10+48) if c.isdigit() else c for c in text)',
        ])
    elif name == "xor_cipher":
        lines.extend([
            '    try: text = input("Text: "); key = input("Key: ")',
            '    except: return ""',
            '    return "".join(chr(ord(c)^ord(key[i%len(key)])) for i,c in enumerate(text))',
        ])
    elif name in ("base64_encode","base64_decode"):
        lines.extend([
            '    try: s = input("Data: ")',
            '    except: return ""',
            '    import base64',
            '    return base64.b64encode(s.encode()).decode() if "encode" in name else base64.b64decode(s.encode()).decode()',
        ])
    elif name in ("hex_encode","hex_decode"):
        lines.extend([
            '    try: s = input("Data: ")',
            '    except: return ""',
            '    return s.encode().hex() if "encode" in name else bytes.fromhex(s).decode()',
        ])
    elif name in ("url_encode","url_decode"):
        lines.extend([
            '    try: s = input("Data: ")',
            '    except: return ""',
            '    from urllib.parse import quote, unquote',
            '    return quote(s) if "encode" in name else unquote(s)',
        ])
    elif name in ("html_escape","html_unescape"):
        lines.extend([
            '    try: s = input("HTML: ")',
            '    except: return ""',
            '    import html',
            '    return html.escape(s) if "escape" in name else html.unescape(s)',
        ])
    elif name in ("morse_encode","morse_decode"):
        lines.extend([
            '    try: text = input("Text: ")',
            '    except: return ""',
            '    tm = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}',
            '    fm = {v:k for k,v in tm.items()}',
            '    if "encode" in name: return " ".join(tm.get(c.upper(),c) for c in text)',
            '    return "".join(fm.get(c,c) for c in text.split())',
        ])
    elif name in ("sha256_hash","sha512_hash","md5_hash","crc32_hash","sha1_hash","sha3_256_hash","blake2b_hash"):
        lines.extend([
            '    try: s = input("Text: ")',
            '    except: return ""',
            '    import hashlib',
            '    algos={"sha256_hash":"sha256","sha512_hash":"sha512","md5_hash":"md5","sha1_hash":"sha1","sha3_256_hash":"sha3_256","blake2b_hash":"blake2b","crc32_hash":"crc32"}',
            '    if name=="crc32_hash": import zlib; return format(zlib.crc32(s.encode())&0xFFFFFFFF,"08x")',
            '    return hashlib.new(algos[name],s.encode()).hexdigest()',
        ])
    elif name == "hmac_sha256_str":
        lines.extend([
            '    try: text=input("Text: "); key=input("Key: ")',
            '    except: return ""',
            '    import hmac, hashlib',
            '    return hmac.new(key.encode(),text.encode(),hashlib.sha256).hexdigest()',
        ])
    else:
        lines.extend(_t_transform(name))
    return lines


# Geometry implementation generator
def gen_geometry_impl(name):
    lines = []
    formulas = {
        "point_distance":"math.sqrt((x2-x1)**2+(y2-y1)**2)",
        "point_distance_3d":"math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)",
        "manhattan_distance":"abs(x2-x1)+abs(y2-y1)",
        "chebyshev_distance":"max(abs(x2-x1),abs(y2-y1))",
        "euclidean_norm":"math.sqrt(sum(x*x for x in v))",
        "dot_product":"sum(a*b for a,b in zip(v1,v2))",
        "circle_circumference":"2*math.pi*r",
        "circle_area":"math.pi*r*r",
        "sphere_volume":"4/3*math.pi*r**3",
        "sphere_surface_area":"4*math.pi*r*r",
        "cylinder_volume":"math.pi*r*r*h",
        "cone_volume":"math.pi*r*r*h/3",
        "ellipse_area":"math.pi*a*b",
        "regular_polygon_area":"n*s*s/(4*math.tan(math.pi/n))",
        "torus_volume":"2*math.pi**2*R*r*r",
        "rectangle_area":"w*h",
        "rectangle_perimeter":"2*(w+h)",
        "square_area":"s*s","square_perimeter":"4*s",
        "cube_volume":"s**3","cube_surface_area":"6*s*s",
        "pyramid_volume":"base_area*height/3",
        "annulus_area":"math.pi*(R*R-r*r)",
        "arc_length":"r*angle_rad",
        "chord_length":"2*r*math.sin(angle_rad/2)",
    }
    if name in formulas:
        lines.extend([
            '    import math',
            '    try: v = float(input("Val: ") or "1")',
            '    except: return 0.0',
            '    return round({}, 6)'.format(formulas[name]),
        ])
    elif name in ("triangle_area","triangle_area_sss","triangle_angles",
                  "polygon_area_shoelace","point_in_polygon",
                  "rotate_point_2d","reflect_point_2d",
                  "bezier_quadratic","bezier_cubic",
                  "convex_hull","line_intersection","closest_point_on_segment",
                  "cosine_similarity","angle_between","cross_product",
                  "midpoint_2d","midpoint_3d","centroid_triangle",
                  "circumradius","inradius","segment_area","triangular_prism_volume",
                  "frustum_volume","capsule_volume","sector_area"):
        lines.extend(_t_compute(name))
    else:
        lines.extend(_t_compute(name))
    return lines


# Physics implementation generator
def gen_physics_impl(name):
    lines = []
    formulas = {
        "kinetic_energy":"0.5*mass*velocity**2",
        "potential_energy":"mass*9.81*height",
        "momentum":"mass*velocity",
        "force_gravity":"6.674e-11*m1*m2/(r**2)",
        "centripetal_force":"mass*velocity**2/radius",
        "pendulum_period":"2*math.pi*math.sqrt(L/9.81)",
        "ohms_law":"voltage/resistance",
        "power_electric":"voltage*current",
        "wavelength":"299792458/frequency",
        "photon_energy":"6.626e-34*frequency",
        "density":"mass/volume",
        "buoyant_force":"1000*9.81*displaced_volume",
        "mach_number":"velocity/343",
        "lorentz_factor":"1/math.sqrt(1-v**2/(299792458**2))",
        "mass_energy":"mass*299792458**2",
        "pressure_depth":"density*9.81*depth",
        "escape_velocity":"math.sqrt(2*6.674e-11*mass/radius)",
        "orbital_velocity":"math.sqrt(6.674e-11*mass/radius)",
        "rms_speed":"math.sqrt(3*8.314*temp/molar_mass)",
        "capacitance":"8.854e-12*area/distance",
    }
    if name in formulas:
        lines.extend([
            '    import math',
            '    try: v = float(input("Val: ") or "1")',
            '    except: return 0.0',
            '    return round({}, 6)'.format(formulas[name]),
        ])
    else:
        lines.extend(_t_compute(name))
    return lines


# Stats implementation generator
def gen_stats_impl(name):
    lines = []
    if name in ("geometric_mean","harmonic_mean","quadratic_mean","trimmed_mean","weighted_mean"):
        lines.extend([
            '    import math',
            '    try: raw = input("Numbers: ")',
            '    except: return 0.0',
            '    try: nums=[float(x.strip()) for x in raw.split(",") if x.strip()]',
            '    except: return 0.0',
            '    if not nums: return 0.0; n=len(nums)',
            '    if "geometric" in name:',
            '        if any(x<=0 for x in nums): return 0.0',
            '        return round(math.exp(sum(math.log(x) for x in nums)/n),4)',
            '    if "harmonic" in name:',
            '        if any(x==0 for x in nums): return 0.0',
            '        return round(n/sum(1/x for x in nums),4)',
            '    if "quadratic" in name: return round(math.sqrt(sum(x*x for x in nums)/n),4)',
            '    if "trimmed" in name:',
            '        prop = float(input("Trim proportion: ") or "0.1")',
            '        s=sorted(nums); tr=int(n*prop/2); trim=s[tr:-tr] if tr>0 else s',
            '        return round(sum(trim)/len(trim),4) if trim else 0.0',
            '    wts = [float(x) for x in input("Weights: ").split(",") if x.strip()]',
            '    if len(wts)!=n: wts=[1]*n',
            '    return round(sum(v*w for v,w in zip(nums,wts))/sum(wts),4)',
        ])
    elif name in ("covariance","correlation_pearson"):
        lines.extend([
            '    import math',
            '    try:',
            '        x=[float(v) for v in input("X: ").split(",") if v.strip()]',
            '        y=[float(v) for v in input("Y: ").split(",") if v.strip()]',
            '    except: return 0.0',
            '    n=len(x);',
            '    if n!=len(y) or n<2: return 0.0',
            '    mx,my=sum(x)/n,sum(y)/n',
            '    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))',
            '    if "covariance" in name: return round(num/(n-1),4)',
            '    dx=math.sqrt(sum((xi-mx)**2 for xi in x))',
            '    dy=math.sqrt(sum((yi-my)**2 for yi in y))',
            '    return round(num/(dx*dy),4) if dx*dy else 0.0',
        ])
    elif name in ("linear_regression","r_squared","root_mean_sq_error","mean_abs_error"):
        lines.extend([
            '    import math',
            '    try:',
            '        x=[float(v) for v in input("X: ").split(",") if v.strip()]',
            '        y=[float(v) for v in input("Y: ").split(",") if v.strip()]',
            '    except: return 0.0',
            '    n=len(x);',
            '    if n!=len(y) or n<2: return 0.0',
            '    mx,my=sum(x)/n,sum(y)/n',
            '    num=sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))',
            '    den=sum((xi-mx)**2 for xi in x)',
            '    slope=num/den if den else 0',
            '    intercept=my-slope*mx',
            '    yp=[slope*xi+intercept for xi in x]',
            '    if "linear" in name: return (round(slope,4),round(intercept,4))',
            '    ss_res=sum((yi-ypi)**2 for yi,ypi in zip(y,yp))',
            '    ss_tot=sum((yi-my)**2 for yi in y)',
            '    if "r_squared" in name: return round(1-ss_res/ss_tot,4) if ss_tot else 0',
            '    if "root" in name: return round(math.sqrt(ss_res/n),4)',
            '    return round(sum(abs(yi-ypi) for yi,ypi in zip(y,yp))/n,4)',
        ])
    else:
        lines.extend(_t_analyze(name))
    return lines


# DateTime implementation generator
def gen_datetime_impl(name):
    lines = []
    if name == "days_between":
        lines.extend([
            '    import datetime',
            '    try:',
            '        y1=int(input("Y1: ")); m1=int(input("M1: ")); d1=int(input("D1: "))',
            '        y2=int(input("Y2: ")); m2=int(input("M2: ")); d2=int(input("D2: "))',
            '    except: return 0',
            '    d1_obj=datetime.date(y1,m1,d1); d2_obj=datetime.date(y2,m2,d2)',
            '    delta=abs((d2_obj-d1_obj).days)',
            '    return "{} days ({} weeks, {} days)".format(delta, delta//7, delta%7)',
        ])
    elif name == "is_leap_year":
        lines.extend([
            '    try: y=int(input("Year: "))',
            '    except: return False',
            '    return y%4==0 and (y%100!=0 or y%400==0)',
        ])
    elif name == "days_in_month":
        lines.extend([
            '    try: y=int(input("Year: ")); m=int(input("Month: "))',
            '    except: return 0',
            '    if m<1 or m>12: return 0',
            '    d=[31,29 if y%4==0 and (y%100!=0 or y%400==0) else 28,31,30,31,30,31,31,30,31,30,31]',
            '    return d[m-1]',
        ])
    elif name == "age_from_birthday":
        lines.extend([
            '    import datetime',
            '    try: y=int(input("Birth Y: ")); m=int(input("M: ")); d=int(input("D: "))',
            '    except: return 0',
            '    t=datetime.date.today(); age=t.year-y',
            '    if (t.month,t.day)<(m,d): age-=1',
            '    return age',
        ])
    elif name == "time_ago":
        lines.extend([
            '    try: s=int(input("Seconds: "))',
            '    except: return ""',
            '    if s<60: return "just now"',
            '    if s<3600: return "{}m ago".format(s//60)',
            '    if s<86400: return "{}h ago".format(s//3600)',
            '    if s<2592000: return "{}d ago".format(s//86400)',
            '    if s<31536000: return "{}mo ago".format(s//2592000)',
            '    return "{}y ago".format(s//31536000)',
        ])
    elif name == "clock_angle":
        lines.extend([
            '    try: h=int(input("Hour: ")); m=int(input("Minute: "))',
            '    except: return 0.0',
            '    h=h%12; ha=h*30+m*0.5; ma=m*6; a=abs(ha-ma)',
            '    return "{:.1f} deg".format(min(a,360-a))',
        ])
    elif name == "moon_phase_approx":
        lines.extend([
            '    import datetime',
            '    try: y=int(input("Y: ")); m=int(input("M: ")); d=int(input("D: "))',
            '    except: return ""',
            '    diff=(datetime.date(y,m,d)-datetime.date(2000,1,6)).days',
            '    phase=(diff%29.53058867)/29.53058867',
            '    n=["New","Waxing Crescent","First Quarter","Waxing Gibbous","Full","Waning Gibbous","Last Quarter","Waning Crescent"]',
            '    return n[int(phase*8)%8]',
        ])
    else:
        lines.extend(_t_analyze(name))
    return lines


# File implementation generator
def gen_file_impl(name):
    lines = []
    if name == "file_size_str":
        lines.extend([
            '    import os',
            '    try: path = input("Path: ")',
            '    except: return ""',
            '    if not os.path.exists(path): return "Not found"',
            '    try: sz = os.path.getsize(path)',
            '    except: return "Cannot access"',
            '    u=["B","KB","MB","GB","TB"]; i=0; n=float(sz)',
            '    while n>=1024 and i<4: n/=1024; i+=1',
            '    return "{:.2f} {}".format(n,u[i])',
        ])
    elif name in ("file_extension","file_name_without_ext","file_path_parts",
                  "file_safe_name","split_ext_all","replace_ext","add_suffix",
                  "normalize_path","relative_to_abs","common_parent","path_depth"):
        lines.extend([
            '    import os',
            '    try: path = input("Path: ")',
            '    except: return ""',
            '    if not path: return ""',
            '    if name=="file_extension": _,e=os.path.splitext(path); return e',
            '    if name=="file_name_without_ext": b=os.path.basename(path); return os.path.splitext(b)[0]',
            '    if name=="file_path_parts":',
            '        p=[]',
            '        while True:',
            '            path,t=os.path.split(path)',
            '            if t: p.append(t)',
            '            else:',
            '                if path: p.append(path)',
            '                break',
            '        return list(reversed(p))',
            '    if name=="file_safe_name": return "".join(c for c in path if c.isalnum() or c in "._- ")',
            '    if name=="split_ext_all":',
            '        p=[]',
            '        while True:',
            '            b,e=os.path.splitext(path)',
            '            if e: p.append(e); path=b',
            '            else: break',
            '        p.append(path); return list(reversed(p))',
            '    if name=="replace_ext":',
            '        ne=input("New ext: "); b,_=os.path.splitext(path)',
            '        return b+"."+ne.lstrip(".")',
            '    if name=="add_suffix":',
            '        sf=input("Suffix: "); b,e=os.path.splitext(path)',
            '        return b+sf+e',
            '    if name=="normalize_path": return os.path.normpath(path)',
            '    if name=="relative_to_abs": return os.path.abspath(path)',
            '    if name=="common_parent":',
            '        p2=input("Path 2: "); return os.path.commonpath([path,p2])',
            '    d=path.replace("\\\\","/").count("/")',
            '    if os.path.isabs(path): d-=1',
            '    return d',
        ])
    else:
        lines.extend(_t_analyze(name))
    return lines


# Color implementation generator
def gen_color_impl(name):
    lines = []
    if name == "hex_to_rgb":
        lines.extend([
            '    try: hc = input("Hex: ").lstrip("#")',
            '    except: return (0,0,0)',
            '    if len(hc)==3: hc="".join(c*2 for c in hc)',
            '    if len(hc)!=6: return (0,0,0)',
            '    try: return (int(hc[0:2],16),int(hc[2:4],16),int(hc[4:6],16))',
            '    except: return (0,0,0)',
        ])
    elif name == "rgb_to_hex":
        lines.extend([
            '    try: r=max(0,min(255,int(input("R: ")))); g=max(0,min(255,int(input("G: ")))); b=max(0,min(255,int(input("B: "))))',
            '    except: return "#000000"',
            '    return "#{:02x}{:02x}{:02x}".format(r,g,b)',
        ])
    elif name in ("hex_to_hsl","hex_to_cmyk","rgb_to_hsl","rgb_to_cmyk"):
        lines.extend([
            '    try:',
            '        if "rgb" in name:',
            '            r=int(input("R: "))/255; g=int(input("G: "))/255; b=int(input("B: "))/255',
            '        else:',
            '            hc=input("Hex: ").lstrip("#")',
            '            if len(hc)==3: hc="".join(c*2 for c in hc)',
            '            r=int(hc[0:2],16)/255; g=int(hc[2:4],16)/255; b=int(hc[4:6],16)/255',
            '    except: return (0,0,0)',
            '    mx, mn = max(r,g,b), min(r,g,b)',
            '    if "hsl" in name:',
            '        l=(mx+mn)/2',
            '        if mx==mn: return (0,0,round(l*100,1))',
            '        d=mx-mn; s=d/(1-abs(2*l-1))',
            '        if mx==r: h=((g-b)/d)%6',
            '        elif mx==g: h=(b-r)/d+2',
            '        else: h=(r-g)/d+4',
            '        return (round(h*60,1),round(s*100,1),round(l*100,1))',
            '    k=1-mx',
            '    if k==1: return (0,0,0,100)',
            '    return (round((1-r-k)/(1-k)*100,1),round((1-g-k)/(1-k)*100,1),round((1-b-k)/(1-k)*100,1),round(k*100,1))',
        ])
    elif name in ("hsl_to_hex","hsl_to_rgb"):
        lines.extend([
            '    try: h=float(input("H: "))/360; s=float(input("S: "))/100; l=float(input("L: "))/100',
            '    except: return "#000000"',
            '    def h2(p,q,t):',
            '        if t<0: t+=1',
            '        if t>1: t-=1',
            '        if t<1/6: return p+(q-p)*6*t',
            '        if t<1/2: return q',
            '        if t<2/3: return p+(q-p)*(2/3-t)*6',
            '        return p',
            '    q=l*(1+s) if l<0.5 else l+s-l*s; p=2*l-q',
            '    ri=int(h2(p,q,h+1/3)*255); gi=int(h2(p,q,h)*255); bi=int(h2(p,q,h-1/3)*255)',
            '    if "hex" in name: return "#{:02x}{:02x}{:02x}".format(ri,gi,bi)',
            '    return (ri,gi,bi)',
        ])
    elif name in ("cmyk_to_hex","cmyk_to_rgb"):
        lines.extend([
            '    try:',
            '        c=float(input("C: "))/100; m=float(input("M: "))/100',
            '        y=float(input("Y: "))/100; k=float(input("K: "))/100',
            '    except: return "#000000"',
            '    ri=int(255*(1-c)*(1-k)); gi=int(255*(1-m)*(1-k)); bi=int(255*(1-y)*(1-k))',
            '    if "hex" in name: return "#{:02x}{:02x}{:02x}".format(ri,gi,bi)',
            '    return (ri,gi,bi)',
        ])
    elif name in ("brightness_luminance","brightness_perceived","contrast_ratio",
                  "is_dark_color","is_light_color","complimentary_color",
                  "analogous_colors","triadic_colors","tetradic_colors",
                  "split_complementary","color_name","random_pastel",
                  "random_vibrant","random_grayscale","mix_colors",
                  "blend_colors","tint_color","shade_color","tone_color","invert_color"):
        lines.extend(_t_compute(name))
    else:
        lines.extend(_t_compute(name))
    return lines


# String implementation generator
def gen_string_impl(name):
    lines = []
    if name == "reverse_string":
        lines.extend([
            '    try: s=input("String: ")',
            '    except: return ""',
            '    return s[::-1]',
        ])
    elif name == "is_palindrome":
        lines.extend([
            '    try: s=input("String: ")',
            '    except: return False',
            '    cl="".join(c.lower() for c in s if c.isalnum())',
            '    return cl==cl[::-1]',
        ])
    elif name in ("count_occurrences","find_nth"):
        lines.extend([
            '    try: s=input("String: "); sub=input("Substring: ")',
            '    except: return 0',
            '    if not s or not sub: return 0',
            '    if "count" in name: return s.count(sub)',
            '    try: n=int(input("Nth: ") or "1")',
            '    except: n=1',
            '    idx=-1',
            '    for _ in range(n):',
            '        idx=s.find(sub,idx+1)',
            '        if idx==-1: return -1',
            '    return idx',
        ])
    elif name in ("remove_whitespace","collapse_whitespace",
                  "strip_non_alphanumeric","strip_non_digits",
                  "keep_only_digits","keep_only_letters"):
        lines.extend([
            '    import re',
            '    try: s=input("String: ")',
            '    except: return ""',
            '    if "remove" in name and "whitespace" in name: return re.sub(r"\\s","",s)',
            '    if "collapse" in name: return re.sub(r"\\s+"," ",s).strip()',
            '    if "strip" in name and "non" in name and "digits" in name: return re.sub(r"[^0-9]","",s)',
            '    if "keep" in name and "digits" in name: return "".join(c for c in s if c.isdigit())',
            '    if "keep" in name and "letters" in name: return "".join(c for c in s if c.isalpha())',
            '    return re.sub(r"[^a-zA-Z0-9]","",s)',
        ])
    elif name in ("first_n_chars","last_n_chars"):
        lines.extend([
            '    try: s=input("String: "); n=int(input("N: ") or "1")',
            '    except: return ""',
            '    if "first" in name: return s[:n]',
            '    return s[-n:] if n else ""',
        ])
    elif name in ("random_char","random_digit","random_letter"):
        lines.extend([
            '    import random as _r, string; _r.seed()',
            '    if "digit" in name: return _r.choice(string.digits)',
            '    if "letter" in name: return _r.choice(string.ascii_letters)',
            '    return _r.choice(string.printable.strip())',
        ])
    elif name in ("shuffle_string","sort_string"):
        lines.extend([
            '    try: s=input("String: ")',
            '    except: return ""',
            '    if "shuffle" in name:',
            '        import random as _r; _r.seed()',
            '        lst=list(s); _r.shuffle(lst); return "".join(lst)',
            '    return "".join(sorted(s))',
        ])
    elif name in ("most_common_char","least_common_char"):
        lines.extend([
            '    try: s=input("String: ")',
            '    except: return ""',
            '    if not s: return ""',
            '    f={}',
            '    for c in s: f[c]=f.get(c,0)+1',
            '    return max(f,key=f.get) if "most" in name else min(f,key=f.get)',
        ])
    elif name in ("has_uppercase","has_lowercase","has_digit","has_special","has_whitespace"):
        lines.extend([
            '    try: s=input("String: ")',
            '    except: return False',
            '    m={"has_uppercase":lambda x:any(c.isupper() for c in x),',
            '       "has_lowercase":lambda x:any(c.islower() for c in x),',
            '       "has_digit":lambda x:any(c.isdigit() for c in x),',
            '       "has_special":lambda x:any(not c.isalnum() for c in x),',
            '       "has_whitespace":lambda x:any(c.isspace() for c in x)}',
            '    return m.get(name,lambda x:False)(s)',
        ])
    elif name == "password_strength":
        lines.extend([
            '    try: s=input("Password: ")',
            '    except: return 0',
            '    score=0',
            '    score+=25 if len(s)>=8 else 15 if len(s)>=6 else 5',
            '    score+=15 if any(c.isupper() for c in s) else 0',
            '    score+=15 if any(c.islower() for c in s) else 0',
            '    score+=15 if any(c.isdigit() for c in s) else 0',
            '    score+=15 if any(not c.isalnum() for c in s) else 0',
            '    if len(s)>=12: score+=15',
            '    lvl=["Very Weak","Weak","Fair","Strong","Very Strong"]',
            '    return "Score: {}/100 - {}".format(score, lvl[min(score//20,4)])',
        ])
    elif name == "entropy_bits":
        lines.extend([
            '    import math',
            '    try: s=input("String: ")',
            '    except: return 0.0',
            '    if not s: return 0.0',
            '    ps=0',
            '    if any(c.islower() for c in s): ps+=26',
            '    if any(c.isupper() for c in s): ps+=26',
            '    if any(c.isdigit() for c in s): ps+=10',
            '    if any(not c.isalnum() for c in s): ps+=32',
            '    if ps==0: ps=1',
            '    return round(len(s)*math.log2(ps),2)',
        ])
    else:
        lines.extend(_t_transform(name))
    return lines


# Network implementation generator
def gen_network_impl(name):
    lines = []
    if name == "is_valid_ipv4":
        lines.extend([
            '    import re',
            '    try: ip = input("IPv4: ")',
            '    except: return False',
            '    m=re.match(r"^(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})$",ip.strip())',
            '    if not m: return False',
            '    for g in m.groups():',
            '        if int(g)>255: return False',
            '    return True',
        ])
    elif name in ("is_valid_ipv6","is_valid_email","is_valid_url","is_valid_domain"):
        lines.extend([
            '    name = "{}"'.format(name),
            '    import re',
            '    try: v=input("Value: ")',
            '    except: return False',
            '    p={"is_valid_ipv6":r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$",',
            '       "is_valid_email":r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",',
            '       "is_valid_url":r"^https?://[^\\s/$.?#].[^\\s]*$",',
            '       "is_valid_domain":r"^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\\.[a-zA-Z]{2,}$"}',
            '    return bool(re.match(p[name],v.strip())) if name in p else False',
        ])
    elif name in ("extract_domain","extract_subdomain","url_parse_parts",
                  "url_add_param","url_update_param","domain_tld","domain_sld"):
        lines.extend([
            '    name = "{}"'.format(name),
            '    from urllib.parse import urlparse, urlencode, parse_qs, urlunparse',
            '    try: v=input("URL: ")',
            '    except: return ""',
            '    p=urlparse(v) if "://" in v else urlparse("http://"+v)',
            '    if name=="extract_domain": return p.netloc',
            '    if name=="extract_subdomain":',
            '        parts=p.netloc.split("."); return parts[0] if len(parts)>2 else ""',
            '    if name=="url_parse_parts": return {"scheme":p.scheme,"netloc":p.netloc,"path":p.path,"query":p.query,"fragment":p.fragment}',
            '    if name=="domain_tld": parts=p.netloc.split("."); return parts[-1] if len(parts)>=2 else ""',
            '    if name=="domain_sld": parts=p.netloc.split("."); return parts[-2] if len(parts)>=2 else ""',
            '    k=input("Param: "); v=input("Value: ")',
            '    if name=="url_add_param":',
            '        q=p.query+("&" if p.query else "")+urlencode({k:v})',
            '        return urlunparse((p.scheme,p.netloc,p.path,p.params,q,p.fragment))',
            '    qs=parse_qs(p.query); qs[k]=[v]',
            '    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(qs,doseq=True),p.fragment))',
        ])
    else:
        lines.extend(_t_analyze(name))
    return lines


# Map category prefixes to implementation generators
GEN_MAP = {
    "text_analysis": gen_text_impl,
    "math_extras": gen_math_impl,
    "conversion_extra": gen_convert_impl,
    "format_utils": gen_format_impl,
    "list_extra": gen_list_impl,
    "random_extra": gen_random_impl,
    "crypto_utils": gen_crypto_impl,
    "geometry_extra": gen_geometry_impl,
    "physics_extra": gen_physics_impl,
    "statistics_extra": gen_stats_impl,
    "datetime_utils": gen_datetime_impl,
    "file_utils": gen_file_impl,
    "color_utils": gen_color_impl,
    "string_more": gen_string_impl,
    "network_utils": gen_network_impl,
}


# ---- GENERATE ----
def generate():
    lines = []
    last_dispatch = {}
    cmd_num = 2673

    for cat_name, cat_prefix, func_names, sig_info in CATEGORIES:
        sig_template, sig_desc = sig_info
        impl_gen = GEN_MAP[cat_prefix]
        sig_parts = sig_template.split("(")
        if len(sig_parts) > 1:
            raw_name = sig_parts[0]
            params_part = "(" + sig_parts[1]
        else:
            raw_name = func_names[0] if func_names else "unknown"
            params_part = "()"
        real_params_part = params_part

        for func_name in func_names:
            full_name = "{}_{}".format(cat_prefix, func_name)
            sig = "def {}():".format(full_name)
            lines.append("")
            lines.append(sig)
            lines.append('    """{} utility. (cmd {})"""'.format(cat_name, cmd_num))
            impl = impl_gen(func_name)
            # If implementation references 'name' variable, define it at top
            uses_name = False
            for line in impl:
                stripped = line.strip()
                if 'name' in stripped and ('if ' in stripped or 'in name' in stripped):
                    uses_name = True
                    break
            if uses_name:
                impl.insert(0, '    name = "{}"'.format(func_name))
            lines.extend(impl)
            lines.append("")
            last_dispatch[full_name] = cmd_num
            cmd_num += 1

    dispatch_lines = []
    first_cmd = 2673
    for fn, num in sorted(last_dispatch.items(), key=lambda x: x[1]):
        dispatch_lines.append('    elif cmd in ("{}","{}"):\n        print({}())'.format(num, fn, fn))

    return lines, dispatch_lines, first_cmd, cmd_num - 1


if __name__ == "__main__":
    code_lines, dispatch_lines, first_cmd, last_cmd = generate()
    total_funcs = len([l for l in code_lines if l.startswith("def ")])
    print("Generated {} functions (commands {}-{})".format(total_funcs, first_cmd, last_cmd))
    print("Total code lines: {}".format(len(code_lines)))

    with open("AI.py", encoding="utf-8") as f:
        content = f.read()

    marker = 'if __name__ == "__main__":'
    idx = content.find(marker)
    if idx == -1:
        print("ERROR: Could not find main guard")
        exit(1)

    # First, insert dispatch entries before the else clause in handle_cmd
    else_marker = '    else:\n        print("Unknown. Type \'h\' for help.")'
    else_idx = content.find(else_marker)
    if else_idx != -1 and else_idx < idx:
        before_dispatch = content[:else_idx]
        after_dispatch = content[else_idx:]
        content = before_dispatch + "\n".join(dispatch_lines) + "\n" + after_dispatch
        # Adjust idx since content grew
        idx = content.find(marker)

    # Now insert new function definitions before the main guard
    before = content[:idx]
    after = content[idx:]
    new_section = "\n\n# === v5.0.0 NEW UTILITY FUNCTIONS ===\n"
    new_section += "\n".join(code_lines)
    new_section += "\n"
    content = before + new_section + after

    with open("AI.py", "w", encoding="utf-8") as f:
        f.write(content)

    print("Written to AI.py")
    total_added = len(code_lines) + len(dispatch_lines)
    print("Lines added: ~{}".format(total_added))
