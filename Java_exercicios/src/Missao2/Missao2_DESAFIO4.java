package Missao2;
/*
 * Autor: Luis Orlando
 * Data 06/11/2023
 */
public class Missao2_DESAFIO4 {

	public static void main(String[] args) {
		System.out.println("MISSAO 2 - DESAFIO 4 - WHILE");
		System.out.println("Mostra os números IMPARES de 11 a 40, inclusive os extremos");
		int i = 11;
		while (i <=40)
		{
			if (i%2 != 0)
			{
				System.out.println(i);	
			}
			i = i +3;
		}
		System.out.println("MISSAO 2 - Desafio Extra 4 – parte 4 - concluido");
	}
}
