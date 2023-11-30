package Missao3;

/*
 * Autor: Luis Orlando
 * Data 08/11/2023
 */

public class Missao3_principal 
{

	public static void main(String[] args) 
	{
		double R_SOMA, R_SUBTRAIR, R_MULTIPLICAR, R_DIVIDIR;
		System.out.println("Inicio da Missao 3");
		Missao3_Calculadora obj_calculadora = new Missao3_Calculadora();
		R_SOMA = obj_calculadora.SOMAR(1,2);
		System.out.println("O resultado da soma :é" + R_SOMA);
		R_SUBTRAIR=obj_calculadora.SUBTRAIR(10.5, 4.2);
		System.out.println("O resultado da subtração :é" + R_SUBTRAIR);
		R_SUBTRAIR=obj_calculadora.MULTIPLICAR(2.2, 5.5);
		System.out.println("O resultado da MULTIPLICAÇÃO :é" + R_MULTIPLICAR);
		R_SUBTRAIR=obj_calculadora.DIVIDIR(2.2, 5.5);
		System.out.println("O resultado da DIVISÃO :é" + R_DIVIDIR);
		obj_calculadora.
	}	
	
}
