using System;
using SistemaCadastro;

var userService = new UserService();
var option = -1;

while (option != 0)
{
    Console.Clear();
    Console.WriteLine("=== Sistema de Cadastro ===");
    Console.WriteLine("1 - Adicionar usuário");
    Console.WriteLine("2 - Listar usuários");
    Console.WriteLine("3 - Remover usuário");
    Console.WriteLine("0 - Sair");
    Console.Write("Escolha uma opção: ");

    var input = Console.ReadLine();
    int.TryParse(input, out option);

    Console.WriteLine();

    switch (option)
    {
        case 1:
            Console.Write("Digite o nome do usuário: ");
            var name = Console.ReadLine();

            if (string.IsNullOrWhiteSpace(name))
            {
                Console.WriteLine("Nome inválido.");
            }
            else
            {
                // O serviço centraliza a manipulação da lista para manter o fluxo principal simples.
                userService.AddUser(name.Trim());
                Console.WriteLine("Usuário adicionado com sucesso.");
            }
            break;

        case 2:
            var users = userService.ListUsers();

            if (users.Count == 0)
            {
                Console.WriteLine("Nenhum usuário cadastrado.");
            }
            else
            {
                Console.WriteLine("Usuários cadastrados:");

                foreach (var user in users)
                {
                    Console.WriteLine($"{user.Id} - {user.Name}");
                }
            }
            break;

        case 3:
            Console.Write("Digite o ID do usuário que deseja remover: ");

            if (int.TryParse(Console.ReadLine(), out var id) && userService.RemoveUser(id))
            {
                Console.WriteLine("Usuário removido com sucesso.");
            }
            else
            {
                Console.WriteLine("Usuário não encontrado.");
            }
            break;

        case 0:
            Console.WriteLine("Encerrando o sistema.");
            break;

        default:
            Console.WriteLine("Opção inválida.");
            break;
    }

    if (option != 0)
    {
        Console.WriteLine();
        Console.WriteLine("Pressione Enter para continuar...");
        Console.ReadLine();
    }
}
