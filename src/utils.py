
def calculate_on_off(indicator):
    on_off_count = 0
    for i in range(3, len(indicator)):
        if (indicator[i-1] or indicator[i-2] or indicator[i-3]) != indicator[i]:
            on_off_count += 1
    if on_off_count > 10:
        return True
    return False
