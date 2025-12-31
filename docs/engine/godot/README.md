# Godot Engine Documentation - LLM-Optimized Format

**Version:** Godot 4.6 (master branch)
**Generated:** 2025-12-26
**Total Documentation Files:** 1,493
**Total Size:** ~49MB

---

## Overview

This directory contains the official Godot Engine documentation optimized for Large Language Model (LLM) consumption. The documentation has been compiled into structured formats that maximize LLM comprehension, search efficiency, and context window utilization.

## Directory Structure

```
llm-docs/
├── classes/          # 1,066 JSON files - Complete API reference
├── tutorials/        # 427 text files - Comprehensive tutorials
├── guides/           # Getting started guides and walkthroughs
├── about/            # General Godot information
├── index.json        # Master metadata and navigation index
├── searchindex.json  # Full-text search index
└── README.md         # This file
```

---

## Format Specifications

### 1. Class Reference (classes/)

**Format:** JSON (`.fjson` extension)
**Count:** 1,066 files
**Structure:** Each file contains complete API documentation for one class

**JSON Schema:**
```json
{
  "title": "ClassName",
  "parents": [{"link": "../parent_class/", "title": "ParentClass"}],
  "body": "<HTML content with full documentation>",
  "meta": {"github_url": "hide"},
  "prev": {"link": "../previous_class/", "title": "PreviousClass"},
  "next": {"link": "../next_class/", "title": "NextClass"}
}
```

**Key Features:**
- Complete method signatures with parameters and return types
- Property definitions with default values
- Signal definitions
- Inheritance hierarchy
- Cross-references to related classes

**Use Cases:**
- Quick API lookups
- Method signature verification
- Class hierarchy navigation
- Type checking and validation

### 2. Tutorials (tutorials/)

**Format:** Plain text (`.txt`)
**Count:** 427 files
**Structure:** Clean, semantic plain text with section headers

**Categories:**
- `2d/` - 2D game development
- `3d/` - 3D game development
- `animation/` - Animation system
- `audio/` - Audio and sound
- `physics/` - Physics engine (2D and 3D)
- `scripting/` - GDScript and other languages
- `shaders/` - Shader programming
- `ui/` - User interface
- `networking/` - Multiplayer and networking
- `xr/` - XR/VR/AR development
- `performance/` - Optimization techniques
- `export/` - Exporting to platforms
- `plugins/` - Plugin development

**Use Cases:**
- Learning Godot concepts
- Understanding workflows
- Best practices
- Step-by-step guides

### 3. Guides (guides/)

**Format:** Plain text (`.txt`)
**Content:** Getting started materials, introduction to Godot, first projects

**Use Cases:**
- Beginner-friendly learning
- Quick start tutorials
- First 2D/3D game development

### 4. About (about/)

**Format:** Plain text (`.txt`)
**Content:** Godot features, system requirements, FAQ, licenses, release policy

---

## LLM Usage Guidelines

Based on Anthropic's prompt engineering best practices, here's how to effectively use this documentation with an LLM agent:

### Structure Your Prompts with XML Tags

```xml
<documentation>
  <class_reference>
    {{classes/class_node.fjson}}
  </class_reference>

  <tutorial>
    {{tutorials/scripting/nodes_and_scene_instances.txt}}
  </tutorial>
</documentation>

<query>
How do I create a child node and add it to the scene tree?
</query>
```

### Long Context Optimization

**Place documentation at the top of your prompt** for 30% better performance:

```xml
<documents>
  <document index="1">
    <source>classes/class_characterbody2d.fjson</source>
    <document_content>
      {{CLASS_CONTENT}}
    </document_content>
  </document>
  <document index="2">
    <source>tutorials/2d/2d_movement.txt</source>
    <document_content>
      {{TUTORIAL_CONTENT}}
    </document_content>
  </document>
</documents>

{{YOUR_QUERY_HERE}}
```

### Quote-Based Grounding

For accuracy, ask the LLM to quote relevant sections first:

```xml
<instructions>
1. Find quotes from the documentation relevant to the user's question
2. Place quotes in <quotes> tags with source attribution
3. Answer the question based on the quoted material
4. Place your answer in <answer> tags
</instructions>

<documentation>
  {{GODOT_DOCS}}
</documentation>

<query>{{USER_QUESTION}}</query>
```

### Example LLM Prompt Template

```xml
<system>
You are a Godot Engine expert assistant. Your role is to help developers
learn and use Godot effectively by referencing official documentation.

When answering questions:
1. Always cite specific documentation sources
2. Quote relevant sections before explaining
3. Provide code examples when applicable
4. Mention version-specific considerations (Godot 4.6)
</system>

<godot_documentation>
  <class_reference>
    {{classes/RELEVANT_CLASS.fjson}}
  </class_reference>

  <tutorials>
    {{tutorials/RELEVANT_TUTORIAL.txt}}
  </tutorials>
</godot_documentation>

<user_query>
{{QUESTION}}
</user_query>

<instructions>
1. Search the documentation for relevant information
2. Quote specific sections with source attribution
3. Explain the concept clearly
4. Provide a working code example
5. Mention any gotchas or best practices
</instructions>
```

---

## Quick Reference

### Finding Classes

All class files follow the pattern: `classes/class_<classname>.fjson`

**Core Classes:**
- `class_node.fjson` - Base class for all scene objects
- `class_node2d.fjson` - Base for 2D transformations
- `class_node3d.fjson` - Base for 3D transformations
- `class_control.fjson` - Base for UI elements
- `class_resource.fjson` - Base for all resources

**Common Nodes:**
- CharacterBody2D/3D - Player movement
- RigidBody2D/3D - Physics objects
- Area2D/3D - Trigger zones
- Sprite2D - 2D images
- MeshInstance3D - 3D models
- Camera2D/3D - Viewport cameras

### Finding Tutorials

Navigate by topic:
- **Movement:** `tutorials/2d/2d_movement.txt`, `tutorials/3d/3d_movement.txt`
- **Input:** `tutorials/inputs/`
- **Physics:** `tutorials/physics/`
- **Signals:** `tutorials/scripting/instancing_with_signals.txt`
- **GDScript:** `tutorials/scripting/gdscript/`

### Search Index

Use `searchindex.json` for full-text search across all documentation. It contains:
- Document titles
- Indexed terms
- Document paths
- Tokenized content

---

## File Format Details

### JSON (.fjson) Files

Files use the `.fjson` extension (Flexible JSON) but are standard JSON format. They contain:

- **HTML content in body** - Structured with semantic HTML tags
- **Navigation links** - Previous/next class references
- **Metadata** - GitHub links, edit info
- **Hierarchy** - Parent/child class relationships

**Parsing Strategy:**
1. Load JSON
2. Extract `body` field (contains HTML documentation)
3. Parse HTML or use directly (semantic tags are LLM-friendly)
4. Use `title` for class name
5. Use `parents` for inheritance chain

### Text (.txt) Files

- Clean, semantic plain text
- Section headers clearly marked
- Code blocks preserved
- Cross-references as text
- No HTML/markup overhead

---

## Integration Examples

### Python Example

```python
import json
from pathlib import Path

docs_path = Path("docs/engine/godot/llm-docs")

# Load class reference
def load_class(class_name):
    file_path = docs_path / f"classes/class_{class_name.lower()}.fjson"
    with open(file_path) as f:
        return json.load(f)

# Load tutorial
def load_tutorial(topic):
    file_path = docs_path / f"tutorials/{topic}.txt"
    return file_path.read_text()

# Example: Get Node class documentation
node_docs = load_class("node")
print(node_docs["title"])  # "Node"

# Example: Get 2D movement tutorial
movement_tutorial = load_tutorial("2d/2d_movement")
```

### LLM Prompt Builder

```python
def build_godot_prompt(query, classes=[], tutorials=[]):
    """Build an LLM prompt with Godot documentation."""

    prompt = "<godot_documentation>\n"

    # Add class references
    if classes:
        prompt += "  <class_reference>\n"
        for class_name in classes:
            docs = load_class(class_name)
            prompt += f"    <class name='{docs['title']}'>\n"
            prompt += f"      {docs['body']}\n"
            prompt += f"    </class>\n"
        prompt += "  </class_reference>\n"

    # Add tutorials
    if tutorials:
        prompt += "  <tutorials>\n"
        for tutorial_path in tutorials:
            content = load_tutorial(tutorial_path)
            prompt += f"    <tutorial source='{tutorial_path}'>\n"
            prompt += f"      {content}\n"
            prompt += f"    </tutorial>\n"
        prompt += "  </tutorials>\n"

    prompt += "</godot_documentation>\n\n"
    prompt += f"<query>{query}</query>"

    return prompt

# Example usage
prompt = build_godot_prompt(
    query="How do I make a player character move?",
    classes=["CharacterBody2D", "Input"],
    tutorials=["2d/2d_movement"]
)
```

---

## Best Practices for LLM Agents

### 1. **Be Selective**
Don't load all documentation at once. Choose:
- Relevant classes (2-5 max)
- Specific tutorials (1-3 max)
- Related topics only

### 2. **Use Hierarchical Structure**
```xml
<documentation priority="high">
  <core_classes>{{Node, CharacterBody2D}}</core_classes>
</documentation>
<documentation priority="medium">
  <related_tutorials>{{Movement tutorial}}</related_tutorials>
</documentation>
```

### 3. **Leverage Search Index**
Query `searchindex.json` first to find relevant documents, then load only those.

### 4. **Cache Common Classes**
Frequently referenced classes (Node, Node2D, Resource) can be cached in context.

### 5. **Version Awareness**
Always mention this is Godot 4.6 documentation when responding to users.

---

## Metadata

- **Source:** Official Godot Documentation (godot-docs repository)
- **License:** CC BY 3.0 (tutorials), MIT (class reference)
- **Build Tool:** Sphinx documentation generator
- **Formats:** JSON for structured data, Plain text for readability
- **Optimization:** Follows Anthropic Claude prompt engineering guidelines

---

## Update Instructions

To regenerate this documentation from source:

```bash
cd docs/engine/godot/godot-docs

# Generate JSON format (class reference)
SPHINX_NO_DESCRIPTIONS=1 .venv/bin/sphinx-build \
  -b json \
  -D extensions=sphinx_tabs.tabs,notfound.extension,sphinx_copybutton,sphinxcontrib.video \
  . _build/json

# Generate text format (tutorials)
SPHINX_NO_DESCRIPTIONS=1 .venv/bin/sphinx-build \
  -b text \
  -D extensions=sphinx_tabs.tabs,notfound.extension,sphinx_copybutton,sphinxcontrib.video \
  . _build/text

# Copy to llm-docs directory
mkdir -p ../llm-docs/{classes,tutorials,guides,about}
cp -r _build/json/classes/*.fjson ../llm-docs/classes/
cp -r _build/text/tutorials ../llm-docs/
cp -r _build/text/getting_started ../llm-docs/guides/
cp -r _build/text/about/*.txt ../llm-docs/about/
cp _build/json/searchindex.json ../llm-docs/
```

---

## Support

For Godot documentation issues: https://github.com/godotengine/godot-docs/issues
For Godot engine issues: https://github.com/godotengine/godot/issues
For LLM integration questions: Refer to Anthropic's prompt engineering guide

---

**Happy Godot Development! 🎮**
