# Auto-extracted from AI.py — aipy_utils_network
# All functions are independent utilities with no AI.py-internal dependencies.

def network_utils_is_valid_ipv4():
    """Network utility. (cmd 3573)"""
    import re
    try: ip = input("IPv4: ")
    except: return False
    m=re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip.strip())
    if not m: return False
    for g in m.groups():
        if int(g)>255: return False
    return True


def network_utils_is_valid_ipv6():
    """Network utility. (cmd 3574)"""
    name = "is_valid_ipv6"
    name = "is_valid_ipv6"
    import re
    try: v=input("Value: ")
    except: return False
    p={"is_valid_ipv6":r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$",
       "is_valid_email":r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
       "is_valid_url":r"^https?://[^\s/$.?#].[^\s]*$",
       "is_valid_domain":r"^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"}
    return bool(re.match(p[name],v.strip())) if name in p else False


def network_utils_is_valid_email():
    """Network utility. (cmd 3575)"""
    name = "is_valid_email"
    name = "is_valid_email"
    import re
    try: v=input("Value: ")
    except: return False
    p={"is_valid_ipv6":r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$",
       "is_valid_email":r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
       "is_valid_url":r"^https?://[^\s/$.?#].[^\s]*$",
       "is_valid_domain":r"^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"}
    return bool(re.match(p[name],v.strip())) if name in p else False


def network_utils_is_valid_url():
    """Network utility. (cmd 3576)"""
    name = "is_valid_url"
    name = "is_valid_url"
    import re
    try: v=input("Value: ")
    except: return False
    p={"is_valid_ipv6":r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$",
       "is_valid_email":r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
       "is_valid_url":r"^https?://[^\s/$.?#].[^\s]*$",
       "is_valid_domain":r"^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"}
    return bool(re.match(p[name],v.strip())) if name in p else False


def network_utils_is_valid_domain():
    """Network utility. (cmd 3577)"""
    name = "is_valid_domain"
    name = "is_valid_domain"
    import re
    try: v=input("Value: ")
    except: return False
    p={"is_valid_ipv6":r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$",
       "is_valid_email":r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
       "is_valid_url":r"^https?://[^\s/$.?#].[^\s]*$",
       "is_valid_domain":r"^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"}
    return bool(re.match(p[name],v.strip())) if name in p else False


def network_utils_extract_domain():
    """Network utility. (cmd 3578)"""
    name = "extract_domain"
    name = "extract_domain"
    from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
    try: v=input("URL: ")
    except: return ""
    p=urlparse(v) if "://" in v else urlparse("http://"+v)
    if name=="extract_domain": return p.netloc
    if name=="extract_subdomain":
        parts=p.netloc.split("."); return parts[0] if len(parts)>2 else ""
    if name=="url_parse_parts": return {"scheme":p.scheme,"netloc":p.netloc,"path":p.path,"query":p.query,"fragment":p.fragment}
    if name=="domain_tld": parts=p.netloc.split("."); return parts[-1] if len(parts)>=2 else ""
    if name=="domain_sld": parts=p.netloc.split("."); return parts[-2] if len(parts)>=2 else ""
    k=input("Param: "); v=input("Value: ")
    if name=="url_add_param":
        q=p.query+("&" if p.query else "")+urlencode({k:v})
        return urlunparse((p.scheme,p.netloc,p.path,p.params,q,p.fragment))
    qs=parse_qs(p.query); qs[k]=[v]
    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(qs,doseq=True),p.fragment))


def network_utils_extract_subdomain():
    """Network utility. (cmd 3579)"""
    name = "extract_subdomain"
    name = "extract_subdomain"
    from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
    try: v=input("URL: ")
    except: return ""
    p=urlparse(v) if "://" in v else urlparse("http://"+v)
    if name=="extract_domain": return p.netloc
    if name=="extract_subdomain":
        parts=p.netloc.split("."); return parts[0] if len(parts)>2 else ""
    if name=="url_parse_parts": return {"scheme":p.scheme,"netloc":p.netloc,"path":p.path,"query":p.query,"fragment":p.fragment}
    if name=="domain_tld": parts=p.netloc.split("."); return parts[-1] if len(parts)>=2 else ""
    if name=="domain_sld": parts=p.netloc.split("."); return parts[-2] if len(parts)>=2 else ""
    k=input("Param: "); v=input("Value: ")
    if name=="url_add_param":
        q=p.query+("&" if p.query else "")+urlencode({k:v})
        return urlunparse((p.scheme,p.netloc,p.path,p.params,q,p.fragment))
    qs=parse_qs(p.query); qs[k]=[v]
    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(qs,doseq=True),p.fragment))


def network_utils_url_parse_parts():
    """Network utility. (cmd 3580)"""
    name = "url_parse_parts"
    name = "url_parse_parts"
    from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
    try: v=input("URL: ")
    except: return ""
    p=urlparse(v) if "://" in v else urlparse("http://"+v)
    if name=="extract_domain": return p.netloc
    if name=="extract_subdomain":
        parts=p.netloc.split("."); return parts[0] if len(parts)>2 else ""
    if name=="url_parse_parts": return {"scheme":p.scheme,"netloc":p.netloc,"path":p.path,"query":p.query,"fragment":p.fragment}
    if name=="domain_tld": parts=p.netloc.split("."); return parts[-1] if len(parts)>=2 else ""
    if name=="domain_sld": parts=p.netloc.split("."); return parts[-2] if len(parts)>=2 else ""
    k=input("Param: "); v=input("Value: ")
    if name=="url_add_param":
        q=p.query+("&" if p.query else "")+urlencode({k:v})
        return urlunparse((p.scheme,p.netloc,p.path,p.params,q,p.fragment))
    qs=parse_qs(p.query); qs[k]=[v]
    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(qs,doseq=True),p.fragment))


def network_utils_url_add_param():
    """Network utility. (cmd 3581)"""
    name = "url_add_param"
    name = "url_add_param"
    from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
    try: v=input("URL: ")
    except: return ""
    p=urlparse(v) if "://" in v else urlparse("http://"+v)
    if name=="extract_domain": return p.netloc
    if name=="extract_subdomain":
        parts=p.netloc.split("."); return parts[0] if len(parts)>2 else ""
    if name=="url_parse_parts": return {"scheme":p.scheme,"netloc":p.netloc,"path":p.path,"query":p.query,"fragment":p.fragment}
    if name=="domain_tld": parts=p.netloc.split("."); return parts[-1] if len(parts)>=2 else ""
    if name=="domain_sld": parts=p.netloc.split("."); return parts[-2] if len(parts)>=2 else ""
    k=input("Param: "); v=input("Value: ")
    if name=="url_add_param":
        q=p.query+("&" if p.query else "")+urlencode({k:v})
        return urlunparse((p.scheme,p.netloc,p.path,p.params,q,p.fragment))
    qs=parse_qs(p.query); qs[k]=[v]
    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(qs,doseq=True),p.fragment))


def network_utils_url_update_param():
    """Network utility. (cmd 3582)"""
    name = "url_update_param"
    name = "url_update_param"
    from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
    try: v=input("URL: ")
    except: return ""
    p=urlparse(v) if "://" in v else urlparse("http://"+v)
    if name=="extract_domain": return p.netloc
    if name=="extract_subdomain":
        parts=p.netloc.split("."); return parts[0] if len(parts)>2 else ""
    if name=="url_parse_parts": return {"scheme":p.scheme,"netloc":p.netloc,"path":p.path,"query":p.query,"fragment":p.fragment}
    if name=="domain_tld": parts=p.netloc.split("."); return parts[-1] if len(parts)>=2 else ""
    if name=="domain_sld": parts=p.netloc.split("."); return parts[-2] if len(parts)>=2 else ""
    k=input("Param: "); v=input("Value: ")
    if name=="url_add_param":
        q=p.query+("&" if p.query else "")+urlencode({k:v})
        return urlunparse((p.scheme,p.netloc,p.path,p.params,q,p.fragment))
    qs=parse_qs(p.query); qs[k]=[v]
    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(qs,doseq=True),p.fragment))


def network_utils_mask_ip():
    """Network utility. (cmd 3583)"""
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


def network_utils_mask_email():
    """Network utility. (cmd 3584)"""
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


def network_utils_port_for_protocol():
    """Network utility. (cmd 3585)"""
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


def network_utils_is_private_ip():
    """Network utility. (cmd 3586)"""
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


def network_utils_is_reserved_ip():
    """Network utility. (cmd 3587)"""
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


def network_utils_count_subdomains():
    """Network utility. (cmd 3588)"""
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


def network_utils_domain_tld():
    """Network utility. (cmd 3589)"""
    name = "domain_tld"
    name = "domain_tld"
    from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
    try: v=input("URL: ")
    except: return ""
    p=urlparse(v) if "://" in v else urlparse("http://"+v)
    if name=="extract_domain": return p.netloc
    if name=="extract_subdomain":
        parts=p.netloc.split("."); return parts[0] if len(parts)>2 else ""
    if name=="url_parse_parts": return {"scheme":p.scheme,"netloc":p.netloc,"path":p.path,"query":p.query,"fragment":p.fragment}
    if name=="domain_tld": parts=p.netloc.split("."); return parts[-1] if len(parts)>=2 else ""
    if name=="domain_sld": parts=p.netloc.split("."); return parts[-2] if len(parts)>=2 else ""
    k=input("Param: "); v=input("Value: ")
    if name=="url_add_param":
        q=p.query+("&" if p.query else "")+urlencode({k:v})
        return urlunparse((p.scheme,p.netloc,p.path,p.params,q,p.fragment))
    qs=parse_qs(p.query); qs[k]=[v]
    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(qs,doseq=True),p.fragment))


def network_utils_domain_sld():
    """Network utility. (cmd 3590)"""
    name = "domain_sld"
    name = "domain_sld"
    from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
    try: v=input("URL: ")
    except: return ""
    p=urlparse(v) if "://" in v else urlparse("http://"+v)
    if name=="extract_domain": return p.netloc
    if name=="extract_subdomain":
        parts=p.netloc.split("."); return parts[0] if len(parts)>2 else ""
    if name=="url_parse_parts": return {"scheme":p.scheme,"netloc":p.netloc,"path":p.path,"query":p.query,"fragment":p.fragment}
    if name=="domain_tld": parts=p.netloc.split("."); return parts[-1] if len(parts)>=2 else ""
    if name=="domain_sld": parts=p.netloc.split("."); return parts[-2] if len(parts)>=2 else ""
    k=input("Param: "); v=input("Value: ")
    if name=="url_add_param":
        q=p.query+("&" if p.query else "")+urlencode({k:v})
        return urlunparse((p.scheme,p.netloc,p.path,p.params,q,p.fragment))
    qs=parse_qs(p.query); qs[k]=[v]
    return urlunparse((p.scheme,p.netloc,p.path,p.params,urlencode(qs,doseq=True),p.fragment))


def network_utils_tld_list():
    """Network utility. (cmd 3591)"""
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


def network_utils_mac_vendor_prefix():
    """Network utility. (cmd 3592)"""
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


def network_utils_ip_version():
    """Network utility. (cmd 3593)"""
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


def network_utils_ip_class():
    """Network utility. (cmd 3594)"""
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


def network_utils_ip_to_int():
    """Network utility. (cmd 3595)"""
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


def network_utils_int_to_ip():
    """Network utility. (cmd 3596)"""
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


def network_utils_ip_network_mask():
    """Network utility. (cmd 3597)"""
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


def network_utils_subnet_address():
    """Network utility. (cmd 3598)"""
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


def network_utils_subnet_broadcast():
    """Network utility. (cmd 3599)"""
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


def network_utils_subnet_host_range():
    """Network utility. (cmd 3600)"""
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


def network_utils_subnet_host_count():
    """Network utility. (cmd 3601)"""
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


def network_utils_ip_in_subnet():
    """Network utility. (cmd 3602)"""
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


def network_utils_mac_address_vendor():
    """Network utility. (cmd 3603)"""
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


def network_utils_mac_address_type():
    """Network utility. (cmd 3604)"""
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


def network_utils_mac_address_random():
    """Network utility. (cmd 3605)"""
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


def network_utils_ip_checksum():
    """Network utility. (cmd 3606)"""
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


def network_utils_ping_simulate():
    """Network utility. (cmd 3607)"""
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

if __name__ == "__main__":
    main()
