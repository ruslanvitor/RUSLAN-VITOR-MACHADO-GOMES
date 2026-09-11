cardapio: dict[str, list[tuple[str, float, str]]] = {
	"Pizzas": [
		("Calabresa", 35.0, "Molho, mussarela, calabresa e cebola"),
		("Carne de Sol", 40.0, "Carne de sol, mussarela, cebola e catupiry"),
		("Margherita", 34.0, "Mussarela, tomate, manjericao e azeite"),
		("Frango com Catupiry", 38.0, "Frango desfiado e catupiry"),
		("Quatro Queijos", 42.0, "Mussarela, provolone, parmesao e gorgonzola"),
		("Portuguesa", 39.0, "Presunto, ovos, cebola, ervilha e azeitona"),
		("Vegetariana", 37.0, "Mussarela, tomate, champignon, milho e pimentao"),
		("Pepperoni", 41.0, "Mussarela, pepperoni artesanal e oregano"),
	],
	"Bebidas": [
		("Coca-Cola 2L", 13.0, "Gelada para compartilhar"),
		("Guarana Antarctica 2L", 11.0, "Gelada para compartilhar"),
		("Coca-Cola lata", 6.0, "Lata 350ml"),
		("Suco de laranja", 9.0, "Suco natural 500ml"),
		("Agua mineral", 4.0, "Garrafa 500ml"),
	],
	"Adicionais": [
		("Borda de Catupiry", 8.0, "Borda recheada cremosa"),
		("Borda de Cheddar", 8.0, "Borda recheada com cheddar"),
		("Mussarela extra", 7.0, "Porcao generosa de mussarela"),
		("Bacon crocante", 9.0, "Bacon dourado e crocante"),
		("Molho especial", 3.0, "Molho da casa 80ml"),
		("Pao de alho", 12.0, "Porcao com 4 unidades"),
	],
}

pizzas: list[str] = [item[0] for item in cardapio["Pizzas"]]
precos: list[float] = [item[1] for item in cardapio["Pizzas"]]