import type { Livro} from "./livro";
import type { Usuario } from "./usuario";

export enum PAGAMENTOS {
    'PENDENTE' = "P",
    'CONCLUIDO' = "C",
    'ATRASADO' = "A",
}


export type Emprestimo = {
    id?: number;
    usuarioFK: string;
    data_emprestimo: number;
    data_devolucao_prevista: number;
    data_devolucao_realizada: number;
    valor_total_emprestimo: number;
    status: PAGAMENTOS;
}


export type itemEmprestimo = {
    livroFK: Livro;
    emprestimoFK: Emprestimo;
}


export type itemEmprestimoBody = {
    livroFK: number;
    quantidade: number;
    emprestimoFK: number;
}