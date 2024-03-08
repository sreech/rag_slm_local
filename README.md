# Deploy Small Language Model, for instance Microsoft Phi2 with custom RAG document

This code helps you ask questions about a text file and get answers using a large language model (LLM). I used LM studio to download the Phi2 SLM model and then loaded custom document as Text loader. Loaded into Vector Store and used RAG RLM prompt to test it out.
Deployed the model in LM studio server.

### Setting Up:

It imports libraries for loading text files, splitting text into chunks, creating embeddings (a way to represent text), searching information, and using a small language model.
It defines the path to a text file on your computer (replace with your file path).
Loading and Splitting Text:

It loads the text file and splits it into smaller chunks for easier processing.
It adds some metadata (like keywords) to the first chunk.
### Creating a Search Index:

It creates a search index using a powerful technique called "embeddings." This helps find relevant parts of the text file based on your question.
### Asking Questions and Getting Answers:

It defines functions to format retrieved text and get your question as input.
It builds a pipeline that retrieves relevant parts of the text file based on your question and uses a large language model to answer your question using the retrieved information.
In a loop, it lets you enter a question, feeds it to the pipeline, and displays the answer.
### Cleaning Up:

After you're done asking questions, it cleans up the search index.
Overall, this code acts like a mini search engine and question answer system specifically for the text file I provided.
