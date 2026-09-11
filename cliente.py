import tkinter as tk
from tkinter import messagebox, ttk
from typing import Any

from main import cardapio


def validar_cliente(nome: str, telefone: str) -> str | None:
    """Retorna uma mensagem de erro ou None quando os dados sao validos."""
    nome = nome.strip()
    telefone = telefone.strip()

    if not nome:
        return "Informe o nome do cliente."
    if not telefone.isdigit():
        return "O telefone deve conter apenas numeros."
    if len(telefone) < 8:
        return "Informe um telefone valido com pelo menos 8 digitos."
    return None


class PizzariaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Forno & Massa | Pedidos")
        self.geometry("1180x760")
        self.minsize(980, 650)
        self.configure(bg="#f5f1ea")
        self.carrinho: list[tuple[str, float]] = []

        self._configurar_estilos()
        self._montar_interface()

    def _configurar_estilos(self):
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("Titulo.TLabel", background="#18251f", foreground="#fffaf2", font=("Segoe UI", 25, "bold"))
        estilo.configure("Subtitulo.TLabel", background="#18251f", foreground="#b9c8bc", font=("Segoe UI", 10))
        estilo.configure("Secao.TLabel", background="#f5f1ea", foreground="#18251f", font=("Segoe UI", 15, "bold"))
        estilo.configure("Texto.TLabel", background="#fffaf2", foreground="#5e665f", font=("Segoe UI", 9))
        estilo.configure("Preco.TLabel", background="#fffaf2", foreground="#d15a32", font=("Segoe UI", 12, "bold"))
        estilo.configure("Acao.TButton", background="#d15a32", foreground="#ffffff", borderwidth=0, padding=(14, 9), font=("Segoe UI", 10, "bold"))
        estilo.map("Acao.TButton", background=[("active", "#b94725")])
        estilo.configure("Secundario.TButton", background="#e8dfd2", foreground="#18251f", borderwidth=0, padding=(12, 8), font=("Segoe UI", 9, "bold"))
        estilo.configure("Carrinho.TFrame", background="#fffaf2")
        estilo.configure("Entrada.TEntry", fieldbackground="#fffaf2", padding=8)
        estilo.configure("Abas.TNotebook", background="#f5f1ea", borderwidth=0)
        estilo.configure("Abas.TNotebook.Tab", background="#e8dfd2", foreground="#18251f", padding=(16, 9), font=("Segoe UI", 9, "bold"))
        estilo.map("Abas.TNotebook.Tab", background=[("selected", "#d15a32")], foreground=[("selected", "#ffffff")])

    def _montar_interface(self):
        cabecalho = tk.Frame(self, bg="#18251f", height=112)
        cabecalho.pack(fill="x")
        cabecalho.pack_propagate(False)
        ttk.Label(cabecalho, text="FORNO & MASSA", style="Titulo.TLabel").pack(anchor="w", padx=34, pady=(22, 0))
        ttk.Label(cabecalho, text="Sabor artesanal, pedido do seu jeito", style="Subtitulo.TLabel").pack(anchor="w", padx=36, pady=(2, 0))

        conteudo = tk.Frame(self, bg="#f5f1ea")
        conteudo.pack(fill="both", expand=True, padx=30, pady=24)
        conteudo.columnconfigure(0, weight=3)
        conteudo.columnconfigure(1, weight=2)
        conteudo.rowconfigure(1, weight=1)

        ttk.Label(conteudo, text="Monte seu pedido", style="Secao.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 12))
        ttk.Label(conteudo, text="Resumo do pedido", style="Secao.TLabel").grid(row=0, column=1, sticky="w", padx=(28, 0), pady=(0, 12))

        self._montar_catalogo(conteudo)
        self._montar_carrinho(conteudo)

    def _montar_catalogo(self, pai: Any) -> None:
        abas = ttk.Notebook(pai, style="Abas.TNotebook")
        abas.grid(row=1, column=0, sticky="nsew")
        for categoria, itens in cardapio.items():
            pagina = tk.Frame(abas, bg="#f5f1ea")
            abas.add(pagina, text=f"  {categoria}  ")
            pagina.columnconfigure(0, weight=1)
            pagina.columnconfigure(1, weight=1)
            for indice, (nome, preco, descricao) in enumerate(itens):
                card = tk.Frame(pagina, bg="#fffaf2", highlightbackground="#e6dbcd", highlightthickness=1)
                card.grid(row=indice // 2, column=indice % 2, sticky="nsew", padx=(0, 12) if indice % 2 == 0 else (0, 0), pady=(0, 12))
                pagina.rowconfigure(indice // 2, weight=1)
                tk.Label(card, text="●", bg="#fffaf2", fg="#d15a32", font=("Segoe UI", 22)).pack(anchor="w", padx=16, pady=(10, 0))
                tk.Label(card, text=nome, bg="#fffaf2", fg="#18251f", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=16, pady=(0, 3))
                ttk.Label(card, text=descricao, style="Texto.TLabel", wraplength=210).pack(anchor="w", padx=16)
                ttk.Label(card, text=f"R$ {preco:.2f}".replace(".", ","), style="Preco.TLabel").pack(anchor="w", padx=16, pady=(8, 6))
                ttk.Button(card, text="Adicionar", style="Acao.TButton", command=lambda n=nome, v=preco: self._adicionar(n, v)).pack(anchor="w", padx=16, pady=(0, 12))

    def _montar_carrinho(self, pai: Any) -> None:
        painel = ttk.Frame(pai, style="Carrinho.TFrame", padding=22)
        painel.grid(row=1, column=1, sticky="nsew", padx=(16, 0))
        painel.columnconfigure(0, weight=1)

        formulario = tk.Frame(painel, bg="#fffaf2")
        formulario.grid(row=0, column=0, sticky="ew")
        formulario.columnconfigure(0, weight=1)
        tk.Label(formulario, text="Dados do cliente", bg="#fffaf2", fg="#18251f", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 10))
        tk.Label(formulario, text="Nome", bg="#fffaf2", fg="#5e665f", font=("Segoe UI", 9)).grid(row=1, column=0, sticky="w")
        self.nome = ttk.Entry(formulario, style="Entrada.TEntry")
        self.nome.grid(row=2, column=0, sticky="ew", pady=(3, 9))
        tk.Label(formulario, text="Telefone", bg="#fffaf2", fg="#5e665f", font=("Segoe UI", 9)).grid(row=3, column=0, sticky="w")
        self.telefone = ttk.Entry(formulario, style="Entrada.TEntry")
        self.telefone.grid(row=4, column=0, sticky="ew", pady=(3, 18))

        self.lista = tk.Listbox(painel, height=12, bg="#fffaf2", fg="#18251f", selectbackground="#d15a32", relief="flat", highlightthickness=1, highlightbackground="#e6dbcd", font=("Segoe UI", 9))
        self.lista.grid(row=1, column=0, sticky="nsew")
        painel.rowconfigure(1, weight=1)
        self.total = tk.StringVar(value="Total  R$ 0,00")
        tk.Label(painel, textvariable=self.total, bg="#fffaf2", fg="#d15a32", font=("Segoe UI", 18, "bold")).grid(row=2, column=0, sticky="w", pady=(18, 12))
        botoes = tk.Frame(painel, bg="#fffaf2")
        botoes.grid(row=3, column=0, sticky="ew")
        ttk.Button(botoes, text="Limpar", style="Secundario.TButton", command=self._limpar).pack(side="left")
        ttk.Button(botoes, text="Finalizar pedido", style="Acao.TButton", command=self._finalizar).pack(side="right")

    def _adicionar(self, pizza: str, preco: float) -> None:
        self.carrinho.append((pizza, preco))
        self._atualizar_carrinho()

    def _atualizar_carrinho(self):
        self.lista.delete(0, tk.END)
        for pizza, preco in self.carrinho:
            self.lista.insert(tk.END, f"  {pizza:<23} R$ {preco:>6.2f}".replace(".", ","))
        valor = sum(preco for _, preco in self.carrinho)
        self.total.set(f"Total  R$ {valor:.2f}".replace(".", ","))

    def _limpar(self):
        self.carrinho.clear()
        self._atualizar_carrinho()

    def _finalizar(self):
        erro = validar_cliente(self.nome.get(), self.telefone.get())
        if erro:
            messagebox.showwarning("Confira seus dados", erro)
            return
        if not self.carrinho:
            messagebox.showwarning("Pedido vazio", "Adicione pelo menos um item ao pedido.")
            return
        valor = sum(preco for _, preco in self.carrinho)
        messagebox.showinfo("Pedido confirmado", f"Pedido de {self.nome.get().strip()} confirmado!\nTotal: R$ {valor:.2f}".replace(".", ","))
        self._limpar()


def cadastrar_cliente():
    """Inicia a interface de cadastro e pedidos."""
    PizzariaApp().mainloop()


if __name__ == "__main__":
    cadastrar_cliente()