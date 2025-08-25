from langchain_core.vectorstores.in_memory import InMemoryVectorStore

# Initialize the vector store
vector_store = InMemoryVectorStore()

# Add vectors and metadata
vectors = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
metadata = [{"text": "Hello world"}, {"text": "Goodbye world"}]
vector_store.add_vectors(vectors, metadata)

# Perform a similarity search
query_vector = [0.1, 0.2, 0.3]
results = vector_store.search(query_vector, k=2)
print(results)  # Output: [(vector, metadata), ...]

# Retrieve a vector by ID
vector_id = 0
vector, meta = vector_store.get_vector(vector_id)
print(vector, meta)  # Output: [0.1, 0.2, 0.3], {"text": "Hello world"}

# Clear the vector store
vector_store.clear()