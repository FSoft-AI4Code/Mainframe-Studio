from typing import Dict, Any, List
from loguru import logger
from schema.summarization import CopybookField, CopybookGroup

class CopybookSummarizer:
    def __init__(self):
        self.current_level = 0
        self.fields: List[CopybookField] = []
        self.groups: List[CopybookGroup] = []
        self.record_length = 0

    def summarize(self, content: str) -> Dict[str, Any]:
        """
        Analyze and summarize a copybook file.
        
        Args:
            content: String containing the copybook content
            
        Returns:
            Dict containing:
                - short_description: str
                - fields: List[CopybookField]
                - groups: List[CopybookGroup]
                - record_length: int
        """
        try:
            lines = content.split('\n')
            self._reset_state()
            
            # Process each line
            for line in lines:
                line = line.strip()
                if not line or line.startswith('*'):
                    continue
                    
                self._process_line(line)
            
            # Generate short description
            short_description = self._generate_description()
            
            return {
                "short_description": short_description,
                "fields": self.fields,
                "groups": self.groups,
                "record_length": self.record_length
            }
            
        except Exception as e:
            logger.error(f"Error summarizing copybook: {str(e)}")
            raise

    def _reset_state(self):
        """Reset the internal state for a new summarization."""
        self.current_level = 0
        self.fields = []
        self.groups = []
        self.record_length = 0

    def _process_line(self, line: str):
        """
        Process a single line of the copybook.
        
        Args:
            line: String containing a single line of the copybook
        """
        # Split the line into components
        parts = line.split()
        if not parts:
            return
            
        level = int(parts[0])
        name = parts[1]
        
        # Extract field properties
        field = CopybookField(
            name=name,
            level=level,
            type=self._determine_type(parts),
            description=self._extract_description(parts),
            occurs=self._extract_occurs(parts),
            redefines=self._extract_redefines(parts),
            usage=self._extract_usage(parts),
            picture=self._extract_picture(parts)
        )
        
        # Update record length based on field type and picture
        self.record_length += self._calculate_field_length(field)
        
        # Add to appropriate list
        if level == 1:
            self.groups.append(CopybookGroup(
                name=name,
                level=level,
                description=field.description,
                fields=[field],
                groups=[]
            ))
        else:
            self.fields.append(field)

    def _determine_type(self, parts: List[str]) -> str:
        """Determine the field type based on the line parts."""
        if any('PIC' in p for p in parts):
            return 'numeric'
        elif any('PICTURE' in p for p in parts):
            return 'numeric'
        elif any('COMP' in p for p in parts):
            return 'computational'
        elif any('COMP-3' in p for p in parts):
            return 'packed-decimal'
        else:
            return 'alphanumeric'

    def _extract_description(self, parts: List[str]) -> str:
        """Extract field description from the line parts."""
        # Look for description after field name
        try:
            desc_start = parts.index(parts[1]) + 1
            if desc_start < len(parts):
                return ' '.join(parts[desc_start:])
        except:
            pass
        return None

    def _extract_occurs(self, parts: List[str]) -> int:
        """Extract OCCURS value if present."""
        try:
            occurs_idx = parts.index('OCCURS')
            if occurs_idx + 1 < len(parts):
                return int(parts[occurs_idx + 1])
        except:
            pass
        return None

    def _extract_redefines(self, parts: List[str]) -> str:
        """Extract REDEFINES value if present."""
        try:
            redefines_idx = parts.index('REDEFINES')
            if redefines_idx + 1 < len(parts):
                return parts[redefines_idx + 1]
        except:
            pass
        return None

    def _extract_usage(self, parts: List[str]) -> str:
        """Extract USAGE value if present."""
        try:
            usage_idx = parts.index('USAGE')
            if usage_idx + 1 < len(parts):
                return parts[usage_idx + 1]
        except:
            pass
        return None

    def _extract_picture(self, parts: List[str]) -> str:
        """Extract PICTURE/PIC value if present."""
        try:
            pic_idx = next(i for i, p in enumerate(parts) if p in ['PICTURE', 'PIC'])
            if pic_idx + 1 < len(parts):
                return parts[pic_idx + 1]
        except:
            pass
        return None

    def _calculate_field_length(self, field: CopybookField) -> int:
        """Calculate the length of a field in bytes."""
        if not field.picture:
            return 0
            
        # Basic length calculation based on picture
        length = 0
        for char in field.picture:
            if char.isdigit():
                length += int(char)
            elif char in ['X', 'A', '9']:
                length += 1
                
        # Adjust for special types
        if field.usage == 'COMP-3':
            length = (length + 1) // 2
        elif field.usage == 'COMP':
            if length <= 4:
                length = 2
            elif length <= 9:
                length = 4
            else:
                length = 8
                
        # Multiply by occurs if present
        if field.occurs:
            length *= field.occurs
            
        return length

    def _generate_description(self) -> str:
        """Generate a short description of the copybook."""
        if not self.groups and not self.fields:
            return "Empty copybook"
            
        # Count fields by type
        type_counts = {}
        for field in self.fields:
            type_counts[field.type] = type_counts.get(field.type, 0) + 1
            
        # Build description
        desc_parts = []
        if self.groups:
            desc_parts.append(f"{len(self.groups)} group(s)")
        if type_counts:
            type_desc = ", ".join(f"{count} {type_}" for type_, count in type_counts.items())
            desc_parts.append(f"{type_desc} field(s)")
        if self.record_length:
            desc_parts.append(f"total length {self.record_length} bytes")
            
        return "Copybook containing " + " with ".join(desc_parts)

