import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    try:
        result = float("nan")
        if operador == "+":
            result = num1 + num2
        elif operador == "-":
            result = num1 - num2
        elif operador == "*":
            result = num1 * num2
        elif operador == "/":
            if num1 == 0 or num2 == 0:
                result = result # Mantém nan se houver divisão por zero
            result = num1 / num2
        elif operador == "**":
            result = num1 ** num2
        else:
            return result # Operador inválido, retorna nan
    
    except ZeroDivisionError:
        raise           # Lança a exceção para ser tratada no bloco principal
    except Exception:
        return result   # Retorna nan para qualquer outro erro


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')

            # Entrada de dados do usuário
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            operador = input('Digite o operador (+, -, *, /, **): ').strip()

            # Execução do cálculo
            result = calculadora(num1, num2, operador)

            # Exibição do resultado
            print(f'\nResultado: {num1} {operador} {num2} = {result:.2f}\n')

        except ValueError:
            print('Erro: Valor inválido! Por favor, digite apenas números!')
            time.sleep(2)
            continue

        except Exception as e:
            print(f'Erro inesperado: {str(e)}')
            time.sleep(2)
            continue

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
            continue

        # Verificar se o usuário deseja continuar
        continuar = input('\nDeseja fazer outra operação? (s/n): ').strip().lower()
        if continuar != 's':
            print('\nVolte sempre!\n')
            break


