from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Initialize query engine as None by default
query_engine = None

try:
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.llms.groq import Groq
    import os

    # Configure LlamaIndex settings
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    Settings.llm = Groq(model="llama3-70b-8192", api_key="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")

    # Initialize the query engine
    try:
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
    except Exception as e:
        print(f"Error initializing query engine: {e}")
except ImportError as e:
    print(f"Error importing required modules: {e}")

def index(request):
    return render(request, 'RAG/index.html')

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            if query_engine is None:
                return JsonResponse({
                    'response': 'The RAG system is not initialized. Please install required dependencies.',
                    'status': 'error'
                })
            
            # Get response from the query engine
            response = query_engine.query(user_message)
            
            return JsonResponse({
                'response': str(response),
                'status': 'success'
            })
        except Exception as e:
            return JsonResponse({
                'error': str(e),
                'status': 'error'
            }, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

