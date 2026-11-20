THRESHOLD = 0.5


def predict(scores):
    """Nhãn có điểm cao nhất trong dict {nhãn: điểm}, hoặc 'unknown' nếu dưới ngưỡng."""
    best = max(scores, key=scores.get)
    if scores[best] < THRESHOLD:
        return "unknown"
    return best