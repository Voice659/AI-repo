# Auto-extracted from AI.py — aipy_text
# All functions are independent utilities with no AI.py-internal dependencies.

def text_analysis_word_count():
    """Text utility. (cmd 2673)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return "No input provided"
    if not isinstance(text, str):
        text = str(text)
    if not text:
        return {"words": 0, "chars": 0, "sentences": 0}
    # Split into words
    words = text.split()
    word_count_val = len(words)
    # Count characters including spaces
    chars = len(text)
    # Count sentences by punctuation
    sentences = 0
    for c in ".!?":
        sentences += text.count(c)
    if sentences == 0 and word_count_val > 0:
        sentences = 1
    # Count whitespace
    spaces = text.count(" ")
    # Build detailed report
    result = {
        "words": word_count_val,
        "chars": chars,
        "sentences": max(sentences, 1),
        "spaces": spaces,
        "avg_word_length": round(chars / word_count_val, 2) if word_count_val else 0
    }
    return result


def text_analysis_char_frequency():
    """Text utility. (cmd 2674)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return "No input"
    if not isinstance(text, str): text = str(text)
    if not text:
        return {}
    freq = {}
    for c in text:
        if c.isprintable():
            freq[c] = freq.get(c, 0) + 1
    result = sorted(freq.items(), key=lambda x: -x[1])
    return result


def text_analysis_word_frequency():
    """Text utility. (cmd 2675)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return "No input"
    if not isinstance(text, str): text = str(text)
    import re
    words = re.findall(r"[a-zA-Z']+", text.lower())
    if not words:
        return []
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    result = sorted(freq.items(), key=lambda x: -x[1])
    return result


def text_analysis_reverse_words():
    """Text utility. (cmd 2676)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    if not text.strip():
        return ""
    words = text.split()
    # Reverse the word order
    reversed_list = list(reversed(words))
    # Join with spaces
    result = " ".join(reversed_list)
    return result


def text_analysis_is_palindrome_sentence():
    """Text utility. (cmd 2677)"""
    try:
        text = input("Enter sentence: ")
    except (ValueError, EOFError):
        return False
    import re
    if not isinstance(text, str): text = str(text)
    if not text.strip():
        return False
    clean = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    is_pal = clean == clean[::-1]
    if is_pal:
        return True
    return False


def text_analysis_count_vowels():
    """Text utility. (cmd 2678)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return 0
    if not isinstance(text, str): text = str(text)
    if not text:
        return 0
    vowels = set("aeiouAEIOU")
    count = 0
    for c in text:
        if c in vowels:
            count += 1
    return count


def text_analysis_count_consonants():
    """Text utility. (cmd 2679)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return 0
    if not isinstance(text, str): text = str(text)
    if not text:
        return 0
    import string
    vowels = set("aeiouAEIOU")
    count = 0
    for c in text:
        if c.isalpha() and c not in vowels:
            count += 1
    return count


def text_analysis_count_syllables_approx():
    """Text utility. (cmd 2680)"""
    try:
        text = input("Enter word: ")
    except (ValueError, EOFError):
        return 0
    if not isinstance(text, str): text = str(text)
    text = text.lower().strip()
    if not text: return 0
    vowels = "aeiouy"
    count = 0
    prev_vowel = False
    for c in text:
        is_v = c in vowels
        if is_v and not prev_vowel:
            count += 1
        prev_vowel = is_v
    if text.endswith("e"):
        count = max(count - 1, 1)
    return count


def text_analysis_unique_words():
    """Text utility. (cmd 2681)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return []
    if not isinstance(text, str): text = str(text)
    import re
    words = re.findall(r"[a-zA-Z']+", text.lower())
    unique = sorted(set(words))
    return unique


def text_analysis_common_words():
    """Text utility. (cmd 2682)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return []
    if not isinstance(text, str): text = str(text)
    import re
    words = re.findall(r"[a-zA-Z']+", text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: -x[1])
    return sorted_words[:15]


def text_analysis_text_summary():
    """Text utility. (cmd 2683)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return {"preview": "", "words": 0, "chars": 0}
    if not isinstance(text, str): text = str(text)
    words = text.split()
    word_count_val = len(words)
    char_count = len(text)
    preview_len = min(200, len(text))
    preview = text[:preview_len]
    if len(text) > preview_len:
        preview += "..."
    return {"preview": preview, "words": word_count_val, "chars": char_count}


def text_analysis_camel_to_snake():
    """Text utility. (cmd 2684)"""
    try:
        text = input("Enter camelCase: ")
    except (ValueError, EOFError):
        return ""
    import re
    if not isinstance(text, str): text = str(text)
    if not text: return ""
    result = re.sub(r"([A-Z])", r"_", text).lower().lstrip("_")
    return result


def text_analysis_snake_to_camel():
    """Text utility. (cmd 2685)"""
    try:
        text = input("Enter snake_case: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    if not text: return ""
    parts = text.split("_")
    result = parts[0] + "".join(p.title() for p in parts[1:])
    return result


def text_analysis_slugify():
    """Text utility. (cmd 2686)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    import re
    if not isinstance(text, str): text = str(text)
    if not text: return ""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    text = text.strip("-")
    return text


def text_analysis_truncate_words():
    """Text utility. (cmd 2687)"""
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


def text_analysis_levenshtein_distance():
    """Text utility. (cmd 2688)"""
    try:
        s1 = input("First string: ")
        s2 = input("Second string: ")
    except (ValueError, EOFError):
        return -1
    if not isinstance(s1, str): s1 = str(s1)
    if not isinstance(s2, str): s2 = str(s2)
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if len(s2) == 0:
        return len(s1)
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            cost = 0 if c1 == c2 else 1
            curr.append(min(curr[j] + 1, prev[j + 1] + 1, prev[j] + cost))
        prev = curr
    return prev[-1]


def text_analysis_damerau_levenshtein():
    """Text utility. (cmd 2689)"""
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


def text_analysis_hamming_distance():
    """Text utility. (cmd 2690)"""
    try:
        s1 = input("First string: ")
        s2 = input("Second string: ")
    except (ValueError, EOFError):
        return -1
    if not isinstance(s1, str): s1 = str(s1)
    if not isinstance(s2, str): s2 = str(s2)
    if len(s1) != len(s2):
        return -1
    diff = 0
    for a, b in zip(s1, s2):
        if a != b:
            diff += 1
    return diff


def text_analysis_jaro_winkler():
    """Text utility. (cmd 2691)"""
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


def text_analysis_longest_common_substring():
    """Text utility. (cmd 2692)"""
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


def text_analysis_longest_common_subsequence():
    """Text utility. (cmd 2693)"""
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


def text_analysis_ngrams():
    """Text utility. (cmd 2694)"""
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


def text_analysis_sentiment_score():
    """Text utility. (cmd 2695)"""
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


def text_analysis_readability_score():
    """Text utility. (cmd 2696)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return 0.0
    if not isinstance(text, str): text = str(text)
    words = text.split()
    if len(words) < 2:
        return 0.0
    sentences = text.count(".") + text.count("!") + text.count("?")
    sentences = max(sentences, 1)
    syllables = sum(1 for c in text.lower() if c in "aeiou")
    grade = 206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syllables / len(words))
    return round(grade, 2)


def text_analysis_phonetic_soundex():
    """Text utility. (cmd 2697)"""
    try:
        text = input("Enter name: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    text = text.upper()
    if not text: return ""
    first = text[0]
    rest = text[1:]
    mapping = {"B":"1","F":"1","P":"1","V":"1","C":"2","G":"2","J":"2","K":"2","Q":"2","S":"2","X":"2","Z":"2","D":"3","T":"3","L":"4","M":"5","N":"5","R":"6"}
    code = first
    prev = ""
    for c in rest:
        if c in mapping and mapping[c] != prev:
            code += mapping[c]
            prev = mapping[c]
        elif c not in mapping:
            prev = ""
    code = code[:4].ljust(4, "0")
    return code


def text_analysis_is_anagram():
    """Text utility. (cmd 2698)"""
    try:
        s1 = input("First word: ")
        s2 = input("Second word: ")
    except (ValueError, EOFError):
        return False
    if not isinstance(s1, str): s1 = str(s1)
    if not isinstance(s2, str): s2 = str(s2)
    c1 = sorted(s1.lower().replace(" ", ""))
    c2 = sorted(s2.lower().replace(" ", ""))
    return c1 == c2


def text_analysis_is_anagram_phrase():
    """Text utility. (cmd 2699)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_random_sentence():
    """Text utility. (cmd 2700)"""
    import random as _r
    subjects = ["The cat","A dog","My friend","The teacher","An artist"]
    verbs = ["runs","jumps","thinks","sings","dances","reads","writes"]
    objects = ["quickly","slowly","loudly","quietly","every day"]
    subj = _r.choice(subjects)
    verb = _r.choice(verbs)
    obj = _r.choice(objects)
    result = "{} {} {}.".format(subj, verb, obj)
    return result


def text_analysis_random_paragraph():
    """Text utility. (cmd 2701)"""
    import random as _r
    sentences = []
    count = _r.randint(3, 6)
    for i in range(count):
        sentences.append(random_sentence())
    result = " ".join(sentences)
    return result


def text_analysis_wrap_text():
    """Text utility. (cmd 2702)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    import textwrap
    if not isinstance(text, str): text = str(text)
    if not text: return ""
    wrapped = textwrap.fill(text, width=70)
    return wrapped


def text_analysis_center_text():
    """Text utility. (cmd 2703)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    try:
        w = int(input("Width: ") or "80")
    except ValueError:
        w = 80
    if not isinstance(text, str): text = str(text)
    result = text.center(w)
    return result


def text_analysis_justify_text():
    """Text utility. (cmd 2704)"""
    try:
        text = input("Enter text: ")
        width_str = input("Width: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    try: width = int(width_str)
    except: width = 72
    words = text.split()
    if not words: return ""
    lines_out = []
    curr = []
    curr_len = 0
    for w in words:
        if curr_len + len(w) + len(curr) > width:
            spaces_needed = width - curr_len
            gaps = len(curr) - 1 or 1
            extra = spaces_needed // gaps
            remainder = spaces_needed % gaps
            line = ""
            for i, word in enumerate(curr):
                line += word
                if i < len(curr) - 1:
                    line += " " + " " * extra
                    if i < remainder:
                        line += " "
            lines_out.append(line)
            curr = [w]
            curr_len = len(w)
        else:
            curr.append(w)
            curr_len += len(w)
    if curr:
        lines_out.append(" ".join(curr))
    return "\n".join(lines_out)


def text_analysis_tab_to_spaces():
    """Text utility. (cmd 2705)"""
    name = "tab_to_spaces"
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    if "tab_to" in name:
        result = text.replace("\t", "    ")
    else:
        result = text.replace("    ", "\t")
    return result


def text_analysis_spaces_to_tabs():
    """Text utility. (cmd 2706)"""
    name = "spaces_to_tabs"
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    if "tab_to" in name:
        result = text.replace("\t", "    ")
    else:
        result = text.replace("    ", "\t")
    return result


def text_analysis_strip_punctuation():
    """Text utility. (cmd 2707)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    import string
    if not isinstance(text, str): text = str(text)
    result = "".join(c for c in text if c not in string.punctuation)
    return result


def text_analysis_strip_numbers():
    """Text utility. (cmd 2708)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    result = "".join(c for c in text if not c.isdigit())
    return result


def text_analysis_swap_case():
    """Text utility. (cmd 2709)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    result = text.swapcase()
    return result


def text_analysis_indent_text():
    """Text utility. (cmd 2710)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    lines_list = text.split("\n")
    indented = "\n".join("    " + line for line in lines_list)
    return indented


def text_analysis_is_pangram():
    """Text utility. (cmd 2711)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return False
    import string
    if not isinstance(text, str): text = str(text)
    letters = set(c.lower() for c in text if c.isalpha())
    return len(letters) >= 26


def text_analysis_is_isogram():
    """Text utility. (cmd 2712)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return False
    if not isinstance(text, str): text = str(text)
    letters = [c.lower() for c in text if c.isalpha()]
    return len(letters) == len(set(letters))


def text_analysis_count_letters():
    """Text utility. (cmd 2713)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return 0
    if not isinstance(text, str): text = str(text)
    count = sum(1 for c in text if c.isalpha())
    return count


def text_analysis_count_digits():
    """Text utility. (cmd 2714)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return 0
    if not isinstance(text, str): text = str(text)
    count = sum(1 for c in text if c.isdigit())
    return count


def text_analysis_count_spaces():
    """Text utility. (cmd 2715)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return 0
    if not isinstance(text, str): text = str(text)
    count = text.count(" ")
    return count


def text_analysis_extract_emails():
    """Text utility. (cmd 2716)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return []
    import re
    if not isinstance(text, str): text = str(text)
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    return emails


def text_analysis_extract_urls():
    """Text utility. (cmd 2717)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return []
    import re
    if not isinstance(text, str): text = str(text)
    pattern = r"https?://[^\s<>()]+"
    urls = re.findall(pattern, text)
    return urls


def text_analysis_split_sentences():
    """Text utility. (cmd 2718)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return []
    import re
    if not isinstance(text, str): text = str(text)
    sentences = re.split(r"(?<=[.!?])\s+", text)
    result = [s for s in sentences if s]
    return result


def text_analysis_rotate_string():
    """Text utility. (cmd 2719)"""
    try:
        text = input("Enter text: ")
        shift = int(input("Shift: ") or "13")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    shift = shift % 26
    result = []
    for c in text:
        if "a" <= c <= "z":
            result.append(chr((ord(c) - 97 + shift) % 26 + 97))
        elif "A" <= c <= "Z":
            result.append(chr((ord(c) - 65 + shift) % 26 + 65))
        else:
            result.append(c)
    return "".join(result)


def text_analysis_ascii_shift():
    """Text utility. (cmd 2720)"""
    try:
        text = input("Enter text: ")
        shift = int(input("Shift: ") or "13")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    shift = shift % 26
    result = []
    for c in text:
        if "a" <= c <= "z":
            result.append(chr((ord(c) - 97 + shift) % 26 + 97))
        elif "A" <= c <= "Z":
            result.append(chr((ord(c) - 65 + shift) % 26 + 65))
        else:
            result.append(c)
    return "".join(result)


def text_analysis_word_wrap_break():
    """Text utility. (cmd 2721)"""
    try:
        text = input("Enter text: ")
        width_str = input("Width: ")
    except (ValueError, EOFError):
        return ""
    try:
        width = int(width_str)
    except ValueError:
        width = 40
    if not isinstance(text, str): text = str(text)
    words = text.split()
    lines_out = []
    curr = ""
    for w in words:
        if curr and len(curr) + 1 + len(w) > width:
            lines_out.append(curr)
            curr = w
        else:
            curr = (curr + " " + w).strip()
    if curr:
        lines_out.append(curr)
    return "\n".join(lines_out)


def text_analysis_letter_frequency_score():
    """Text utility. (cmd 2722)"""
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


def text_analysis_is_heterogram():
    """Text utility. (cmd 2723)"""
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


def text_analysis_count_syllables_rule():
    """Text utility. (cmd 2724)"""
    try:
        text = input("Enter word: ")
    except (ValueError, EOFError):
        return 0
    if not isinstance(text, str): text = str(text)
    text = text.lower().strip()
    if not text: return 0
    vowels = "aeiouy"
    count = 0
    prev_vowel = False
    for c in text:
        is_v = c in vowels
        if is_v and not prev_vowel:
            count += 1
        prev_vowel = is_v
    if text.endswith("e"):
        count = max(count - 1, 1)
    return count


def text_analysis_unique_letter_ratio():
    """Text utility. (cmd 2725)"""
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


def text_analysis_avg_word_length():
    """Text utility. (cmd 2726)"""
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


def text_analysis_sentence_length_stats():
    """Text utility. (cmd 2727)"""
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


def text_analysis_detect_language():
    """Text utility. (cmd 2728)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return "unknown"
    if not isinstance(text, str): text = str(text)
    text_lower = text.lower()
    common_en = ["the","and","for","are","but","not","you","all","can","had"]
    common_ru = ["что","как","все","она","так","его","только","меня","было","нет"]
    en_score = sum(1 for w in common_en if w in text_lower)
    ru_score = sum(1 for w in common_ru if w in text_lower)
    if en_score > ru_score: return "en"
    if ru_score > en_score: return "ru"
    return "unknown"


def text_analysis_keyword_extract():
    """Text utility. (cmd 2729)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return []
    import re
    if not isinstance(text, str): text = str(text)
    words = re.findall(r"[a-zA-Z]{4,}", text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_kw = sorted(freq.items(), key=lambda x: -x[1])
    return [w for w, c in sorted_kw[:10]]


def text_analysis_count_char_types():
    """Text utility. (cmd 2730)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return {"letters":0,"digits":0,"spaces":0,"punctuation":0}
    import string
    if not isinstance(text, str): text = str(text)
    letters = sum(1 for c in text if c.isalpha())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    punct = sum(1 for c in text if c in string.punctuation)
    return {"letters":letters,"digits":digits,"spaces":spaces,"punctuation":punct}


def text_analysis_mask_emails():
    """Text utility. (cmd 2731)"""
    name = "mask_emails"
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    import re
    if not isinstance(text, str): text = str(text)
    def _mask(m):
        parts = m.group(0).split("@")
        name = parts[0][0] + "***" if parts[0] else "***"
        return name + "@" + parts[1]
    result = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", _mask, text)
    return result


def text_analysis_mask_phones():
    """Text utility. (cmd 2732)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    import re
    if not isinstance(text, str): text = str(text)
    def _mask_phone(m):
        digits = "".join(c for c in m.group(0) if c.isdigit())
        if len(digits) >= 10:
            return "***-***-{}".format(digits[-4:])
        return m.group(0)
    result = re.sub(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", _mask_phone, text)
    return result


def text_analysis_pluralize_word():
    """Text utility. (cmd 2733)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_singularize_word():
    """Text utility. (cmd 2734)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_camel_split():
    """Text utility. (cmd 2735)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_kebab_to_camel():
    """Text utility. (cmd 2736)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_camel_to_kebab():
    """Text utility. (cmd 2737)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_remove_extra_spaces():
    """Text utility. (cmd 2738)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    import re
    if not isinstance(text, str): text = str(text)
    result = re.sub(r"\s+", " ", text).strip()
    return result


def text_analysis_is_uppercase():
    """Text utility. (cmd 2739)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_is_lowercase():
    """Text utility. (cmd 2740)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_count_substring():
    """Text utility. (cmd 2741)"""
    try:
        text = input("Enter text: ")
        sub = input("Enter substring: ")
    except (ValueError, EOFError):
        return 0
    if not isinstance(text, str): text = str(text)
    if not sub: return 0
    count = text.lower().count(sub.lower())
    return count


def text_analysis_find_all_positions():
    """Text utility. (cmd 2742)"""
    try:
        text = input("Enter text: ")
        sub = input("Enter substring: ")
    except (ValueError, EOFError):
        return []
    if not isinstance(text, str): text = str(text)
    if not sub: return []
    positions = []
    start = 0
    while True:
        idx = text.find(sub, start)
        if idx == -1: break
        positions.append(idx)
        start = idx + 1
    return positions


def text_analysis_replace_multiple():
    """Text utility. (cmd 2743)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    replacements = {"a":"@","e":"3","i":"1","o":"0","s":"$"}
    result = text
    for old, new in replacements.items():
        result = result.replace(old, new)
    return result


def text_analysis_prefix_lines():
    """Text utility. (cmd 2744)"""
    try:
        text = input("Enter text: ")
        prefix_str = input("Prefix: ") or "> "
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    lines_list = text.split("\n")
    result = "\n".join(prefix_str + line for line in lines_list)
    return result


def text_analysis_suffix_lines():
    """Text utility. (cmd 2745)"""
    try:
        text = input("Enter text: ")
        suffix_str = input("Suffix: ") or " |"
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    lines_list = text.split("\n")
    result = "\n".join(line + suffix_str for line in lines_list)
    return result


def text_analysis_quote_text():
    """Text utility. (cmd 2746)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    result = "\"" + text + "\""
    return result


def text_analysis_unquote_text():
    """Text utility. (cmd 2747)"""
    try:
        text = input("Enter quoted text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    result = text.strip("'\"")
    return result


def text_analysis_title_case():
    """Text utility. (cmd 2748)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    result = text.title()
    return result


def text_analysis_invert_case():
    """Text utility. (cmd 2749)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    result = text.swapcase()
    return result


def text_analysis_alternating_case():
    """Text utility. (cmd 2750)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    result = "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text))
    return result


def text_analysis_count_lines():
    """Text utility. (cmd 2751)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return 0
    if not isinstance(text, str): text = str(text)
    lines_list = text.split("\n")
    non_empty = sum(1 for l in lines_list if l.strip())
    return non_empty


def text_analysis_longest_word():
    """Text utility. (cmd 2752)"""
    try:
        text = input("Enter text: ")
    except (ValueError, EOFError):
        return ""
    if not isinstance(text, str): text = str(text)
    import re
    words = re.findall(r"[a-zA-Z']+", text)
    if not words: return ""
    longest = max(words, key=len)
    return longest


def text_analysis_shortest_word():
    """Text utility. (cmd 2753)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_most_frequent_word():
    """Text utility. (cmd 2754)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_rarest_word():
    """Text utility. (cmd 2755)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_count_sentences():
    """Text utility. (cmd 2756)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_count_paragraphs():
    """Text utility. (cmd 2757)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_text_checksum():
    """Text utility. (cmd 2758)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_text_hash_djb2():
    """Text utility. (cmd 2759)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_is_blank():
    """Text utility. (cmd 2760)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_is_empty():
    """Text utility. (cmd 2761)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result


def text_analysis_is_alpha():
    """Text utility. (cmd 2762)"""
    try:
        value = input("Enter input: ")
    except (ValueError, EOFError):
        return "Error reading input"
    if value is None:
        return "No input received"
    value = str(value)
    if not value:
        return ""
    # Apply transformation step by step
    step1 = value.strip()
    step2 = step1.lower()
    step3 = step2.replace(" ", "_")
    result = step3
    return result
