# Retrieval Augmented Generation (RAG)

## Process of setting up a RAG workflow

1. Select an LLM
2. Create and aggregate your knowledge base
    - Using databases or vector stores like `Pinecone`, `FAISS`, `ChromaDB`
3. Add a retriever
    - Using tools like: `Elasticsearch` or `vector search`
4. Connect the workflow

## Tools to use

`n8n`
`langflow`
Open source frameworks like `Haystack`, `LlamaIndex`, `Langchain`

[Open weights LLM](https://promptmetheus.com/resources/llm-knowledge-base/open-weights-model) (their parameters or weights are publicly available and you can modify them without any restriction) such as `LLaMA series` or `Mistral 7B`

Open weights models don't provide access to model architecture or source code for the training pipeline. They can however be fine-tuned and adapted to specific tasks.

## Use cases

Private document analysis workflows - such workflows don't share sensitive data with third-party AI providers.
