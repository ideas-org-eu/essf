def evaluate_labor_practices(data):
    """
    Evaluates labor practices based on fair wages, safe working conditions, and absence of child labor.
    """
    score = 0
    if data.get('fair_wages', False):
        score += 30
    if data.get('safe_conditions', False):
        score += 30
    if not data.get('child_labor', False):
        score += 40

    # Additional criteria can be added here
    if data.get('employee_benefits', False):
        score += 20
    if data.get('diversity_inclusion', False):
        score += 20

    return min(score, 100)  # Ensure the score does not exceed 100


def evaluate_corporate_governance(data):
    """
    Evaluates corporate governance based on transparency and absence of corruption.
    """
    score = 0
    if data.get('transparency', False):
        score += 50
    if not data.get('corruption', False):
        score += 50

    # Additional criteria can be added here
    if data.get('board_independence', False):
        score += 20
    if data.get('audit_committee', False):
        score += 20

    return min(score, 100)  # Ensure the score does not exceed 100


def evaluate_data_privacy(data):
    """
    Evaluates data privacy based on data protection compliance and user privacy protection.
    """
    score = 0
    if data.get('data_protection_compliance', False):
        score += 50
    if data.get('privacy_protection', False):
        score += 50

    # Additional criteria can be added here
    if data.get('third_party_audits', False):
        score += 20
    if data.get('incident_response', False):
        score += 20

    return min(score, 100)  # Ensure the score does not exceed 100


def check_ethics(data):
    """
    Checks the ethical practices of a given entity based on labor practices, corporate governance, and data privacy.
    """
    labor_score = evaluate_labor_practices(data)
    governance_score = evaluate_corporate_governance(data)
    privacy_score = evaluate_data_privacy(data)

    # Adjusted scoring weights for a balanced evaluation
    total_score = labor_score + governance_score + privacy_score
    status = "Ethical" if total_score >= 150 else "Needs Improvement"

    return {
        "status": status,
        "total_score": total_score,
        "details": {
            "labor_practices_score": labor_score,
            "corporate_governance_score": governance_score,
            "data_privacy_score": privacy_score
        }
    }
