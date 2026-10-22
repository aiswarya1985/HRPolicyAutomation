"""11 · tools — wrap retrieve (08) + re-rank (10) as one tool the agent calls.

Retriever-as-tool: wide retrieval -> re-rank -> narrow, cited result. The
agent decides when to call it (see agent.py, 13).
"""

import json

from langchain.tools import tool

from hr_assistant import config
from hr_assistant.reranker import rerank
from hr_assistant.vector_store import get_retriever

import logging
logger = logging.getLogger(__name__)

def create_search_tool(vector_store):
    """Return a @tool function that searches + re-ranks the HR policy corpus."""

    @tool
    def search_hr_policy(question: str) -> str:
        """Search the HR policy documents for information about leave,
        work from home,
        probation, notice period, 
        reimbursement, code of conduct, 
        holidays, maternity/
        paternity leave, travel expenses, or the exit process."""
        logger.info("Entering search_hr_policy() with question: %s", question)
        retriever = get_retriever(vector_store, 
                        k=config.RERANK_CANDIDATE_K)
        candidates = retriever.invoke(question)
        logger.info("Candidates:\n%s", json.dumps([c.model_dump() for c in candidates], indent=2, default=str))
        top_chunks = rerank(question, candidates, 
                    top_n=config.TOP_K_RESULTS)
        logger.info("Top Chunks:\n%s", json.dumps([c.model_dump() for c in top_chunks], indent=2, default=str))
        return "\n\n".join(
            f"[Source: {c.metadata['source']}]\n{c.page_content}" for c in top_chunks
        )

    return search_hr_policy
