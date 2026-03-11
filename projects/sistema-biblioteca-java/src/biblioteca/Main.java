package biblioteca;

import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BibliotecaService service = new BibliotecaService();
        int opcao = -1;

        while (opcao != 0) {
            System.out.println("=== Sistema de Biblioteca ===");
            System.out.println("1 - Cadastrar livro");
            System.out.println("2 - Listar livros");
            System.out.println("3 - Remover livro");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");

            if (scanner.hasNextInt()) {
                opcao = scanner.nextInt();
                scanner.nextLine();
            } else {
                scanner.nextLine();
                opcao = -1;
            }

            System.out.println();

            switch (opcao) {
                case 1:
                    System.out.print("Digite o título do livro: ");
                    String titulo = scanner.nextLine();

                    if (titulo.isBlank()) {
                        System.out.println("Título inválido.");
                    } else {
                        service.cadastrarLivro(titulo.trim());
                        System.out.println("Livro cadastrado com sucesso.");
                    }
                    break;

                case 2:
                    List<Livro> livros = service.listarLivros();

                    if (livros.isEmpty()) {
                        System.out.println("Nenhum livro cadastrado.");
                    } else {
                        System.out.println("Livros cadastrados:");

                        // A listagem exibe uma visão direta do conteúdo atual do ArrayList.
                        for (Livro livro : livros) {
                            System.out.println(livro.getId() + " - " + livro.getTitulo());
                        }
                    }
                    break;

                case 3:
                    System.out.print("Digite o ID do livro que deseja remover: ");

                    if (scanner.hasNextInt() && service.removerLivro(scanner.nextInt())) {
                        System.out.println("Livro removido com sucesso.");
                    } else {
                        System.out.println("Livro não encontrado.");
                    }

                    scanner.nextLine();
                    break;

                case 0:
                    System.out.println("Encerrando o sistema.");
                    break;

                default:
                    System.out.println("Opção inválida.");
                    break;
            }

            System.out.println();
        }

        scanner.close();
    }
}
