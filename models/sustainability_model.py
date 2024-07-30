def evaluate_carbon_footprint(data):
  
    # Evaluates the carbon footprint based on emissions compared to industry average.
    score = 50 if data.get('emissions', float('inf')) < data.get('industry_average_emissions', float('inf')) else 0
    return score

def evaluate_waste_management(data):
  
    # Evaluates waste management based on the presence of recycling programs and waste reduction efforts.
    score = 0
    if data.get('recycling_program', False):
        score += 30
    if data.get('waste_reduction', False):
        score += 30
    return score

def evaluate_resource_usage(data):
    # Evaluates resource usage based on efficiency in water and energy usage, and use of renewable energy.

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
