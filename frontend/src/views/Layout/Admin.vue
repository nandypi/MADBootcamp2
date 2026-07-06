<template>
  <div class="container">
    <h1>Admin Dashboard</h1>

    <!-- Add Book -->
    <div class="card">
      <h2>Add New Book</h2>

      <input
        v-model="newBook.title"
        placeholder="Book Title"
      />

      <textarea
        v-model="newBook.description"
        placeholder="Description"
      ></textarea>

      <button @click="createBook">Add Book</button>
    </div>

    <hr>

    <!-- Books Table -->
    <h2>Books</h2>

    <table border="1" cellpadding="10">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Description</th>
          <th width="180">Action</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.id }}</td>
          <td>{{ book.title }}</td>
          <td>{{ book.description }}</td>

          <td>
            <button @click="openEdit(book)">
              Edit
            </button>

            <button @click="deleteBook(book.id)">
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Edit Modal -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">

        <h2>Edit Book</h2>

        <input v-model="editBook.title">

        <textarea
          v-model="editBook.description"
        ></textarea>

        <br><br>

        <button @click="updateBook">
          Save
        </button>

        <button @click="showModal=false">
          Cancel
        </button>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const API = "http://localhost:5000/books"

const books = ref([])

const newBook = ref({
  title: '',
  description: ''
})

const showModal = ref(false)

const editBook = ref({
  id: null,
  title: '',
  description: ''
})

const token = localStorage.getItem("token")

const headers = {
  "Content-Type": "application/json",
  Authorization: `Bearer ${token}`
}

async function loadBooks() {
  const res = await fetch(API, {
    headers
  })

  const data = await res.json()

  console.log(data)

  books.value = data.books
}

async function createBook() {

  const res = await fetch(API,{
    method:"POST",
    headers,
    body:JSON.stringify(newBook.value)
  })

  const data = await res.json()

  console.log(data)

  alert(data.message)

  newBook.value={
    title:'',
    description:''
  }

  loadBooks()
}

function openEdit(book){

  editBook.value={
    ...book
  }

  showModal.value=true
}

async function updateBook(){

  const res = await fetch(`${API}/${editBook.value.id}`,{
    method:"PUT",
    headers,
    body:JSON.stringify(editBook.value)
  })

  const data=await res.json()

  alert(data.message)

  showModal.value=false

  loadBooks()
}

async function deleteBook(id){

  const ok = confirm("Are you sure you want to delete this book?")

  if(!ok) return

  const res = await fetch(`${API}/${id}`,{
    method:"DELETE",
    headers
  })

  const data=await res.json()

  alert(data.message)

  loadBooks()
}

onMounted(()=>{

    const token=localStorage.getItem("token")
    const user=localStorage.getItem("user")

    if(!token || !user){
        router.push("/login?msg=Please login")
        return
    }

    const user_obj=JSON.parse(user)

    if(user_obj.role!="admin"){
        alert("You are not allowed here")
        router.push("/user")
        return
    }

    loadBooks()

})
</script>

<style scoped>

.card{
    margin-bottom:30px;
}

input,
textarea{
    display:block;
    width:400px;
    margin-bottom:10px;
    padding:8px;
}

button{
    margin-right:10px;
    padding:8px 15px;
    cursor:pointer;
}

table{
    border-collapse:collapse;
}

th,td{
    padding:10px;
}

.modal{
    position:fixed;
    inset:0;
    background:rgba(0,0,0,.4);
    display:flex;
    justify-content:center;
    align-items:center;
}

.modal-content{
    background:white;
    padding:30px;
    width:500px;
    border-radius:10px;
}

</style>