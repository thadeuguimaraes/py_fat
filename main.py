def calculate_percentage(state_sales, total_sales):
    """
    Calcula o percentual de representação de cada estado no faturamento total.
    """
    percentages = {}
    for state, sales in state_sales.items():
        percentage = (sales / total_sales) * 100
        percentages[state] = percentage
    return percentages

# Exemplo de uso
state_sales = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
total_sales = sum(state_sales.values())
percentages = calculate_percentage(state_sales, total_sales)

for state, percentage in percentages.items():
    print(f"{state} representou {percentage:.2f}% do faturamento total.")
