<script setup lang="ts">
import { ref } from "vue";

const itensMenu = ref([
  {
    label: "Home",
    icon: "pi pi-home",
  },
  {
    label: "Pagamentos",
    icon: "pi pi-wallet",
  },
  {
    label: "Meus pedidos",
    icon: "pi pi-briefcase",
  },
]);
</script>

<template>
  <header>
    <div class="flex align-items-center justify-content-center">
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-home mr-1"></i>
          <NuxtLink to="/home">Livros</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-wallet mr-1"></i>
          <NuxtLink to="/pagamento">Pagamentos</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-briefcase mr-1"></i>
          <NuxtLink to="/pedidos">Meus Pedidos</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-shopping-cart mr-1"></i>
          <NuxtLink to="/carrinho">Carrinho</NuxtLink>
        </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
header {
  width: 100vw;
  height: var(--altura-header);

  .menu-item{
    height: var(--altura-header);
    
    a{
      text-decoration: none;
      color: black;
    }
    &:hover{
      transform: scale(1.1);
    }
  }
}
</style>