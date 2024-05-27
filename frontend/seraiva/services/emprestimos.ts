import { BACKEND_URL } from "~/models/app";
import type { Emprestimo, itemEmprestimo, itemEmprestimoBody} from "~/models/emprestimos";

export const salvarVenda = (venda: Emprestimo): Promise<Emprestimo | null> => {
  return useFetch<Emprestimo>(`${BACKEND_URL}/emprestimos/`, {
    method: 'POST',
    body: venda
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};


export const salvarVendaProdutos = (emprestimos: Array<itemEmprestimoBody>): Promise<itemEmprestimo | null> => {
  return useFetch<itemEmprestimo>(`${BACKEND_URL}/itememprestimo/`, {
    method: 'POST',
    body: emprestimos
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};