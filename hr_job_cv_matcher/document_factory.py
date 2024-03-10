from pathlib import Path

import chainlit
from pdf_to_text_client import extract_text_from_pdf
from langchain.schema import Document

from config import cfg
from log_init import logger



def convert_to_doc(file: chainlit.types.AskFileResponse) -> Document:
    path = write_to_temp_folder(file)
    source = path.absolute()
    content = extract_text_from_pdf(path)
    return Document(page_content=content, metadata={'source': source})



def write_to_temp_folder(file) -> Path:
    temp_doc_location = cfg.temp_doc_location
    new_path = temp_doc_location / (file.name)
    logger.info(f"new path: {new_path}")
    with open(new_path, "wb") as f:
        f.write(file.content)
    return new_path