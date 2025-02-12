// 12 de Fevereiro de 2025
// Classe Adição
import java.util.Scanner; // programa utiliza a classe Scanner

public class Addition
{
    //inicia a execução main
    public  static void main(String[] args)
    {
        //cria um Scanner para obter entrada a partir da janela de comando
        Scanner input = new Scanner(System.in);

        int number1; // Primeiro Numero
        int number2; // Segundo Numero
        int sum; // Soma dos numeros

        System.out.print("Enter first interger: "); // prompt
        number1 = input.nextInt(); // Lê o primeiro

        System.out.print("Enter second interger: ");
        number2 = input.nextInt(); // Lê o Segundo

        sum = number1 + number2; // soma os numeros, depois armazena o total em sum

        System.out.printf("Sum is %d%n", sum); // exibe a soma

    } // fim do metodo main

} // fim da classe Addition
