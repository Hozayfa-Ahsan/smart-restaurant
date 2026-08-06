                +----------------------+
                |      Browser         |
                +----------+-----------+
                           |
                           |
                           v
                  Flask Web Server
                           |
        +------------------+------------------+
        |                                     |
        |                                     |
        v                                     v
 Restaurant Website                  Chatbot API
                                              |
                                              v
                                      RAG Pipeline
                                              |
               +------------------------------+
               |
               v
         Pinecone Vector DB
               |
               v
         Relevant Documents
               |
               v
        Gemini 2.5 Flash
               |
               v
         AI Generated Answer