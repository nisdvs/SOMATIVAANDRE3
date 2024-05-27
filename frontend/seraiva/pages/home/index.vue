<script setup lang="ts">
import { getLivro } from '~/services/livro';
import { type Livro } from '~/models/livro';
import { onMounted, ref, Ref } from 'vue';
import { useToast } from 'primevue/usetoast';

const toast = useToast();

const show = () => {
  toast.add({ severity: 'success', summary: 'Livro Adicionado', detail: 'Acesse-o em seu carrinho', life: 3000 });
};

const livros: Ref<Array<Livro>> = ref([]);

definePageMeta({
  middleware: 'auth',
});

const atualizarLivro = () => {
  getLivro().then((LivroEncontrados) => {
    console.log('Livros encontrados:', LivroEncontrados?.results[0].nome);
    livros.value = LivroEncontrados?.results ?? [];
  });
};

onMounted(() => {
  atualizarLivro();
});
</script>

<template>
  <main class="home-container flex flex-column align-items-center">
    <h2 class="mt-4 mb-4">🥃 Nossos Livros</h2>
    <Toast />
    <div class="livro-container grid align-items-center justify-content-center">
      <div v-for="(livro, index) in livros" :key="index">
        <LivroItem :livro="livro" @eventoAdicionado="show" />
      </div>
    </div>
  </main>
</template>

<style scoped lang="scss">
.home-container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: red;
  background-image: url('background1.jpg');
  background-repeat: repeat;
  background-size: cover;
}

.p-toast-summary {
  padding: 1.5rem !important;
}
</style>
