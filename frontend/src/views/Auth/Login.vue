<template>
    <h1>Login Page</h1>

    <form @submit.prevent="Login">

    <pre>
{{ formdata }}
    </pre>

    <input required v-model="formdata.email" type="email" placeholder="Email here">
    <input required v-model="formdata.password" type="password">

    <button type="submit">Login</button>

</form>
    <p>{{ message }}</p>

    <p>Don't have an account? <RouterLink to="/register">Click here to Register</RouterLink></p>
</template>

<script>

export default {
    data() {
        return {
            message: "",
            formdata: {
                email: '',
                password: ''
            }
        }
    },
    methods: {
        async Login() {
            // alert('function callbackend is working')
            this.message = "Calling backend..."

            let url = 'http://127.0.0.1:5000/login';
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify(this.formdata)
            });

            console.log(response)
            
            const data = await response.json()
            this.message = data.message
            
            if (response.ok) {

                console.log(data)

                localStorage.setItem('token', JSON.stringify(data.access_token))
                localStorage.setItem('user', JSON.stringify(data.user))

                if (data.user.role == 'admin') {
                    this.$router.push('/admin')
                } else {
                    this.$router.push('/user')
                }

            } else {
                console.log('some error came')
            }

        }

    },
    mounted() {
        const url_msg = this.$route.query.msg;
        if (url_msg) {
            alert(url_msg)
        }
    }
}

</script>

