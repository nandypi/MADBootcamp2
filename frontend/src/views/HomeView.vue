<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="home-container">
    <div class="card">
      <h1>Welcome to MAD2 APP</h1>
      <p class="subtitle">
        Your one-stop platform to get started.
      </p>

      <div class="links">
        <RouterLink to="/login" class="btn primary">
          Login
        </RouterLink>

        <RouterLink to="/register" class="btn secondary">
          Register
        </RouterLink>
      </div>

      <p class="about">
        Want to learn more?
        <RouterLink to="/about">About the App</RouterLink>
      </p>
    </div>
  </div>
</template>

<style scoped>
/* Full-page background */
.home-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #4f46e5, #7c3aed);
  font-family: Arial, Helvetica, sans-serif;
  padding: 20px;
}

/* Card */
.card {
  background: white;
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  text-align: center;
  max-width: 450px;
  width: 100%;
}

/* Heading */
h1 {
  color: #333;
  margin-bottom: 10px;
  font-size: 2rem;
}

/* Subtitle */
.subtitle {
  color: #666;
  margin-bottom: 30px;
}

/* Button container */
.links {
  display: flex;
  gap: 15px;
  justify-content: center;
  margin-bottom: 25px;
}

/* Buttons */
.btn {
  text-decoration: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: bold;
  transition: 0.3s ease;
}

.primary {
  background: #4f46e5;
  color: white;
}

.primary:hover {
  background: #4338ca;
  transform: translateY(-2px);
}

.secondary {
  background: #10b981;
  color: white;
}

.secondary:hover {
  background: #059669;
  transform: translateY(-2px);
}

/* About link */
.about {
  color: #555;
}

.about a {
  color: #4f46e5;
  text-decoration: none;
  font-weight: bold;
}

.about a:hover {
  text-decoration: underline;
}
</style>