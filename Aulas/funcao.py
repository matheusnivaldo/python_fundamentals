#! /usr/bin/python3
# -*- Coding: utf-8 -*-

# def soma(x,y):
#     return x+y

# # print(soma(10,11))

# produtos = []


# def cadastrar_produto(produto):
#     global produtos
#     produtos.append(produto)

# def listar_produtos():
#     global produtos
#     for p in produtos:
#         print(p)



# def deleta_produto():
#     global produtos
#     produtos.remove("Limao")
#     print("Produto removido")

# def deletar_produto(prod):
#     global produtos
#     if prod in produtos:
#         print("Produto removido")
#         produtos.remove(prod)
#     else:
#         print("Produto inexistente")

# cadastrar_produto("Pacoca")
# cadastrar_produto("Limao")
# cadastrar_produto("Fliperama")

# listar_produtos()


# listar_produtos()

# deletar_produto(str(input("Deseja apagar qual produto:")))

# listar_produtos()

# if __name__ == "__main__":
#     def create_list(): 
#         new_list = []

carrinho = [{"nome":"Tenis","valor":21.70},              
            {"nome":"Camiseta","valor":10.33}]  
            
black_friday = lambda x: x / 2  
for c in carrinho:      
    print ("Nome do produto: ",c["nome"])      
    print ("Valor original: ",c["valor"])      
    print ("Valor com desconto: ",black_friday(c["valor"]))      
    print ("=-=-=-=-=-=-=-=-=-=")