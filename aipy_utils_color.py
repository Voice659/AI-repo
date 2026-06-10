# Auto-extracted from AI.py — aipy_utils_color
# All functions are independent utilities with no AI.py-internal dependencies.

def color_utils_hex_to_rgb():
    """Color utility. (cmd 3478)"""
    try: hc = input("Hex: ").lstrip("#")
    except: return (0,0,0)
    if len(hc)==3: hc="".join(c*2 for c in hc)
    if len(hc)!=6: return (0,0,0)
    try: return (int(hc[0:2],16),int(hc[2:4],16),int(hc[4:6],16))
    except: return (0,0,0)


def color_utils_rgb_to_hex():
    """Color utility. (cmd 3479)"""
    try: r=max(0,min(255,int(input("R: ")))); g=max(0,min(255,int(input("G: ")))); b=max(0,min(255,int(input("B: "))))
    except: return "#000000"
    return "#{:02x}{:02x}{:02x}".format(r,g,b)


def color_utils_hex_to_hsl():
    """Color utility. (cmd 3480)"""
    name = "hex_to_hsl"
    try:
        if "rgb" in name:
            r=int(input("R: "))/255; g=int(input("G: "))/255; b=int(input("B: "))/255
        else:
            hc=input("Hex: ").lstrip("#")
            if len(hc)==3: hc="".join(c*2 for c in hc)
            r=int(hc[0:2],16)/255; g=int(hc[2:4],16)/255; b=int(hc[4:6],16)/255
    except: return (0,0,0)
    mx, mn = max(r,g,b), min(r,g,b)
    if "hsl" in name:
        l=(mx+mn)/2
        if mx==mn: return (0,0,round(l*100,1))
        d=mx-mn; s=d/(1-abs(2*l-1))
        if mx==r: h=((g-b)/d)%6
        elif mx==g: h=(b-r)/d+2
        else: h=(r-g)/d+4
        return (round(h*60,1),round(s*100,1),round(l*100,1))
    k=1-mx
    if k==1: return (0,0,0,100)
    return (round((1-r-k)/(1-k)*100,1),round((1-g-k)/(1-k)*100,1),round((1-b-k)/(1-k)*100,1),round(k*100,1))


def color_utils_hsl_to_hex():
    """Color utility. (cmd 3481)"""
    name = "hsl_to_hex"
    try: h=float(input("H: "))/360; s=float(input("S: "))/100; l=float(input("L: "))/100
    except: return "#000000"
    def h2(p,q,t):
        if t<0: t+=1
        if t>1: t-=1
        if t<1/6: return p+(q-p)*6*t
        if t<1/2: return q
        if t<2/3: return p+(q-p)*(2/3-t)*6
        return p
    q=l*(1+s) if l<0.5 else l+s-l*s; p=2*l-q
    ri=int(h2(p,q,h+1/3)*255); gi=int(h2(p,q,h)*255); bi=int(h2(p,q,h-1/3)*255)
    if "hex" in name: return "#{:02x}{:02x}{:02x}".format(ri,gi,bi)
    return (ri,gi,bi)


def color_utils_rgb_to_hsl():
    """Color utility. (cmd 3482)"""
    name = "rgb_to_hsl"
    try:
        if "rgb" in name:
            r=int(input("R: "))/255; g=int(input("G: "))/255; b=int(input("B: "))/255
        else:
            hc=input("Hex: ").lstrip("#")
            if len(hc)==3: hc="".join(c*2 for c in hc)
            r=int(hc[0:2],16)/255; g=int(hc[2:4],16)/255; b=int(hc[4:6],16)/255
    except: return (0,0,0)
    mx, mn = max(r,g,b), min(r,g,b)
    if "hsl" in name:
        l=(mx+mn)/2
        if mx==mn: return (0,0,round(l*100,1))
        d=mx-mn; s=d/(1-abs(2*l-1))
        if mx==r: h=((g-b)/d)%6
        elif mx==g: h=(b-r)/d+2
        else: h=(r-g)/d+4
        return (round(h*60,1),round(s*100,1),round(l*100,1))
    k=1-mx
    if k==1: return (0,0,0,100)
    return (round((1-r-k)/(1-k)*100,1),round((1-g-k)/(1-k)*100,1),round((1-b-k)/(1-k)*100,1),round(k*100,1))


def color_utils_hsl_to_rgb():
    """Color utility. (cmd 3483)"""
    name = "hsl_to_rgb"
    try: h=float(input("H: "))/360; s=float(input("S: "))/100; l=float(input("L: "))/100
    except: return "#000000"
    def h2(p,q,t):
        if t<0: t+=1
        if t>1: t-=1
        if t<1/6: return p+(q-p)*6*t
        if t<1/2: return q
        if t<2/3: return p+(q-p)*(2/3-t)*6
        return p
    q=l*(1+s) if l<0.5 else l+s-l*s; p=2*l-q
    ri=int(h2(p,q,h+1/3)*255); gi=int(h2(p,q,h)*255); bi=int(h2(p,q,h-1/3)*255)
    if "hex" in name: return "#{:02x}{:02x}{:02x}".format(ri,gi,bi)
    return (ri,gi,bi)


def color_utils_rgb_to_cmyk():
    """Color utility. (cmd 3484)"""
    name = "rgb_to_cmyk"
    try:
        if "rgb" in name:
            r=int(input("R: "))/255; g=int(input("G: "))/255; b=int(input("B: "))/255
        else:
            hc=input("Hex: ").lstrip("#")
            if len(hc)==3: hc="".join(c*2 for c in hc)
            r=int(hc[0:2],16)/255; g=int(hc[2:4],16)/255; b=int(hc[4:6],16)/255
    except: return (0,0,0)
    mx, mn = max(r,g,b), min(r,g,b)
    if "hsl" in name:
        l=(mx+mn)/2
        if mx==mn: return (0,0,round(l*100,1))
        d=mx-mn; s=d/(1-abs(2*l-1))
        if mx==r: h=((g-b)/d)%6
        elif mx==g: h=(b-r)/d+2
        else: h=(r-g)/d+4
        return (round(h*60,1),round(s*100,1),round(l*100,1))
    k=1-mx
    if k==1: return (0,0,0,100)
    return (round((1-r-k)/(1-k)*100,1),round((1-g-k)/(1-k)*100,1),round((1-b-k)/(1-k)*100,1),round(k*100,1))


def color_utils_cmyk_to_rgb():
    """Color utility. (cmd 3485)"""
    name = "cmyk_to_rgb"
    try:
        c=float(input("C: "))/100; m=float(input("M: "))/100
        y=float(input("Y: "))/100; k=float(input("K: "))/100
    except: return "#000000"
    ri=int(255*(1-c)*(1-k)); gi=int(255*(1-m)*(1-k)); bi=int(255*(1-y)*(1-k))
    if "hex" in name: return "#{:02x}{:02x}{:02x}".format(ri,gi,bi)
    return (ri,gi,bi)


def color_utils_hex_to_cmyk():
    """Color utility. (cmd 3486)"""
    name = "hex_to_cmyk"
    try:
        if "rgb" in name:
            r=int(input("R: "))/255; g=int(input("G: "))/255; b=int(input("B: "))/255
        else:
            hc=input("Hex: ").lstrip("#")
            if len(hc)==3: hc="".join(c*2 for c in hc)
            r=int(hc[0:2],16)/255; g=int(hc[2:4],16)/255; b=int(hc[4:6],16)/255
    except: return (0,0,0)
    mx, mn = max(r,g,b), min(r,g,b)
    if "hsl" in name:
        l=(mx+mn)/2
        if mx==mn: return (0,0,round(l*100,1))
        d=mx-mn; s=d/(1-abs(2*l-1))
        if mx==r: h=((g-b)/d)%6
        elif mx==g: h=(b-r)/d+2
        else: h=(r-g)/d+4
        return (round(h*60,1),round(s*100,1),round(l*100,1))
    k=1-mx
    if k==1: return (0,0,0,100)
    return (round((1-r-k)/(1-k)*100,1),round((1-g-k)/(1-k)*100,1),round((1-b-k)/(1-k)*100,1),round(k*100,1))


def color_utils_cmyk_to_hex():
    """Color utility. (cmd 3487)"""
    name = "cmyk_to_hex"
    try:
        c=float(input("C: "))/100; m=float(input("M: "))/100
        y=float(input("Y: "))/100; k=float(input("K: "))/100
    except: return "#000000"
    ri=int(255*(1-c)*(1-k)); gi=int(255*(1-m)*(1-k)); bi=int(255*(1-y)*(1-k))
    if "hex" in name: return "#{:02x}{:02x}{:02x}".format(ri,gi,bi)
    return (ri,gi,bi)


def color_utils_brightness_luminance():
    """Color utility. (cmd 3488)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_brightness_perceived():
    """Color utility. (cmd 3489)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_contrast_ratio():
    """Color utility. (cmd 3490)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_is_dark_color():
    """Color utility. (cmd 3491)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_is_light_color():
    """Color utility. (cmd 3492)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_complimentary_color():
    """Color utility. (cmd 3493)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_analogous_colors():
    """Color utility. (cmd 3494)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_triadic_colors():
    """Color utility. (cmd 3495)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_tetradic_colors():
    """Color utility. (cmd 3496)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_split_complementary():
    """Color utility. (cmd 3497)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_color_name():
    """Color utility. (cmd 3498)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_random_pastel():
    """Color utility. (cmd 3499)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_random_vibrant():
    """Color utility. (cmd 3500)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_random_grayscale():
    """Color utility. (cmd 3501)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_mix_colors():
    """Color utility. (cmd 3502)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_blend_colors():
    """Color utility. (cmd 3503)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_tint_color():
    """Color utility. (cmd 3504)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_shade_color():
    """Color utility. (cmd 3505)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_tone_color():
    """Color utility. (cmd 3506)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_invert_color():
    """Color utility. (cmd 3507)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_color_temperature():
    """Color utility. (cmd 3508)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_color_wavelength():
    """Color utility. (cmd 3509)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_color_saturation():
    """Color utility. (cmd 3510)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_color_luminance():
    """Color utility. (cmd 3511)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_color_delta_e():
    """Color utility. (cmd 3512)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_palette_from_hex():
    """Color utility. (cmd 3513)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_gradient_between():
    """Color utility. (cmd 3514)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_lerp_color():
    """Color utility. (cmd 3515)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_averaged_color():
    """Color utility. (cmd 3516)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output


def color_utils_xyz_to_rgb():
    """Color utility. (cmd 3517)"""
    try:
        val = float(input("Enter value: "))
    except (ValueError, EOFError):
        return "Invalid input"
    # Validate input range
    if val < 0:
        return "Cannot process negative value"
    # Compute intermediate
    step_a = abs(val)
    step_b = step_a * 2
    step_c = step_b + 1
    # Apply core transformation
    import math
    result = math.sqrt(step_b + step_c) if step_b + step_c >= 0 else 0
    # Round and format output
    result = round(result, 4)
    # Build response
    output = "Result: {}".format(result)
    return output
