from statistics import mean, median, stdev

def calculate_stats(values):
    return {
        "mean": mean(values),
        "median": median(values),
        "min": min(values),
        "max": max(values),
        "stdev": stdev(values) if len(values) > 1 else 0
    }
