import os
import shutil
import tempfile
import re
import structlog
from typing import Dict, Any, Optional, List, Tuple

logger = structlog.get_logger()

def get_output_dir(sub_dir: str = None) -> str:
    """
    Get or create output directory path
    
    Args:
        sub_dir: Optional subdirectory name
        
    Returns:
        Full path to output directory
    """
    base_dir = os.path.join(os.getcwd(), "output")
    
    if sub_dir:
        full_dir = os.path.join(base_dir, sub_dir)
    else:
        full_dir = base_dir
        
    os.makedirs(full_dir, exist_ok=True)
    return full_dir

def sanitize_filename(filename: str) -> str:
    """
    Sanitize a filename to ensure it's valid across operating systems
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Replace invalid characters with underscores
    sanitized = re.sub(r'[\\/*?:"<>|]', '_', filename)
    # Ensure the filename isn't too long
    max_length = 255
    if len(sanitized) > max_length:
        name, ext = os.path.splitext(sanitized)
        sanitized = name[:max_length-len(ext)] + ext
    return sanitized

def save_file(content: str, filename: str, sub_dir: str = None) -> Dict[str, Any]:
    """
    Save content to a file
    
    Args:
        content: Content to save
        filename: Filename to use
        sub_dir: Optional subdirectory under the output directory
        
    Returns:
        Dictionary with status and file path
    """
    try:
        filename = sanitize_filename(filename)
        output_dir = get_output_dir(sub_dir)
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return {
            "status": "success",
            "file_path": file_path,
            "message": f"File saved to {file_path}"
        }
    except Exception as e:
        logger.error(f"Error saving file: {str(e)}")
        return {
            "status": "error",
            "message": f"Failed to save file: {str(e)}"
        }
