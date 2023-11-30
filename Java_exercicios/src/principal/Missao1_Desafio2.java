package principal;

public class Missao1_Desafio2 {
	
	public static void main(String[] args) 
	{
		// apresenta o titulo da missao (etapa "a")
		System.out.println("Missao 1 - Desafio 2 Cálculo Bimestral ");
		// declara as seis variaveis inteiras (etapa "b" da atividade)
		int Trab1B, Prova1B, Trab2B, Prova2B, Nota1B, Nota2B;
		double Media_Final;
		//atribui valor as variáveis (etapa "c" da atividade
			//Avaliações do primeiro Bimestre
			Trab1B= 15;
			Prova1B= 51;
			// Avaliações do segundo Bimestre
			Trab2B= 28;
			Prova2B= 63;
		//Realiza o calculo da Nota do primeiro Bimestre (Etapa "d" da Atividade)
		Nota1B = Trab1B + Prova1B;
		// Realiza o calculo da nota do segundo Bimestre (etapa "e" da atividade)
		Nota2B = Trab2B + Prova2B;
		// Calculo a Média final (etapa "f" da atividade)
		Media_Final = (double)(Nota1B + Nota2B)/2;
		//Apresenta o resultado no console (Etapa "g" da atividade)
		System.out.println("A média do final do aluno é : " + Media_Final);
		// Finaliza a atividade (etapa "h" da atividade)
		System.out.println("Desafio 4 Concluido ! - Média Calculada com cast! ");
		System.out.println("alteração do desafio 2 ");
	}

}
