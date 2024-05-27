import { defineStore } from 'pinia';
import type { Livro } from "~/models/livro";

export type CarrinhoItem = {
    livro: Livro;
    quantidade: number;
}

export type Carrinho = {
    itens: Array<CarrinhoItem>;    
}

export const useCarrinhoStore = defineStore('carrinhoStore', {
    state: (): Carrinho => ({
        itens: []
    }),
    actions: {
        adicionarNoCarrinho(novoLivro: Livro) {
            const livroJaExiste = this.getLivroDoCarrinho(novoLivro);
            if (livroJaExiste) {
                livroJaExiste.quantidade += 1;
                this.itens = [
                    ...this.itens.filter(item => item.livro.id !== livroJaExiste.livro.id),
                    livroJaExiste
                ];
            } else {
                this.itens.push({
                    quantidade: 1,
                    livro: novoLivro
                });
            }
        },
        removerDoCarrinho(carrinhoItem: CarrinhoItem) {
            const posicaoNoCarrinho = this.getLivroDoCarrinhoIndex(carrinhoItem.livro);
            if (posicaoNoCarrinho !== -1) {
                this.itens.splice(posicaoNoCarrinho, 1);
            }
        },
        esvaziarCarrinho() {
            this.itens = [];
        }
    },
    getters: {
        estaNoCarrinho: (state: Carrinho) => (livroParaEncontrar: Livro): boolean => {
            return state.itens.findIndex(item => item.livro.id === livroParaEncontrar.id) !== -1;
        },
        getLivroDoCarrinho: (state: Carrinho) => (livroParaEncontrar: Livro) => {
            return state.itens.find(item => item.livro.id === livroParaEncontrar.id);
        },
        getLivroDoCarrinhoIndex: (state: Carrinho) => (livroParaEncontrar: Livro) => {
            return state.itens.findIndex(item => item.livro.id === livroParaEncontrar.id);
        },
        getCarrinho: (state: Carrinho) => (): Array<CarrinhoItem> => {
            return state.itens;
        },
        getValorTotalDoCarrinho: (state: Carrinho) => (): Number => {
            let soma = 0;
            state.itens.forEach(item => {
                soma += (item.livro.valor_emprestimo * item.quantidade);
            });
            return soma;
        }
    }
});
