package principal;
/*
 * Autor: Luis Orlando
 * Data: 02/11/2023
 */
public class Missao1_principal 
{
	public static void main(String[] args) 
	{
		// apresenta o titulo da missao
		System.out.println("inicio da missao 1");
		System.out.println("Autor: Luis Orlando");
		System.out.println("Data: 02/11/2023");
		System.out.println("Calculo da nota bimestral");
		//declara as variaveis
		int Nota_Trabalho;
		int Nota_Prova;
		int Nota_Bimestre;
		//atribui valor as variai
		Nota_Trabalho = 22;
		Nota_Prova = 58;
		//realiza a soma (passo 3 da atividade)
		Nota_Bimestre = Nota_Trabalho + Nota_Prova;
		// Apresenta o resultado da nota bimestral no console (passo 4 da atividade)
		System.out.println("A nota bimestral é: " + Nota_Bimestre);
	}

}
