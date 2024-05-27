export type Usuario = {
    id: number;
    nome: string;
    email: string;
    telefone: string;
    categoria: string;
    is_active: boolean;
    groups: Array<string>;
    user_permissions: Array<string>;
}