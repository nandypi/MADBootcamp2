<template>
    <h1>Admin Dashboard</h1>
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

    let user_obj = JSON.parse(user)
    if (user_obj.role != 'admin') {
        alert('You are not allowed here')
        router.push('/user')
    }

})


</script>