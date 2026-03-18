"""
Calculadora de IMC (Índice de Massa Corporal)
BMI Calculator - suporta unidades métricas e imperiais
"""


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula o IMC dado peso (kg) e altura (m).
    
    Args:
        peso: Peso em quilogramas
        altura: Altura em metros
        
    Returns:
        Valor do IMC arredondado com 2 casas decimais
        
    Raises:
        ValueError: Se peso ou altura forem inválidos
    """
    if peso <= 0:
        raise ValueError("O peso deve ser maior que zero.")
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    
    return round(peso / (altura ** 2), 2)


def converter_imperial_para_metrico(peso_lb: float, altura_in: float) -> tuple[float, float]:
    """
    Converte peso de libras para kg e altura de polegadas para metros.
    
    Args:
        peso_lb: Peso em libras
        altura_in: Altura em polegadas
        
    Returns:
        Tupla (peso_kg, altura_m)
    """
    peso_kg = peso_lb * 0.453592
    altura_m = altura_in * 0.0254
    return round(peso_kg, 2), round(altura_m, 4)


def classificar_imc(imc: float) -> dict:
    """
    Classifica o IMC de acordo com os critérios da OMS.
    
    Args:
        imc: Valor do IMC
        
    Returns:
        Dicionário com 'categoria', 'descricao' e 'cor'
    """
    categorias = [
        (16.0,  "Magreza Grave",       "Muito abaixo do peso recomendado",      "🔵"),
        (17.0,  "Magreza Moderada",    "Abaixo do peso recomendado",            "🟢"),
        (18.5,  "Magreza Leve",        "Levemente abaixo do peso recomendado",  "🟡"),
        (25.0,  "Peso Normal",         "Peso saudável",                         "✅"),
        (30.0,  "Sobrepeso",           "Acima do peso recomendado",             "🟠"),
        (35.0,  "Obesidade Grau I",    "Obesidade moderada",                    "🔴"),
        (40.0,  "Obesidade Grau II",   "Obesidade severa",                      "🔴"),
        (float("inf"), "Obesidade Grau III", "Obesidade mórbida",               "🔴"),
    ]

    for limite, categoria, descricao, cor in categorias:
        if imc < limite:
            return {"categoria": categoria, "descricao": descricao, "cor": cor}

    return {"categoria": "Obesidade Grau III", "descricao": "Obesidade mórbida", "cor": "🔴"}


def exibir_resultado(imc: float, classificacao: dict) -> None:
    """Exibe o resultado formatado no terminal."""
    separador = "=" * 45
    print(f"\n{separador}")
    print(f"  {classificacao['cor']}  RESULTADO DO IMC")
    print(separador)
    print(f"  IMC calculado  : {imc:.2f}")
    print(f"  Classificação  : {classificacao['categoria']}")
    print(f"  Descrição      : {classificacao['descricao']}")
    print(separador)
    print()


def obter_float(mensagem: str) -> float:
    """Solicita um número float ao usuário com validação."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor <= 0:
                print("  ⚠️  Por favor, insira um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("  ⚠️  Valor inválido. Use apenas números (ex: 70 ou 1.75).")


def escolher_unidade() -> str:
    """Solicita ao usuário a escolha do sistema de unidades."""
    print("\n  Escolha o sistema de unidades:")
    print("  [1] Métrico  (kg / cm)")
    print("  [2] Imperial (lb / in)")

    while True:
        escolha = input("\n  Opção: ").strip()
        if escolha in ("1", "2"):
            return "metrico" if escolha == "1" else "imperial"
        print("  ⚠️  Opção inválida. Digite 1 ou 2.")


def menu_principal() -> None:
    """Loop principal da calculadora de IMC."""
    print("\n" + "=" * 45)
    print("     🏃 CALCULADORA DE IMC  (OMS)")
    print("=" * 45)

    while True:
        sistema = escolher_unidade()

        if sistema == "metrico":
            peso = obter_float("\n  Peso (kg): ")
            altura_cm = obter_float("  Altura (cm): ")
            altura_m = altura_cm / 100
        else:
            peso_lb = obter_float("\n  Peso (lb): ")
            altura_in = obter_float("  Altura (in): ")
            peso, altura_m = converter_imperial_para_metrico(peso_lb, altura_in)
            print(f"\n  (Convertido: {peso} kg / {altura_m:.2f} m)")

        try:
            imc = calcular_imc(peso, altura_m)
            classificacao = classificar_imc(imc)
            exibir_resultado(imc, classificacao)
        except ValueError as e:
            print(f"\n  ❌ Erro: {e}\n")

        continuar = input("  Calcular novamente? (s/n): ").strip().lower()
        if continuar not in ("s", "sim", "y", "yes"):
            print("\n  Até logo! 👋\n")
            break


if __name__ == "__main__":
    menu_principal()