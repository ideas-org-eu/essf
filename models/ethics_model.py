def evaluate_labor_practices(data):
    # Example criteria: fair wages, safe working conditions, no child labor
    score = 0
    if data.get('fair_wages', False):
        score += 30
    if data.get('safe_conditions', False):
        score += 30
    if not data.get('child_labor', False):
        score += 40
    return score

def evaluate_corporate_governance(data):
    # Example criteria: transparency, no corruption
    score = 0
    if data.get('transparency', False):
        score += 50
    if not data.get('corruption', False):
        score += 50
    return score

def evaluate_data_privacy(data):
    # Example criteria: data protection compliance, user privacy protection
    score = 0
    if data.get('data_protection_compliance', False):
        score += 50
    if data.get('privacy_protection', False):
        score += 50
    return score

def check_ethics(data):
    labor_score = evaluate_labor_practices(data)
    governance_score = evaluate_corporate_governance(data)
    privacy_score = evaluate_data_privacy(data)
    total_score = labor_score + governance_score + privacy_score
    return {
        "status": "Ethical" if total_score > 100 else "Needs Improvement",
        "total_score": total_score,
        "details": {
            "labor_practices_score": labor_score,
            "corporate_governance_score": governance_score,
            "data_privacy_score": privacy_score
        }
    }
