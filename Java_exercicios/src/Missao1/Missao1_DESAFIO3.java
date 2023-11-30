package Missao1;

public class Missao1_DESAFIO3 {

	public static void main(String[] args) 
	{
		// apresenta o titulo da missao (etapa "a")
		System.out.println("MISSÃO 1 - DESAFIO 3 – Conversão de Tipos ");
		
		// declara as duas variaveis inteiro (etapa "2" da atividade)
		int A, B;
		// declara as duas variaveis double (etapa "3" da atividade)
		int R1; 
		double R2;
		
		// Atribuição de Valores  (etapa "4 e 5" da atividade)
		A= 7;
		B= 6;
		
		//Calculo de media com e sem cast
		R1 = (A + B)/2;
		R2 = (double)(A + B)/2;
		
		System.out.println("O Resultado sem cast é: " + R1);
		System.out.println("O Resultado com cast é: " + R2);
		System.out.println("DESAFIO 3 CONCLUÍDO! ");
	}

}
