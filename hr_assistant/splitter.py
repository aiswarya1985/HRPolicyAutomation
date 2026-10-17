"""06 · splitter — chop each document into small, searchable, overlapping
chunks (config.CHUNK_SIZE / CHUNK_OVERLAP)."""

from venv import logger

from langchain_text_splitters import RecursiveCharacterTextSplitter

from hr_assistant import config
import logging

logger = logging.getLogger(__name__)


def split_into_chunks(documents):
    """Split documents into small overlapping chunks. Metadata (source,
    policy_category) carries over onto every chunk automatically."""
    logger.info("Splitting %d document(s) into chunks (size=%d, overlap=%d)...", len(documents), config.CHUNK_SIZE, config.CHUNK_OVERLAP)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
    )
    logger.info("chunking complete: %d chunk(s) created.", len(documents))
    return text_splitter.split_documents(documents)
