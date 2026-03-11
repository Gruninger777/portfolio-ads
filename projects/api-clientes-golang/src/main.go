package main

import (
	"encoding/json"
	"log"
	"net/http"
	"sync"
)

type Cliente struct {
	ID    int    `json:"id"`
	Nome  string `json:"nome"`
	Email string `json:"email"`
}

type NovoCliente struct {
	Nome  string `json:"nome"`
	Email string `json:"email"`
}

var (
	clientes = []Cliente{
		{ID: 1, Nome: "Ana Souza", Email: "ana@email.com"},
	}
	proximoID = 2
	mutex     sync.Mutex
)

func main() {
	http.HandleFunc("/clientes", clientesHandler)

	log.Println("Servidor iniciado em http://localhost:8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}

func clientesHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	switch r.Method {
	case http.MethodGet:
		listarClientes(w)
	case http.MethodPost:
		adicionarCliente(w, r)
	default:
		w.WriteHeader(http.StatusMethodNotAllowed)
		json.NewEncoder(w).Encode(map[string]string{
			"erro": "Método não permitido",
		})
	}
}

// listarClientes retorna todos os clientes atualmente mantidos em memória.
func listarClientes(w http.ResponseWriter) {
	json.NewEncoder(w).Encode(clientes)
}

// adicionarCliente lê o JSON recebido, cria um novo cliente e o adiciona à lista.
func adicionarCliente(w http.ResponseWriter, r *http.Request) {
	var novoCliente NovoCliente

	if err := json.NewDecoder(r.Body).Decode(&novoCliente); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode(map[string]string{
			"erro": "JSON inválido",
		})
		return
	}

	if novoCliente.Nome == "" || novoCliente.Email == "" {
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode(map[string]string{
			"erro": "Nome e e-mail são obrigatórios",
		})
		return
	}

	mutex.Lock()
	cliente := Cliente{
		ID:    proximoID,
		Nome:  novoCliente.Nome,
		Email: novoCliente.Email,
	}
	clientes = append(clientes, cliente)
	proximoID++
	mutex.Unlock()

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(cliente)
}
