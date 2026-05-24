"""
Fase 5 - Fundamentos de Programación
Problema 3: Reabastecimiento de inventario
Autor: Yulian Sayid Mendoza Figueroa

Descripción:
A partir de una matriz con la información [Código, Nombre, Stock Actual, Stock Mínimo],
el programa determina la cantidad exacta que debe pedirse para cada artículo.
"""

def cantidad_a_pedir(stock_actual, stock_minimo):
    """Devuelve la cantidad exacta a solicitar para un artículo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def main():
    # Matriz con 5 artículos: [Código, Nombre, Stock Actual, Stock Mínimo Requerido]
    inventario = [
        ["A101", "Teclado", 8, 15],
        ["A102", "Mouse", 20, 10],
        ["A103", "Monitor", 4, 6],
        ["A104", "Memoria USB", 12, 12],
        ["A105", "Disco SSD", 3, 7]
    ]

    print("=" * 70)
    print("LISTA DE PEDIDOS PARA REABASTECIMIENTO DE INVENTARIO")
    print("=" * 70)
    print(f'{"Código":<10}{"Artículo":<20}{"Stock Actual":<15}{"Stock Mínimo":<15}{"Cantidad a Pedir":<18}')
    print("-" * 70)

    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        pedido = cantidad_a_pedir(stock_actual, stock_minimo)

        print(f'{codigo:<10}{nombre:<20}{stock_actual:<15}{stock_minimo:<15}{pedido:<18}')

    print("-" * 70)
    print("Fin del informe.")


if __name__ == '__main__':
    main()
