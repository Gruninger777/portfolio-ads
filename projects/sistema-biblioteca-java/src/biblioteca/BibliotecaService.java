package biblioteca;

import java.util.ArrayList;
import java.util.List;

public class BibliotecaService {
    private final ArrayList<Livro> livros = new ArrayList<>();
    private int proximoId = 1;

    public void cadastrarLivro(String titulo) {
        // O ID é gerado localmente para manter o exemplo simples e funcional.
        livros.add(new Livro(proximoId++, titulo));
    }

    public List<Livro> listarLivros() {
        return livros;
    }

    public boolean removerLivro(int id) {
        for (Livro livro : livros) {
            if (livro.getId() == id) {
                return livros.remove(livro);
            }
        }

        return false;
    }
}
