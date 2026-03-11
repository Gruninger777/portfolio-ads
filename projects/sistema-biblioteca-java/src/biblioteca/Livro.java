package biblioteca;

public class Livro {
    private int id;
    private String titulo;

    public Livro(int id, String titulo) {
        this.id = id;
        this.titulo = titulo;
    }

    public int getId() {
        return id;
    }

    public String getTitulo() {
        return titulo;
    }
}
