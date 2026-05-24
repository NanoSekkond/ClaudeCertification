# RAG
Basically break down a document in chunks and index them with their text embeddings. Then you don't send the whole document but only the relevant bits to the agent.

## How do we break it down?
- Size based: Break down the document in chunks of equal length. Words or characters. It lacks context, but it can be fixed by adding a bit of overlap. This adds duplication between chunks.
- Structure based: Paragraphs, sections, anything. In markdown you could use # or ##. If you have plain text you can't do this.
- Semantic based: Check how related each sentence is to the next and decide based on that when to break it. Way more complex.

## Text Embeddings
Turn text into vectors, then turn input into vector and compare **cosine similarity** or **vector distance**. This process is cheap and can even be done on a CPU. We ideally want to combine Semantic Search with Lexical Search, since Text Embeddings can't notice important parts in a sentence, they prioritize the words all the same.

## BM25 Lexical Search
Check how often each word in the search query shows up in the text, if it shows up less it is more important. This means that we should search for that word.

## Combining Both
They use a specific formula called RRF_Score. Search more info online, it is a math operation nothing weird.