<template>
  <div class="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
    <div class="relative py-3 sm:max-w-xl sm:mx-auto">
      <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
        <div class="max-w-md mx-auto">
          <h1 class="text-2xl font-semibold text-gray-900">API Data</h1>
          
          <!-- Loading state -->
          <div v-if="loading" class="mt-4 text-gray-500">
            Loading data...
          </div>
          
          <!-- Error state -->
          <div v-if="error" class="mt-4 text-red-500">
            {{ error }}
          </div>
          
          <!-- Data display -->
          <div v-if="data && !loading" class="mt-6">
            <ul class="divide-y divide-gray-200">
              <li v-for="item in data" :key="item.id" class="py-4">
                <div class="flex space-x-3">
                  <div class="flex-1 space-y-1">
                    <div class="flex items-center justify-between">
                      <h3 class="text-sm font-medium">{{ item.name }}</h3>
                      <p class="text-sm text-gray-500">{{ item.price }}</p>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
          
          <!-- Refresh button -->
          <button 
            @click="fetchData" 
            class="mt-6 px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Refresh Data
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: null,
      loading: true,
      error: null
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      this.loading = true
      try {
        const response = await fetch('http://localhost:8000/api/menu/')
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        this.data = await response.json()
        this.error = null
      } catch (err) {
        this.error = 'Failed to fetch data: ' + err.message
        console.error(err)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>