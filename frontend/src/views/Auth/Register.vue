<template>
    <h1>Register Page</h1>

    <form @submit.prevent="createAccount">

        <pre>
{{ formdata }}
        </pre>

        <input v-model="formdata.username" type="text" placeholder="User name">
        <input v-model="formdata.email" type="email" placeholder="Email here">
        <input v-model="formdata.password" type="password">

        <button type="submit">Create Account</button>

    </form>

    <div>{{ message }}</div>   

    

    <p>Already have an account? <RouterLink to="/login">Click here to Login</RouterLink></p>
</template>

<script>

export default {
    name: "Register",
    data() {
        return {
            message: "Hey!",

            formdata: {
                username: '',
                email: '',
                password: ''
            }

        };
    },
    methods: {
        async createAccount() {
            // alert('function callbackend is working')
            this.message = "Calling backend..."

            let url = 'http://127.0.0.1:5000/register';
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

            } else {
                console.log('some error came')
            }

        }
    }
};

</script>

<style scoped>



</style>