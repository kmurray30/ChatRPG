import atexit
import os
import json
import uuid

import openai
from dotenv import load_dotenv
from llama_index.core.schema import (TextNode)
from llama_index.core import (SimpleDirectoryReader, StorageContext,
                              VectorStoreIndex, load_index_from_storage, Document)
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.vector_stores.milvus import MilvusVectorStore
from milvus import default_server

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

data_files_path = "../../entities/"

def generate_guid():
    return str(uuid.uuid4())

def create_text_node_from_json(file_path):
    with open(file_path, 'r') as file:
        data: dict = json.load(file)

    description = data.get('description')
    data.pop('description')
    entity_id = generate_guid()

    node = TextNode(
        text=description,
        id_=entity_id,
        metadata=data
    )

    return node

def load_text_nodes_from_directory(directory_path):
    nodes: list[TextNode] = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            node = create_text_node_from_json(file_path)
            nodes.append(node)
    return nodes

def on_exit():
    # Stop and clean up Milvus server if it is running
    if (default_server.running):
        print("Stopping Milvus server")
        default_server.stop()
        default_server.cleanup()
    print("Exiting the script")

def loadVectors(storeName):
    # Load vectors
    try:
        storage_context = StorageContext.from_defaults(
            persist_dir=f"../../storage/{storeName}"
        )
        index = load_index_from_storage(storage_context)

        index_loaded = True
    except:
        index_loaded = False

    if not index_loaded:
        # load data
        nodes = load_text_nodes_from_directory(data_files_path)

        # build index

        vector_store = MilvusVectorStore(host="localhost", port=default_server.listen_port, dim=1536, collection_name=storeName, overwrite=True)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        index = VectorStoreIndex(nodes, storage_context=storage_context)

        # persist index
        index.storage_context.persist(persist_dir=f"../../storage/{storeName}")

    engine = index.as_query_engine(similarity_top_k=3)

    query_engine_tools = [
        QueryEngineTool(
            query_engine=engine,
            metadata=ToolMetadata(
                name=storeName,
                description=(
                    f"Use this tool every time"
                ),
            ),
        ),
    ]
    return query_engine_tools

# Begin execution here

atexit.register(on_exit)
# Only start milvus server if it is not already running
if (default_server.running):
    print("Milvus server is already running")
else:
    print("Starting Milvus server")
    default_server.start()
    print(f"Milvus server initialized on port {default_server.listen_port}")

# Load vectors
query_engine_tools = loadVectors("entities")

from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-0613")

agent = ReActAgent.from_tools(
    query_engine_tools,
    llm=llm,
    verbose=True,
    # context=context
)

print("Ask me anything!")
while(True):
    inputStr = input()
    if (inputStr == "exit"):
        break
    response = agent.chat(inputStr)
    print(str(response))
    print("\nAsk me anything else! (or type 'exit' to quit)")