#!/usr/bin/env python3
"""
Generate optimized Claude Deep Research prompts for each game in the benchmark list.

This script:
1. Extracts all game names from benchmark_deep_research.md
2. Combines multiple templates (VIDEO_ANALYSIS, YOUTUBE_ANALYSIS, CLAUDE_DEEP_RESEARCH, GAME_NAME)
3. Removes redundancies and creates focused, optimized prompts
4. Generates individual prompt files in docs/benchmarks/prompts/
"""

import re
import json
from pathlib import Path
from typing import List, Set, Dict, Optional

class GamePromptGenerator:
    def __init__(self, repo_root: Path = None):
        """Initialize the prompt generator."""
        if repo_root is None:
            repo_root = Path(__file__).parent.parent

        self.repo_root = repo_root
        self.benchmarks_dir = repo_root / "docs" / "benchmarks"
        self.prompts_dir = self.benchmarks_dir / "prompts"
        self.template_dir = self.benchmarks_dir / "_template"

        # Create prompts directory if it doesn't exist
        self.prompts_dir.mkdir(parents=True, exist_ok=True)

        # Store extracted games and metadata
        self.games: Dict[str, Dict[str, str]] = {}
        self.tier_mapping: Dict[str, str] = {}

    def extract_games_from_markdown(self) -> Dict[str, Dict[str, str]]:
        """Extract all game names and metadata from benchmark_deep_research.md."""
        benchmark_file = self.benchmarks_dir / "benchmark_deep_research.md"

        if not benchmark_file.exists():
            raise FileNotFoundError(f"Benchmark file not found: {benchmark_file}")

        content = benchmark_file.read_text()
        games = {}

        # Pattern to find TIER sections (## TIER 1, ## TIER 2, ## TIER 3)
        tier_pattern = r'## (TIER \d+[^\n]*)\n\n(.*?)(?=## TIER|\Z)'
        # Pattern to find games: **Game Name** — Developer (with optional year)
        game_pattern = r'\*\*([^*]+?)\*\*\s*(?:\([^)]+\))?\s*—\s*([^\n]+)'

        for tier_match in re.finditer(tier_pattern, content, re.DOTALL):
            tier_name = tier_match.group(1).strip()
            tier_content = tier_match.group(2)

            # Extract tier number for sorting
            tier_num = re.search(r'TIER (\d+)', tier_name)
            tier_key = f"TIER_{tier_num.group(1)}" if tier_num else tier_name

            for game_match in re.finditer(game_pattern, tier_content):
                game_name = game_match.group(1).strip()
                developer = game_match.group(2).strip()

                # Clean up developer info (remove year if attached)
                developer = re.sub(r'\s*\(\d{4}\)\s*', '', developer)

                # Skip non-game entries (like "Additional" headers or category names)
                if not self._is_valid_game_entry(game_name):
                    continue

                games[game_name] = {
                    'developer': developer,
                    'tier': tier_key,
                    'relevance': self._determine_relevance(tier_key)
                }
                self.tier_mapping[game_name] = tier_key

        self.games = games
        return games

    def _is_valid_game_entry(self, game_name: str) -> bool:
        """Check if an entry is a valid game (not a category header)."""
        # Filter out false positives - entries that are not actual games
        invalid_patterns = [
            'Additional',
            'Combat',
            'Budget',
            'Small team',
            'References',
            'ABANDONED',
            'optional',
            'Post-Launch',
            'See',
            'Read',
            'Any of the',
            'These games',
            'Official',
            'Community',
            'Existing',
            'first chapter',
        ]
        return not any(keyword in game_name for keyword in invalid_patterns)

    def _determine_relevance(self, tier: str) -> str:
        """Determine relevance level based on tier."""
        tier_relevance = {
            'TIER_1': 'immediate',
            'TIER_2': 'important',
            'TIER_3': 'reference'
        }
        return tier_relevance.get(tier, 'reference')

    def generate_optimized_prompt(self, game_name: str, game_info: Dict[str, str]) -> str:
        """
        Generate an optimized research prompt combining all templates.

        This removes redundancies and focuses the prompt on high-value research areas.
        """
        relevance = game_info.get('relevance', 'reference')
        developer = game_info.get('developer', 'Unknown')
        tier = game_info.get('tier', 'TIER_3')

        # Build the optimized prompt
        prompt = f"""<research_context>
You are conducting competitive analysis for "Shahnameh: Legends of Persia," an episodic action-adventure game based on Persian mythology, being developed by a 2-person software engineering team using AI-assisted development and free/local tools.

Your task is to research <game_name>{game_name}</game_name> and create a focused benchmark analysis tailored to Shahnameh development.

IMPORTANCE LEVEL: {relevance.upper()} ({tier})
DEVELOPER: {developer}
</research_context>

<project_constraints>
- Team Size: 2 software engineers (not game developers)
- Development Approach: Claude Code AI-driven development
- Budget: $0/month (free tools: Stable Diffusion, Blender, AudioCraft, etc.)
- Target: 3-episode action-adventure game (2-3 hrs each)
- Focus: Persian mythology (Shahnameh epic)

</project_constraints>

<research_strategy>
Based on relevance tier, focus on specific areas:

TIER 1 (Immediate Study): DEEP ANALYSIS
- Complete mechanics breakdown
- Detailed team/budget analysis
- Full combat system deep dive
- Business model and episodic strategy lessons
- YouTube video analysis (4-5 videos minimum)

TIER 2 (Important Reference): FOCUSED ANALYSIS
- Key mechanics and design patterns
- Team size and scope decisions
- Relevant lessons for Shahnameh
- 2-3 YouTube videos highlighting key features

TIER 3 (Comprehensive Reference): TARGETED ANALYSIS
- Specific mechanics applicable to Shahnameh
- Design lessons relevant to our constraints
- 1-2 key YouTube videos if available
</research_strategy>

<prioritized_research_sections>
Based on relevance tier, prioritize these areas:

ALWAYS INCLUDE:
1. **Basic Information** - Team, budget, sales, scores
2. **User Reception** - What players love/hate (Steam reviews, Reddit)
3. **Shahnameh Relevance** - Why THIS game matters to our project
4. **Key Takeaways** - Actionable lessons for 2-person team

TIER 1 - ALSO INCLUDE:
5. **Complete Combat Analysis** - Mechanics, feel, boss design patterns
6. **Development Insights** - Process, tools, iteration, asset pipeline
7. **YouTube Deep Dive** - 4-5 videos with timestamps
8. **Full Scope Analysis** - Content volume, design decisions, team achievements
9. **Episodic Lessons** (if applicable) - Release timing, pricing, player retention

TIER 2 - ALSO INCLUDE:
5. **Key Combat Mechanics** - Most relevant systems
6. **Development Highlights** - Team size achievements, smart decisions
7. **YouTube Analysis** - 2-3 videos with key timestamps
8. **Scope & Feasibility** - What's achievable for small team

TIER 3 - FOCUS ON:
5. **Specific Mechanics** - Only what applies to Shahnameh
6. **YouTube References** - If videos exist, note them
7. **Feasibility Analysis** - What we can realistically adopt
</prioritized_research_sections>

<research_instructions>
Research <game_name>{game_name}</game_name> comprehensively using web searches, YouTube, reviews, developer interviews, GDC talks, Reddit discussions, and other credible sources.

KEY RESEARCH QUESTIONS:

1. **Why is this game relevant to Shahnameh?**
   - What problem/design challenge does it solve?
   - Which aspect(s) apply to our project?

2. **Team Size & Budget Reality**
   - How many people made this game?
   - What was the budget (if public)?
   - What did they achieve relative to team size?
   - How did they maximize limited resources?

3. **For Combat Games:**
   - Combat feel and weight (weighty, responsive, floaty?)
   - Boss design patterns
   - Difficulty balancing approach
   - Animation commitment vs. cancellation
   - How is it similar/different from Dark Souls?

4. **For Episodic Games:**
   - Episode pricing and timing
   - Content per episode
   - Player retention between releases
   - Why episodic succeeded or failed

5. **For Mythology/Cultural Games:**
   - How did they research the culture?
   - Did they consult experts?
   - What authenticity decisions did they make?
   - Community reception from represented culture?

6. **Production & Tools**
   - Which engine/tools did they use?
   - Asset pipeline (outsourced, procedural, AI?)
   - Optimization strategies
   - Performance targets achieved

7. **YouTube Video Analysis**
   - Find 2-5 most valuable videos (reviews, GDC talks, analysis)
   - Extract timestamps for key insights
   - Note what makes each video worth watching
   - Focus on actionable lessons, not plot summaries

8. **Small Team Lessons**
   - What shortcuts did they take?
   - What quality compromises happened?
   - What smart decisions magnified their impact?
   - Which free/cheap tools could replace their paid ones?

9. **Feasibility for Our Constraints**
   - What can a 2-person team + free AI tools realistically adopt?
   - What requires larger budget/team?
   - Specific design patterns we can implement
   - Pitfalls to avoid
</research_instructions>

<output_structure>
Structure your analysis using these sections. Be concise - focus on what matters for Shahnameh:

**GAME OVERVIEW** [2-3 paragraphs]
- Title, developer, release, platforms, team size, budget, sales
- One-sentence description
- Why it matters to Shahnameh

**CORE RELEVANCE** [1 paragraph]
- Specific mechanic/feature/approach relevant to our project
- How we can apply this lesson
- What makes it applicable to 2-person + AI team

**USER RECEPTION** [1-2 paragraphs]
- Metacritic/user scores
- Most praised aspects (3-5 points)
- Most criticized aspects (3-5 points)
- What this tells us about player expectations

**GAMEPLAY MECHANICS** [2-3 paragraphs if TIER 1/2, 1 paragraph if TIER 3]
- Combat system (weight, responsiveness, skill ceiling)
- Progression and pacing
- What works, what doesn't
- Specific mechanics applicable to Shahnameh

**NARRATIVE & STORYTELLING** [1-2 paragraphs]
- Story structure and delivery
- Character development approach
- How cultural/mythological elements were handled (if relevant)
- Lessons for Persian storytelling in Shahnameh

**ART & PRESENTATION** [1 paragraph]
- Art direction and style
- Technical quality achieved
- Performance optimization approach
- Inspiration for Shahnameh's visual direction

**AUDIO DESIGN** [1 paragraph if applicable]
- Music and cultural instruments
- Sound design approach
- Voice acting quality (if relevant)
- Persian music/audio integration ideas

**DEVELOPMENT INSIGHTS** [1 paragraph]
- Team structure and size impact
- Tools and technology used
- Asset pipeline efficiency
- Iteration and testing approach

**SCOPE & CONTENT** [1 paragraph]
- Game length and content volume
- Team size vs. output quality ratio
- Smart scoping decisions
- What to avoid for 2-person team

**KEY TAKEAWAYS FOR SHAHNAMEH** [2-4 paragraphs]

Design Lessons:
- ✅ Adopt: [Specific mechanic/approach]
- ❌ Avoid: [Specific issue/complexity]
- 🤔 Consider: [Interesting idea worth exploring]

For 2-Person Team:
- Achievable: [Realistic elements we can implement]
- Stretch Goals: [Difficult but possible with AI tools]
- Out of Scope: [What requires larger team/budget]

Actionable Insights:
- 3-5 specific things to implement/test/research

**YOUTUBE VIDEO ANALYSIS** (TIER 1 ONLY) [2-3 paragraphs]
List most valuable videos found:
- Title, channel, duration
- Key timestamps and insights
- Why each video matters for Shahnameh development

**SOURCES**
List all sources with URLs for verification

</output_structure>

<quality_standards>
✓ Cite sources for ALL factual claims (sales, team size, budget)
✓ Distinguish between confirmed facts and reasonable estimates
✓ Use specific examples with timestamps when referencing videos
✓ Be honest about what's achievable for a 2-person team
✓ Provide actionable insights, not generic observations
✓ Focus on Shahnameh relevance, not game description
✓ Note unavailable information as "Unknown" not guesses
✓ Be objective - analyze both strengths and weaknesses
</quality_standards>

<special_focus_areas>
If {game_name} matches any of these, give EXTRA attention:

- **Small team success story:** How did they punch above their weight?
- **Episodic structure:** Release timing, pricing model, player retention lessons
- **Mythology/cultural setting:** Research approach, authenticity, community reception
- **Souls-like/melee combat:** Combat feel, boss design, difficulty balancing
- **Indie that succeeded commercially:** Marketing on low budget, pricing strategy
- **Free/cheap asset tools:** Any techniques we could replicate with free tools
</special_focus_areas>

<research_depth_expectations>
TIER 1 Games: Comprehensive research (3-4 hours) - Deep analysis of all sections
TIER 2 Games: Focused research (2-3 hours) - Emphasize mechanics and team size lessons
TIER 3 Games: Targeted research (1-2 hours) - Only deeply analyze sections relevant to Shahnameh
</research_depth_expectations>

<thinking_before_research>
Before writing each section, think through:
- What's most relevant to Shahnameh development?
- How does this compare to our 2-person + AI constraints?
- What can we realistically implement vs. aspirational?
- Are there Persian mythology/cultural parallels?
- What would software engineers (not game devs) need to know?
- How does this inform our episodic release strategy?
</thinking_before_research>

---

**GAME TO RESEARCH:** <game_name>{game_name}</game_name>
**DEVELOPER:** {developer}
**RELEVANCE TIER:** {tier}

---

Begin your research now. Provide comprehensive analysis following the output structure above, prioritized by relevance tier.
"""

        return prompt

    def save_prompt_to_file(self, game_name: str, prompt: str, tier_number: int) -> Path:
        """Save generated prompt to a file with tier-based prefix."""
        # Sanitize filename
        safe_name = re.sub(r'[^\w\s-]', '', game_name.lower())
        safe_name = re.sub(r'[-\s]+', '_', safe_name)

        filename = self.prompts_dir / f"{tier_number:02d}_{safe_name}_research_prompt.md"
        filename.write_text(prompt)
        return filename

    def generate_index_file(self, games: Dict[str, Dict[str, str]]) -> Path:
        """Generate an index file of all prompts organized by tier."""
        # Sort games by tier
        tier_1 = sorted([g for g, info in games.items() if info['tier'] == 'TIER_1'])
        tier_2 = sorted([g for g, info in games.items() if info['tier'] == 'TIER_2'])
        tier_3 = sorted([g for g, info in games.items() if info['tier'] == 'TIER_3'])

        # Helper function to generate filename with number prefix
        def get_numbered_filename(game_name, tier_offset):
            safe_name = re.sub(r'[^\w\s-]', '', game_name.lower())
            safe_name = re.sub(r'[-\s]+', '_', safe_name)
            return f"{tier_offset:02d}_{safe_name}_research_prompt.md"

        index_content = f"""# Shahnameh Game Research Prompts Index

This directory contains optimized research prompts for all {len(games)} games in the competitive analysis.

Each prompt is customized to the game's relevance tier and designed to extract maximum value for Shahnameh: Legends of Persia development.

## How to Use

1. **Select a game prompt** from the tier that matches your priority
2. **Copy the entire prompt** from the markdown file
3. **Paste into Claude Deep Research** (Claude.ai/research)
4. **Let Claude research** (takes 30-45 minutes per game)
5. **Save the output** to `docs/benchmarks/[game-name]/[game-name].md`

## Search Tips

- Use TIER 1 for immediate, deep analysis
- Use TIER 2 when you need focused lessons
- Use TIER 3 as reference for specific mechanics

---

## TIER 1: Immediate Study ({len(tier_1)} games)

These games have the highest relevance to Shahnameh and warrant comprehensive research.

**Priority Study Order:**
"""

        for i, game in enumerate(tier_1, 1):
            filename = get_numbered_filename(game, i)
            index_content += f"\n{i}. **[{game}]({filename})** - {games[game]['developer']}"

        index_content += f"\n\n## TIER 2: Important Reference ({len(tier_2)} games)\n\nImportant reference points for specific mechanics and design decisions.\n\n"

        for i, game in enumerate(tier_2, 10):
            filename = get_numbered_filename(game, i)
            index_content += f"- **[{i}. {game}]({filename})** - {games[game]['developer']}\n"

        index_content += f"\n## TIER 3: Comprehensive Reference ({len(tier_3)} games)\n\nSpecific mechanics and design lessons for detailed coverage.\n\n"

        for i, game in enumerate(tier_3, 30):
            filename = get_numbered_filename(game, i)
            index_content += f"- **[{i}. {game}]({filename})** - {games[game]['developer']}\n"

        index_content += f"""

---

## Prompt Structure

Each prompt is optimized to:

✅ **Remove Redundancies** - Combines templates without duplication
✅ **Prioritize by Tier** - Tier 1 gets deep analysis, Tier 3 gets targeted focus
✅ **Focus on Shahnameh** - Every section explains relevance to our project
✅ **Respect Team Constraints** - Emphasizes 2-person + AI tool feasibility
✅ **Enable Fast Research** - Clear priorities minimize research time
✅ **Extract Actionable Insights** - Focus on what we can implement

## Statistics

- **Total Games:** {len(games)}
- **Tier 1 (Immediate):** {len(tier_1)} games
- **Tier 2 (Important):** {len(tier_2)} games
- **Tier 3 (Reference):** {len(tier_3)} games

---

## Research Progress Tracking

Track your progress:
- [ ] Complete all TIER 1 research (priority)
- [ ] Complete TIER 2 research (weeks 5-8)
- [ ] Complete TIER 3 research (as needed)

---

## Integration with Benchmark System

After Claude Deep Research completes:
1. Save to `docs/benchmarks/[game-name]/[game-name].md`
2. Use `VIDEO_ANALYSIS_TEMPLATE.md` for detailed video breakdowns
3. Reference in main project documentation
4. Extract actionable insights to implementation plan

---

**Generated:** 2025-12-30
**Prompt System Version:** 1.0
"""

        index_file = self.prompts_dir / "README.md"
        index_file.write_text(index_content)
        return index_file

    def generate_metadata_file(self, games: Dict[str, Dict[str, str]]) -> Path:
        """Generate a JSON metadata file of all games."""
        metadata = {
            'generated_date': '2025-12-30',
            'total_games': len(games),
            'tiers': {
                'TIER_1': 0,
                'TIER_2': 0,
                'TIER_3': 0
            },
            'games': []
        }

        # Create tier-based counters for numbering
        tier_counters = {'TIER_1': 1, 'TIER_2': 10, 'TIER_3': 30}

        for game, info in sorted(games.items()):
            tier = info['tier']
            metadata['tiers'][tier] += 1

            safe_name = re.sub(r'[^\w\s-]', '', game.lower())
            safe_name = re.sub(r'[-\s]+', '_', safe_name)

            tier_number = tier_counters[tier]
            prompt_file = f"{tier_number:02d}_{safe_name}_research_prompt.md"

            metadata['games'].append({
                'name': game,
                'developer': info['developer'],
                'tier': tier,
                'relevance': info['relevance'],
                'priority_number': tier_number,
                'prompt_file': prompt_file
            })

            # Increment counter for this tier
            tier_counters[tier] += 1

        metadata_file = self.prompts_dir / "games_metadata.json"
        metadata_file.write_text(json.dumps(metadata, indent=2))
        return metadata_file

    def run(self) -> dict:
        """Run the complete prompt generation pipeline."""
        print("🎮 Shahnameh Game Research Prompt Generator")
        print("=" * 60)

        # Step 1: Extract games
        print("\n📚 Step 1: Extracting games from benchmark document...")
        games = self.extract_games_from_markdown()
        print(f"✅ Found {len(games)} games")

        # Count by tier
        tier_1 = sum(1 for g in games.values() if g['tier'] == 'TIER_1')
        tier_2 = sum(1 for g in games.values() if g['tier'] == 'TIER_2')
        tier_3 = sum(1 for g in games.values() if g['tier'] == 'TIER_3')
        print(f"   - TIER 1: {tier_1} games")
        print(f"   - TIER 2: {tier_2} games")
        print(f"   - TIER 3: {tier_3} games")

        # Step 2: Generate prompts with tier-based numbering
        print("\n🔧 Step 2: Generating optimized research prompts...")
        generated_prompts = []

        # Create tier-based counters for numbering
        tier_counters = {'TIER_1': 1, 'TIER_2': 10, 'TIER_3': 30}
        tier_start_nums = {'TIER_1': 1, 'TIER_2': 10, 'TIER_3': 30}

        for game_name, game_info in sorted(games.items()):
            prompt = self.generate_optimized_prompt(game_name, game_info)
            tier = game_info['tier']
            tier_number = tier_counters[tier]

            prompt_file = self.save_prompt_to_file(game_name, prompt, tier_number)
            generated_prompts.append((game_name, prompt_file))
            print(f"   ✅ {tier_number:02d}. {game_name} ({tier})")

            # Increment counter for this tier
            tier_counters[tier] += 1

        # Step 3: Generate index
        print("\n📑 Step 3: Generating index file...")
        index_file = self.generate_index_file(games)
        print(f"   ✅ Index created: {index_file.name}")

        # Step 4: Generate metadata
        print("\n📊 Step 4: Generating metadata...")
        metadata_file = self.generate_metadata_file(games)
        print(f"   ✅ Metadata created: {metadata_file.name}")

        # Summary
        print("\n" + "=" * 60)
        print("✨ Generation Complete!")
        print("=" * 60)
        print(f"📁 Location: {self.prompts_dir}")
        print(f"📝 Prompts generated: {len(generated_prompts)}")
        print(f"📑 Index file: README.md")
        print(f"📊 Metadata file: games_metadata.json")
        print("\n🚀 Next Steps:")
        print("   1. Open docs/benchmarks/prompts/README.md")
        print("   2. Select a game prompt (start with TIER 1)")
        print("   3. Copy prompt and paste into Claude Deep Research")
        print("   4. Save output to docs/benchmarks/[game-name]/[game-name].md")

        return {
            'total_games': len(games),
            'prompts_generated': len(generated_prompts),
            'games': games,
            'prompts_dir': str(self.prompts_dir)
        }


def main():
    """Main entry point."""
    try:
        generator = GamePromptGenerator()
        result = generator.run()

        # Print sample of extracted games
        print("\n📚 Sample Games (first 10):")
        for i, game in enumerate(sorted(generator.games.keys())[:10], 1):
            info = generator.games[game]
            print(f"   {i}. {game} ({info['tier']}) - {info['developer']}")

        return 0
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
