#!/usr/bin/env python3
"""
Create folder structure for each game and add deep_research.md template file.

This script:
1. Reads the games_metadata.json to get all game names
2. Creates a folder for each game in docs/benchmarks/[game-name]/
3. Creates a deep_research.md file in each folder with a template header
"""

import json
import re
from pathlib import Path


class GameFolderCreator:
    def __init__(self, repo_root: Path = None):
        """Initialize the folder creator."""
        if repo_root is None:
            repo_root = Path(__file__).parent.parent

        self.repo_root = repo_root
        self.benchmarks_dir = repo_root / "docs" / "benchmarks"
        self.prompts_dir = self.benchmarks_dir / "prompts"
        self.metadata_file = self.prompts_dir / "games_metadata.json"

    def get_folder_name(self, game_name: str) -> str:
        """Convert game name to folder name (lowercase, dashes)."""
        safe_name = re.sub(r'[^\w\s-]', '', game_name.lower())
        safe_name = re.sub(r'[-\s]+', '-', safe_name)
        return safe_name

    def create_template_content(self, game_name: str, priority_number: int, tier: str) -> str:
        """Create the template content for deep_research.md."""
        template = f"""# {game_name} - Deep Research Analysis

**Priority:** {priority_number:02d} ({tier})
**Research Status:** ⏳ TODO - Copy prompt from `docs/benchmarks/prompts/{priority_number:02d}_*.md` and paste into Claude Deep Research

---

## Research Process

1. **Get the prompt**
   - Open `docs/benchmarks/prompts/` folder
   - Find file: `{priority_number:02d}_*_research_prompt.md` (starts with {priority_number:02d})
   - Copy entire prompt text

2. **Run Claude Deep Research**
   - Go to Claude.ai/research
   - Create new research session
   - Paste the prompt
   - Wait 30-45 minutes for research completion

3. **Save results**
   - Copy Claude's output
   - Paste into the sections below
   - Save this file when complete

---

## Game Overview

*To be filled in by Claude Deep Research*

### Basic Information
- Developer:
- Release Date:
- Platforms:
- Team Size:
- Budget:
- Sales:

### Why This Game Matters to Shahnameh
*Analysis of relevance to our project*

---

## User Reception

### Critical Reception
- Metacritic Score:
- Key Praise:
- Key Criticisms:

### Community Sentiment
- Player Reception:
- Active Community:
- Long-term Engagement:

---

## Core Gameplay Mechanics

### Combat System
*Analysis of combat design, weight, responsiveness, skill ceiling*

### Progression Systems
*Level system, skill trees, equipment, pacing*

### Exploration & World Design
*World structure, traversal, points of interest*

---

## Narrative & Storytelling

### Story Structure
*Type, length, themes, delivery methods*

### Character Development
*Protagonist, supporting cast, antagonists*

### Cultural Representation
*If applicable: authenticity, consultation, community reception*

---

## Art Direction & Presentation

### Visual Style
*Art direction, color palette, distinctive elements*

### Technical Achievement
*Performance, optimization, platform parity*

### Inspiration for Shahnameh
*Visual techniques and cultural parallels*

---

## Audio Design

### Music
*Style, memorable themes, cultural elements*

### Sound Design & Voice Acting
*Quality and impact assessment*

---

## Development Insights

### Production Approach
*Team structure, tools, iteration process*

### Asset Creation Pipeline
*How they created assets efficiently*

### Scalability for 2-Person Team
*What's achievable with limited resources*

---

## Scope & Content Analysis

### Game Length
- Main Story:
- Completionist:
- Replayability:

### Content Density
*How much content per hour of gameplay*

### Team Size Achievement
*What they achieved relative to team size*

---

## Key Takeaways for Shahnameh

### Design Lessons

**Combat:**
- ✅ Adopt:
- ❌ Avoid:

**Narrative:**
- ✅ Adopt:
- ❌ Avoid:

**Art & Audio:**
- ✅ Adopt:
- ❌ Avoid:

**Scope:**
- ✅ Adopt:
- ❌ Avoid:

### Business Model Insights
*Pricing, marketing, episodic lessons if applicable*

### Feasibility for 2-Person + AI Team
- **Achievable Elements:**
- **Stretch Goals:**
- **Out of Scope:**

### Actionable Insights
List 5-10 specific things to implement/test/research

---

## YouTube Video Analysis

### Top Videos Found
1. **Video Title** - Channel Name (Duration)
   - Key Timestamp: [MM:SS]
   - Main Insight:

2. **Video Title** - Channel Name (Duration)
   - Key Timestamp: [MM:SS]
   - Main Insight:

---

## Sources & References

### Official Resources
- Website:
- Developer Interviews:
- GDC Talks:

### Reviews & Articles
- [Review 1]:
- [Review 2]:

### Community Resources
- Reddit:
- Wiki:

### Video References
- [Video 1]:
- [Video 2]:

---

## Research Notes

*Personal observations and key insights for the team*

---

## Comparison to Other Games

*How this game relates to other benchmarks in the collection*

| Aspect | {game_name} | Game A | Game B |
|--------|-----------|--------|--------|
| Combat Feel | | | |
| Scope | | | |
| Team Size | | | |
| Budget Efficiency | | | |

---

## Integration with Shahnameh Development

### Immediate Applications
1.
2.
3.

### Design Decisions Informed
1.
2.
3.

### Follow-up Research Needed
- [ ]
- [ ]

---

**Analysis Completed:** [DATE]
**Analyst:** Claude Code
**Status:** ⏳ Pending Deep Research
**Review Status:** Not yet reviewed

"""
        return template

    def run(self):
        """Run the complete folder creation pipeline."""
        print("🎮 Shahnameh Game Folder Creator")
        print("=" * 60)

        # Step 1: Load metadata
        print("\n📚 Step 1: Loading game metadata...")
        if not self.metadata_file.exists():
            print(f"❌ Metadata file not found: {self.metadata_file}")
            return 1

        metadata = json.loads(self.metadata_file.read_text())
        games = metadata['games']
        print(f"✅ Loaded {len(games)} games")

        # Step 2: Create folders and templates
        print("\n📁 Step 2: Creating game folders and templates...")
        created_count = 0
        skipped_count = 0

        for game_info in games:
            game_name = game_info['name']
            folder_name = self.get_folder_name(game_name)
            game_folder = self.benchmarks_dir / folder_name
            deep_research_file = game_folder / "deep_research.md"

            # Create folder if it doesn't exist
            game_folder.mkdir(parents=True, exist_ok=True)

            # Create deep_research.md if it doesn't exist
            if not deep_research_file.exists():
                template_content = self.create_template_content(
                    game_name,
                    game_info['priority_number'],
                    game_info['tier']
                )
                deep_research_file.write_text(template_content)
                print(f"   ✅ {game_info['priority_number']:02d}. {game_name}")
                created_count += 1
            else:
                print(f"   ⏭️  {game_info['priority_number']:02d}. {game_name} (already exists)")
                skipped_count += 1

        # Step 3: Summary
        print("\n" + "=" * 60)
        print("✨ Folder Creation Complete!")
        print("=" * 60)
        print(f"📁 Folders created: {created_count}")
        print(f"⏭️  Folders skipped: {skipped_count}")
        print(f"📍 Location: {self.benchmarks_dir}")
        print("\n🚀 Next Steps:")
        print("   1. Open docs/benchmarks/prompts/README.md")
        print("   2. Choose a game (start with TIER 1: 01-09)")
        print("   3. Copy the prompt file (e.g., 01_assassins_creed_mirage_research_prompt.md)")
        print("   4. Paste into Claude Deep Research")
        print("   5. Save results to docs/benchmarks/[game-name]/deep_research.md")

        return 0


def main():
    """Main entry point."""
    try:
        creator = GameFolderCreator()
        return creator.run()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
