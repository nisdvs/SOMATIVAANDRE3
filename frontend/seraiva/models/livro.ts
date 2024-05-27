export type CategoriaLivro = {
    id: number;
    nome: string;
}
export type Genero = {
    id: number;
    nome: string;
}
export type Formato = {
    id: number;
    categoria: string;
}
export type Livro = {
    id: number;
    nome: string;
    ano: number;
    generoFK: Genero;
    qtd_paginas: number;
    formatoFK: Formato;
    quantidade: number;
    numero_edicao: number;
    descricao: string;
    valor_emprestimo: number;
    qtd_estoque: number;
    estrelas: number;
    foto: Array<string>;
    categoriaFK: CategoriaLivro
}
