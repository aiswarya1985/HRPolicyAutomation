"""03 · logging_config — one place to turn on readable console logging."""

import logging
import os

_CONFIGURED = False

def configure_logging(level: "str | int | None" = None) -> None:
    """Attach a plain-message handler to the root logger, once per process."""
    global _CONFIGURED
    if _CONFIGURED:
        return
        
    log_level = level or os.getenv("LOG_LEVEL", "INFO")
    
    # 1. Console Handler (Keeps the clean output for your terminal)
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
    )
    
    # 2. File Handler (Detailed format)
    file_handler = logging.FileHandler("hrpolicy_automation.log", mode="a", encoding="utf-8")
    
    # Format: Timestamp | Level | File | Method | Line | Message
    file_format = (
        "%(asctime)s | %(levelname)-8s | "
        "[File: %(filename)s] "                  # e.g., ingestion.py
        "[Method: %(funcName)s] "                # e.g., ingest_hr_policies
        "[Line: %(lineno)d] | "                  # e.g., 54
        "%(message)s"
    )
    file_handler.setFormatter(logging.Formatter(file_format))
    
    # Attach the file handler to the root logger
    logging.getLogger().addHandler(file_handler)
    
    # Streamlit config fix
    logging.getLogger("hr_assistant").setLevel(log_level)
    _CONFIGURED = True