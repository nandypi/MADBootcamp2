<template>
    <h1>User Dashboard</h1>

    <p>{{ message }}</p>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'

const router = useRouter()

const message = ref('hello user')



onMounted( () => {
    const token = localStorage.getItem('token')
    const user = localStorage.getItem('user')
    console.log(token, user)
    if (!user || !token) {
        router.push('/login?msg=Please login to enter')
    }
})


</script>