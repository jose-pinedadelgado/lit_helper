from __future__ import annotations
from pathlib import Path
from typing import Iterable, List
from llama_index.core import SimpleDirectoryReader

def discover_documents(
        document_dir: str | Path,
        extensions: Iterable[str] = (".pdf",),
) -> List[Path]:
    """
    Discover documents in a directory with specified extensions.

    Args:
        document_dir (str | Path): The directory to search for documents.
        extensions (Iterable[str]): A list of file extensions to include.

    Returns:
        List[Path]: A list of Paths to the discovered documents.
    """
    base = Path(document_dir)
    if not base.exists():
        return []
    
    extension_list = {ext.lower() for ext in extensions}
    docs: List[Path] = []
    for p in base.rglob("*"):
        if p.is_file() and p.suffix.lower() in extension_list:
            docs.append(p)
    return sorted(docs)
    
def load_pdf(path: str | Path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"PDF file not found in: {p}")
    return SimpleDirectoryReader(input_files=[str(p)]).load_data()
    # type: ignore

    reader = SimpleDirectoryReader(document_dir, recursive=True, required_exts=extensions)
    return reader.load_data()  # type: ignore