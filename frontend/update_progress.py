import os
import time
from datetime import datetime

# Specific development file types and folder layers ignored by the mapping process
IGNORE_LIST = {
    '.git', '.claude', '.github', 'node_modules', '__pycache__', 
    'update_progress.py', 'PROGRESS.md', 'repomix-output.txt', '.next', 'dist'
}

def get_project_tree(dir_path, prefix=""):
    """Recursively calculates a visual text-based layout of directories and files."""
    tree = ""
    try:
        items = sorted(os.listdir(dir_path))
    except PermissionError:
        return ""
    
    # Filter out hidden deployment or asset directories
    items = [item for item in items if item not in IGNORE_LIST]
    
    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        tree += f"{prefix}{connector}{item}\n"
        
        if os.path.isdir(path):
            next_prefix = prefix + ("    " if is_last else "│   ")
            tree += get_project_tree(path, next_prefix)
    return tree

def get_recent_files(dir_path, limit=5):
    """Identifies and indexes the most recently updated project code files."""
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        # Skip evaluating ignored system directory paths
        dirs[:] = [d for d in dirs if d not in IGNORE_LIST]
        
        for file in files:
            if file in IGNORE_LIST:
                continue
            path = os.path.join(root, file)
            try:
                mod_time = os.path.getmtime(path)
                file_list.append((path, mod_time))
            except FileNotFoundError:
                continue
                
    # Sort paths descending by date modified
    file_list.sort(key=lambda x: x, reverse=True)
    return file_list[:limit]

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("⏳ Analyzing project structure and identifying current development delta...")
    
    folder_tree = get_project_tree(root_dir)
    recent_files = get_recent_files(root_dir)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    markdown_content = f"""# 🚀 Project Progress Status
*Last Synced: {timestamp}*

## 📁 Current File Structure Map
```text
{folder_tree if folder_tree else 'Project root is currently clear.'}```

## ⏱️ Recently Modified Files (Active Workspace Delta)
"""
    if recent_files:
        for path, mod_time in recent_files:
            relative_path = os.path.relpath(path, root_dir)
            readable_time = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
            markdown_content += f"- `{relative_path}` *(Modified: {readable_time})*\n"
    else:
        markdown_content += "- No recent modifications detected in this work session.\n"
        
    markdown_content += """
## 📝 Next Steps / Tasks to Do
- [ ] *Insert your active architectural prompt or next component requirement here*
"""

    with open(os.path.join(root_dir, "PROGRESS.md"), "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    print("✅ PROGRESS.md documentation block compiled successfully.")

if __name__ == "__main__":
    main()
