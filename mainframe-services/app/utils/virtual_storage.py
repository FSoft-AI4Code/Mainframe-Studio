from typing import Dict, Optional, List
from pathlib import Path
import io
import zipfile
import os

class TemplateCache:
    """
    Singleton class to cache template files in memory.
    """
    _instance = None
    _template_files: Dict[str, bytes] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TemplateCache, cls).__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls, template_base: str) -> None:
        """
        Initialize the template cache by loading all template files into memory.
        
        Args:
            template_base: Base path of the template directory
        """
        if not cls._template_files:
            for root, _, files in os.walk(template_base):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        # Store the file with its relative path as the key
                        rel_path = os.path.relpath(file_path, os.path.dirname(template_base))
                        cls._template_files[rel_path] = f.read()

    @classmethod
    def get_template_files(cls) -> Dict[str, bytes]:
        """
        Get all cached template files.
        
        Returns:
            Dictionary of template files with their paths as keys
        """
        return cls._template_files.copy()

class VirtualStorage:
    """
    A utility class that simulates file storage operations in memory without physical writes.
    """
    def __init__(self):
        self._storage: Dict[str, bytes] = {}

    def write_file(self, content: str | bytes, file_path: str | Path) -> Dict[str, str | bytes]:
        """
        Simulates writing content to a file path without physical storage.
        
        Args:
            content: The content to write (string or bytes)
            file_path: The target file path
            
        Returns:
            Dict containing file_path and content
        """
        if isinstance(content, str):
            content = content.encode('utf-8')
        
        path_str = str(file_path)
        self._storage[path_str] = content
        
        return {
            "file_path": path_str,
            "content": content
        }

    def read_file(self, file_path: str | Path) -> Optional[bytes]:
        """
        Retrieves content from the virtual storage.
        
        Args:
            file_path: The file path to read from
            
        Returns:
            The content as bytes if exists, None otherwise
        """
        path_str = str(file_path)
        return self._storage.get(path_str)

    def delete_file(self, file_path: str | Path) -> bool:
        """
        Removes a file from virtual storage.
        
        Args:
            file_path: The file path to delete
            
        Returns:
            True if file was deleted, False if it didn't exist
        """
        path_str = str(file_path)
        if path_str in self._storage:
            del self._storage[path_str]
            return True
        return False

    def exists(self, file_path: str | Path) -> bool:
        """
        Checks if a file exists in virtual storage.
        
        Args:
            file_path: The file path to check
            
        Returns:
            True if file exists, False otherwise
        """
        return str(file_path) in self._storage

    def clear(self) -> None:
        """
        Clears all stored files from virtual storage.
        """
        self._storage.clear()

    def create_zip_from_files(self, file_paths: List[str | Path]) -> bytes:
        """
        Creates a ZIP file containing the specified virtual files.
        
        Args:
            file_paths: List of file paths to include in the ZIP
            
        Returns:
            ZIP file as bytes
            
        Raises:
            FileNotFoundError: If any of the specified files don't exist in virtual storage
        """
        # Create a BytesIO object to store the ZIP file
        zip_buffer = io.BytesIO()
        
        # Create a ZIP file in memory
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for file_path in file_paths:
                path_str = str(file_path)
                if path_str not in self._storage:
                    raise FileNotFoundError(f"File not found in virtual storage: {path_str}")
                
                # Get the content and add it to the ZIP
                content = self._storage[path_str]
                # Use just the filename as the archive name
                archive_name = Path(path_str).name
                zip_file.writestr(archive_name, content)
        
        # Get the ZIP file content
        zip_buffer.seek(0)
        return zip_buffer.getvalue()

    def create_zip_from_all_files(self) -> bytes:
        """
        Creates a ZIP file containing all files in virtual storage.
        
        Returns:
            ZIP file as bytes
        """
        return self.create_zip_from_files(list(self._storage.keys())) 