def evaluate_carbon_footprint(data):
    # Example criteria: below industry average emissions
    score = 50 if data.get('emissions', float('inf')) < data.get('industry_average_emissions', float('inf')) else 0
    return score

def evaluate_waste_management(data):
    # Example criteria: effective recycling and waste reduction programs
    score = 0
    if data.get('recycling_program', False):
        score += 30
    if data.get('waste_reduction', False):
        score += 30
    return score

def evaluate_resource_usage(data):
    # Example criteria: efficient use of water and energy, renewable resources
    score = 0
    if data.get('water_efficiency', False):
        score += 20
    if data.get('energy_efficiency', False):
        score += 20
    if data.get('uses_renewable_energy', False):
        score += 10
    return score

def check_sustainability(data):
    carbon_score = evaluate_carbon_footprint(data)
    waste_score = evaluate_waste_management(data)
    resource_score = evaluate_resource_usage(data)
    total_score = carbon_score + waste_score + resource_score
    return {
        "status": "Sustainable" if total_score > 100 else "Needs Improvement",
        "total_score": total_score,
        "details": {
            "carbon_footprint_score": carbon_score,
            "waste_management_score": waste_score,
            "resource_usage_score": resource_score
        }
    }
