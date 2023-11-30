package Missao4;
/*
 * Autor: Luis Orlando
 * Data: 14/11/23
 */
public class Missao4_principal {

	public static void main(String[] args) 
	{
		String Nome_Autor;
		String Data_Codigo;
		Nome_Autor = "Luis Orlando";
		Data_Codigo = "14/11/2023";
		String Msg_inicial = "Inicio da Missão 4";
		System.out.println(Msg_inicial);
		// Mostra a Frase concatenada
		System.out.println("Este código foi desenvolvido por " + Nome_Autor + " em " + Data_Codigo + ".");
		
		// Opção Extra !!
		System.out.println("Repetindo de outra forma:");
		String frase = "Este código foi desenvolvido por " + Nome_Autor + " em " + Data_Codigo + "." ;
		System.out.println(frase);
		//fim da opçao Extra
		System.out.println("------------");
		System.out.println("verificando o comprimento da string");
		String Nome="Luiz";
		int tamanho=Nome.length();
		System.out.println("O tamanho da variavel Nome é " + tamanho);
		
	
		System.out.println ("-----------");
		System.out.println("verificando se duas strings são iguais (maneira1) ");
		
		String Nome_Cadastrado = "Luiz";
		String Nome_Digitado;
		System.out.println("Digite seu Nome:");
		Nome_Digitado = .next();
		if(Nome_Cadastrado.equals(Nome_Digitado))
			System.out.println("Os nomes são iguais!");
		else
			System.out.println("Os nomes são diferentes!");

	}

}
